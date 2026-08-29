# 話別詳細 — 夏（青竹）追加分 26〜29

> 統合マスター_YYMMDD.md（インデックス）から分割。共通ルール・タグ設計・要対応リストはインデックス側を参照。

**制作完了・アップロード済み（26〜29は要対応リストのとおり2026-08-22までに完了）。** 9月分（13〜25）の後に制作したが、**新状態を1ヶ月早く試すため8月に前倒し投入**した。季節は夏に戻る。
> ⚠️「アップロード未実施」は制作当時の古い記述。2026-08-23にYouTube Studioのコンテンツ一覧を確認したところ、チャンネル全体で30本が既に登録済み（公開済み・公開予約含む）で、26〜29も含まれている。

保存先：`C:\Users\shime\Downloads\茶丸\` 配下の各話フォルダ

### この4本の狙い

9月分（15・21＝目覚め／17・23＝ブレインフォグ）と**季節の固有性で明確に差別化する**。

**目覚め — 「蝉が鳴き出す前」**
夏の明け方には固有性がある。日の出が4時半頃と早く、**蝉が鳴き出す前の30〜60分だけ、真夏なのに静かで涼しい**。一日で唯一涼しい時間帯という実用的な訴求も立つ。9月版（朝露・すすき）とコンセプトが正面から被らない。

**ブレインフォグ — 夏の自然音は40Hzの下地として理想的**
- 実需が明確：「暑さで思考がまとまらない午後」
- **技術的な利点**：蝉の遠音・水音は広帯域の持続音なので、**40Hzトーン（volume 0.05）が自然に溶ける**。静寂の多い曲だと小音量でも40Hzが浮いて聴こえる
- **選定ロジックとの相性**：自然音を主体テクスチャにすると rng が構造的に小さくなり、「rng最小の2曲」が機能しやすい

### 配置と重複チェック

| 状態 | 9月分 | 8月追加分 |
|---|---|---|
| 目覚め | 窓辺(鈴) / 縁側(ピアノ) | **茶室(箏) / 縁側(尺八)** |
| ブレインフォグ | 窓辺(箏) / 茶室(尺八) | **庭(ピアノ) / 窓辺(鈴)** |

**目覚め4本で箏・尺八・ピアノ・鈴を1本ずつ使い切る**形になっている。

### 投稿日

残り予約（8/18・21・24・26・28・31）の合間に差し込む。

```
8/18(既) 8/19(26) 8/21(既) 8/23(27) 8/24(既) 8/26(既) 8/27(28) 8/28(既) 8/30(29) 8/31(既)
```

> 2週間で10本＝週約5本になり通常の倍。**これ以上の追加はしない。**

---

## 26 ｜ 🆕 目覚め（夏の明け方の茶室・30分）

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | 目覚め / 明け方 |
| 尺 | 30分（30:00） |
| 舞台 | 茶室 |
| 主役楽器 | 箏 |
| 自然音 | 夜明け前の静けさ・竹林の風（**蝉なし・確認済み**） |
| 茶丸 | 片目 |
| 公開目安 | 8/19 |

**① タイトル【日本語】**
```
蝉が鳴き出す前の30分｜夏の明け方の和のモーニングBGM ‑ 早起きの朝に
```

**① タイトル【English】**
```
Before the Cicadas 30min | Summer Dawn Japanese Wake-up Ambient | Koto
```

**② 概要【日本語】**
```
夏の明け方の茶室に、ごく小さな箏の音が流れはじめます。
まだ蝉が鳴き出していない、一日でいちばん静かな時間です。

目覚ましではありません。すでに起きたあとの、
頭がまだ動き出していない時間に流しておくためのBGMです。

盛り上がりは作らず、静かなところから少しだけ明るくなるように。
30分かけて、外が白んでいくのに合わせて整えました。

茶丸の間 / Chamaru
和の集中・休息・安眠BGMを届けるチャンネルです。
茶丸は、この部屋にいるだるまです。

