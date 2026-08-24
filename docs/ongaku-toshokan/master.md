# Ongaku Toshokan マスタードキュメント

**作成日：2026-08-24**（このセッションでの作業をまとめたもの）
関連：[handoff20260823.md](./handoff20260823.md)（プロジェクトの位置づけ・規約確認・リリース判断の経緯）／別プロジェクト：[Level Trim](../Level%20Trim/master20260824.md)

---

## 1. プロジェクト概要（要約）

| 項目 | 値 |
|---|---|
| アーティスト名義 | `Ongaku Toshokan`（音楽図書館） |
| ディストリビューター | RouteNote（**Level Trimと同一アカウント**、名義のみ分離） |
| C/Pライン | 本名（川上悟志 / Satoshi Kawakami） |
| リリース形態 | アルバムではなく**単曲×10本**（2026-08-23確定） |
| 音源 | Suno生成、既存の「窓辺の四季」プロジェクト（`和風BGM/静シリーズ/窓辺の四季`）由来 |
| YouTube連携 | `@ongakutoshokan`（図書館の窓辺シリーズ）と同一世界観・同一原題を使用 |

名義を分けた理由・配信先の判定・リリース頻度の設計思想は [handoff20260823.md](./handoff20260823.md) を参照。

### 曲一覧

| # | 曲名（英語） | 原題（日本語） | 尺 | 状態 |
|---|---|---|---|---|
| 01 | Rainy Kyoto | 雨の日の京都 | 約102分 | **リリース済み**（RouteNote審査中） |
| 02 | Morning Kyoto | 朝の京都 | 約65分 | 未入稿 |
| 03 | Late Night Kyoto | 夜更けの京都 | 約65分 | 未入稿 |
| 04 | Ryokan Night | 温泉旅館の夜 | 約61分 | 未入稿 |
| 05 | Bamboo Forest | 竹林の朝 | 約68分 | 未入稿 |
| 06 | Cherry Blossom Kyoto | 桜舞う京都 | 約64分 | 未入稿 |
| 07 | Snowy Kyoto | 雪の京都 | 約64分 | 未入稿 |
| 08 | Autumn Kyoto | 紅葉の京都 | 約64分 | 未入稿 |
| 09 | Summer Veranda | 夏の縁側と風鈴 | 約61分 | 未入稿 |
| 10 | Fresh Green | 新緑の庭 | 約64分 | 未入稿 |

各曲1時間超の長尺は意図的（作業用BGMとして設計）。

---

## 2. このセッションでの作業ログ（2026-08-24）

### 2.1 フォルダ整理
`Madobe no shiki`フォルダ内、`01 Rainy Kyoto.mp3`のようにファイル名だけだった10曲を、`番号_曲名`のサブフォルダに仕分け。後日、フォルダ名に日本語原題を併記する形に統一（`02_Morning Kyoto (朝の京都)`等）。

### 2.2 音源スペック確認
`ffprobe`で全10曲を確認。**全曲、MP3 320kbps/44.1kHz/ステレオで合格**（RouteNoteの受付規格を満たす。再エンコード不要）。

### 2.3 リリース形態の決定
当初アルバム（10曲入り1本）として想定していたが、**単曲×10本のリリースに変更**（2026-08-23確定）。理由：週2曲ペースでのリリース希望と、RouteNoteの審査待ち期間（27〜29営業日）を踏まえた入稿計画のため。

### 2.4 ジャケット画像の調達
既存プロジェクト`和風BGM/静シリーズ/窓辺の四季`に、各曲5枚前後の候補画像と、YouTube「図書館の窓辺」チャンネル用に**既に選定済みの最終版画像**（`season5_v2_metadata.md`に記載）が存在することが判明。候補から選び直す必要はなく、その最終版をそのまま各曲フォルダにコピー。

- **コピーで対応**（moveではない）：これらの画像は`season5_v2_metadata.md`のYouTube側チェックリストに直接パス参照されている現役ファイルのため、移動すると別プロジェクトの手順が壊れるリスクがあった
- 01は既存の`Rainy Kyoto artwork.jpg`をそのまま使用、02〜10は上記の方法で調達済み
- **Canvaでの3000×3000リサイズは全曲未実施**

### 2.5 曲名の日本語併記
「和風であることを英語圏のリスナーにも伝えたい」という意図から、`Bamboo Forest Japan`のような国名の後付けタグ方式を検討したが、RouteNote公式Style Guide（後述）の「purely descriptive」「generic metadata」の禁止事項に抵触するリスクが高いと判断。代わりに**原題を英語タイトルに併記する方式**を採用：

