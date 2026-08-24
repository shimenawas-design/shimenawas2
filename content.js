// =====================================================================
// content.js
// ---------------------------------------------------------------------
// このファイルは Gemini (https://gemini.google.com/*) のページに
// 自動的に埋め込まれる「コンテンツスクリプト」です。
// ページのDOM（HTML構造）を直接読み取れる唯一のスクリプトなので、
// 「チャット内に表示されている生成画像のURLを集める」役割を担います。
//
// ポップアップ(popup.js) → background.js → content.js という順で
// メッセージが送られてきて、この中の「自動スクロール→画像抽出」処理が
// 実行されます。
// =====================================================================

/**
 * 進捗メッセージをポップアップに送る（ポップアップが閉じている場合は
 * 送信先が無いためエラーになるが、その場合は無視してよい）。
 */
function notifyProgress(message) {
  try {
    chrome.runtime.sendMessage({ action: "GEMINI_DL_PROGRESS", message }).catch(() => {
      // ポップアップが閉じている場合はここに来るが、問題ないので何もしない
    });
  } catch (e) {
    // 拡張機能のコンテキストが無効な場合などは無視する
  }
}

// ---------------------------------------------------------------------
// 自動スクロール処理
// ---------------------------------------------------------------------
// Geminiのチャット画面は、過去のメッセージ・画像を「表示領域に入って
// きてから」読み込む（遅延読み込み/レイジーロード）ことがあります。
// そのままDOMを読み取ると、画面外の画像が見つからず取りこぼしてしまう
// ため、実際に抽出処理を行う前に自動でスクロールし、なるべく多くの
// 画像を読み込ませてから抽出します。

/**
 * ページ内で実際にスクロールできる要素（チャットの会話欄など）を
 * できるだけ正確に推測する関数。
 * Geminiのクラス名は変わる可能性があるため、「縦にスクロール可能で、
 * かつ中身が画面の高さより大きい要素」という条件で汎用的に探す。
 */
function findScrollableContainer() {
  const candidates = document.querySelectorAll("body *");
  let best = null;
  let bestScrollableHeight = 0;

  for (const el of candidates) {
    // 巨大なDOM探索を避けるため、画面に表示されている要素だけを見る
    const style = window.getComputedStyle(el);
    const overflowY = style.overflowY;
    const isScrollableStyle = overflowY === "auto" || overflowY === "scroll";
    if (!isScrollableStyle) continue;

    const scrollableHeight = el.scrollHeight - el.clientHeight;
    // ある程度の高さがあり、かつ画面内に見えている要素のみを候補にする
    if (scrollableHeight > 100 && el.clientHeight > 100) {
      if (scrollableHeight > bestScrollableHeight) {
        bestScrollableHeight = scrollableHeight;
        best = el;
      }
    }
  }

  // 適切なスクロール要素が見つからない場合は、ページ全体（documentの
  // スクロール要素）をフォールバックとして使う
  return best || document.scrollingElement || document.documentElement;
}

/**
 * 待機用のヘルパー関数（指定ミリ秒だけ処理を止める）。
 */
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/**
 * チャット欄を上から下まで自動でスクロールし、遅延読み込みされる
 * 画像をできるだけ読み込ませる関数。
 * ・スクロール位置が変化しなくなったら「最後まで到達した」とみなして終了
 * ・安全のため、最大試行回数の上限を設けて無限ループを防ぐ
 */
