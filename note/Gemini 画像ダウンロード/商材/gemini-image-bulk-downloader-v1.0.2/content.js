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

// UI装飾（ナビゲーション・入力欄など）に含まれる画像を除外するための
// セレクタ。この中に含まれる<img>は生成画像ではないとみなす。
//
// 注意: 以前は <button> も除外対象にしていましたが、多くのAI画像生成
// サービスでは「クリックで拡大表示する」ために生成画像自体を<button>で
// 囲んでいることがあり、それによって本物の生成画像まで除外されてしまう
// 実害が確認されたため外しています。
const EXCLUDE_ANCESTOR_SELECTOR =
  'header, nav, aside, footer, [role="navigation"], [role="banner"], [role="complementary"], [contenteditable="true"]';

/**
 * ページ内の <img> 要素を、通常のDOMだけでなく「Shadow DOM」の中まで
 * 再帰的にたどって全て集める関数。
 *
 * GeminiのようなモダンなWebアプリはWeb Components（独自タグ）を使って
 * おり、画像がShadow DOM（親のDOMツリーからは通常見えない領域）の中に
 * 描画されている場合があります。通常の document.querySelectorAll("img")
 * ではShadow DOMの中は探索できないため、この関数で明示的に潜って探します。
 * （ただし「閉じた」Shadow DOM (mode: "closed") はブラウザの仕様上、
 * 拡張機能からも中身を読み取ることができません）
 */
function collectAllImagesDeep(root, results) {
  if (!root || !root.querySelectorAll) return;

  root.querySelectorAll("img").forEach((img) => results.add(img));

  // Shadow DOM を持つ要素があれば、その中も再帰的に探索する
  root.querySelectorAll("*").forEach((el) => {
    if (el.shadowRoot) {
      collectAllImagesDeep(el.shadowRoot, results);
    }
  });
}

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
 * <img> 要素にすでに描画されているピクセルデータを、canvasに描き写して
 * data: URL（画像データを直接埋め込んだ文字列）として取り出す関数。
 *
 * 実機のGeminiページで検証したところ、生成画像のURLは blob: 形式で、
 * <img>タグとしての表示（img-src）は問題なく行えるものの、その同じ
 * blob: URLに対して fetch() / XMLHttpRequest で中身を取得しようとすると
 * 常に失敗する（ネットワークリクエストすら発生しない）ことが分かった。
 * ページのCSP設定などにより、blob: URLへの fetch が許可されていない
 * ためと見られる。一方、画像は<img>としてすでにデコード済みなので、
 * canvasに描画してtoDataURL()で取り出す方法であればこの制限を回避できる。
 */
function blobImageToDataUrl(img) {
  const canvas = document.createElement("canvas");
  canvas.width = img.naturalWidth || img.width;
  canvas.height = img.naturalHeight || img.height;
  const ctx = canvas.getContext("2d");
  ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
  return canvas.toDataURL("image/png");
}

/**
 * blob: 形式のURL（ページ内でJavaScriptにより一時的に作られたURL）を、
 * ダウンロード可能な data: URL に変換する関数。
 *
 * 重要: blob: URLはそれを作成したページの中でしか有効ではありません。
 * background.js（サービスワーカー）は別の実行コンテキストなので、
 * content.js側から見えている blob: URL をそのまま background.js に
 * 渡してダウンロードさせようとしても失敗します。そのため、
 * blob: URLの中身はここ（content.js）で先に読み込んでおき、
 * どこからでも使える data: URL に変換してから渡します。
 *
 * まずcanvas経由での変換を試み（上記の理由でこちらが本命）、
 * 何らかの理由でcanvasが失敗した場合のみ、念のためfetch()による
 * 従来方式にフォールバックします。
 */
async function resolveDownloadableUrl(img, url) {
  if (!url || !url.startsWith("blob:")) return url;

  try {
    return blobImageToDataUrl(img);
  } catch (canvasError) {
    console.warn("[Gemini画像DL] canvas経由の変換に失敗しました。fetchにフォールバックします:", url, canvasError);
  }

  try {
    const response = await fetch(url);
    const blob = await response.blob();
    return await new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => resolve(reader.result);
      reader.onerror = () => reject(reader.error || new Error("FileReaderでの変換に失敗しました"));
      reader.readAsDataURL(blob);
    });
  } catch (error) {
    console.warn("[Gemini画像DL] blob画像をdata URLに変換できませんでした:", url, error);
    return null;
  }
}