#モーニングBGM #目覚め #和風BGM #朝活 #箏 #夏 #japaneseambient
```

**② 概要【English】**
```
Very small koto notes begin in a tea room at summer dawn.
The cicadas have not started yet — the quietest hour of the day.

This is not an alarm. It is meant to play quietly after you are already up,
during the time when your mind has not started moving yet.

There is no peak — only one direction, from quiet to a little brighter,
following the sky as it lightens over thirty minutes.

Chamaru / 茶丸の間
Japanese ambient for focus, rest and sleep.
Chamaru is the daruma who lives in this room.

#japaneseambient #morningmusic #wakeup #koto #gentlemorning
```

**③ タグ**
```
モーニングBGM, 目覚め, 和風BGM, 朝活, 箏, 早起き, 夏BGM, japanese ambient, morning music, wake up music, koto music
```

**④ Suno — Style** ✅原本
```
Japanese morning ambient, solo koto with single sparse notes, very sparse at first then gradually a little brighter, slow steady tempo, no drums, no sudden dynamics, the cool still air before dawn in summer, a faint breeze through a bamboo grove, no cicadas, clear and cool turning warm, minimal
```
**④ Suno — Exclude** ✅原本
```
vocals, drums, percussion, alarm sounds, sudden onset, buildup, climax, bright synths, cicadas
```
> Exclude に `cicadas` を追加している唯一の回。**完成音源に蝉が入っていないことを聴感で確認済み。**

**⑤ Gemini — 動画用背景** ✅原本
```
A photorealistic interior of a traditional Japanese wa-modern tea room at dawn in summer, shot at eye level, front view. A worn dark wooden table surface fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale dawn light comes through a shoji window on the left, the room still dim, the sky just beginning to lighten from deep indigo toward pale blue. Through the window, a grove of fresh green bamboo is visible in the early light, softly blurred, still and windless. In the blurred background: tatami mats, a shoji screen, and a single morning glory in a small vase placed off to the side, out of focus. Deep indigo turning to cool pale blue and warm washi-paper tones, still and quiet. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景** ✅原本
```
A photorealistic interior of a traditional Japanese wa-modern tea room at dawn in summer, shot at eye level, front view, 16:9. A worn dark wooden table surface fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale dawn light comes through a shoji window on the left, the room still dim, the sky beyond just beginning to lighten from deep indigo toward pale blue. Through the window, a grove of fresh green bamboo is visible in the early light, softly blurred, still and windless. The right third of the frame is a plain shoji screen in shadow, simple and uncluttered with nothing on it. In the blurred background: tatami mats and a single morning glory in a small vase placed to the left, out of focus. Deep indigo and cool pale blue against warm washi-paper tones, high contrast between the lit window on the left and the shadowed right side. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style.
```
> 夏の明け方は**藍色→淡い水色**。9月版より一段暗く冷たい色から始める。朝顔の小物で夏の明け方であることが一目で伝わる。

**⑥ サムネ**：主ラベル `目覚め` / バッジ `30 MIN`
**⑦ 茶丸座標（動画背景）**：cx=1500, basey=1180

**⑧ ファイル**
- 動画：`蝉が鳴き出す前の30分｜夏の明け方の和のモーニングBGM.mp4`（113MB / 30:00）
- サムネ：`thumb_26_wake.png`
- 音源：`26_final.wav` ／ 合成済み背景：`bg26_with_chamaru.png`

---

## 27 ｜ 🆕 目覚め（夏の明け方の縁側・30分）

> **音域で一方向を作る回。** 低音域の長い息から始め、空が白むにつれて中音域へ上げる。
> **音量は上げない**ので「盛り上げない」原則は守られる。目覚め4本のなかで唯一、暗いところから始まる設計。

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | 目覚め / 明け方（夜明け前から） |
| 尺 | 30分（30:00） |
| 舞台 | 縁側 |
| 主役楽器 | 尺八 |
| 自然音 | 夜明け前の暗さ・打ち水・終盤に遠い蝉 |
| 茶丸 | 片目 |
| 公開目安 | 8/23 |