async function autoScrollToLoadAllImages() {
  const container = findScrollableContainer();
  const originalScrollTop = container.scrollTop;

  const MAX_STEPS = 60; // 安全のための上限（これ以上長いチャットは想定しない）
  const WAIT_MS = 220; // 1回スクロールしてから画像読み込みを待つ時間

  let previousScrollHeight = -1;
  let unchangedCount = 0;

  for (let step = 0; step < MAX_STEPS; step++) {
    notifyProgress(`画像を読み込むためにページをスクロール中…（${step + 1}回目）`);

    container.scrollTop = container.scrollHeight;
    await sleep(WAIT_MS);

    // スクロール後もページの高さが変わらない状態が2回続いたら、
    // それ以上読み込む新しいコンテンツが無いと判断して終了する
    if (container.scrollHeight === previousScrollHeight) {
      unchangedCount++;
      if (unchangedCount >= 2) break;
    } else {
      unchangedCount = 0;
    }
    previousScrollHeight = container.scrollHeight;
  }

  // ユーザーが元々見ていた位置になるべく近い場所へスクロールを戻す
  // (一番下に居た場合が多いので、基本は一番下に戻す)
  container.scrollTop = container.scrollHeight;
  void originalScrollTop; // 将来的に元位置へ復元したくなった場合のために変数だけ残す

  notifyProgress("画像を検索しています…");
}

// ---------------------------------------------------------------------
// 画像抽出処理
// ---------------------------------------------------------------------

// UI装飾（アバター・ナビゲーション・ボタンなど）に含まれる画像を
// 除外するためのセレクタ。この中に含まれる<img>は生成画像ではないと
// みなす。
const EXCLUDE_ANCESTOR_SELECTOR =
  'header, nav, aside, footer, button, [role="navigation"], [role="banner"], [role="complementary"], [contenteditable="true"]';

/**
 * <img> 要素から「最も解像度が高いと思われる画像URL」を取得する関数。
 * srcset（複数解像度の候補が書かれた属性）や、<picture><source>の
 * srcsetも確認し、一番幅(w)が大きい候補を選ぶ。
 */
function pickBestSourceUrl(img) {
  let bestUrl = null;
  let bestWidth = -1;

  const considerSrcset = (srcset) => {
    if (!srcset) return;
    // "url1 100w, url2 300w" のような形式を1つずつ解析する
    srcset.split(",").forEach((entry) => {
      const parts = entry.trim().split(/\s+/);
      const url = parts[0];
      const widthMatch = (parts[1] || "").match(/(\d+)w/);
      const width = widthMatch ? parseInt(widthMatch[1], 10) : 0;
      if (url && width >= bestWidth) {
        bestWidth = width;
        bestUrl = url;
      }
    });
  };

  // <picture><source srcset="..."></picture> の形式にも対応する
  const picture = img.closest("picture");
  if (picture) {
    picture.querySelectorAll("source").forEach((source) => {
      considerSrcset(source.getAttribute("srcset"));
    });
  }
  considerSrcset(img.getAttribute("srcset"));

  if (bestUrl) return bestUrl;
  return img.currentSrc || img.src;
}

/**
 * ページ内から「Geminiが生成した画像」と思われる <img> 要素を集めて、
 * 画像URLの配列を返す関数。
 *
 * 注意: GeminiのHTML構造（クラス名など）はGoogle側の仕様変更で
 * 変わる可能性があります。そのため、
 *   1. まず「それらしいクラス名・属性」を持つ候補セレクタで絞り込む
 *   2. それで1件も見つからない場合は、ページ内の全<img>を対象にした
 *      「汎用フォールバック」で探す
 * という2段構えにして、クラス名が変わっても動き続けやすくしています。
 * それでも動かない場合は、Chromeの検証ツール(F12)で実際の<img>タグを
 * 確認し、下の SELECTORS 配列に新しいセレクタを追加してください。
 */
