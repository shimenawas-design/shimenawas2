# RouteNote ブラウザ自動操作のレシピ

2026-09-12 の5曲入稿で確立した手順。Claude in Chrome（`mcp__claude-in-chrome__*`）を使う。

## 起動

ツールは deferred なので、最初に1回でまとめてロードする。

```
ToolSearch query: select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__find,mcp__claude-in-chrome__form_input,mcp__claude-in-chrome__file_upload,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__tabs_create_mcp
```

## ⚠️ タブが最前面でないとクリックが無反応になる

CDP の入力イベントは背面タブに届かない。クリックしたのに何も起きない場合、まずこれを疑う。
**RouteNote 作業専用のウィンドウを立ち上げて常に前面に置く**のが確実（ユーザー提案・合意済み）。

クリック座標が本当に届いているかの検証はヒットテストで行う：

```javascript
document.addEventListener('mousedown', e => {
  window.__hit = { x: e.clientX, y: e.clientY, el: e.target.outerHTML.slice(0, 200) };
}, { once: true });
```

クリック後に `window.__hit` を読めば、どの要素に当たったかが分かる。

## 入力方法の使い分け

| 対象 | 方法 |
|---|---|
| 普通のテキスト入力 | `form_input` |
| **Artist Name** | 実クリックで入力 → ドロップダウン最下部の「Create a new profile」を実クリック |
| **Genre** | `#genre` のリスト項目を実クリック（readonly input なので入力は効かない） |
| チェックボックス | `form_input` または実クリック |
| **Save ボタン** | 実クリック |
| ファイル | `file_upload`（**10MB上限**） |

`form_input` で埋めた値は React の state に乗らないことがある。保存後に必ず再読み込みして検証する。

## Save は「タイムアウトしても成功している」

Save の実クリックは CDP 側でタイムアウトを返すことが多いが、**POST 自体は完走している**。
エラーとして扱わず、20秒以上待ってからページを再読み込みして値を確認する。

## ファイルサイズの壁

`file_upload` は 10MB が上限。

- ジャケット（1〜1.5MB）→ 自動でアップロードできる
- 音源（140〜157MB）→ **不可能。ユーザーに手動アップロードを依頼して待つ**

ローカルHTTPサーバ経由で DataTransfer に流し込む手も試したが、CORS と private network access で失敗した。追わなくてよい。

## 壊れたリリース枠は作り直す

一度 Album Details の保存に失敗し続けるリリース枠が発生した（UPC 5064115864921）。
4通りの方法を試してすべて失敗。**復旧を試みるより、新しいリリースを作り直すほうが速い。**
壊れた枠は Discography のゴミ箱アイコンから削除できる。

## 検証用の一発クエリ

```javascript
`url=${location.pathname} | inReview=${
  document.body.innerText.match(/In Review[\s\S]{0,40}?(\d+)/)?.[1]
} actionNeeded=${
  document.body.innerText.match(/Action Needed[\s\S]{0,40}?(\d+)/)?.[1]
}`
```

## 配信済みリリースは編集できない

Release Details の「Edit Album Details」リンクは配信申請後に無効化される（クリックしても何も起きない）。
メタデータの修正はサポート依頼が必要。**入稿前の確認が唯一の防衛線。**