**① タイトル【日本語】**
```
夜が明けるまでの30分｜夏の明け方の和のモーニングBGM ‑ 早起きの朝に
```

**① タイトル【English】**
```
The Cool Hour Before Sunrise 30min | Japanese Wake-up Ambient | Shakuhachi
```

**② 概要【日本語】**
```
夏の明け方の縁側に、低い尺八の息づかいが流れはじめます。
まだ外は暗く、風だけが通っていく時間です。

目覚ましではありません。すでに起きたあとの、
頭がまだ動き出していない時間に流しておくためのBGMです。

音量は上げず、低いところから少しずつ高いところへ。
30分かけて、空が白んで最初の蝉が鳴くまでを辿ります。

茶丸の間 / Chamaru
和の集中・休息・安眠BGMを届けるチャンネルです。
茶丸は、この部屋にいるだるまです。

#モーニングBGM #目覚め #和風BGM #朝活 #尺八 #夏 #japaneseambient
```

**② 概要【English】**
```
A low shakuhachi breath begins on a veranda before sunrise in summer.
It is still dark outside, and only the air is moving.

This is not an alarm. It is meant to play quietly after you are already up,
during the time when your mind has not started moving yet.

The volume never rises — only the register, from low to middle.
Thirty minutes tracing the sky as it lightens, up to the first cicada.

Chamaru / 茶丸の間
Japanese ambient for focus, rest and sleep.
Chamaru is the daruma who lives in this room.

#japaneseambient #morningmusic #wakeup #shakuhachi #gentlemorning
```

**③ タグ**
```
モーニングBGM, 目覚め, 和風BGM, 朝活, 尺八, 夜明け, 早起き, 夏BGM, japanese ambient, morning music, wake up music, shakuhachi
```

**④ Suno — Style（27-A・前半用／暗い立ち上がり）** ✅原本
```
Japanese morning ambient, solo shakuhachi in the low register with long breathy sustained notes, very sparse, slow steady tempo, no drums, no sudden dynamics, never louder, the dark cool hour before sunrise in summer, a faint breeze and the sound of water on stone, dark and cool, minimal
```

**④ Suno — Style（27-B・後半用／最初の光）** ✅原本
```
Japanese morning ambient, solo shakuhachi rising from the low to the middle register with long breathy notes, still very sparse, slow steady tempo, no drums, no sudden dynamics, never louder, first light at summer dawn, a faint breeze and a single distant cicada beginning far away, cool turning warm, minimal
```

**④ Suno — Exclude（27-A・27-B 共通）** ✅原本
```
vocals, drums, percussion, alarm sounds, sudden onset, buildup, climax, bright synths
```

> **この回だけプロンプトを2本に分けている。** 「終盤にだけ蝉」はSunoが従わず全編に散らす可能性が高いため、後半用を別生成して繋ぐ方式。
> 選定は **前半＝27-A群のt1最小 / 後半＝27-B群のt3最大**。