> `Rainy Kyoto (雨の日の京都)` のように、Track Title欄に英語+（日本語原題）で入力する

音源ファイル名自体は英語のみで維持（Sunoの書き出しファイルは日本語ファイル名だとffmpegでエンコードエラーになる既知の問題があるため）。フォルダ名には日本語原題を併記。

| # | RouteNote Track Title（確定） |
|---|---|
| 01 | `Rainy Kyoto (雨の日の京都)` |
| 02 | `Morning Kyoto (朝の京都)` |
| 03 | `Late Night Kyoto (夜更けの京都)` |
| 04 | `Ryokan Night (温泉旅館の夜)` |
| 05 | `Bamboo Forest (竹林の朝)` |
| 06 | `Cherry Blossom Kyoto (桜舞う京都)` |
| 07 | `Snowy Kyoto (雪の京都)` |
| 08 | `Autumn Kyoto (紅葉の京都)` |
| 09 | `Summer Veranda (夏の縁側と風鈴)` |
| 10 | `Fresh Green (新緑の庭)` |

※05 `Bamboo Forest`は原題「竹林の**朝**」の「朝」のニュアンスが英語名に反映されていない。必要なら`Bamboo Forest Morning (竹林の朝)`への変更も検討可（未確定）。

### 2.6 RouteNote公式ポリシーの一次情報確認（2026-08-23確認）

`support.routenote.com`を直接確認。以下は確認日時点の情報、提出直前に再確認が必要。

- **[Can I upload AI releases?](https://support.routenote.com/kb-article/can-i-upload-ai-releases/)**（更新2026-08-17）：AI楽曲は受け入れるが、Content Recognition DSP・韓国系ストア（Melon/Genie/Bugs/Flo/Vibe）・Amazonには配信不可。使用ツールへのリンク提出必須。追加審査で通常より時間がかかる場合あり
- **[AI楽曲のフォーマット規定](https://support.routenote.com/kb-article/how-should-i-format-a-release-containing-ai-generated-music/)**（更新2026-08-20）：AI企業名を明記しないこと以外の特別な要件なし
- **[審査待ち時間](https://support.routenote.com/kb-article/how-long-will-i-be-waiting-for-my-release-to-go-live/)**（更新2026-08-17）：**現在27〜29営業日**（入稿量増加により通常より延長中）。承認後24時間でストア送信、7〜14日で反映
- **[RouteNote Style Guide](https://support.routenote.com/kb-article/routenote-style-guide/)**（更新2026-07-06）：「purely descriptive」なタイトル（例："Chill Lo-fi Groove"）や総称的なメタデータは拒否対象。この規定が2.5の判断根拠

「スパム的に見える大量AI入稿は拒否」「高頻度入稿は手動レビュー対象」という記述は、今回の一次情報検索では確認できず**未確認のまま**（前回セッションからの伝聞）。

### 2.7 リリース頻度・入稿カレンダーの検討
Level Trimと合わせて**週2〜3件を、週末にまとめて予約投稿**したいという希望を確認。27〜29営業日の審査期間を踏まえ、7週間の安全マージンで逆算した入稿カレンダー（土曜バッチ）を提案：

| 入稿weekend | 内容 |
|---|---|
| 8/29(土) | 02 Morning Kyoto／03 Late Night Kyoto |
| 9/5(土) | 04 Ryokan Night／05 Bamboo Forest |
| 9/12(土) | 06 Cherry Blossom Kyoto／07 Snowy Kyoto |
| 9/19(土) | 08 Autumn Kyoto／09 Summer Veranda |
| 9/26(土) | 10 Fresh Green（最終1曲） |

Level Trim側の入稿と合わせて、同一RouteNoteアカウントでの合算頻度が「週2〜3件」の希望を満たすかは要継続確認（**未確定・仮案**）。

---

## 3. ファイル配置

```
RouteNote/Ongaku toshokan/
├── master20260824.md          本書
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

---

## 4. 残タスク

1. **ジャケット画像10枚をCanvaで3000×3000にリサイズ**（未実施）
2. **05 Bamboo Forestのタイトル表記を確定**（「朝」のニュアンスを含めるか）
3. **入稿カレンダーの確定**（Level Trim側との合算頻度を踏まえて）
4. **RouteNoteの「高頻度入稿は拒否」情報の裏取り**（現状未確認のまま運用している）
5. 01 Rainy Kyotoの審査結果確認（承認／リジェクト理由）
6. 02〜10の入稿（[handoff20260823.md](./handoff20260823.md)のチェックリスト参照）
