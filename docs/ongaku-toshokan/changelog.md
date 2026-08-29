# Ongaku Toshokan 作業ログ（2026-08-24）

現状の要点だけ知りたい場合は [master20260824.md](./master.md) を見れば十分。本書は経緯・判断理由の記録用（普段は読み込み不要）。

---

## フォルダ整理
`Madobe no shiki`フォルダ内、`01 Rainy Kyoto.mp3`のようにファイル名だけだった10曲を、`番号_曲名`のサブフォルダに仕分け。後日、フォルダ名に日本語原題を併記する形に統一（`02_Morning Kyoto (朝の京都)`等）。

## 音源スペック確認
`ffprobe`で全10曲を確認。**全曲、MP3 320kbps/44.1kHz/ステレオで合格**（RouteNoteの受付規格を満たす。再エンコード不要）。

## リリース形態の決定
当初アルバム（10曲入り1本）として想定していたが、**単曲×10本のリリースに変更**（2026-08-23確定）。理由：週2曲ペースでのリリース希望と、RouteNoteの審査待ち期間（27〜29営業日）を踏まえた入稿計画のため。

## ジャケット画像の調達
既存プロジェクト`和風BGM/静シリーズ/窓辺の四季`に、各曲5枚前後の候補画像と、YouTube「図書館の窓辺」チャンネル用に**既に選定済みの最終版画像**（`season5_v2_metadata.md`に記載）が存在することが判明。候補から選び直す必要はなく、その最終版をそのまま各曲フォルダにコピー。

- **コピーで対応**（moveではない）：これらの画像は`season5_v2_metadata.md`のYouTube側チェックリストに直接パス参照されている現役ファイルのため、移動すると別プロジェクトの手順が壊れるリスクがあった
- 01は既存の`Rainy Kyoto artwork.jpg`をそのまま使用、02〜10は上記の方法で調達済み

## 曲名の日本語併記の判断
「和風であることを英語圏のリスナーにも伝えたい」という意図から、`Bamboo Forest Japan`のような国名の後付けタグ方式を検討したが、RouteNote公式Style Guideの「purely descriptive」「generic metadata」の禁止事項に抵触するリスクが高いと判断。代わりに**原題を英語タイトルに併記する方式**を採用（`Rainy Kyoto (雨の日の京都)`）。

音源ファイル名自体は英語のみで維持（Sunoの書き出しファイルは日本語ファイル名だとffmpegでエンコードエラーになる既知の問題があるため）。フォルダ名には日本語原題を併記。

※05 `Bamboo Forest`は原題「竹林の**朝**」の「朝」のニュアンスが英語名に反映されていない。必要なら`Bamboo Forest Morning (竹林の朝)`への変更も検討可（未確定）。

## RouteNote公式ポリシーの一次情報確認（2026-08-23確認）

`support.routenote.com`を直接確認。以下は確認日時点の情報、提出直前に再確認が必要。

- **[Can I upload AI releases?](https://support.routenote.com/kb-article/can-i-upload-ai-releases/)**（更新2026-08-17）：AI楽曲は受け入れるが、Content Recognition DSP・韓国系ストア（Melon/Genie/Bugs/Flo/Vibe）・Amazonには配信不可。使用ツールへのリンク提出必須。追加審査で通常より時間がかかる場合あり
- **[AI楽曲のフォーマット規定](https://support.routenote.com/kb-article/how-should-i-format-a-release-containing-ai-generated-music/)**（更新2026-08-20）：AI企業名を明記しないこと以外の特別な要件なし
- **[審査待ち時間](https://support.routenote.com/kb-article/how-long-will-i-be-waiting-for-my-release-to-go-live/)**（更新2026-08-17）：**現在27〜29営業日**（入稿量増加により通常より延長中）。承認後24時間でストア送信、7〜14日で反映
- **[RouteNote Style Guide](https://support.routenote.com/kb-article/routenote-style-guide/)**（更新2026-07-06）：「purely descriptive」なタイトル（例："Chill Lo-fi Groove"）や総称的なメタデータは拒否対象。この規定が日本語併記の判断根拠

「スパム的に見える大量AI入稿は拒否」「高頻度入稿は手動レビュー対象」という記述は、今回の一次情報検索では確認できず**未確認のまま**（前回セッションからの伝聞）。

## リリース頻度・入稿カレンダーの検討経緯
Level Trimと合わせて**週2〜3件を、週末にまとめて予約投稿**したいという希望を確認。27〜29営業日の審査期間を踏まえ、7週間の安全マージンで逆算した入稿カレンダーを検討。最新の確定版は [master20260824.md](./master.md) を参照（本書には経緯のみ記載、日付は更新のたび古くなるため転記しない）。
