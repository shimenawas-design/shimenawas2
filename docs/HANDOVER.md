# 引継ぎ書 — Gemini 画像一括ダウンローダー（Chrome拡張機能）

作成日: 2026-08-24
リポジトリ: `shimenawas-design/shimenawas2`
作業ブランチ: `claude/gemini-batch-image-downloader-626pj5`
このドキュメント作成時点の最新コミット: `aab927c`

このドキュメントは、リモート環境からローカルPCでの作業に引き継ぐための
状況整理メモです。「何を作っていて」「何が終わっていて」「何が未解決で」
「次に何をすればよいか」をまとめています。

---

## 1. 作っているもの

Google Gemini（`https://gemini.google.com/`）のチャット画面に表示された
生成画像を、ポップアップのボタン1つで一括ダウンロードするChrome拡張機能
（Manifest V3）。

- `manifest.json` — 拡張機能の設定ファイル
- `content.js` — Geminiのページに注入され、自動スクロール→画像URL抽出を行う
- `background.js` — ポップアップとcontent.jsの橋渡し役。実際のダウンロード
  （`chrome.downloads` API）を行うサービスワーカー
- `popup.html` / `popup.css` / `popup.js` — ツールバーアイコンをクリックした
  ときのUI
- `icons/` — 拡張機能アイコン（Python製スクリプトで生成した簡易PNG）
- `docs/INSTALL_README.txt` — 非技術者向けインストール手順書（配布ZIPに同梱）
- `scripts/build-zip.sh` — 配布用ZIPを作るビルドスクリプト（`dist/`に出力、
  `.gitignore`済みなので毎回再生成する）

---

## 2. 現在の状態（結論）

**追記（2026-08-24 ローカル作業）:** 画像抽出ができない問題の原因を
特定し、修正した（コミット `302cc97`）。ログイン済みの実際のGeminiで
生成画像入りチャットを開き、DOM構造とネットワーク挙動を直接確認した
ところ、生成画像は `<button>` の中の `<img>`（`blob:` 形式のURL）と
して表示されており、button除外を外した抽出ロジック自体は正しく候補を
見つけられていた。しかし**その`blob:` URLに対して`fetch()`/XHRで
中身を取得しようとすると、ネットワークリクエストすら発生せず常に
失敗する**（ページ自身のコンソールで直接再現。Gemini側のCSPで
`img-src`はblob:を許可するが`connect-src`は許可していないためと
見られる）ことが判明し、これが「1件も見つからない」症状の真因
だった。`<img>`が既に保持しているデコード済みピクセルデータを
canvasに描画し`toDataURL()`で取り出す方式に変更し、実際に2枚の
生成画像で変換成功を確認済み（詳細は content.js のコメントと
コミットメッセージを参照）。バージョンを1.0.1に上げ、配布用ZIPを
再ビルドし、`docs/INSTALL_README.txt`にテスター向けのログ報告手順
を追記した。ただし、この修正は**JavaScriptのシミュレーションでの
検証のみ**で、実際にChromeへ拡張機能として読み込んでポップアップの
ボタンから一気通貫でダウンロードが成功するかは、ローカルPCでの
実機確認がまだ必要（下記4節参照）。

- **インストール・UI操作は問題なく動作する**ことを実機で確認済み
  （ポップアップの表示、プレフィックス入力、ボタン押下、進捗表示など）
- 画像検出ロジック自体とblob→data URL変換は、実際のGeminiページ上での
  JavaScript直接検証により動作を確認済み（上記追記を参照）。ただし
  拡張機能としてインストールした状態での一気通貫の実機確認はまだ
  行われていない

## 3. これまでの経緯（時系列・詳しいものから直近まで）

1. 初版実装（機能要件どおりのMVP。画像抽出セレクタは未検証の推測ベース）
2. ユーザビリティ改善: 自動スクロール（遅延読み込み対策）、セレクタの
   多重防御、複数ダウンロード許可への案内、進捗のリアルタイム表示
3. ZIP配布に対応。ここで実機テストが始まり、立て続けに問題が発覚：
   - ZIPがフォルダで二重に入れ子になり、Chromeの「拡張機能を読み込む」
     ダイアログでmanifest.jsonが見つからない → ZIP直下にファイルを
     フラットに配置する構成へ変更（`scripts/build-zip.sh`参照）
   - 日本語ファイル名がWindowsで文字化け → ファイル名をASCII
     （`INSTALL_README.txt`）に変更
   - `manifest.json`に`default_locale: "ja"`を指定していたが対応する
     `_locales/`が無く「Default locale was specified, but _locales
     subtree is missing.」エラー → `default_locale`自体を削除
   - フォルダ選択ダイアログでファイルが表示されず操作ミス
     → 説明書に「フォルダ選択画面はフォルダしか出ない仕様」「ダブル
     クリックで中に入らずシングルクリックで選ぶ」ことを明記
   - `Could not establish connection. Receiving end does not exist.`
     エラー → 拡張機能インストール前から開いていたタブには
     content scriptが自動注入されない仕様が原因。タブ再読み込みで解消。
     あわせてこのエラーを検知して日本語の案内文に変換する処理を追加
