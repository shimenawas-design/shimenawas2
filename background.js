// =====================================================================
// background.js（サービスワーカー）
// ---------------------------------------------------------------------
// Manifest V3 の拡張機能では、常時起動しっぱなしの「バックグラウンド
// ページ」の代わりに、必要なときだけ起動する「サービスワーカー」を
// 使います。
//
// このファイルの役割:
//   1. popup.js から「ダウンロード開始」の指示を受け取る
//   2. 現在アクティブなタブ(content.js)に「画像を抽出して」と依頼する
//   3. content.js から返ってきた画像URLの一覧を、
//      chrome.downloads API を使って1枚ずつローカルに保存する
//
// ※ ダウンロード処理を popup.js ではなく background.js に置く理由:
//    ポップアップ画面はユーザーがクリックした瞬間に閉じてしまう
//    ことがあり、その場合ポップアップ内のJavaScriptは停止して
//    しまいます。サービスワーカーで処理することで、ポップアップが
//    閉じても一括ダウンロードの処理を最後まで安定して継続できます。
// =====================================================================

/**
 * 指定したタブに対して「画像を抽出して」というメッセージを送り、
 * content.js からの応答（画像URLの配列）を待つ関数。
 */
async function requestImageUrlsFromTab(tabId) {
  return chrome.tabs.sendMessage(tabId, { action: "EXTRACT_IMAGES" });
}

/**
 * 待機用のヘルパー関数（指定ミリ秒だけ処理を止める）。
 */
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/**
 * 進捗メッセージをポップアップに送る（ポップアップが閉じている場合は
 * 送信先が無いためエラーになるが、その場合は無視してよい）。
 */
function notifyProgress(message) {
  chrome.runtime.sendMessage({ action: "GEMINI_DL_PROGRESS", message }).catch(() => {
    // ポップアップが閉じている場合はここに来るが、問題ないので何もしない
  });
}

// 1件ダウンロードするごとに空ける間隔（ミリ秒）。
// Chromeは短時間に大量のダウンロードを開始すると「複数ファイルの
// ダウンロード」の許可を求めるダイアログを出すことがあるため、
// 少し間隔を空けることでその発生頻度を抑えつつ、進捗も見やすくする。
const DOWNLOAD_INTERVAL_MS = 350;

/**
 * 画像URLの配列を、指定されたファイル名プレフィックスを使って
 * 1枚ずつ順番にダウンロードする関数。
 *
 * chrome.downloads.download() を同時に大量に呼び出すと、Chromeが
 * 「複数ファイルの自動ダウンロード」とみなしてブロックしたり、
 * ユーザーに確認を求めたりすることがあるため、1件ずつ完了を待って
 * 順番に、かつ少し間隔を空けて実行する（連続ダウンロード方式）ように
 * しています。
 */
async function downloadImagesSequentially(imageUrls, prefix) {
  let successCount = 0;
  const failedUrls = [];

  for (let i = 0; i < imageUrls.length; i++) {
    const url = imageUrls[i];
    // 連番を3桁のゼロ埋めにする（例: 001, 002, ...）
    const serial = String(i + 1).padStart(3, "0");

    // URLの拡張子を可能な範囲で推測する（取得できなければ png を既定にする）
    const extensionMatch = url.match(/\.(png|jpg|jpeg|webp|gif)(?:[?&#]|$)/i);
    const extension = extensionMatch ? extensionMatch[1].toLowerCase() : "png";

    const filename = `${prefix}_${serial}.${extension}`;

    notifyProgress(`ダウンロード中… (${i + 1}/${imageUrls.length}) ${filename}`);

    try {
      // chrome.downloads.download はPromiseを返す（ダウンロードIDが解決値）
      await chrome.downloads.download({
        url: url,
        filename: filename,
        // saveAs: false にすることで、毎回「保存先を選ぶダイアログ」を
        // 出さずに、既定のダウンロードフォルダへ自動保存する
        saveAs: false,
        conflictAction: "uniquify", // 同名ファイルがあれば自動的に連番を振り直す
      });
      successCount++;
    } catch (error) {
      console.error(`[Gemini画像DL] ダウンロード失敗: ${url}`, error);
      failedUrls.push(url);
    }

    // 次のダウンロードまで少し間隔を空ける
    // （Chromeの「複数ダウンロード」ブロックを避けるため）
    if (i < imageUrls.length - 1) {
      await sleep(DOWNLOAD_INTERVAL_MS);
    }
  }

  return { successCount, failedCount: failedUrls.length, failedUrls };
}

// =====================================================================
// popup.js からのメッセージを受け取るリスナー
// =====================================================================
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request && request.action === "START_BULK_DOWNLOAD") {
    // 非同期処理を行うため、即座に別関数を呼び出して、
    // 完了したら sendResponse() を呼ぶ（そのため最後に return true が必要）
    handleBulkDownload(request.prefix, request.tabId, sendResponse);
    return true; // 非同期でsendResponseを呼ぶことをChromeに伝える
  }
});

async function handleBulkDownload(prefix, tabId, sendResponse) {
  try {
    // ---- 1. content.js に画像抽出を依頼する ----
    //         （content.js側でまず自動スクロールして遅延読み込み画像を
    //           表示させてから、DOMを解析して画像URLを集める）
    notifyProgress("Geminiのページをスクロールして画像を読み込んでいます…");
    const extractResult = await requestImageUrlsFromTab(tabId);

    if (!extractResult || !extractResult.ok) {
      sendResponse({
        ok: false,
        errorType: "EXTRACT_FAILED",
        message:
          "ページから画像情報を取得できませんでした。Geminiのチャット画面を開き直してから再度お試しください。",
      });
      return;
    }

    const imageUrls = extractResult.imageUrls || [];

    // ---- 2. 画像が1枚も見つからなかった場合はエラーとして通知する ----
    if (imageUrls.length === 0) {
      sendResponse({
        ok: false,
        errorType: "NO_IMAGES_FOUND",
        message:
          "このページには生成された画像が見つかりませんでした。画像を生成したチャット画面でお試しください。",
      });
      return;
    }

    // ---- 3. 見つかった画像を順番にダウンロードする ----
    const safePrefix = (prefix && prefix.trim()) || "gemini_image";
    const result = await downloadImagesSequentially(imageUrls, safePrefix);

    sendResponse({
      ok: true,
      totalFound: imageUrls.length,
      successCount: result.successCount,
      failedCount: result.failedCount,
    });
  } catch (error) {
    console.error("[Gemini画像DL] 一括ダウンロード処理中にエラーが発生しました:", error);

    const rawMessage = String(error && error.message ? error.message : error);

    // "Could not establish connection. Receiving end does not exist." は、
    // content.js がそのタブにまだ読み込まれていない場合に発生する。
    // よくある原因は「拡張機能をインストール/更新した後、既に開いていた
    // Geminiのタブを再読み込みしていない」こと。Chromeの仕様上、
    // content_scriptsは拡張機能の読み込み後に新しく開く（または
    // 再読み込みする）ページにしか自動で追加されないため。
    if (/Receiving end does not exist|Could not establish connection/i.test(rawMessage)) {
      sendResponse({
        ok: false,
        errorType: "CONTENT_SCRIPT_NOT_LOADED",
        message:
          "拡張機能とGeminiのページがまだ接続されていません。Geminiのタブを再読み込み（F5キーなど）してから、もう一度お試しください。",
      });
      return;
    }

    sendResponse({
      ok: false,
      errorType: "UNEXPECTED_ERROR",
      message: "予期しないエラーが発生しました: " + rawMessage,
    });
  }
}
