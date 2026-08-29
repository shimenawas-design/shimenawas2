# Ongaku Toshokan / A Year in Kyoto

規約・配信先判定は [../policy.md](../policy.md)（両プロジェクト共通）を参照。
詳しい経緯は [archive/handoff-2026-08-23.md](./archive/handoff-2026-08-23.md)。

---

## 基本情報

| 項目 | 値 |
|---|---|
| アーティスト名義 | `Ongaku Toshokan`（音楽図書館） |
| ディストリビューター | RouteNote（Level Trim と**同一アカウント、名義のみ分離**） |
| YouTubeチャンネル | https://www.youtube.com/@ongakutoshokan （**中身未確認**） |
| C/Pライン | Satoshi Kawakami |
| リリース形態 | アルバム（10曲） |

### なぜ名義を分けたか
`Level Trim`（エンジニア向け作業用BGM・キュレーションされたアーティスト）と `Ongaku Toshokan`（ライブラリ的な多作路線）は要求される戦略が真逆。同一名義に混ぜると**ジャンル信号が割れて両方が「分類不能」扱いになる**。

⚠️ ただし名義を分けても、Deezer/Spotify の AI検出とスパム判定は**トラック単位・アカウント単位**で走る。**検出の盾にはならない。**

---

## トラックリスト（10曲・ローカルにMP3で保管）

季節（桜→新緑→夏→秋→雪）と時間帯（朝・雨・深夜）で京都を一巡する構成。

```
01 Rainy Kyoto        06 Cherry Blossom Kyoto
02 Morning Kyoto      07 Snowy Kyoto
03 Late Night Kyoto   08 Autumn Kyoto
04 Ryokan Night       09 Summer Veranda
05 Bamboo Forest      10 Fresh Green
```

### 音源の来歴
- **MP4からの変換によるMP3**。1ファイル30MB超（320kbpsなら約12.5分に相当）
- **指摘済み**：MP4の音声は通常AAC（既に非可逆）なので、MP3化は非可逆→非可逆の再エンコードであり音質は劣化する
- **ユーザーの判断**：音源の変換は不要。現状のMP3で提出する
- → ただし品質とは別に、**規格適合が未確認**（下記）

---

## メタデータ（ドラフト・未承認）

| 項目 | 案 |
|---|---|
| アルバム名 | `A Year in Kyoto` |
| ジャンル | Ambient（副ジャンル欄があれば New Age） |

**アルバム名の根拠**：10曲が年間を巡る構成であることが一目で伝わり、「曲の寄せ集め」ではなく「作品」として読める。検索性を優先するなら `Kyoto Ambience` だが、汎用的すぎて埋もれる。

**英語説明文（案）**
```
Ten ambient pieces tracing a year in Kyoto — rain on temple stone, morning light, summer shade, and snow.
Instrumental and unhurried: made for reading, working, and winding down.
```

### 細かい指摘（任意対応）
- `Fresh Green` は新緑の直訳で英語としてやや据わりが悪い。`Early Summer Green` などが自然
- 10曲中5曲に "Kyoto" が入っている。テーマとして自然な範囲だが、**Spotifyのスパム指標に「メタデータのSEO操作」がある**ので、これ以上増やさないこと

---

## 残タスク（優先順）

### 1. 🔴 MP3のスペック確認
RouteNote は **MP3 (320kbps / 44.1kHz)** か **FLAC (44.1kHz)** しか受け付けない。
MP4由来だと元が128〜256kbpsのことがあり、その場合は**音質の話ではなく規格不適合で弾かれる**。

```bash
for f in *.mp3; do
  echo "=== $f"
  ffprobe -v error \
    -show_entries stream=codec_name,bit_rate,sample_rate,channels \
    -show_entries format=duration,size \
    -of default=noprint_wrappers=1 "$f"
done
```

**合格条件**：`sample_rate=44100` かつ `bit_rate` が 320000 前後。

**不合格だった場合**：MP3から再エンコードしても品質は戻らない。**元WAV（または元のMP4）に遡って変換し直す。**

```bash
# 元WAVがある場合
ffmpeg -i "01 Rainy Kyoto.wav" -af "aresample=resampler=soxr:precision=28" \
  -ar 44100 -map_metadata -1 "01 Rainy Kyoto.flac"

# 元MP4しかない場合（AAC→MP3の劣化は避けられないが規格は満たせる）
ffmpeg -i "01 Rainy Kyoto.mp4" -vn -ar 44100 -c:a libmp3lame -b:a 320k \
  -map_metadata -1 "01 Rainy Kyoto.mp3"
```

### 2. 🔴 `Ongaku Toshokan` の重複チェック
Spotify / Apple Music で既存アーティストと衝突していないか確認する。
Level Trim のときは `Faint Signal` → `Even Keel` と2回重複して3案目でようやく通った。**ローマ字表記の日本語名は特に被りやすい。**

### 3. アルバム名・説明文の確定
### 4. ジャケット画像（3000×3000）— **未着手**。京都の季節を巡る構成に合わせた案が必要
### 5. RouteNote へ入稿（[../policy.md](../policy.md) のチェックリスト参照）

### 6. YouTube @ongakutoshokan の実態確認
登録者数・動画本数・**収益化(YPP)の有無**。

⚠️ **既に収益化済みで別ジャンルのコンテンツがある場合、AI生成BGMを大量投入するとチャンネル単位で収益化を失うリスクがある。** YouTubeの「大量生産的・反復的コンテンツ」判定はチャンネル単位。混ぜる前に必ず確認すること。

| 状況 | 判断 |
|---|---|
| 未収益化・投稿が少ない/休止中 | **最有力。** 作業用BGMライブラリとして再定義 |
| 既に音楽系で稼働・収益化済み | 内容次第。親和性があれば統合、違えば新規 |
| 別ジャンルで収益化済み | **新規チャンネルを立てる。既存資産に混ぜない** |

---

## 既知のつまずき（RouteNote）

- **Add Audioステップでブラウザの状態不整合により「重複ファイル」エラーが繰り返し出ることがある。** 10曲×30MB＝300MB超のアップロードなので、通信が不安定だと再発しやすい。エラーが出たらリロードしてやり直す
- 途中でできた中途半端な下書きは、ゴミ箱アイコンで削除しておく
- リリースタイトルのIME誤変換を目視確認（過去にカタカナ「アイドルループ」になった事例あり）
