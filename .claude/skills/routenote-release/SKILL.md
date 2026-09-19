---
name: routenote-release
description: RouteNoteへのAI楽曲の入稿から配信申請までを実行する。「今週分のアップロード」「RouteNoteに入稿して」「リリース作業を進めて」等で起動。Ongaku Toshokan / Level Trim / Hollow Rotor / Vermilion Gate の4名義すべてに対応。
---

# RouteNote 入稿〜配信スキル

RouteNote の5ステップリリースウィザードをブラウザ自動操作で完走させる。
音源ファイル（100MB超）のアップロードだけはユーザーが手動で行い、それ以外はすべて自動化できる。

## 0. 着手前に必ず読むもの

1. **`docs/` on GitHub** — `shimenawas-design/shimenawas2` branch `claude/new-session-8v0hvp`
   全AI音楽プロジェクトの唯一の正典。`gh api` で読む（ローカルにgitリポジトリは無い）。
   - `docs/policy.md` — 全名義共通の入稿要件
   - `docs/<名義>/master.md` — 名義ごとの曲目・進捗
2. **入稿予定フォルダ** — `C:\Users\shime\Downloads\RouteNote\入稿予定\<YYYY-MM-DD>\入稿情報.md`
   その週に出す曲・音源パス・ジャケットパス・UPCが書いてある。無ければ作る。

作業で新しく判明した RouteNote の仕様は、**必ず両方に追記してから終わる**。

## 1. 絶対に守るルール

### 🚫 Record Label Name に本名を入れない
**Label ＝ アーティスト名義** と完全に一致させる。`Ongaku Toshokan` の曲なら Label も `Ongaku Toshokan`。
本名 `Satoshi Kawakami` を使うのは **C/Pライン（Composition Copyright / Sound Recording Copyright）と Composer 欄だけ**。
配信申請後はUI上からメタデータを修正できない（Release Details の「Edit Album Details」リンクは無効化される）。取り返しがつかない。

### ジャケットは JPG 必須
PNG はアップロード時にリジェクトされる。3000×3000・RGB・25MB未満。

```python
from PIL import Image
im = Image.open(src).convert('RGB')
im.resize((3000, 3000), Image.LANCZOS).save(dst, 'JPEG', quality=92)
```

### Ambient というジャンルは存在しない
選択肢は Alternative / Anime / Blues / Brazilian / Children's Music / Christian & Gospel / Classical / Comedy / Country / Dance / Easy Listening / Electronic / Enka / Fitness & Workout / French Pop / German Folk / German Pop / Hip Hop/Rap / Holiday / Indian / **Instrumental** / J-Pop / Jazz / K-Pop / Karaoke / Kayokyoku / Korean / Latin / New Age / Opera / Pop / R&B/Soul / Reggae / Rock / Singer/Songwriter / Soundtrack / Spoken Word / Vocal / World。

| 名義 | ジャンル |
|---|---|
| Ongaku Toshokan | Instrumental |
| Level Trim | Electronic |
| Hollow Rotor | **Fitness & Workout**（ユーザー決定、2026-09-19） |
| Vermilion Gate | Instrumental |

### 名義の表記ゆれに注意
既存カタログに `Ongaku toshokan`（t小文字）が混在している。新規は必ず `Ongaku Toshokan`。

### タイトルは英語のみ
既存曲が英語のみで登録済みのため統一する。

## 2. 全曲共通の入力値

| 項目 | 値 |
|---|---|
| Language | English |
| Does this release contain cover versions? | No |
| Compilation Album | No |
| Composer (Writers) | First `Satoshi` / Last `Kawakami` |
| Does this release contain lyrics? | No |
| Contributors | Producer ＝ アーティスト名義 |
| Composition Copyright | 西暦 / `Satoshi Kawakami` |
| Sound Recording Copyright | 西暦 / `Satoshi Kawakami` |
| **Record Label Name** | **アーティスト名義と同じ** |
| Originally Released | 入稿日 |
| Pre Order Date | 空欄 |
| **Sales Start Date** | **曲ごとに指定**（2026-09-17方針。日付は `docs/<名義>/master.md` の入稿スケジュール参照）。審査前の指定でも保存・受理される。画面上は「Release Date」と表示される。**指定日まで保留されるかは最初の承認が出るまで未確認**（`docs/policy.md` 5.1） |
| Explicit Content | Not Explicit |
| Manage Stores | Select all stores、**YouTube Content ID だけチェックを外す**（AI楽曲は対象外） |
| Territories | 空欄＝全世界 |
| 配信モデル | Distribute **Free** |

公開日は入稿日ではなくSales Start Dateで決める（入稿と公開を切り離す方針、2026-09-17）。

## 3. 手順