function extractGeminiImageUrls() {
  const SELECTORS = [
    // Gemini生成画像は Google のコンテンツ配信ドメインから配信されることが多い
    'img[src*="googleusercontent.com"]',
    'img[src*="ggpht.com"]',
    // 画像生成結果を表示する専用コンポーネント（Web Components）の候補
    "single-image img",
    "image-viewer img",
    // data属性で画像コンテナを示している場合の候補
    '[data-test-id*="image"] img',
    '[data-test-id*="generated"] img',
    // クラス名に "image" を含む要素の中の img タグ
    '.image-container img',
    '.generated-image img',
  ];

  const collectFromSelectors = (selectors) => {
    const found = new Set();
    for (const selector of selectors) {
      try {
        document.querySelectorAll(selector).forEach((el) => found.add(el));
      } catch (e) {
        console.warn("[Gemini画像DL] セレクタの評価に失敗しました:", selector, e);
      }
    }
    return found;
  };

  const filterAndCollectUrls = (imgElements) => {
    const urls = [];
    imgElements.forEach((img) => {
      // ナビゲーションやボタンなど、UI装飾の中にある画像は除外する
      if (img.closest(EXCLUDE_ANCESTOR_SELECTOR)) return;

      const rawUrl = pickBestSourceUrl(img);
      if (!rawUrl) return;

      // data:URL（インラインの極小アイコンなど）は生成画像ではないことが多いので除外
      if (rawUrl.startsWith("data:")) return;

      // アイコン・アバター・ロゴなど、生成画像ではない小さな画像を除外する
      const width = img.naturalWidth || img.width || 0;
      const height = img.naturalHeight || img.height || 0;
      if (width > 0 && width < 128) return;
      if (height > 0 && height < 128) return;

      // ファイル名やパスに "avatar" "logo" "icon" "favicon" を含むものは
      // ユーザーアイコンやサービスロゴである可能性が高いため除外する
      if (/avatar|logo|favicon|profile/i.test(rawUrl)) return;

      urls.push(getHighResolutionUrl(rawUrl));
    });
    return urls;
  };

  // ---- 1. まずは「それらしい」セレクタで絞り込んで探す ----
  let imageUrls = filterAndCollectUrls(collectFromSelectors(SELECTORS));

  // ---- 2. 1件も見つからなければ、ページ内の全<img>を対象に再検索する ----
  //         （HTML構造の変更によりSELECTORSが古くなった場合の保険）
  if (imageUrls.length === 0) {
    const allImages = document.querySelectorAll("img");
    imageUrls = filterAndCollectUrls(allImages);
  }

  // 重複するURL（同じ画像を2回取得してしまった場合）を除去して返す
  return Array.from(new Set(imageUrls));
}

/**
 * Googleの画像配信URL（googleusercontent.com / ggpht.com）は、末尾に
 * 「=w200-h200」や「=s512」のようなサイズ指定パラメータが
 * ついていることが多いです。
 * このパラメータを「=s0」（オリジナルサイズを意味する）に
 * 置き換えることで、なるべく高解像度の画像を取得できるようにします。
 */
function getHighResolutionUrl(url) {
  try {
    const parsed = new URL(url, window.location.href);
    if (parsed.hostname.includes("googleusercontent.com") || parsed.hostname.includes("ggpht.com")) {
      // 末尾の "=w123-h456" や "=s123" のようなサイズ指定を取り除く
      const base = url.replace(/=(w\d+-h\d+|s\d+)([^&]*)?$/i, "");
      // "=s0" を付けることでオリジナル解像度の取得を試みる
      return base.endsWith("=") ? base + "0" : base + "=s0";
    }
  } catch (e) {
    // URLの解析に失敗した場合は、元のURLをそのまま返す
    console.warn("[Gemini画像DL] URL解析に失敗しました:", url, e);
  }
  return url;
}

// =====================================================================
// background.js からのメッセージを受け取るリスナー
// =====================================================================
// background.js が chrome.tabs.sendMessage() でこのタブに
// {action: "EXTRACT_IMAGES"} を送ってくると、
// 「自動スクロール → 画像抽出」を行い、結果を返信(sendResponse)します。
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request && request.action === "EXTRACT_IMAGES") {
    (async () => {
      try {
        await autoScrollToLoadAllImages();
        const imageUrls = extractGeminiImageUrls();
        sendResponse({ ok: true, imageUrls });
      } catch (error) {
        console.error("[Gemini画像DL] 画像抽出中にエラーが発生しました:", error);
        sendResponse({ ok: false, error: String(error && error.message ? error.message : error) });
      }
    })();
    // 非同期でsendResponseを呼ぶことをChromeに伝えるため true を返す
    return true;
  }
});
