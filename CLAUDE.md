# このリポジトリについて

AI音楽（Suno）を制作し、RouteNote経由で配信するプロジェクトのドキュメント管理リポジトリ。
**リモート（claude.ai/code）とローカルPCの両方のセッションから編集される。**

現在のブランチ：`claude/new-session-8v0hvp`

## 進行中のプロジェクト

| 名義 | 内容 | ドキュメント |
|---|---|---|
| `Level Trim` | エンジニア向け作業用集中BGM（Electronic / IDM）。6曲シリーズ | `docs/level-trim/` |
| `Ongaku Toshokan` | 京都アンビエント・アルバム（10曲）。同一RouteNoteアカウント、名義のみ分離 | `docs/ongaku-toshokan/` |

---

## ⚠️ ドキュメント運用のルール（厳守）

過去に**ローカルとリポジトリで同じ文書が別名で二重管理され、どちらが正か分からなくなる事故**が起きた。以下を必ず守ること。

### 1. ドキュメントの唯一の置き場は `docs/<プロジェクト名>/`
ローカルの音源フォルダ内にドキュメントを置かない。**コピーを作らない。**

### 2. セッション開始時に必ず pull する
```bash
git pull origin claude/new-session-8v0hvp
```
他方のセッションが更新している可能性が常にある。

### 3. ドキュメントを編集したら、その場で commit & push する
```bash
git add -A && git commit -m "..." && git push -u origin claude/new-session-8v0hvp
```
「あとでまとめて」は禁止。**セッションを終える前ではなく、編集直後に押す。**

### 4. ファイル名は既存の命名に合わせる
- 生きている文書（随時更新）：`master.md`, `prompts.md`, `release-plan.md`
- スナップショット（作成時点で固定）：`handoff-YYYY-MM-DD.md`, `review-YYYY-MM-DD.md`, `market-research-YYYY-MM.md`

日付は必ず `YYYY-MM-DD` 形式。`handoff20260823.md` のような形式を新たに作らない。

---

## 音源・画像ファイルの扱い

**リポジトリでは管理しない**（`.gitignore` 済み）。WAVは1曲80MB前後になり、gitに載せるものではない。

音源はローカルにのみ存在する：
```
RouteNote/
├── Level Trim/<曲名>/*.wav
└── Ongaku Toshokan/*.mp3
```

**推奨構成**：このリポジトリを `RouteNote/` 直下にcloneし、音源フォルダと同居させる。
そうすればドキュメントと音源が同じ場所にあり、かつドキュメントだけがgitで同期される。

```
RouteNote/                 ← ここでgit管理
├── CLAUDE.md
├── docs/
├── Level Trim/            ← .gitignore対象
└── Ongaku Toshokan/       ← .gitignore対象
```

完成したジャケット画像だけを残したい場合は `git add -f` で個別に追加する。

---

## 作業上の既知の注意点

### 音源ファイル
- **ファイル名に日本語を使わない** — ffmpegでエンコードエラーになる
- **ファイル名に `#` を使わない** — シェルでコメント開始文字として扱われる
- RouteNoteの受付規格は **MP3(320kbps/44.1kHz)** または **FLAC(44.1kHz)** のみ
- Sunoの書き出しは48kHz。変換時は `-af "aresample=resampler=soxr:precision=28" -ar 44100`
- **`-map_metadata -1` を必ず付ける** — "made with suno" の埋め込みメタデータを削除するため

### RouteNote入稿時（AI楽曲の要件）
- AI企業名をクレジット・言及しない
- 主要アーティストを **Producer** として記載
- C/Pラインに**本名（Satoshi Kawakami）**を記載
- **YouTube Content ID のチェックを外す**（AI楽曲は対象外）
- RouteNote自身が「AIリリースの要件は常に変わり続けている」と明言しているため、**提出直前に必ず公式ページを再確認する**

### 規約情報の扱い
- 配信先の規約は数ヶ月単位で書き換わる。文書内の情報は**下調べであり最終根拠ではない**
- 各判定に「確認済み／未確認」と確認日を明記する
- 二次情報と一次情報が食い違ったら一次情報を優先し、その旨を書く
- 2026年のトレンド系記事にはAI生成のSEOブログが多い（accio.com / soundverse.ai / audiartist.com / insmelo.com 等）。根拠にしない