ウィザードは Album Details → Add Audio → Add Artwork → Manage Stores → Finish: Distribute の5段。
ブラウザ操作の具体的なコツは [automation.md](automation.md) を参照。

1. **Create Release** で枠を作る。UPCが発番されるので `入稿情報.md` に記録する。
2. **Album Details** を上表どおり埋めて Save。
   - Artist Name は入力後、ドロップダウン最下部の **「Create a new profile」** を実クリックして確定する。選ばないと保存が弾かれる。
   - Genre は読み取り専用のカスタムUI。`#genre` のリスト項目を実クリックする。
   - 保存後20秒以上待ってから再読み込みして検証する。
3. **Add Audio** — 音源は100MB超のため `file_upload`（10MB上限）では送れない。**ユーザーに依頼して待つ。** 複数曲あるときは、先に全曲の Album Details・Artwork・Manage Stores まで済ませてから、音源をまとめて依頼する（各曲のUPCと `addaudiomp3/form/<UPC>` を伝える）。
   - **トラック情報画面（Track Parameters）で「Save and Continue」を押さない**（ユーザーにも伝える）。下記の末尾欠落が起きる。
   - 音源が入ったら、配信申請の前に**全曲のトラック情報を読み取りで照合**する（[automation.md](automation.md)の照合スクリプト）。照合項目は、トラック側アーティスト・作曲者（Satoshi Kawakami）・制作者・役割（Producer）・タイトル。
4. **Add Artwork** — JPGを `file_upload` で送る。**Chromeが画面に見えていないとアップロードが止まる**（[automation.md](automation.md)）。
5. **Manage Stores** — Select all stores → YouTube Content ID のチェックを外す。全選択で外れたまま残る店が2つある（内部ID did48・did50。Amazonや韓国系ストアなどAI楽曲の対象外の店と思われるが未確認）。
6. **Finish: Distribute** — Terms のチェックボックス → Distribute Free → **確認モーダルの「Complete Release」を必ずクリック**。

### ⚠️ Complete Release モーダルを押し忘れると80%で止まる
「Distribute Free」を押しただけでは配信申請が完了しない。直後に出る確認モーダルの「Complete Release」を押して初めて In Review になる。押し忘れてもエラーは出ず、Discography 上で静かに80%のまま残る。

### ⚠️ トラックメタデータの末尾1文字欠落（原因判明、2026-09-19）
トラック情報画面（`/rn/audiometadata/<node_id>/edit`）で「Save and Continue」を押すたびに、**作曲者・制作者・役割が末尾1文字ずつ削られる**（`Satoshi`→`Satosh`→`Satos`、`Producer`→`Produce`）。ブラウザ自動操作（プログラム経由の入力・送信）で起きる。ユーザー本人の手動操作では、9/19の10曲とも起きなかった。
サーバーは画面の入力欄ではなく、隠し項目 `composer_value`／`composer2_value`／`contributors_name`／`contributors_role` を正として保存する。
**直し方**：画面操作ではなくフォームを直接POSTし、各値の**末尾に捨て文字を1つ足して**送る（サーバーが末尾1文字を落とすため、`Satoshix`→`Satoshi`になる）。手順は [automation.md](automation.md)。
"Publishing Information" 警告モーダルは、この食い違いを知らせるものだが、出ないこともある。

### ⚠️ トラック側アーティストが別名義になることがある（2026-09-19）
音源を入れた後、トラック側のアーティスト欄（読み取り専用）に、**直近に作った別名義**が入ったことがある（Fresh Green が Hollow Rotor になった）。アルバム側は正しいままで、配信申請後は直せない。**音源を入れたら必ず全曲を照合する。** 直すには、トラック情報画面で、Artist欄に名義を入力し「Create a new profile」を選んで保存する（ここでも末尾欠落が起きるので、続けて直接POSTで直す）。

### ⚠️ 「Duplicate audio file loaded」（2026-09-19）
音源は最初のアップロードで登録済みで、「Save and continue」が重複として拒否される状態。トラック情報画面から保存しても Step 2 は完了にならない。**リリース画面の「Delete Track」でトラックを削除し、音源を1回だけ入れ直す**と解決する。削除するのはRouteNote上の下書きトラックだけで、手元の音源には影響しない。

## 4. 完了確認

`https://www.routenote.com/rn/releases` を開き、In Review 件数が増えていることを確認する。
Action Needed に残っていたら未完了。

## 5. 終わったら記録する

- `入稿情報.md` に UPC と ✅入稿完了 を書く
- `docs/<名義>/master.md` を更新して GitHub に push（`gh api` で Contents API、base64 + JSON + PUT）
- 新しく判明した RouteNote の挙動は `docs/policy.md` にも追記する
