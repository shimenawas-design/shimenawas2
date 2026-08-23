// =====================================================================
// content.js
// ---------------------------------------------------------------------
// このファイルは Gemini (https://gemini.google.com/*) のページに
// 自動的に埋め込まれる「コンテンツスクリプト」です。
// ページのDOM（HTML構造）を直接読み取れる唯一のスクリプトなので、
// 「チャット内に表示されている生成画像のURLを集める」役割を担います。
//
// ポップアップ(popup.js) → background.js → content.js という順で
// メッセージが送られてきて、この中の「画像抽出処理」が実行されます。
// =====================================================================

/**
 * ページ内から「Geminiが生成した画像」と思われる <img> 要素を集めて、
 * 画像URLの配列を返す関数。
 *
 * 注意: GeminiのHTML構造（クラス名など）はGoogle側の仕様変更で
 * 変わる可能性があります。そのため、1つのセレクタだけに頼らず、
 * 複数の候補セレクタを試す「多重防御」の作りにしています。
 * もし将来動かなくなった場合は、Chromeの検証ツール(F12)で
 * 生成画像の <img> タグを確認し、下の SELECTORS 配列に
 * 新しいセレクタを追加してください。
 */
function extractGeminiImageUrls() {
  // ---- 1. 画像候補になりそうな要素を集めるためのセレクタ一覧 ----
  const SELECTORS = [
    // Gemini生成画像は Google のコンテンツ配信ドメイン
    // (googleusercontent.com) から配信されることが多い
    'img[src*="googleusercontent.com"]',
    // 画像生成結果を表示する専用コンポーネント（Web Components）の候補
    "single-image img",
    "image-viewer img",
    // data属性で画像コンテナを示している場合の候補
    '[data-test-id*="image"] img',
    '[data-test-id*="generated"] img',
    // クラス名に "image" を含む要素の中の img タグ（汎用フォールバック）
    '.image-container img',
    '.generated-image img',
  ];

  // Set を使って重複した <img> 要素を除外する
  const candidateImages = new Set();
  for (const selector of SELECTORS) {
    try {
      document.querySelectorAll(selector).forEach((el) => candidateImages.add(el));
    } catch (e) {
      // 存在しないセレクタでエラーになっても処理を止めない
      console.warn("[Gemini画像DL] セレクタの評価に失敗しました:", selector, e);
    }
  }

  // ---- 2. 候補の中から「本物の生成画像」だけをフィルタリングする ----
  const imageUrls = [];
  candidateImages.forEach((img) => {
    // 表示中の実際のURL（currentSrc）を優先的に使う。無ければ src を使う。
    const rawUrl = img.currentSrc || img.src;
    if (!rawUrl) return;

    // data:URL（インラインの極小アイコンなど）は生成画像ではないことが多いので除外
    if (rawUrl.startsWith("data:")) return;

    // アイコン・アバター・ロゴなど、生成画像ではない小さな画像を除外する
    // (幅・高さが小さいものはUI装飾用アイコンの可能性が高い)
    const width = img.naturalWidth || img.width || 0;
    const height = img.naturalHeight || img.height || 0;
    if (width > 0 && width < 128) return;
    if (height > 0 && height < 128) return;

    // ファイル名やパスに "avatar" "logo" "icon" "favicon" を含むものは
    // ユーザーアイコンやサービスロゴである可能性が高いため除外する
    if (/avatar|logo|favicon|profile/i.test(rawUrl)) return;

    imageUrls.push(getHighResolutionUrl(rawUrl));
  });

  // 重複するURL（同じ画像を2回取得してしまった場合）を除去して返す
  return Array.from(new Set(imageUrls));
}

/**
 * Googleの画像配信URL（googleusercontent.com）は、末尾に
 * 「=w200-h200」や「=s512」のようなサイズ指定パラメータが
 * ついていることが多いです。
 * このパラメータを「=s0」（オリジナルサイズを意味する）に
 * 置き換えることで、なるべく高解像度の画像を取得できるようにします。
 */
function getHighResolutionUrl(url) {
  try {
    const parsed = new URL(url, window.location.href);
    if (parsed.hostname.includes("googleusercontent.com")) {
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
// {action: "EXTRACT_IMAGES"} を送ってくると、ここで画像を抽出して
// 結果を返信(sendResponse)します。
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request && request.action === "EXTRACT_IMAGES") {
    try {
      const imageUrls = extractGeminiImageUrls();
      sendResponse({ ok: true, imageUrls });
    } catch (error) {
      console.error("[Gemini画像DL] 画像抽出中にエラーが発生しました:", error);
      sendResponse({ ok: false, error: String(error && error.message ? error.message : error) });
    }
  }
  // sendResponseを非同期で使うわけではないが、明示的にtrueを返して
  // メッセージチャンネルの互換性を保つ
  return true;
});
