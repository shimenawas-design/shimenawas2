# 引継ぎ書 — Gemini 画像一括ダウンローダー（Chrome拡張機能）

作成日: 2026-08-24
最終更新: 2026-08-24（ローカルPCでの作業により、既知の不具合はすべて解消・実機確認済み）
リポジトリ: `shimenawas-design/shimenawas2`
作業ブランチ: `claude/gemini-batch-image-downloader-626pj5`
このドキュメント更新時点の最新コミット（origin に push 済み）: `dba388a`

このドキュメントは、別の環境（リモートのClaudeセッションや他の開発者）に
作業を引き継ぐための状況整理メモです。「何を作っていて」「何が終わっていて」
「何が未解決で」「次に何をすればよいか」をまとめています。

---

## 1. 作っているもの

Google Gemini（`https://gemini.google.com/`）のチャット画面に表示された
生成画像を、ポップアップのボタン1つで一括ダウンロードするChrome拡張機能
（Manifest V3）。現在のバージョン: `1.0.2`。

- `manifest.json` — 拡張機能の設定ファイル
- `content.js` — Geminiのページに注入され、自動スクロール→画像URL抽出を行う。
  抽出した `blob:` 画像は、`<img>` の描画済みピクセルデータをcanvasに
  描き写して `data:` URLに変換してから返す（理由は3節・6節を参照）
- `background.js` — ポップアップとcontent.jsの橋渡し役。実際のダウンロード
  （`chrome.downloads` API）を行うサービスワーカー。`data:` URLに対して
  Chromeが指定ファイル名を無視することがある問題への対策として、
  `chrome.downloads.onDeterminingFilename` でファイル名を強制指定している
- `popup.html` / `popup.css` / `popup.js` — ツールバーアイコンをクリックした
  ときのUI
- `icons/` — 拡張機能アイコン（Python製スクリプトで生成した簡易PNG）
- `docs/INSTALL_README.txt` — 非技術者向けインストール手順書（配布ZIPに同梱。
  複数人での動作確認用に、うまくいかない場合のログ報告手順も記載済み）
- `scripts/build-zip.sh` — 配布用ZIPを作るビルドスクリプト（Mac/Linux想定。
  Windows単体では `python3` はあっても `zip` コマンドが無いことが多く、
  その場合はPowerShellの `Compress-Archive` で代用する。`dist/`はgitignore
  対象なので毎回再生成する）

---

## 2. 現在の状態（結論）

**画像の一括ダウンロードは、実機（開発者本人のログイン済みChrome、実際に
生成した画像）で一気通貫の成功を確認済み。** ポップアップの「一括ダウン
ロードを実行」ボタンを押すだけで、指定した接頭辞（例: `Route_`）付きの
連番ファイル名（`Route_001.png` 〜）で、生成画像が正しく保存されることを
確認した。

これまでに見つかった不具合は以下の2つで、両方とも修正済み・push済み。

1. **画像が1件も見つからない問題**（コミット `302cc97`）
   抽出ロジック自体は生成画像（`<button>`内の`<img>`、`blob:` 形式の
   URL）を正しく候補として見つけられていたが、その `blob:` URLに対して
   `fetch()` / `XMLHttpRequest` で中身を取得しようとすると、ネットワーク
   リクエストすら発生せず常に失敗することが分かった（Geminiページ自身の
   コンソールで直接再現。Gemini側のCSPで `img-src` はblob:を許可するが
   `connect-src` は許可していないためと見られる）。
   → `<img>` が既に保持しているデコード済みピクセルデータをcanvasに
   描画し `toDataURL()` で取り出す方式に変更して解決。

2. **ファイル名の接頭辞が反映されず「ダウンロード.png」等になる問題**
   （コミット `dba388a`）
   `chrome.downloads.download()` の `filename` オプションは、`data:` URL
   （このアプリの画像は変換後すべてこれ）に対しては無視されることがある
   既知のChromeの挙動で、実機テストで実際に発生した。
   → `chrome.downloads.onDeterminingFilename` イベントでファイル名を
   強制的に上書きするよう変更して解決。実機で `Route_001.png` 〜
   `Route_006.png` のように正しく連番保存されることを確認済み。

- **インストール・UI操作は問題なく動作する**ことを実機で確認済み
  （ポップアップの表示、プレフィックス入力、ボタン押下、進捗表示など）
- 配布用ZIP `gemini-image-bulk-downloader-v1.0.2.zip` をビルド済み

### 未検証・今後の課題（3節参照）

- 大量の画像や長いチャット履歴での自動スクロールのロングラン動作
- 開発者本人以外の複数アカウント・複数チャットでの横展開確認
- Chromeウェブストアでの正式公開は今のところ想定しておらず、
  「パッケージ化されていない拡張機能」としての配布のみ

---

## 3. これまでの経緯（時系列）

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
     除外条件に追加
5. 上記修正版を試したところ、今度は**「生成された画像が見つかりません
   でした」と1件も抽出されなくなった**（ロゴも含めて0件）。除外セレクタ
   に含めていた `button` を外した（多くのAI画像生成UIは、画像をクリック
   で拡大表示できるよう`<button>`で画像を囲むことが多く、それに巻き込ま
   れて除外されていた）ことで、ここまでは前進した
6. **（ローカルPC作業）** ログイン済みの実際のGeminiでDOM構造・ネット
   ワーク挙動を直接検証し、上記2節の「1」の根本原因（blob: URLへの
   fetch失敗）を特定・修正（コミット`302cc97`）。抽出フィルタが読み込み
   中のプレースホルダー画像を誤って拾ってしまう問題もあわせて対処。
   このタイミングでバージョンを1.0.1に上げ、ZIPを再ビルド
