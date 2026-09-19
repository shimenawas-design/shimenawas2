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

## 2. 曲一覧・現在の状態（2026-09-19更新）

| # | RouteNote Track Title | 尺 | 音源 | 画像 | 状態 |
|---|---|---|---|---|---|
| 01 | `Rainy Kyoto (雨の日の京都)` | 約102分 | 確認済み | 済 | **審査中**（入稿 8/23） |
| 02 | `Morning Kyoto (朝の京都)` | 約65分 | 確認済み | jacket.png（Canvaリサイズ待ち） | **審査中**（入稿 8/29） |
| 03 | `Late Night Kyoto (夜更けの京都)` | 約65分 | 確認済み | jacket.png（Canvaリサイズ待ち） | **審査中**（入稿 8/29） |
| 04 | `Ryokan Night (温泉旅館の夜)` | 約61分 | 確認済み | 3000×3000済み（右側コラージュ切り出し） | **入稿完了・審査中**（入稿 9/12） |
| 05 | `Morning Bamboo Forest` | 約68分 | 確認済み | 3000×3000済み（同上） | **入稿完了・審査中**（入稿 9/12）。タイトルは原題「竹林の朝」の「朝」を反映 |
| 06 | `Cherry Blossom Kyoto (桜舞う京都)` | 約64分 | 確認済み | 3000×3000済み（同上） | **入稿完了・審査中**（入稿 9/12） |
| 07 | `Snowy Kyoto (雪の京都)` | 約64分 | 確認済み | 3000×3000済み（2026-09-08、同上） | **入稿完了・審査中**（入稿 9/19、Sales Start Date 11/07） |
| 08 | `Autumn Kyoto (紅葉の京都)` | 約64分 | 確認済み | 3000×3000済み（同上） | **入稿完了・審査中**（入稿 9/19、Sales Start Date 11/07） |
| 09 | `Summer Veranda (夏の縁側と風鈴)` | 約61分 | 確認済み | 3000×3000済み（同上） | **入稿完了・審査中**（入稿 9/19、Sales Start Date 11/14） |
| 10 | `Fresh Green (新緑の庭)` | 約64分 | 確認済み | 3000×3000済み（同上） | **入稿完了・審査中**（入稿 9/19、Sales Start Date 11/14）。**全10曲入稿完了** |

音源スペックは全曲MP3 320kbps/44.1kHz確認済み（再エンコード不要）。各曲1時間超の長尺は意図的（作業用BGMとして設計）。

**UPC（審査中の10曲）**：
- 2026-08-30 RouteNote画面で確認：01 Rainy Kyoto = 5064115158501／02 Morning Kyoto = 5064115052656／03 Late Night Kyoto = 5064115006369
- 2026-09-12 入稿完了時に確認：04 Ryokan Night = 5064140064709／05 Morning Bamboo Forest = 5064140844356／06 Cherry Blossom Kyoto = 5064140546236
- 2026-09-19 入稿完了時に確認：07 Snowy Kyoto = 5064140895525／08 Autumn Kyoto = 5064115703893／09 Summer Veranda = 5064140376796／10 Fresh Green = 5064115660547

**04〜06の入稿は、音源アップロードのみユーザーが実施し、それ以外（リリース作成〜Album Details〜ジャケット〜ストア設定〜規約同意〜配信申請）はアシスタントがブラウザ自動操作で代行した（2026-09-12）。** 手順は `.claude/skills/routenote-release/SKILL.md` に集約。

## 3. 入稿カレンダー（2026-09-17更新：入稿はまとめて、公開日だけ分散）

在庫解消のため運用変更（[../policy.md](../policy.md) 5章）。**07〜10は2026-09-19に一括入稿済み。Sales Start Dateを指定し、公開日だけ従来ペース（週2〜3件、Level Trim/Hollow Rotorと合算）で分散させている。**

