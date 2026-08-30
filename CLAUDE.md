# このリポジトリについて

AI音楽（Suno）を制作し、RouteNote経由で配信するプロジェクトのドキュメント管理リポジトリ。
**リモート（claude.ai/code）とローカルPCの両方のセッションから編集される。**

ブランチ：`claude/new-session-8v0hvp`

---

## 📍 現況（2026-08-24）

| 名義 | 状態 |
|---|---|
| **Level Trim** | 全6曲。#1 `Idle Loop` は審査中（リリース日 9/6）。#2〜#6 は音源FLAC変換済み・ジャケット画像生成済み。**残り：全曲リスニング再確認／Canvaで3000×3000リサイズ／Thread Pool再生成の判断** |
| **Ongaku Toshokan** | 京都BGM、**単曲×10本**（各1時間超）。MP3スペック全曲合格（320kbps/44.1kHz）。`01 Rainy Kyoto` は審査中。**残り：02〜10の入稿／Canvaリサイズ** |

**⚠️ RouteNoteの審査待ちは現在27〜29営業日（約6週間）。** 入稿カレンダーはこれを織り込んで組むこと（`docs/policy.md` 参照）。

**選定基準を反転して全曲を再構築したため、Level Trim の旧リスニング確認は無効。** 再確認が必要。

---

## 📂 どの文書を読むか（**必要なものだけ読むこと**）

全文書を読むと約45,000トークン消費する。**タスクに応じて1〜2ファイルだけ開く。**

| やること | 開くファイル |
|---|---|
| **今の状態を知る（まずここ）** | `docs/level-trim/master.md` / `docs/ongaku-toshokan/master.md` ← **軽量・現状のみ** |
| 曲を作る・プロンプトを見る | `docs/level-trim/prompts.md`（Suno・Gemini両方） |
| 規約・配信先・AI環境・Spotify仕様 | `docs/policy.md` ← **両プロジェクト共通** |
| なぜそうしたかの経緯を追う | `docs/*/changelog.md` ← **普段は不要** |
| **リスニング確認をする** | `docs/level-trim/listening-check.md` ← **いま最優先の作業** |
| 未対処のレビュー指摘 | `docs/level-trim/review-2026-08-24.md` |
| リリース設計の判断根拠 | `docs/level-trim/release-plan.md`（※日程部分は無効） |
| 市場・ジャンルの戦略検討 | `docs/level-trim/market-research-2026-08.md` |
| 過去の経緯を遡る | `docs/*/archive/` ← **通常は開かない** |
| ドキュメント整理の手法を知る | `docs/doc-practices.md` |

各文書は自分の担当範囲だけを持ち、重複させない。**同じ情報を2箇所に書かないこと。**

---

## ⚠️ ドキュメント運用のルール（厳守）

過去に**ローカルとリポジトリで同じ文書が別名で二重管理され、どちらが正か分からなくなる事故**が起きた。

1. **ドキュメントの唯一の置き場は `docs/` 配下。** ローカルの音源フォルダ内にコピーを作らない
2. **セッション開始時に `git pull origin claude/new-session-8v0hvp`**
3. **編集したらその場で commit & push。**「あとでまとめて」は禁止
4. **ファイル名の規約**
   - 生きている文書（随時更新）：`master.md` `changelog.md` `prompts.md` `policy.md` `release-plan.md`
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