4. ここでようやく「ダウンロードには成功」の報告が来たが、**保存された
   のはGemini自体のロゴ（キラキラマーク、`.svg`）1枚だけ**で、本来の
   生成画像3枚が抽出されていなかった。原因を2つ特定：
   - ロゴの`.svg`ファイルがドメインベースのセレクタ
     （`googleusercontent.com`等）にたまたまマッチし、除外条件
     （`avatar`/`logo`/`favicon`/`profile`）もすり抜けていた
   - 「セレクタ優先探索→0件ならフォールバック」という2段構えのロジックで、
     ロゴが1件見つかったことで件数が0にならず、フォールバック（全`<img>`
     を対象にした広域探索）が実行されなかった
   - → 対策: 常に「ページ内の全`<img>`要素（Shadow DOMの中も含めて
     再帰的に）」をディープスキャンする一本化した方式に変更。
     `.svg`拡張子と`sparkle`/`spinner`というファイル名パターンを
     除外条件に追加。blob: URL（ページ内限定の一時URL）は
     content.js側でdata: URLに変換してからbackground.jsに渡す方式も追加
     （background.js側からはblob: URLに直接アクセスできないため）
5. 上記修正版を試したところ、今度は**「生成された画像が見つかりません
   でした」と1件も抽出されなくなった**（ロゴも含めて0件）。フィルタが
   強くなりすぎて本物の画像まで除外している可能性が高いと判断。
   最有力の仮説として、除外セレクタに含めていた `button` を外した
   （多くのAI画像生成UIは、画像をクリックで拡大表示できるよう
   `<button>`で画像を囲むことが多く、それに巻き込まれて除外されて
   いた可能性）。
   **この修正（コミット`aab927c`）はまだ実機で確認できていない。**

---

## 4. 次にやること（優先順位順）

### ステップ1: 最新版を実機で試す
1. `git pull` して最新コミット（`aab927c`以降）を取得
2. `./scripts/build-zip.sh` を実行して`dist/`にZIPを作るか、リポジトリの
   ルートフォルダ（`manifest.json`がある場所）をそのまま
   `chrome://extensions` の「パッケージ化されていない拡張機能を読み込む」
   で読み込む（開発中はZIP化せず直接ソースフォルダを読み込む方が
   コード変更のたびにZIPを作り直さなくて済むので楽）
3. 既存の拡張機能が入っている場合は一度「削除」してから読み込み直す
4. Geminiのタブを**再読み込み**（content.js再注入のため必須）
5. 画像を生成した状態のチャットで「一括ダウンロードを実行」を押す

### ステップ2: それでも見つからない場合はデバッグログを仕込む

`content.js` の `extractGeminiImageUrls` 関数（現在257行目付近、
`async function extractGeminiImageUrls() {` で検索）に、各フィルタ
段階の件数を出力するログを追加すると、どこで弾かれているか特定できます。
例えば以下のように書き換えます（`allImages.forEach` の中身を全て
置き換えるイメージ）:

```js
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

  allImages.forEach((img) => {
    if (img.closest(EXCLUDE_ANCESTOR_SELECTOR)) { excludedByAncestor++; return; }

    const rawUrl = pickBestSourceUrl(img);
    if (!rawUrl) { excludedByNoUrl++; return; }

    if (rawUrl.startsWith("data:")) { excludedByDataUrl++; return; }
    if (/\.svg(?:[?#]|$)/i.test(rawUrl)) { excludedBySvg++; return; }

    const width = img.naturalWidth || img.width || 0;
    const height = img.naturalHeight || img.height || 0;
    if ((width > 0 && width < 128) || (height > 0 && height < 128)) {
      excludedBySize++;
      console.log(`[Gemini画像DL][debug] サイズで除外: ${width}x${height} ${rawUrl.slice(0, 100)}`);
      return;
    }

    if (/avatar|logo|favicon|profile|sparkle|spinner/i.test(rawUrl)) { excludedByKeyword++; return; }

    console.log(`[Gemini画像DL][debug] 候補に採用: ${width}x${height} ${rawUrl.slice(0, 100)}`);
    qualifyingImages.push({ img, rawUrl: getHighResolutionUrl(rawUrl) });
  });

  console.log("[Gemini画像DL][debug] 除外内訳:", {
    excludedByAncestor, excludedByNoUrl, excludedByDataUrl,
    excludedBySvg, excludedBySize, excludedByKeyword,
    残った候補: qualifyingImages.length,
  });

  // ...この後は元のコードのまま（blob:URL変換ループ）
```