7. **（ローカルPC作業・実機テスト）** ユーザー本人が拡張機能を実際に
   Chromeへ読み込んで一括ダウンロードを実行し、画像自体は正しくすべて
   保存されることを確認。ただし保存されたファイル名が
   「ダウンロード.png」「ダウンロード (1).png」等になってしまい、
   指定した接頭辞が反映されていない不具合を発見。上記2節の「2」の
   原因（`chrome.downloads.download()`のfilenameがdata: URLに対して
   無視される既知のChromeの挙動）を特定・修正（コミット`dba388a`）。
   再度実機で確認し、`Route_001.png`のように正しい連番ファイル名で
   保存されることを確認。バージョンを1.0.2に上げ、origin へ push 済み

---

## 4. 次にやること（優先順位順）

現時点で致命的な既知の不具合は無い状態。以降は品質を高めるための
任意項目として:

1. **他の画像枚数・チャットパターンでの追加確認**
   検証済みなのは「画像2枚のチャット」「画像6枚のチャット」の2パターン。
   非常に長いチャット履歴（自動スクロールが何十回も必要なケース）や、
   1チャット内に生成画像が大量にある場合の動作は未検証
2. **複数人での配布検証**
   `dist/gemini-image-bulk-downloader-v1.0.2.zip` と
   `docs/INSTALL_README.txt` を使って、開発者以外の複数人に実際に
   インストール・ダウンロードしてもらう。うまくいかない場合は
   README記載の手順でF12コンソールの `[Gemini画像DL][debug]` ログを
   集めてもらうと、原因調査がスムーズ
3. **（任意）Chromeウェブストアでの正式公開を検討する場合**
   現状は「パッケージ化されていない拡張機能」としての配布のみを想定
   した作りになっている。ウェブストア公開には別途、審査要件の確認
   （権限の説明文、プライバシーポリシー等）が必要になる

---

## 5. 開発時の作業フロー（コード変更〜確認）

1. コードを変更する（`content.js` / `background.js` / `popup.*`）
2. `chrome://extensions` を開き、この拡張機能のカードにある
   🔄（更新）ボタンを押す（拡張機能全体の再読み込み）
3. **`content.js`を変更した場合は、Geminiのタブも必ず再読み込み**する
   （更新ボタンだけでは既存タブに新しいcontent.jsが反映されないため）
4. `background.js`のログは拡張機能カードの「Service Worker」リンクから
   開発者ツールを開いて確認する
5. `content.js`のログはGeminiのタブ上でF12を押して確認する
   （`[Gemini画像DL][debug]` のログで、各除外フィルタの通過件数が
   確認できるようになっている）
6. 問題なければ `git add` → `git commit` → `git push`
7. 配布用ZIPを作り直す場合は `./scripts/build-zip.sh` を実行する
   （Windows単体で `zip` コマンドが無い場合は、PowerShellの
   `Compress-Archive` で `manifest.json` / `background.js` / `content.js`
   / `popup.html` / `popup.css` / `popup.js` / `icons/` /
   `docs/INSTALL_README.txt` を `dist/<パッケージ名>-v<バージョン>/`
   にフラットにコピーしてから `Compress-Archive -Path
   "<staging>\*" -DestinationPath <zip> ` する。manifest.jsonを
   PowerShellで読む際は `[System.IO.File]::ReadAllText(path,
   [System.Text.Encoding]::UTF8)` のように明示的にUTF-8で読まないと、
   日本語部分が文字化けして`ConvertFrom-Json`が失敗するので注意）

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
- **Geminiページの生成画像（`blob:` URL）はfetch()/XHRで取得できない**
  （CSPの`connect-src`制限とみられる。`img-src`はblob:を許可するため
  `<img>`としての表示自体は問題ない）。そのため、content.js側では
  fetchではなく、既に描画済みの`<img>`をcanvasに描いて`toDataURL()`で
  data: URLとして取り出す方式にしている（fetchが使える場合に備えて
  フォールバックとしては残してある）
- **`chrome.downloads.download()`の`filename`オプションは、`data:` URL
  に対して無視されることがある既知のChromeの挙動**。background.jsでは
  `chrome.downloads.onDeterminingFilename`イベントで、ダウンロードID
  ごとに希望のファイル名を強制的に上書きすることで対処している
- **画像抽出は「特定のクラス名に依存しない」汎用スキャン方式**
  （Shadow DOM内も含めて全`<img>`を集め、サイズ・拡張子・ファイル名の
  パターン・置かれている場所で絞り込む）。Googleの仕様変更で
  クラス名が変わってもある程度動き続けることを狙っている

---

## 7. リポジトリ・ブランチ情報

```
リポジトリ: https://github.com/shimenawas-design/shimenawas2
ブランチ:   claude/gemini-batch-image-downloader-626pj5
最新コミット（origin に push 済み）: dba388a
```

ローカルでの取得例:

```bash
git clone https://github.com/shimenawas-design/shimenawas2.git
cd shimenawas2
git checkout claude/gemini-batch-image-downloader-626pj5
```

別のClaudeセッション（リモート/クラウド環境）に引き継ぐ場合は、上記の
リポジトリ・ブランチを渡した上で、このファイル（`docs/HANDOVER.md`）を
最初に読んでもらうよう伝えると、現状把握がスムーズです。