**⑤ Gemini — 動画用背景** ✅原本
```
A photorealistic view of a traditional Japanese engawa veranda before sunrise in summer, shot at eye level, front view. A worn dark wooden veranda floor fills the foreground, freshly dampened with water, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Very soft pale light comes from the open side on the left, the scene still mostly dark, the sky just beginning to lighten from deep indigo. Beyond the veranda, a dim green garden with fresh bamboo is visible in the near-dark, softly blurred. In the blurred background: wooden pillars, a paper screen, and a small ceramic water ladle placed off to the side, out of focus. Deep indigo and dark wood tones with the faintest cool light, still and quiet. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景** ✅原本
```
A photorealistic view of a traditional Japanese engawa veranda before sunrise in summer, shot at eye level, front view, 16:9. A worn dark wooden veranda floor fills the lower foreground, freshly dampened with water and faintly reflecting the sky, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Very soft pale light comes from the open side on the left, the scene still mostly dark, the sky just beginning to lighten from deep indigo at the horizon. Beyond the veranda, a dim green bamboo grove is visible in the near-dark, softly blurred. The right third of the frame is a dark wooden pillar and a paper screen in deep shadow, simple and uncluttered. Deep indigo and near-black wood tones with a single band of faint cool light on the left, strongly low-key. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style.
```
> **26より暗くする**（26＝空が白み始めた頃 / 27＝まだ暗い夜明け前）。打ち水で濡れた縁側が夏の明け方を示す。

**⑥ サムネ**：主ラベル `目覚め` / バッジ `30 MIN`
**⑦ 茶丸座標（動画背景）**：cx=1300, basey=1270

**⑧ ファイル**
- 動画：`夜が明けるまでの30分｜夏の明け方の和のモーニングBGM.mp4`（102MB / 30:00）
- サムネ：`thumb_27_wake.png`
- 音源：`27_final.wav` ／ 合成済み背景：`bg27_with_chamaru.png`

---

## 28 ｜ 🆕 ブレインフォグ（夏の朝の庭・60分）✅40Hz

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | ブレインフォグ / 朝 |
| 尺 | 60分（60:00） |
| 舞台 | 庭 |
| 主役楽器 | ピアノ（ごく少ない単音） |
| 自然音 | 蹲踞の水音（持続・主体テクスチャ） |
| 茶丸 | 片目 |
| 40Hz | ✅ 実施済み（L=200Hz / R=240Hz の分離をFFTで実測確認） |
| 公開目安 | 8/27 |

**① タイトル【日本語】**
```
夏の朝、思考がまとまらない時の60分｜和のBGM ‑ 40Hz帯の持続音を重ねて
```

**① タイトル【English】**
```
Japanese Ambient for Brain Fog 60min | Summer Morning Garden | Headphones
```
> **A/Bテストのため、28は「状態名」で引く英語タイトルにしている。** 29と入れ替えないこと。

**② 概要【日本語】**
```
夏の朝の庭に、蹲踞の水音がずっと流れています。
ピアノの単音をごくわずかに置き、最後まで同じ密度で流れるように整えました。

この回には、40Hz帯の低い持続音を左右で分けて重ねています。
効果を断定するものではなく、音の設計として取り入れたものです。
ヘッドホンやイヤホンでの試聴を推奨します（左右の分離が前提のため）。

朝から思考がまとまらない時、頭が散らかっている時に、
そっと流してみてください。

茶丸の間 / Chamaru
和の集中・休息・安眠BGMを届けるチャンネルです。
茶丸は、この部屋にいるだるまです。

#ブレインフォグ #和風BGM #40Hz #バイノーラルビート #ピアノ #夏 #japaneseambient
```

**② 概要【English】**
```
Water runs continuously from a stone basin in a garden on a summer morning.
Only a few single piano notes are placed on top, at an even density from start to finish.

This track has a 40Hz binaural layer (200Hz left / 240Hz right) blended underneath.
This is a factual description of the audio design, not a claim of effect.
Headphones recommended — the layer depends on left/right separation.

For mornings when your thinking will not come together.

Chamaru / 茶丸の間
Japanese ambient for focus, rest and sleep.
Chamaru is the daruma who lives in this room.

