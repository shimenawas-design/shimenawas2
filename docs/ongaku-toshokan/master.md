# Ongaku Toshokan マスタードキュメント

**作成日：2026-08-24**（現状の状態のみを載せた軽量版。経緯・判断理由は [changelog.md](./changelog.md) 参照）
関連：[../policy.md](../policy.md)（規約・配信先）／別プロジェクト：[Level Trim](../level-trim/master.md)

---

## 1. プロジェクト概要

| 項目 | 値 |
|---|---|
| アーティスト名義 | `Ongaku Toshokan`（音楽図書館） |
| ディストリビューター | RouteNote（**Level Trimと同一アカウント**、名義のみ分離） |
| C/Pライン | 本名（川上悟志 / Satoshi Kawakami） |
| リリース形態 | アルバムではなく**単曲×10本** |
| 音源 | Suno生成、既存の「窓辺の四季」プロジェクト由来 |

## 2. 曲一覧・現在の状態（2026-09-14更新）

| # | RouteNote Track Title | 尺 | 音源 | 画像 | 状態 |
|---|---|---|---|---|---|
| 01 | `Rainy Kyoto (雨の日の京都)` | 約102分 | 確認済み | 済 | **審査中**（入稿 8/23） |
| 02 | `Morning Kyoto (朝の京都)` | 約65分 | 確認済み | jacket.png（Canvaリサイズ待ち） | **審査中**（入稿 8/29） |
| 03 | `Late Night Kyoto (夜更けの京都)` | 約65分 | 確認済み | jacket.png（Canvaリサイズ待ち） | **審査中**（入稿 8/29） |
| 04 | `Ryokan Night (温泉旅館の夜)` | 約61分 | 確認済み | 3000×3000済み（右側コラージュ切り出し） | **入稿完了・審査中**（入稿 9/12） |
| 05 | `Morning Bamboo Forest` | 約68分 | 確認済み | 3000×3000済み（同上） | **入稿完了・審査中**（入稿 9/12）。タイトルは原題「竹林の朝」の「朝」を反映 |
| 06 | `Cherry Blossom Kyoto (桜舞う京都)` | 約64分 | 確認済み | 3000×3000済み（同上） | **入稿完了・審査中**（入稿 9/12） |
| 07 | `Snowy Kyoto (雪の京都)` | 約64分 | 確認済み | 3000×3000済み（2026-09-08、同上） | 未入稿 |
| 08 | `Autumn Kyoto (紅葉の京都)` | 約64分 | 確認済み | 3000×3000済み（同上） | 未入稿 |
| 09 | `Summer Veranda (夏の縁側と風鈴)` | 約61分 | 確認済み | 3000×3000済み（同上） | 未入稿 |
| 10 | `Fresh Green (新緑の庭)` | 約64分 | 確認済み | 3000×3000済み（同上） | 未入稿 |

音源スペックは全曲MP3 320kbps/44.1kHz確認済み（再エンコード不要）。各曲1時間超の長尺は意図的（作業用BGMとして設計）。

**UPC（審査中の6曲）**：
- 2026-08-30 RouteNote画面で確認：01 Rainy Kyoto = 5064115158501／02 Morning Kyoto = 5064115052656／03 Late Night Kyoto = 5064115006369
- 2026-09-12 入稿完了時に確認：04 Ryokan Night = 5064140064709／05 Morning Bamboo Forest = 5064140844356／06 Cherry Blossom Kyoto = 5064140546236

**04〜06の入稿は、音源アップロードのみユーザーが実施し、それ以外（リリース作成〜Album Details〜ジャケット〜ストア設定〜規約同意〜配信申請）はアシスタントがブラウザ自動操作で代行した（2026-09-12）。** 手順は `.claude/skills/routenote-release/SKILL.md` に集約。

## 3. 入稿カレンダー（2026-08-24時点の最新版）

Level Trimと合算で週2〜3件、土曜バッチ予約投稿。詳細は [Level Trimのmaster](../level-trim/master.md) と合わせて管理。

