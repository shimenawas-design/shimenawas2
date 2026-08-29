# リリース計画（2026-08-23 更新）

関連：[prompts.md](./prompts.md)（プロンプト） / [master.md](./master.md)（音源制作の経緯） / [../policy.md](../policy.md)（規約・配信先） / [market-research-2026-08.md](./market-research-2026-08.md)（市場調査）

---

## #1 `Idle Loop` — 確定事項

| 項目 | 値 |
|---|---|
| **Release Date** | **2026/09/06** |
| Uploaded | 2026/08/22 |
| ステータス（8/23時点） | Pending Moderation（In Review） |
| UPC | 5064115821122 |
| アーティスト / レーベル | Level Trim |
| C Line / P Line | Satoshi Kawakami（本名 ✓ RouteNote の AI ルール要件） |
| 配信モデル | Distribute Free（ロイヤリティ85%） |
| Instrumental フラグ | ✓ |
| YouTube Content ID | Monetisation タブでOFFを確認済み（8/23）。Manage Stores は編集ロック済みのため再確認不可 |
| Add Localisations | 未完了（任意項目、影響なし） |

### 決定：リリース日を延期しない

当初「エディトリアル入稿のために後ろ倒し」を検討したが、**延期しない**方針に変更。

**理由**
- 公開まで14日しかなく、必要工程（承認 → ストア送信最大7日 → Spotifyページ生成最大2週 → claim 24〜72h）が物理的に入らない
- 採用率18%は**全入稿の平均**。フォロワー0・実績0・AI生成インストの新人という条件では現実的にはるかに低い
- Release Radar は既存フォロワーにしか届かない → 現時点で0人なので価値がない
- 本命の成長経路は「同一ジャンルで3〜5リリース積んで Discover Weekly に載る」ルート。**カタログ蓄積の起点を10週間遅らせるコストの方が大きい**

→ **`Idle Loop` のエディトリアル入稿は捨てる。#2 で確実に取る。**

---

## シリーズ命名の変更

引継ぎ資料では今後 `Background Process — [一語]` に統一予定だったが、**プレフィックスは付けない**方針に変更。

**理由**
- 1曲目が既に `Idle Loop`（プレフィックスなし）で確定しており、#2 から付けると1曲目だけシリーズ外に見える
- Spotify のUIで `Background Process — Warm Ca...` と切れる
- シリーズ性は「エンジニアリング用語の2語」という命名パターン＋統一アートワーク＋同一サウンドで十分成立する

**`Background Process` は後で EP / アルバム名として使う。**

### 曲名プール（プロセスの"状態"。順序に意味を持たせない）

`Idle Loop`(#1 済) / `Warm Cache`(#2) / `Long Poll` / `Thread Pool` / `Backpressure` / `Hot Path`

※ `Cold Start` は「立ち上がり＝build-up」を連想させ、設計原則の `no build-up` と衝突するため不採用。

---

## #2 `Warm Cache` — 設計

### 方針：ジャンルを変えない。変数を1つだけ動かす

市場調査で挙がった「Atmospheric DnB」「Maqam×IDM」は**#2 でやってはいけない**。
ジャンル信号が混ざると「分類不能」扱いになり Discover Weekly に入らないため。**投入は #4 以降。**

- 用途：`Idle Loop` が「定常作業」なら `Warm Cache` は「**深い集中が持続している状態**」＝作業時間中いちばん長い区間＝リピート回数が伸びる枠
- 市場調査の3案のうち「**Brown noise を素材として取り込む**」だけは #2 で使える（ジャンルを変えず加算するだけなので信号を割らない）

### Suno スタイル欄・据え置く語／動かす語
**[prompts.md](./prompts.md) を参照**（唯一の正）。

### アートワーク
保管してある予備案（Gemini生成「ワークスペースのぼかし」構図）を使用。Canvaで3000×3000にリサイズ。

---

## スケジュール

| 時期 | やること |
|---|---|
| **9/6** | `Idle Loop` 公開 |
| **9/6 以降すぐ** | artists.spotify.com で `Level Trim` を検索 → claim 申請（承認24〜72h） |
| 〜9月中旬 | `Warm Cache` 制作・Extendで長尺化・44.1kHz FLAC変換（`-map_metadata -1` 必須） |
| **9月中旬** | RouteNote 入稿。**Release Date は 11/1 前後**に設定 |
| **9月末〜10月初** | Spotify for Artists → Music → **Pitch a Song**（リリース31〜40日前の窓＝採用率18%） |
| 11月以降 | #3 以降は **4〜6週間隔**。プロフィール取得済みなので待ち時間は発生しない |

**長い待ちは初回だけ。** #2 が8週間隔になるのはページ生成待ちを1回吸収するため。#3 から通常ペースに戻す。

### Spotify for Artists の claim 手順
**[../policy.md](../policy.md) の第4章を参照。**

### 入稿フォームのコツ
ジャンル・ムード・楽器編成の記入欄は、**プレイリスト名と重なる語**を意識する：
`instrumental` / `ambient` / `focus` / `IDM` / `electronic`
英語説明文は [archive/handoff-2026-08-22.md](./archive/handoff-2026-08-22.md) の確定版をそのまま使用。

---

## 未解決・次に確認すること

- [ ] `Idle Loop` のモデレーション結果（承認 / リジェクト理由）
- [ ] 9/6 公開後、Spotify 上で `Level Trim` のアーティストページが生成されているか
- [ ] Apple Music for Artists も同様に claim（公開後）
- [ ] #4 以降で Atmospheric DnB / Maqam×IDM を投入する判断（#3 まで積んでから再検討）
