# Ongaku Toshokan マスタードキュメント

**作成日：2026-08-24**（現状の状態のみを載せた軽量版。経緯・判断理由は [changelog20260824.md](./changelog.md) 参照）
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

## 2. 曲一覧・現在の状態（2026-08-24時点）

| # | RouteNote Track Title | 尺 | 音源 | 画像 | 状態 |
|---|---|---|---|---|---|
| 01 | `Rainy Kyoto (雨の日の京都)` | 約102分 | 確認済み | 済 | **リリース済み・審査中** |
| 02 | `Morning Kyoto (朝の京都)` | 約65分 | 確認済み | jacket.png（Canvaリサイズ待ち） | 未入稿 |
| 03 | `Late Night Kyoto (夜更けの京都)` | 約65分 | 確認済み | jacket.png（Canvaリサイズ待ち） | 未入稿 |
| 04 | `Ryokan Night (温泉旅館の夜)` | 約61分 | 確認済み | jacket.png（Canvaリサイズ待ち） | 未入稿 |
| 05 | `Bamboo Forest (竹林の朝)` | 約68分 | 確認済み | jacket.png（Canvaリサイズ待ち） | 未入稿。タイトル表記は未確定（changelog参照） |
| 06 | `Cherry Blossom Kyoto (桜舞う京都)` | 約64分 | 確認済み | jacket.png（Canvaリサイズ待ち） | 未入稿 |
| 07 | `Snowy Kyoto (雪の京都)` | 約64分 | 確認済み | jacket.png（Canvaリサイズ待ち） | 未入稿 |
| 08 | `Autumn Kyoto (紅葉の京都)` | 約64分 | 確認済み | jacket.png（Canvaリサイズ待ち） | 未入稿 |
| 09 | `Summer Veranda (夏の縁側と風鈴)` | 約61分 | 確認済み | jacket.png（Canvaリサイズ待ち） | 未入稿 |
| 10 | `Fresh Green (新緑の庭)` | 約64分 | 確認済み | jacket.png（Canvaリサイズ待ち） | 未入稿 |

音源スペックは全曲MP3 320kbps/44.1kHz確認済み（再エンコード不要）。各曲1時間超の長尺は意図的（作業用BGMとして設計）。

## 3. 入稿カレンダー（2026-08-24時点の最新版）

Level Trimと合算で週2〜3件、土曜バッチ予約投稿。詳細は [Level Trimのmaster](../level-trim/master.md) と合わせて管理。

| 入稿（土曜） | Ongaku Toshokan | リリース目安 |
|---|---|---|
| 8/29 | 02 Morning Kyoto／03 Late Night Kyoto | 10/17 |
| 9/5 | 04 Ryokan Night／05 Bamboo Forest | 10/24 |
| 9/12 | 06 Cherry Blossom Kyoto／07 Snowy Kyoto | 10/31 |
| 9/19 | 08 Autumn Kyoto／09 Summer Veranda | 11/7 |
| 9/26 | 10 Fresh Green（最終） | 11/14 |

## 4. 残タスク（優先順）

1. **ジャケット画像10枚をCanvaで3000×3000にリサイズ**
2. **05 Bamboo Forestのタイトル表記を確定**（「朝」のニュアンスを含めるか）
3. **RouteNoteの「高頻度入稿は拒否」情報の裏取り**（未確認のまま運用中）
4. 01 Rainy Kyotoの審査結果確認（承認／リジェクト理由）
5. 02〜10の入稿（[../policy.md](../policy.md)のチェックリスト参照）

## 5. ファイル配置

```
RouteNote/Ongaku toshokan/
├── master20260824.md          本書（現状のみ）
├── changelog20260824.md       経緯・判断理由の詳細ログ
├── handoff20260823.md         プロジェクトの位置づけ・規約確認
└── Madobe no shiki/
    ├── 01_Rainy Kyoto (雨の日の京都)/
    │   ├── 01 Rainy Kyoto.mp3
    │   └── Rainy Kyoto artwork.jpg
    ├── 02_Morning Kyoto (朝の京都)/
    │   ├── 02 Morning Kyoto.mp3
    │   └── 朝の京都 Morning Kyoto.png
    └── ...（03〜10も同様の構成）
```
