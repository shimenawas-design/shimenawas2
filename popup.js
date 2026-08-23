// =====================================================================
// popup.js
// ---------------------------------------------------------------------
// popup.html 上で動作するスクリプトです。
// ユーザーの入力（ファイル名プレフィックス）を受け取り、
// 「一括ダウンロードを実行」ボタンが押されたら background.js に
// 処理の開始を依頼します。
//
// 実際の「DOM解析」や「ダウンロード」の重い処理はここでは行わず、
// content.js / background.js に任せることで、ポップアップが
// 途中で閉じられても処理が安定して継続できるようにしています。
// =====================================================================

// ---- 画面上の要素を取得しておく ----
const prefixInput = document.getElementById("prefix-input");
const filenamePreview = document.getElementById("filename-preview");
const downloadBtn = document.getElementById("download-btn");
const btnLabel = document.getElementById("btn-label");
const btnIcon = document.getElementById("btn-icon");
const statusEl = document.getElementById("status");

const DEFAULT_PREFIX = "gemini_image";

/**
 * 入力されたプレフィックスから、実際に使えるファイル名の
 * プレフィックスを作る関数。
 * ファイル名に使えない記号（\ / : * ? " < > | など）を
 * アンダースコアに置き換えて安全な文字列にする。
 */
function sanitizePrefix(rawValue) {
  const trimmed = (rawValue || "").trim();
  const base = trimmed.length > 0 ? trimmed : DEFAULT_PREFIX;
  return base.replace(/[\\/:*?"<>|]/g, "_");
}

/**
 * 入力欄の下にある「保存例」のプレビューテキストを更新する関数。
 */
function updateFilenamePreview() {
  const safePrefix = sanitizePrefix(prefixInput.value);
  filenamePreview.textContent = `保存例: ${safePrefix}_001.png`;
}

/**
 * ステータス表示欄にメッセージを表示する関数。
 * type には "info" | "success" | "error" のいずれかを指定する。
 */
function showStatus(message, type) {
  statusEl.textContent = message;
  statusEl.className = `status status--${type}`;
}

function hideStatus() {
  statusEl.className = "status status--hidden";
  statusEl.textContent = "";
}

/**
 * ボタンを「処理中」の見た目・状態に切り替える関数。
 */
function setButtonBusy(isBusy) {
  downloadBtn.disabled = isBusy;
  if (isBusy) {
    btnIcon.textContent = "⏳";
    btnLabel.textContent = "処理中...";
  } else {
    btnIcon.textContent = "⬇";
    btnLabel.textContent = "一括ダウンロードを実行";
  }
}

// 入力欄が変化するたびに、保存例のプレビューを更新する
prefixInput.addEventListener("input", updateFilenamePreview);
updateFilenamePreview();

// ---- メインボタンのクリック処理 ----
downloadBtn.addEventListener("click", async () => {
  hideStatus();

  const safePrefix = sanitizePrefix(prefixInput.value);

  try {
    setButtonBusy(true);
    showStatus("Geminiのページを確認しています…", "info");

    // ---- 1. 現在アクティブなタブを取得する ----
    const [activeTab] = await chrome.tabs.query({ active: true, currentWindow: true });

    if (!activeTab || !activeTab.id) {
      showStatus("対象のタブが見つかりませんでした。もう一度お試しください。", "error");
      setButtonBusy(false);
      return;
    }

    // ---- 2. 対象がGeminiのページかどうかを確認する ----
    const isGeminiPage = typeof activeTab.url === "string" && activeTab.url.startsWith("https://gemini.google.com/");
    if (!isGeminiPage) {
      showStatus(
        "この機能は Gemini (gemini.google.com) のページでのみ利用できます。Geminiのチャット画面を開いてから再度お試しください。",
        "error"
      );
      setButtonBusy(false);
      return;
    }

    showStatus("画像を検索してダウンロードしています…", "info");

    // ---- 3. background.js に一括ダウンロードの開始を依頼する ----
    const response = await chrome.runtime.sendMessage({
      action: "START_BULK_DOWNLOAD",
      prefix: safePrefix,
      tabId: activeTab.id,
    });

    // ---- 4. 結果に応じてステータス表示を切り替える ----
    if (!response) {
      showStatus("拡張機能内部で通信エラーが発生しました。もう一度お試しください。", "error");
    } else if (!response.ok) {
      // 画像が見つからなかった場合や抽出に失敗した場合のエラー表示
      showStatus(`⚠ ${response.message}`, "error");
    } else if (response.failedCount > 0) {
      showStatus(
        `✅ ${response.successCount}枚のダウンロードに成功しました（${response.failedCount}枚は失敗しました）。`,
        "success"
      );
    } else {
      showStatus(`✅ ${response.successCount}枚の画像をダウンロードしました！`, "success");
    }
  } catch (error) {
    console.error("[Gemini画像DL] ポップアップ処理中にエラーが発生しました:", error);
    showStatus(
      "予期しないエラーが発生しました。Geminiのページを再読み込みしてから、再度お試しください。",
      "error"
    );
  } finally {
    setButtonBusy(false);
  }
});