| 入稿（土曜） | Ongaku Toshokan | リリース目安 |
|---|---|---|
| ~~8/29~~ | ~~02 Morning Kyoto／03 Late Night Kyoto~~ | 10/17（**入稿済み**） |
| ~~9/12~~ | ~~04 Ryokan Night／05 Morning Bamboo Forest／06 Cherry Blossom Kyoto~~ | 10/31（**入稿済み、当初計画の9/5+9/12分を1回にまとめて実施**） |
| 9/19 | 07 Snowy Kyoto／08 Autumn Kyoto | 11/7 |
| 9/26 | 09 Summer Veranda／10 Fresh Green（最終） | 11/14 |

## 3.5 入稿時の実務メモ（2026-09-12 実地で判明）

- **ジャケットはJPG必須**。PNGはリジェクトされる（3000×3000・RGB・25MB未満）
- **リリースタイトルは英語のみ**。日本語原題は併記しない（既存3曲に合わせる）
- **アーティスト名はドロップダウンの「Create a new profile」を選んで確定する**。入力しただけでは保存時に弾かれる
- **⚠️ 既存曲の名義表記が割れている**：`Rainy Kyoto`＝`Ongaku Toshokan`／`Morning Kyoto`・`Late Night Kyoto`＝`Ongaku toshokan`（t小文字）。**今後は `Ongaku Toshokan` に統一**（2026-09-12決定）。審査中の2曲はメタデータ修正可能なため、表記を揃えることを推奨
- **⚠️ 「Distribute Free」の確認モーダルを押し忘れると80%で止まる**（2026-09-12判明）。Distribute Freeクリック後に出る「Complete Release」モーダルを押さないと、エラーも出ないまま配信申請が完了しない。Discography上で静かに80%のまま残るため、Distribute操作の最後に必ずこのモーダルの有無を確認する
- **⚠️ トラックメタデータの末尾1文字が欠落することがある**（2026-09-12、Morning Bamboo Forestで発生。`Satosh`／`Kawakam`／`Ongaku Toshoka`のように末尾1文字が切れた状態で保存された。原因未特定）。配信直前にRouteNote側が警告モーダルで教えてくれることがあるが出ないこともあるため、**Add Audioの後は必ずトラックメタデータを目視確認する**。修正は `https://www.routenote.com/rn/audiometadata/<node_id>/edit`

## 4. 残タスク（優先順）

1. ~~ジャケット画像を3000×3000にリサイズ~~ → **04〜10の7曲完了（2026-09-08）**。02・03（審査中の既提出分）は未リサイズのまま据え置き
2. ~~05のタイトル表記を確定~~ → **完了（2026-09-12）**：`Morning Bamboo Forest`
3. ~~04〜06の入稿~~ → **完了（2026-09-12）**：Ryokan Night・Morning Bamboo Forest・Cherry Blossom Kyoto
4. 01 Rainy Kyotoの審査結果確認（承認／リジェクト理由）
5. 07〜10の入稿（[../policy.md](../policy.md)のチェックリスト参照。手順は [routenote-release スキル](../../.claude/skills/routenote-release/SKILL.md)）

※「RouteNoteの高頻度入稿は拒否」情報は、2026-08-24の一次情報検索では確認できず**未確認のまま撤回済み**（[../policy.md](../policy.md) 第2章参照）。裏取りタスクとしては解消。

## 5. ファイル配置

ドキュメントは**リポジトリの `docs/` が唯一の正**（リポジトリ直下の `CLAUDE.md` 参照）。音源・画像は `.gitignore` 対象でローカルにのみ存在する。

```
RouteNote/                     ← ここでgit管理
├── CLAUDE.md
├── docs/ongaku-toshokan/      ← ドキュメントはすべてここ
└── Ongaku Toshokan/           ← .gitignore対象
    └── Madobe no shiki/
        ├── 01_Rainy Kyoto (雨の日の京都)/
        │   ├── 01 Rainy Kyoto.mp3
        │   └── Rainy Kyoto artwork.jpg
        ├── 02_Morning Kyoto (朝の京都)/
        │   ├── 02 Morning Kyoto.mp3
        │   └── 朝の京都 Morning Kyoto.png
        └── ...（03〜10も同様の構成。04〜10のジャケットは3000×3000済み）
```