/**
 * ページ内から「Geminiが生成した画像」と思われる <img> 要素を集めて、
 * 画像URLの配列を返す関数（非同期）。
 *
 * 注意: GeminiのHTML構造（クラス名など）はGoogle側の仕様変更で
 * 変わる可能性があります。そのため、特定のクラス名に依存せず、
 * ページ内（Shadow DOMの中も含む）の全<img>要素を対象にしたうえで、
 * 「サイズ」「拡張子」「ファイル名のパターン」「置かれている場所」で
 * 生成画像らしいものだけを残す、という汎用的な絞り込み方をしています。
 * それでもうまく抽出できなくなった場合は、Chromeの検証ツール(F12)で
 * 実際の<img>タグの様子を確認し、下のフィルタ条件を調整してください。
 */
async function extractGeminiImageUrls() {
  const allImages = new Set();
  collectAllImagesDeep(document, allImages);
  console.log(`[Gemini画像DL][debug] 発見した<img>の総数: ${allImages.size}`);

  const qualifyingImages = [];
  let excludedByAncestor = 0;
  let excludedByNoUrl = 0;
  let excludedByDataUrl = 0;
  let excludedBySvg = 0;
  let excludedBySize = 0;
  let excludedByKeyword = 0;
  let excludedByIncomplete = 0;

  allImages.forEach((img) => {
    // ナビゲーションやボタンなど、UI装飾の中にある画像は除外する
    if (img.closest(EXCLUDE_ANCESTOR_SELECTOR)) { excludedByAncestor++; return; }

    const rawUrl = pickBestSourceUrl(img);
    if (!rawUrl) { excludedByNoUrl++; return; }

    // data:URL（インラインの極小アイコンなど）は生成画像ではないことが多いので除外
    // （blob: URLは後段でdata:URLに変換するため、ここでは除外しない）
    if (rawUrl.startsWith("data:")) { excludedByDataUrl++; return; }

    // SVG（ベクター画像）はGeminiのロゴ・アイコン類でよく使われる形式で、
    // AIが生成する画像（写真・イラスト）は通常ラスター画像（png/jpg/webp等）
    // なので、拡張子が.svgのものは除外する
    if (/\.svg(?:[?#]|$)/i.test(rawUrl)) { excludedBySvg++; return; }

    // 読み込み中・デコード中でまだピクセルデータが確定していない画像は
    // （生成アニメーション中の一時的なプレースホルダー等）、正しくcanvasに
    // 描き写せないため除外する
    const width = img.naturalWidth || img.width || 0;
    const height = img.naturalHeight || img.height || 0;
    if (!img.complete || width === 0 || height === 0) {
      excludedByIncomplete++;
      return;
    }

    // アイコン・アバター・ロゴなど、生成画像ではない小さな画像を除外する
    if ((width > 0 && width < 128) || (height > 0 && height < 128)) {
      excludedBySize++;
      console.log(`[Gemini画像DL][debug] サイズで除外: ${width}x${height} ${rawUrl.slice(0, 100)}`);
      return;
    }

    // ファイル名やパスに以下のような単語を含むものは、ユーザーアイコンや
    // Gemini自体のロゴ・装飾アイコンである可能性が高いため除外する
    // ("sparkle" はGeminiのキラキラマークのロゴファイル名に含まれる)
    if (/avatar|logo|favicon|profile|sparkle|spinner/i.test(rawUrl)) { excludedByKeyword++; return; }

    console.log(`[Gemini画像DL][debug] 候補に採用: ${width}x${height} ${rawUrl.slice(0, 100)}`);
    qualifyingImages.push({ img, rawUrl: getHighResolutionUrl(rawUrl) });
  });

  console.log("[Gemini画像DL][debug] 除外内訳:", {
    excludedByAncestor,
    excludedByNoUrl,
    excludedByDataUrl,
    excludedBySvg,
    excludedByIncomplete,
    excludedBySize,
    excludedByKeyword,
    残った候補: qualifyingImages.length,
  });

  // blob: URLの変換など、非同期処理が必要なため for...of で順番に処理する
  const resolvedUrls = [];
  for (const { img, rawUrl } of qualifyingImages) {
    const resolved = await resolveDownloadableUrl(img, rawUrl);
    if (resolved) resolvedUrls.push(resolved);
  }

  // 重複するURL（同じ画像を2回取得してしまった場合）を除去して返す
  return Array.from(new Set(resolvedUrls));
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
        const imageUrls = await extractGeminiImageUrls();
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