そのうえで:
1. `chrome://extensions` の対象拡張機能で「Service Worker」リンクを開く
   （background.js側のログ確認用）
2. Geminiのタブ上で F12 → Console タブを開く（content.js側のログ確認用）
3. 「一括ダウンロードを実行」を押す
4. Consoleに出た `[Gemini画像DL][debug]` のログを確認する。特に
   「発見した`<img>`の総数」が0であれば、そもそも`<img>`自体が
   見つかっていない（Shadow DOM閉じている/別の要素で描画されている等）。
   0でないのに「残った候補」が0なら、どのフィルタで何件弾かれたかが
   `除外内訳`で分かる

### ステップ3: 実際のDOM構造を目視確認する

Geminiで画像を生成した状態で、生成画像を右クリック→「検証」
（Inspect）を選ぶと、DevToolsのElementsパネルでその画像の実際の
HTML構造が見られます。確認すると良いポイント:

- `<img>`タグかどうか（`<canvas>`や背景画像(`background-image`)で
  描画されている可能性もゼロではない）
- `src`属性が `https://...`（googleusercontent.com等）か、
  `blob:https://gemini.google.com/...`か、それ以外か
- 親要素をたどっていくと `#shadow-root` という表示が出てくるか
  （出てくる場合はShadow DOM内にある証拠）
- クラス名やカスタムタグ名（`<single-image>`のような独自タグが
  実際にあるかどうか。今の実装はクラス名に依存しない汎用スキャン
  方式なので無くても動くはずだが、参考情報として有用）

この情報が分かれば、`extractGeminiImageUrls`のフィルタ条件を
ピンポイントで調整できます。

---

## 5. 開発時の作業フロー（ローカルPCでのコード変更〜確認）

1. コードを変更する（`content.js` / `background.js` / `popup.*`）
2. `chrome://extensions` を開き、この拡張機能のカードにある
   🔄（更新）ボタンを押す（拡張機能全体の再読み込み）
3. **`content.js`を変更した場合は、Geminiのタブも必ず再読み込み**する
   （更新ボタンだけでは既存タブに新しいcontent.jsが反映されないため）
4. `background.js`のログは拡張機能カードの「Service Worker」リンクから
   開発者ツールを開いて確認する
5. `content.js`のログはGeminiのタブ上でF12を押して確認する
6. 問題なければ `git add` → `git commit` → `git push`
   （このセッションで使っていたコミットメッセージ規約: 変更の背景・
   原因・対応内容を書く。フッターの `Co-Authored-By` /
   `Claude-Session` 行はローカル作業では不要）
7. 配布用ZIPを作り直す場合は `./scripts/build-zip.sh` を実行
   （`dist/`はgitignore対象なので毎回ローカルで作る）

---

## 6. 覚えておくと良い設計上の注意点

- **`default_locale`はmanifest.jsonに書かない**（`_locales/`ディレクトリを
  用意しない限りエラーになる。今は使っていない）
- **配布ZIPはフォルダで包まない**（Windowsの「すべて展開」がZIP名と
  同名のフォルダを自動生成するため、ZIP側にも同名フォルダを入れると
  二重入れ子になる）
- **配布物の日本語ファイル名は避ける**（Windows展開時に文字化けする
  ことがある。`INSTALL_README.txt`のように英数字にする）
- **content scriptは拡張機能インストール/更新前から開いていたタブには
  自動注入されない**（Chromeの仕様。タブの再読み込みが必要）
- **`blob:`形式のURLはbackground.js（別の実行コンテキスト）から直接
  ダウンロードできない**ため、content.js側で`fetch`→`data:`URLに
  変換してから渡す設計にしている
- **画像抽出は「特定のクラス名に依存しない」汎用スキャン方式**
  （Shadow DOM内も含めて全`<img>`を集め、サイズ・拡張子・ファイル名の
  パターン・置かれている場所で絞り込む）。Googleの仕様変更で
  クラス名が変わってもある程度動き続けることを狙っているが、
  裏を返すと「除外条件の付けすぎ／付けなさすぎ」のバランス調整が
  常に必要というのが現在直面している課題そのもの

---

## 7. リポジトリ・ブランチ情報

```
リポジトリ: https://github.com/shimenawas-design/shimenawas2
ブランチ:   claude/gemini-batch-image-downloader-626pj5
最新コミット（このドキュメント作成時点）: aab927c
```

ローカルでの取得例:

```bash
git clone https://github.com/shimenawas-design/shimenawas2.git
cd shimenawas2
git checkout claude/gemini-batch-image-downloader-626pj5
```

以上です。ステップ1〜3を順に試していただければ、次にどこを直せば
良いかがかなり絞り込めるはずです。良い結果でも悪い結果でも、
Console に出たログをそのまま貼っていただければ、次の一手を
具体的に判断できます。
