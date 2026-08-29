# このリポジトリについて

AI音楽（Suno）を制作し、RouteNote経由で配信するプロジェクトのドキュメント管理リポジトリ。
**リモート（claude.ai/code）とローカルPCの両方のセッションから編集される。**

ブランチ：`claude/new-session-8v0hvp`

---

## 📍 現況（2026-08-24）

| 名義 | 状態 |
|---|---|
| **Level Trim** | 全6曲。#1 `Idle Loop` はRouteNote提出済み・**Pending Moderation**（リリース日 9/6）。#2〜#6 は音源結合まで完了、**未試聴・44.1kHz変換未実施・ジャケット未生成** |
| **Ongaku Toshokan** | 京都アンビエント10曲。**MP3のスペック未確認**・名義の重複チェック未実施・アルバム名未確定・ジャケット未着手 |

**いま最優先の3件**
1. Warm Cache の末尾を 5:45 に詰める（ハミング開始点とカット位置が一致・余裕ゼロ）
2. Ongaku Toshokan の MP3 が 320kbps/44.1kHz か `ffprobe` で確認
3. YouTube @ongakutoshokan の収益化状態を確認（混ぜる前に）

---

## 📂 どの文書を読むか（**必要なものだけ読むこと**）

全文書を読むと約45,000トークン消費する。**タスクに応じて1〜2ファイルだけ開く。**

| やること | 開くファイル |
|---|---|
| 曲を作る・プロンプトを見る | `docs/level-trim/prompts.md` |
| 日程・リリース計画 | `docs/level-trim/release-plan.md` |
| 規約・配信先・AI環境・Spotify仕様 | `docs/policy.md` ← **両プロジェクト共通** |
| 音源制作の経緯・結合手法 | `docs/level-trim/master.md` |
| 未対処のレビュー指摘 | `docs/level-trim/review-2026-08-24.md` |
| 京都アルバムの作業 | `docs/ongaku-toshokan/album.md` |
| 市場・ジャンルの戦略検討 | `docs/level-trim/market-research-2026-08.md` |
| 過去の経緯を遡る | `docs/*/archive/` ← **通常は開かない** |

各文書は自分の担当範囲だけを持ち、重複させない。**同じ情報を2箇所に書かないこと。**

---

## ⚠️ ドキュメント運用のルール（厳守）

過去に**ローカルとリポジトリで同じ文書が別名で二重管理され、どちらが正か分からなくなる事故**が起きた。

1. **ドキュメントの唯一の置き場は `docs/` 配下。** ローカルの音源フォルダ内にコピーを作らない
2. **セッション開始時に `git pull origin claude/new-session-8v0hvp`**
3. **編集したらその場で commit & push。**「あとでまとめて」は禁止
4. **ファイル名の規約**
   - 生きている文書（随時更新）：`master.md` `prompts.md` `release-plan.md` `policy.md` `album.md`
   - スナップショット：`handoff-YYYY-MM-DD.md` `review-YYYY-MM-DD.md` `market-research-YYYY-MM.md`
   - 日付は必ず `YYYY-MM-DD`。`handoff20260823.md` のような形式を新たに作らない
5. **古くなった文書は削除せず `archive/` に移す**

---

## 音源・画像ファイル

**リポジトリでは管理しない**（`.gitignore` 済み）。WAVは1曲80MB前後になる。

**推奨構成**：このリポジトリを `RouteNote/` 直下にcloneし、音源フォルダと同居させる。

```
RouteNote/                 ← ここでgit管理
├── CLAUDE.md
├── docs/
├── Level Trim/            ← .gitignore対象
└── Ongaku Toshokan/       ← .gitignore対象
```

完成したジャケット画像だけ残したい場合は `git add -f` で個別に追加する。

---

## 技術的な注意点（頻出）

### ファイル名
- **日本語を使わない** — ffmpegでエンコードエラーになる
- **`#` を使わない** — シェルでコメント開始文字として扱われる（`02 Warm Cache.wav` のように番号だけにする）

### 音源変換
RouteNoteの受付規格は **MP3(320kbps/44.1kHz)** または **FLAC(44.1kHz)** のみ。Sunoの書き出しは48kHz。

```bash
ffmpeg -i in.wav -af "aresample=resampler=soxr:precision=28" \
  -ar 44100 -map_metadata -1 out.flac
```

- `-map_metadata -1` は **"made with suno" の埋め込みメタデータ削除のため必須**
- 48000→44100 は整数比でないためリサンプラーを明示する
- **非可逆音源（MP3/AAC）からFLACを作っても品質は戻らない。** 必ず元WAVから変換する

### RouteNote入稿（AI楽曲の要件）
詳細は `docs/policy.md`。要点だけ：

- AI企業名をクレジット・言及しない
- 主要アーティストを **Producer** として記載
- C/Pラインに**本名（Satoshi Kawakami）**
- **YouTube Content ID のチェックを外す**
- **提出直前に必ず公式ページを再確認する**（RouteNote自身が「AIリリースの要件は常に変わり続けている」と明言）

### 規約情報の扱い
- 文書内の情報は**下調べであり最終根拠ではない**。各判定に「確認済み／未確認」と確認日を明記する
- 二次情報と一次情報が食い違ったら一次情報を優先し、その旨を書く
- 2026年のトレンド系記事にはAI生成のSEOブログが多い（accio.com / soundverse.ai / audiartist.com / insmelo.com 等）。根拠にしない

---

## ユーザー自身の操作が必要なこと（アシスタントは代行不可）

Suno生成 / Canvaリサイズ / RouteNoteのログイン・アップロード・規約同意 / Spotify for Artistsのclaim / YouTubeへの投稿

→ **スクリーンショットを見ながら次の操作を案内する形で伴走する。**

アシスタントが実行できるのは、ローカルの ffmpeg/ffprobe での変換・解析まで（librosa等は未インストール）。