| 公開予定（Sales Start Date） | Ongaku Toshokan | 入稿 |
|---|---|---|
| ~~8/29~~ | ~~02 Morning Kyoto／03 Late Night Kyoto~~ | 10/17（**入稿済み**） |
| ~~9/12~~ | ~~04 Ryokan Night／05 Morning Bamboo Forest／06 Cherry Blossom Kyoto~~ | 10/31（**入稿済み**） |
| 11/7 | 07 Snowy Kyoto／08 Autumn Kyoto | **入稿済み（2026-09-19）** |
| 11/14 | 09 Summer Veranda／10 Fresh Green（最終） | **入稿済み（2026-09-19）** |

## 3.5 入稿時の実務メモ（2026-09-12 実地で判明）

- **ジャケットはJPG必須**。PNGはリジェクトされる（3000×3000・RGB・25MB未満）
- **リリースタイトルは英語のみ**。日本語原題は併記しない（既存3曲に合わせる）
- **アーティスト名はドロップダウンの「Create a new profile」を選んで確定する**。入力しただけでは保存時に弾かれる
- **⚠️ 既存曲の名義表記が割れている**：`Rainy Kyoto`＝`Ongaku Toshokan`／`Morning Kyoto`・`Late Night Kyoto`＝`Ongaku toshokan`（t小文字）。**今後は `Ongaku Toshokan` に統一**（2026-09-12決定）。審査中の2曲はメタデータ修正可能なため、表記を揃えることを推奨
- **⚠️ 「Distribute Free」の確認モーダルを押し忘れると80%で止まる**（2026-09-12判明）。Distribute Freeクリック後に出る「Complete Release」モーダルを押さないと、エラーも出ないまま配信申請が完了しない。Discography上で静かに80%のまま残るため、Distribute操作の最後に必ずこのモーダルの有無を確認する
- **⚠️ トラックメタデータの末尾1文字が欠落する。原因判明（2026-09-19）**：トラック情報画面（`/rn/audiometadata/<node>/edit`）で「Save and Continue」を押すたびに、作曲者・制作者・役割の値が**末尾1文字ずつ削られる**（`Satoshi`→`Satosh`→`Satos`）。ブラウザ自動操作（プログラム経由の入力・送信）で起きる。ユーザー本人の手動操作では9/19の10曲とも発生しなかった。**トラック情報画面は保存しない**のが最善。欠落した場合は、フォームを直接POSTし、各値の**末尾に捨て文字を1つ足して**送ると完全な値で保存される（詳細は [routenote-release スキル](../../.claude/skills/routenote-release/SKILL.md)）
- **⚠️ 音源を入れた後のトラック側アーティストが別名義になることがある**（2026-09-19、Fresh Greenで発生）。トラック側のアーティスト欄は読み取り専用で、直近に作った別名義（Hollow Rotor）が入った。**音源アップロード後は、全曲のトラック側アーティスト・作曲者・制作者を読み取りで照合する**。配信申請後は直せない
- **音源画面で「Duplicate audio file loaded」が出たら**（2026-09-19、Dead Weightで発生）：音源は最初のアップロードで登録済みで、「Save and continue」が重複として拒否される。トラック情報画面からの保存でも Step 2 は完了にならなかった。**リリース画面の「Delete Track」でトラックを削除し、音源を1回だけ入れ直して**解決した

## 4. 残タスク（優先順）

1. ~~ジャケット画像を3000×3000にリサイズ~~ → **04〜10の7曲完了（2026-09-08）**。02・03（審査中の既提出分）は未リサイズのまま据え置き
2. ~~05のタイトル表記を確定~~ → **完了（2026-09-12）**：`Morning Bamboo Forest`
3. ~~04〜06の入稿~~ → **完了（2026-09-12）**：Ryokan Night・Morning Bamboo Forest・Cherry Blossom Kyoto
4. 01 Rainy Kyotoの審査結果確認（承認／リジェクト理由）
5. ~~07〜10の一括入稿~~ → **完了（2026-09-19）**。**全10曲の入稿が完了。新曲制作の予定は現状なし**

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