#japaneseambient #brainfog #binauralbeats #40hz #pianomusic
```

**③ タグ**
```
ブレインフォグ, 和風BGM, 40Hz, バイノーラルビート, ピアノ, 水の音, 夏BGM, japanese ambient, brain fog, binaural beats, 40hz binaural, focus ambient
```

**④ Suno — Style** ✅原本
```
Japanese traditional ambient, a continuous gentle water sound from a stone basin as the main texture with only a few sparse felt piano single notes, very sparse repeating pattern, steady slow-medium tempo, no drums, no build-up, a quiet summer morning garden, clear and dry, meditative, minimal, even density throughout
```
**④ Suno — Exclude** ✅原本
```
vocals, drums, percussion, buildup, climax, orchestral swell, synth pads, pop
```
**④ 後処理**：40Hz重ね実施済み（音量統一の前）

**⑤ Gemini — 動画用背景** ✅原本
```
A photorealistic view of a quiet traditional Japanese garden on a misty summer morning, shot at eye level, front view. A worn dark wooden deck edge fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft diffused morning light comes from the left through a low white mist that hangs across the garden. Beyond the deck, a stone water basin with water running quietly and a grove of fresh green bamboo dissolve into the mist, heavily softened. The scene is deliberately sparse and uncluttered, with very few objects and low contrast. Muted matcha-green fading into soft white, still and quiet, hazy. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景** ✅原本
```
A photorealistic view of a quiet traditional Japanese garden on a misty summer morning, shot at eye level, front view, 16:9. A worn dark wooden deck edge fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft diffused morning light comes from the left through a low white mist that hangs across the garden. Beyond the deck, a stone water basin with water running quietly is faintly visible, and a grove of fresh green bamboo dissolves into the mist, heavily softened. The right third of the frame is almost entirely mist, pale and empty. The scene is deliberately sparse and uncluttered, with very few objects and low contrast. Muted matcha-green fading into soft white, still and quiet, hazy. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style.
```
> **霧は「ブレインフォグ」の視覚メタファー。** 同時に情報量を減らし、右側がテキスト領域として自然に空く。集中回（澄んだ朝）との差別化にもなる。

**⑥ サムネ**：主ラベル `頭のもや`（状態名主体） / バッジ `40Hz` `60 MIN`
**⑦ 茶丸座標（動画背景）**：cx=1350, basey=1480, th=520

**⑧ ファイル**
- 動画：`夏の朝、思考がまとまらない時の60分｜40Hz帯の持続音を重ねて.mp4`（261MB / 60:00）
- サムネ：`thumb_28_brainfog.png`
- 音源：`28_final.wav` ／ 合成済み背景：`bg28_with_chamaru.png`

---

## 29 ｜ ブレインフォグ（夏の午後の窓辺・60分）✅40Hz・✅アップロード済み

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | ブレインフォグ / 午後 |
| 尺 | 60分（60:00） |
| 舞台 | 窓辺 |
| 主役楽器 | 鈴（ごく低頻度） |
| 自然音 | 遠い蝉時雨（**持続・確認済み**）・すだれ越しの風 |
| 茶丸 | 片目 |
| 40Hz | ✅ 実施済み |
| 公開設定 | 公開予約 2026/10/07 |

**① タイトル【日本語】**
```
蝉時雨の午後、頭が重い時の60分｜和のBGM ‑ 40Hz帯の持続音を重ねて
```

**① タイトル【English】**
```
40Hz Binaural Japanese Ambient 60min | For Heavy Summer Afternoons | Headphones
```
> **A/Bテストのため、29は「周波数」で引く英語タイトルにしている。** 28と入れ替えないこと。

**② 概要【日本語】**
```
夏の午後の窓辺に、遠い蝉時雨がずっと響いています。
すだれを下ろした薄暗い部屋に、鈴の音をときおりだけ。

最後まで同じ密度で流れるように整えました。

この回には、40Hz帯の低い持続音を左右で分けて重ねています。
効果を断定するものではなく、音の設計として取り入れたものです。
ヘッドホンやイヤホンでの試聴を推奨します（左右の分離が前提のため）。

暑さで頭が重くなる午後に、そっと流してみてください。

茶丸の間 / Chamaru
和の集中・休息・安眠BGMを届けるチャンネルです。
茶丸は、この部屋にいるだるまです。

#ブレインフォグ #和風BGM #40Hz #バイノーラルビート #蝉 #夏 #japaneseambient
```

**② 概要【English】**
```
Distant cicadas fill a summer afternoon beyond the window.
In a dim room behind a bamboo blind, a bell sounds only occasionally.

The density stays even from start to finish.

This track has a 40Hz binaural layer (200Hz left / 240Hz right) blended underneath.
This is a factual description of the audio design, not a claim of effect.
Headphones recommended — the layer depends on left/right separation.

For afternoons when the heat makes your head feel heavy.

Chamaru / 茶丸の間
Japanese ambient for focus, rest and sleep.
Chamaru is the daruma who lives in this room.

#japaneseambient #brainfog #binauralbeats #40hz #cicadas
```

**③ タグ**
```
ブレインフォグ, 和風BGM, 40Hz, バイノーラルビート, 鈴の音, 蝉の声, 夏BGM, japanese ambient, brain fog, binaural beats, 40hz binaural, focus ambient
```

**④ Suno — Style** ✅原本
```
Japanese traditional ambient, a continuous distant cicada drone as the main texture with only occasional rin bell placed very sparsely, steady slow-medium tempo, no drums, no build-up, still hot afternoon air behind a bamboo blind, warm and dry, meditative, minimal, even density throughout
```
**④ Suno — Exclude** ✅原本
```
vocals, drums, percussion, buildup, climax, orchestral swell, synth pads, pop, sharp transients
```
**④ 後処理**：40Hz重ね実施済み

> **蝉は持続的なノイズフロアとして使っている。** 完成音源が断続的でないことを聴感で確認済み。
> `rng`最小の選定は「持続的な蝉」という要件と構造的に一致する（断続的な蝉は音圧が波打ち rng が上がるため自動的に弾かれる）。

**⑤ Gemini — 動画用背景** ✅原本
```
A photorealistic interior of a traditional Japanese wa-modern room by a window on a hot summer afternoon, shot at eye level, front view. A worn dark wooden window ledge fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. A bamboo blind (sudare) hangs over the window on the left, casting soft horizontal stripes of light and shadow across the room. Beyond the blind, a sunlit green bamboo grove is visible, softly blurred and slightly overexposed against the shaded interior. The scene is deliberately sparse with very few objects. In the blurred background: tatami mats and a plain paper screen, out of focus. Muted matcha-green and warm washi-paper tones in shade, still and quiet. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景** ✅原本
```
A photorealistic interior of a traditional Japanese wa-modern room by a window on a hot summer afternoon, shot at eye level, front view, 16:9. A worn dark wooden window ledge fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. A bamboo blind (sudare) hangs over the window on the left, casting sharp horizontal stripes of light and shadow across the room. Beyond the blind, a sunlit green bamboo grove is visible, softly blurred and slightly overexposed against the shaded interior. The right third of the frame is a plain wall and tatami in deep shade, simple and uncluttered. The scene is deliberately sparse with very few objects. Muted matcha-green and warm washi-paper tones in shade, with strong contrast between the bright striped light on the left and the dark right side. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style.
```
> **すだれの横縞は小サイズでも認識できる**ので、サムネの識別性が高い。29だけ視覚的に明確に浮く。

**⑥ サムネ**：主ラベル `40Hz`（周波数主体） / バッジ `頭のもや` `60 MIN`
**⑦ 茶丸座標（動画背景）**：cx=1550, basey=1350, th=540

**⑧ ファイル**
- 動画：`蝉時雨の午後、頭が重い時の60分｜40Hz帯の持続音を重ねて.mp4`（260MB / 60:00）
- サムネ：`thumb_29_brainfog.png`
- 音源：`29_final.wav` ／ 合成済み背景：`bg29_with_chamaru.png`

---

