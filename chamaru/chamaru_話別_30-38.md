# 話別詳細 — 紅葉 30〜38（10月分）

> 統合マスター_YYMMDD.md（インデックス）から分割。共通ルール・タグ設計・要対応リストはインデックス側を参照。

**制作完了（音源・画像合成・サムネ・動画エンコードとも2026-08-30時点で全9話完了）。** テーマは紅葉。8月＝夏（青竹）、9月＝初秋（すすき・月見）からの切り替え。原本は `指示書_3038_動画制作.md`。

### この9本の狙い

- **虫の音を入れない**：10月中旬で虫はほぼ鳴き終わるが、Sunoは "autumn" から虫の音を出しやすいため、全9本のSuno Excludeに `crickets, insects` を明示的に追加している
- **画面疲れ（33・37）に紅葉を入れない**：紅葉は高彩度で「目を休める」目的と矛盾するため、苔・常緑・灰色の石・雨の低彩度で作る。Geminiプロンプトの `with no autumn colour — only deep greens and greys` を必ず残す
- **鹿威し（ししおどし）**：まだ使っていない和の音。断続音なので均一密度が必要な集中・ブレインフォグには使えず、余白の多い31（安眠）・32（リセット）だけで使う

### 茶丸の使い分け

- **片目版**（`chamaru_oneeye_cutout.png`）：30・34・35・36
- **正面版**（`chamaru_master_cutout.png`）：31・32・33・37・38

### 出力先

```
30_集中_紅葉の朝の庭\
31_安眠_紅葉の宵の庭\
32_リセット_紅葉の午後の窓辺\
33_画面疲れ_雨の夕暮れの茶室\
34_ブレインフォグ_紅葉の午後の囲炉裏端\
35_目覚め_初霜の明け方の庭\
36_集中_紅葉の朝の窓辺\
37_画面疲れ_苔庭の夕暮れの縁側\
38_安眠_秋の夜長の縁側\
```

### ⚠️35〜38の背景について

`指示書_3038_動画制作.md` のGeminiプロンプト（下記⑤）どおりに最初に生成した画像が、なぜか34（囲炉裏端）と同じ室内シーンの使い回しになっていた（2026-08-29発覚）。ユーザーが同じプロンプトで再生成し、話ごとの舞台（庭・窓辺・縁側）と一致することを確認した上で、実際にはその再生成画像（`{話数}__001.png`）を使って茶丸を合成している。下記⑤のプロンプトは原本のまま掲載しているが、**実際に採用した画像ファイルは⑧に記載のとおり**。

---

## 30 ｜ 集中（紅葉の朝の庭・60分）

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | 集中 / 朝 |
| 尺 | 60分（60:00） |
| 舞台 | 庭 |
| 主役楽器 | 箏 |
| 自然音 | 落ち葉・朝の風 |
| 茶丸 | 片目 |
| 公開目安 | 10/02 |

**① タイトル【日本語】**
```
紅葉の庭で集中する60分｜落ち葉と箏の和のBGM ‑ 作業・勉強用
```

**① タイトル【English】**
```
60 Min Japanese Ambient for Focus | Koto & Falling Leaves | Study & Work
```

**② 概要【日本語】**
```
紅葉の庭に、静かな箏の音が流れます。
乾いた落ち葉が風にすれる音だけを残した、60分の集中用BGMです。

盛り上がりを作らず、最後まで同じ密度で流れるように整えました。
音が意識に上がってこないことを目指しています。

頭がぼんやりする朝、思考が散らかっている時、
作業や勉強のはじまりに置いてみてください。

茶丸の間 / Chamaru
和の集中・休息・安眠BGMを届けるチャンネルです。
茶丸は、この部屋にいるだるまです。

#作業用BGM #集中 #和風BGM #勉強用BGM #箏 #紅葉 #japaneseambient
```

**② 概要【English】**
```
Quiet koto notes in a Japanese garden in autumn colour.
A 60-minute ambient track for focus, with only dry leaves moving in a morning wind.

No build-ups and no sudden dynamics — the density stays even from start to finish.
Designed to stay below your attention rather than draw it.

For scattered mornings, and for the first hour of work or study.

Chamaru / 茶丸の間
Japanese ambient for focus, rest and sleep.
Chamaru is the daruma who lives in this room.

#japaneseambient #studymusic #focusmusic #koto #autumn
```

**③ タグ**
```
作業用BGM, 集中BGM, 和風BGM, 勉強用BGM, 箏, 落ち葉, 紅葉, japanese ambient, study music, focus music, koto music
```

**④ Suno — Style** ✅原本
```
Japanese traditional ambient, solo koto, sparse repeating pattern, steady slow-medium tempo, no drums, no build-up, dry autumn leaves moving in a gentle morning wind, crisp and clear, meditative, minimal
```
**④ Suno — Exclude** ✅原本
```
vocals, drums, percussion, buildup, climax, orchestral swell, synth pads, pop, crickets, insects
```

**⑤ Gemini — 動画用背景** ✅原本
```
A photorealistic view of a quiet traditional Japanese garden on an autumn morning, shot at eye level, front view. A worn dark wooden deck edge fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft clear morning light comes from the left. Beyond the deck, moss, stepping stones and Japanese maple trees in full red and orange autumn colour are visible, softly blurred, with a few dry leaves scattered on the ground. In the blurred background: a stone water basin and a small ceramic cup placed off to the side, out of focus. Deep red and amber against dark wood and moss green, crisp and serene. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景** ✅原本
```
A photorealistic view of a quiet traditional Japanese garden on an autumn morning, shot at eye level, front view, 16:9. A worn dark wooden deck edge fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft clear morning light comes from the left. Beyond the deck, Japanese maple trees in vivid red and orange autumn colour are visible on the left, softly blurred, with dry leaves scattered on the moss. The right third of the frame is a plain dark wooden wall in shadow, simple and uncluttered. Vivid red and amber against dark wood, high contrast between the lit left side and the shadowed right side. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style.
```
> サムネは実際には動画用（gemini_image_001.png）を流用（サムネ専用素材は生成していない）。

**⑥ サムネ**：主ラベル `集中` / バッジ `60 MIN`
**⑦ 茶丸座標（動画背景）**：cx=480, basey=555, th=320

**⑧ ファイル**
- 動画：`紅葉の庭で集中する60分.mp4`（197MB / 60:00）
- サムネ：`thumb_30_shuchu.png`
- 音源：`紅葉の庭で集中する60分.wav` ／ 合成済み背景：`bg30_with_chamaru.png`（採用元 gemini_image_001.png）

---

## 31 ｜ 安眠（紅葉の宵の庭・90分）

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | 安眠 / 宵〜夜 |
| 尺 | 90分（90:00） |
| 舞台 | 庭 |
| 主役楽器 | ピアノ |
| 自然音 | 紅葉の残光・遠い鹿威し |
| 茶丸 | 正面 |
| 公開目安 | 10/05 |

**① タイトル【日本語】**
```
紅葉の庭が暮れていく90分｜和のスリープBGM ‑ 睡眠・瞑想
```

**① タイトル【English】**
```
90 Min Japanese Ambient for Sleep | Autumn Garden at Dusk | Piano & Water Fountain
```

**② 概要【日本語】**
```
紅葉の庭に、日が落ちていきます。
やわらかなピアノと、遠くの鹿威しの音だけを残した、90分の睡眠用BGMです。

盛り上がりを作らず、少しずつ静かになっていくように整えました。
音が意識に残らないことを目指しています。

日が暮れてから、灯りを落としたあとに、
小さな音量で流しておいてください。

茶丸の間 / Chamaru
和の集中・休息・安眠BGMを届けるチャンネルです。
茶丸は、この部屋にいるだるまです。

#睡眠用BGM #安眠 #和風BGM #紅葉 #ピアノ #鹿威し #japaneseambient
```

**② 概要【English】**
```
The light fades over a garden in full autumn colour.
A 90-minute sleep ambient track with soft felt piano and a distant bamboo water fountain.

No build-ups — it grows quieter little by little toward the end.
Designed to leave nothing behind in your attention.

For nights that follow an overwhelming day.
Play it at a low volume after the lights are out.

Chamaru / 茶丸の間
Japanese ambient for focus, rest and sleep.
Chamaru is the daruma who lives in this room.

#japaneseambient #sleepmusic #nightambient #pianomusic #autumn
```

**③ タグ**
```
睡眠用BGM, 安眠BGM, 和風BGM, 寝る前BGM, ピアノ, 鹿威し, 紅葉, japanese ambient, sleep music, night ambient, piano music, overwhelm, overstimulation
```

**④ Suno — Style** ✅原本
```
Japanese sleep ambient, low warm drone, soft solo felt piano occasional and distant, extremely slow, almost no melody, a quiet autumn garden after sunset and a faint distant shishi-odoshi bamboo water fountain, dark and still, fading into quiet
```
**④ Suno — Exclude** ✅原本
```
vocals, drums, percussion, tempo, buildup, bright tones, high frequencies, crickets, insects
```
> `shishi-odoshi` をSunoが理解しない可能性があるため `bamboo water fountain` を併記。31・32だけで使う音（余白が多い状態のみ）。

**⑤ Gemini — 動画用背景** ✅原本
```
A photorealistic view of a quiet traditional Japanese garden at dusk in autumn, shot at eye level, front view. A worn dark wooden deck edge fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. The last warm light of sunset comes from the left, low and golden, the garden already settling into shadow. Beyond the deck, Japanese maple trees in deep red autumn colour stand against a sky fading from amber to deep indigo, softly blurred, with a bamboo shishi-odoshi water fountain barely visible in the dark. In the blurred background: a stone lantern placed off to the side, out of focus. Deep red and amber against indigo and dark wood, quiet and still. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景** ✅原本
```
A photorealistic view of a quiet traditional Japanese garden at dusk in autumn, shot at eye level, front view, 16:9. A worn dark wooden deck edge fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. The last warm light of sunset comes from the left, low and golden. Beyond the deck, Japanese maple trees in deep red autumn colour stand against a sky fading from amber to deep indigo on the left, softly blurred. The right third of the frame is dark garden in deep shadow, simple and uncluttered. Deep red and amber against indigo and dark wood, high contrast between the glowing left side and the shadowed right side. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style.
```
> サムネは動画用（gemini_image_003.png）を流用。

**⑥ サムネ**：主ラベル `安眠` / バッジ `90 MIN`
**⑦ 茶丸座標（動画背景）**：cx=420, basey=555, th=310

**⑧ ファイル**
- 動画：`紅葉の庭が暮れていく90分.mp4`（265MB / 90:00）
- サムネ：`thumb_31_anmin.png`
- 音源：`紅葉の庭が暮れていく90分.wav` ／ 合成済み背景：`bg31_with_chamaru.png`（採用元 gemini_image_003.png）

---

## 32 ｜ リセット（紅葉の午後の窓辺・90分）

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | リセット / 午後 |
| 尺 | 90分（90:00） |
| 舞台 | 窓辺 |
| 主役楽器 | 鈴 |
| 自然音 | 鹿威し・秋の風 |
| 茶丸 | 正面 |
| 公開目安 | 10/09 |

**① タイトル【日本語】**
```
午後の窓辺で紅葉を眺める90分｜和の休息BGM ‑ 休憩・切り替えに
```

**① タイトル【English】**
```
90 Min Japanese Ambient | When the Day Has Been Too Much | Bells & Autumn Wind
```

**② 概要【日本語】**
```
午後の窓辺から、紅葉の庭が見えています。
控えめな鈴の音と、遠くの鹿威しだけを残した、90分の休息用BGMです。

盛り上がりを作らず、ゆっくりと流れるように整えました。
何かをしながらでも、手を止めても、どちらでも。

根を詰めたあとの休憩や、気持ちの切り替えに、
少しのあいだ流してみてください。

茶丸の間 / Chamaru
和の集中・休息・安眠BGMを届けるチャンネルです。
茶丸は、この部屋にいるだるまです。

#休息BGM #リラックス #和風BGM #紅葉 #鈴 #鹿威し #japaneseambient
```

**② 概要【English】**
```
A garden in autumn colour, seen from a window in the afternoon.
A 90-minute ambient track for rest, with restrained bell tones and a distant bamboo water fountain.

No build-ups — it simply moves slowly from beginning to end.
Works whether you keep working or put everything down.

For when the day has been too much, for breaks after long
stretches of concentration, and for switching gears.

Chamaru / 茶丸の間
Japanese ambient for focus, rest and sleep.
Chamaru is the daruma who lives in this room.

#japaneseambient #relaxingmusic #autumn #overwhelm #restmusic
```

**③ タグ**
```
休息BGM, リラックスBGM, 和風BGM, 切り替え, 鈴の音, 鹿威し, 紅葉, japanese ambient, relaxing music, overwhelm, overstimulation
```

**④ Suno — Style** ✅原本
```
Japanese ambient, occasional rin bell and small suzu bells placed very sparsely, very slow, spacious, lots of silence, a dry autumn wind and a faint distant shishi-odoshi bamboo water fountain, calm and warm, contemplative
```
**④ Suno — Exclude** ✅原本
```
vocals, drums, percussion, rhythm, melody hooks, buildup, bright synths, crickets, insects
```

**⑤ Gemini — 動画用背景** ✅原本
```
A photorealistic interior of a traditional Japanese wa-modern room by a window on an autumn afternoon, shot at eye level, front view. A worn dark wooden window ledge fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft low golden afternoon light comes through the open shoji window on the left. Beyond the window, a garden with Japanese maple trees in red and orange autumn colour is visible, softly blurred, with a bamboo shishi-odoshi water fountain among the moss. In the blurred background: tatami mats and a single red maple leaf resting on the ledge to the side, out of focus. Muted amber and red against warm washi-paper tones, calm and warm. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景** ✅原本
```
A photorealistic interior of a traditional Japanese wa-modern room by a window on an autumn afternoon, shot at eye level, front view, 16:9. A worn dark wooden window ledge fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft low golden afternoon light comes through the open shoji window on the left. Beyond the window, Japanese maple trees in vivid red and orange autumn colour fill the left side, softly blurred. The right third of the frame is a plain shoji screen in shadow, simple and uncluttered. Vivid red and amber against warm washi-paper tones, high contrast between the bright window on the left and the shadowed right side. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style.
```
> サムネは動画用（gemini_image_006.png）を流用。

**⑥ サムネ**：主ラベル `リセット` / バッジ `90 MIN`
**⑦ 茶丸座標（動画背景）**：cx=500, basey=555, th=310

**⑧ ファイル**
- 動画：`午後の窓辺で紅葉を眺める90分.mp4`（270MB / 90:00）
- サムネ：`thumb_32_reset.png`
- 音源：`午後の窓辺で紅葉を眺める90分.wav` ／ 合成済み背景：`bg32_with_chamaru.png`（採用元 gemini_image_006.png）

---

## 33 ｜ 画面疲れ（雨の夕暮れの茶室・60分）⚠️紅葉なし

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | 画面疲れ / 夕暮れ |
| 尺 | 60分（60:00） |
| 舞台 | 茶室 |
| 主役楽器 | 箏（低音域のみ） |
| 自然音 | 静かな雨・軒の雫 |
| 茶丸 | 正面 |
| 公開目安 | 10/12 |

**① タイトル【日本語】**
```
雨の夕暮れに目を休める60分｜和の休息BGM ‑ 画面から離れる時間に
```

**① タイトル【English】**
```
60 Min Japanese Ambient for a Screen Break | Rain at Dusk | Low Koto, No Highs
```

**② 概要【日本語】**
```
雨の夕暮れ、茶室に低く落ち着いた和の音が流れます。
箏の低音域だけを使い、高い音を抑えて設計しました。

一日中画面を見たあとの時間に、
画面を消して、音だけを流しておくための60分です。

盛り上がりを作らず、暗く静かな雨の情景とともに。
目と耳を休める時間に置いてみてください。

茶丸の間 / Chamaru
和の集中・休息・安眠BGMを届けるチャンネルです。
茶丸は、この部屋にいるだるまです。

#休息BGM #デジタルデトックス #和風BGM #目の休息 #雨の音 #japaneseambient
```

**② 概要【English】**
```
Low, settled Japanese sounds in a tea room on a rainy evening.
Only the low and middle register of the koto — the high frequencies are deliberately held back.

Sixty minutes for the hour after a full day of screens.
Turn the screen off and leave only the sound playing.

No build-ups, alongside the quiet of steady rain.
For the time you set aside to rest your eyes and ears.

Chamaru / 茶丸の間
Japanese ambient for focus, rest and sleep.
Chamaru is the daruma who lives in this room.

#japaneseambient #screenbreak #digitaldetox #eyerest #rainsounds
```

**③ タグ**（`紅葉` は入れない）
```
休息BGM, デジタルデトックス, 和風BGM, 目の休息, 箏, 雨の音, japanese ambient, screen break, digital detox, eye rest
```

**④ Suno — Style** ✅原本
```
Japanese ambient, solo koto in the low and middle register only, very slow, spacious, lots of silence, steady quiet rain and water dripping from the eaves at dusk, warm dark tones, no high frequencies, gentle and dim, contemplative
```
**④ Suno — Exclude** ✅原本
```
vocals, drums, percussion, rhythm, melody hooks, buildup, bright synths, high frequencies, sharp transients, crickets, insects
```
**後処理**：6.5kHz程度のローパスを軽くかける（`chamaru_build.py` の `lowpass_hz: 6500` で対応済み）

**⑤ Gemini — 動画用背景** ✅原本 ⚠️紅葉なし
```
A photorealistic interior of a traditional Japanese wa-modern tea room at dusk during steady rain in autumn, shot at eye level, front view. A worn dark wooden table surface fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft dim grey light comes from a shoji window on the left, low and weak, the room settling into shadow. Through the window, a moss garden with evergreen bamboo and wet stone in the rain is visible, softly blurred, with no autumn colour — only deep greens and greys. In the blurred background: tatami mats and a plain shoji screen, out of focus, with very few objects. Muted grey-green, wet dark wood, very low saturation, dim and restful. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景** ✅原本 ⚠️紅葉なし
```
A photorealistic interior of a traditional Japanese wa-modern tea room at dusk during steady rain in autumn, shot at eye level, front view, 16:9. A worn dark wooden table surface fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft dim grey light comes from a shoji window on the left, low and weak. Through the window, a moss garden with evergreen bamboo and wet stone in the rain is visible on the left, softly blurred, with no autumn colour — only deep greens and greys. The right third of the frame is a plain shoji screen in deep shadow, simple and uncluttered. Muted grey-green and wet dark wood, very low saturation, dim and restful. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style.
```
> `with no autumn colour — only deep greens and greys` を消さないこと。サムネは動画用（gemini_image_008.png）を流用。実際の採用画像も紅葉なしを確認済み。

**⑥ サムネ**：主ラベル `目を休める` / バッジ `60 MIN`
**⑦ 茶丸座標（動画背景）**：cx=510, basey=555, th=300

**⑧ ファイル**
- 動画：`雨の夕暮れに目を休める60分.mp4`（168MB / 60:00）
- サムネ：`thumb_33_screen.png`
- 音源：`雨の夕暮れに目を休める60分.wav` ／ 合成済み背景：`bg33_with_chamaru.png`（採用元 gemini_image_008.png）

---

## 34 ｜ ブレインフォグ（紅葉の午後の囲炉裏端・60分）✅40Hz

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | ブレインフォグ / 午後 |
| 尺 | 60分（60:00） |
| 舞台 | 囲炉裏端 |
| 主役楽器 | 箏 |
| 自然音 | 薪火（持続） |
| 茶丸 | 片目 |
| 公開目安 | 10/16 |

**① タイトル【日本語】**
```
頭が回らない秋の午後に60分｜和のBGM ‑ 40Hz帯の持続音を重ねて
```

**① タイトル【English】**
```
Japanese Ambient for Brain Fog 60min | Hearthside Autumn Afternoon | Headphones
```

**② 概要【日本語】**
```
秋の午後の囲炉裏端に、薪のはぜる音がずっと続いています。
箏の音をごくわずかに置き、最後まで同じ密度で流れるように整えました。

この回には、40Hz帯の低い持続音を左右で分けて重ねています。
効果を断定するものではなく、音の設計として取り入れたものです。
ヘッドホンやイヤホンでの試聴を推奨します（左右の分離が前提のため）。

午後になって頭が回らなくなる時間に、
そっと流してみてください。

茶丸の間 / Chamaru
和の集中・休息・安眠BGMを届けるチャンネルです。
茶丸は、この部屋にいるだるまです。

#ブレインフォグ #和風BGM #40Hz #バイノーラルビート #焚き火の音 #紅葉 #japaneseambient
```

**② 概要【English】**
```
Firewood crackles steadily beside a sunken hearth on an autumn afternoon.
Only a few koto notes are placed on top, at an even density from start to finish.

This track has a 40Hz binaural layer (200Hz left / 240Hz right) blended underneath.
This is a factual description of the audio design, not a claim of effect.
Headphones recommended — the layer depends on left/right separation.

For the hours in the afternoon when your head stops moving.

Chamaru / 茶丸の間
Japanese ambient for focus, rest and sleep.
Chamaru is the daruma who lives in this room.

#japaneseambient #brainfog #binauralbeats #40hz #firesounds
```

**③ タグ**
```
ブレインフォグ, 和風BGM, 40Hz, バイノーラルビート, 箏, 焚き火の音, 紅葉, japanese ambient, brain fog, binaural beats, 40hz binaural, focus ambient
```

**④ Suno — Style** ✅原本
```
Japanese traditional ambient, a continuous crackling hearth fire as the main texture with only a few sparse koto touches, very sparse repeating pattern, steady slow-medium tempo, no drums, no build-up, a quiet autumn afternoon indoors, warm and dry, meditative, minimal, even density throughout
```
**④ Suno — Exclude** ✅原本
```
vocals, drums, percussion, buildup, climax, orchestral swell, synth pads, pop, crickets, insects
```
**後処理**：40Hz重ねを必ず実行（音量統一の前。`chamaru_build.py` の `binaural_40hz: true` で対応済み・実測ピーク L=200.0/R=240.0で確認済み）

> 薪火を主体テクスチャにしている。広帯域の持続音なので40Hzトーンが自然に溶ける。

**⑤ Gemini — 動画用背景** ✅原本
```
A photorealistic interior of a traditional Japanese wa-modern room beside a sunken irori hearth on an autumn afternoon, shot at eye level, front view. A worn dark wooden floor beside the hearth fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft low golden afternoon light comes from a shoji window on the left, with a warm glow from the burning hearth fire. Beyond the window, Japanese maple trees in red autumn colour are visible, softly blurred. The scene is deliberately sparse and uncluttered. In the blurred background: a hanging iron kettle and tatami mats, out of focus, with very few objects. Muted amber and red, dark wood and warm fire tones, still and quiet. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景** ✅原本
```
A photorealistic interior of a traditional Japanese wa-modern room beside a sunken irori hearth on an autumn afternoon, shot at eye level, front view, 16:9. A worn dark wooden floor beside the hearth fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft low golden afternoon light comes from a shoji window on the left, with a warm glow from the burning hearth fire on the left. Beyond the window, Japanese maple trees in red autumn colour are visible, softly blurred. The right third of the frame is plain tatami and a dark wall in shadow, simple and uncluttered. Muted amber and red against dark wood and warm fire tones, high contrast between the glowing left side and the shadowed right side. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style.
```
> ブレインフォグ回は静かで情報量の少ない絵にする（小物を増やさない）。サムネは動画用（gemini_image_011.png）を流用。

**⑥ サムネ**：主ラベル `頭のもや` / バッジ `40Hz` `60 MIN`（**状態名主体で統一。28と同じくA/Bテストの対象外・入れ替えない**）
**⑦ 茶丸座標（動画背景）**：cx=640, basey=555, th=300

**⑧ ファイル**
- 動画：`頭が回らない秋の午後に60分.mp4`（173MB / 60:00）
- サムネ：`thumb_34_brainfog.png`
- 音源：`頭が回らない秋の午後に60分.wav` ／ 合成済み背景：`bg34_with_chamaru.png`（採用元 gemini_image_011.png）

---

## 35 ｜ 目覚め（初霜の明け方の庭・30分）

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | 目覚め / 明け方 |
| 尺 | 30分（30:00） |
| 舞台 | 庭 |
| 主役楽器 | 鈴 |
| 自然音 | 初霜・小鳥 |
| 茶丸 | 片目 |
| 公開目安 | 10/19 |

**① タイトル【日本語】**
```
初霜の庭で目を覚ます30分｜和のモーニングBGM ‑ 秋の朝に
```

**① タイトル【English】**
```
30 Min Gentle Wake-up Ambient | First Frost in an Autumn Garden | Bells
```

**② 概要【日本語】**
```
初霜の降りた庭に、ごく小さな鈴の音が流れはじめます。
冷たく澄んだ空気だけが動いている時間です。

目覚ましではありません。すでに起きたあとの、
頭がまだ動き出していない時間に流しておくためのBGMです。

盛り上がりは作らず、静かなところから少しだけ明るくなるように。
30分かけて、冷たい朝が少しずつゆるんでいくように整えました。

茶丸の間 / Chamaru
和の集中・休息・安眠BGMを届けるチャンネルです。
茶丸は、この部屋にいるだるまです。

#モーニングBGM #目覚め #和風BGM #朝活 #鈴 #紅葉 #japaneseambient
```

**② 概要【English】**
```
Very small bell tones begin over a garden touched by the first frost.
Only the cold, clear air is moving.

This is not an alarm. It is meant to play quietly after you are already up,
during the time when your mind has not started moving yet.

There is no peak — only one direction, from quiet to a little brighter,
as thirty minutes of cold morning slowly soften.

Chamaru / 茶丸の間
Japanese ambient for focus, rest and sleep.
Chamaru is the daruma who lives in this room.

#japaneseambient #morningmusic #wakeup #gentlemorning #autumn
```

**③ タグ**
```
モーニングBGM, 目覚め, 和風BGM, 朝活, 鈴の音, 初霜, 紅葉, japanese ambient, morning music, wake up music, gentle morning
```

**④ Suno — Style** ✅原本
```
Japanese morning ambient, occasional rin bell and small suzu bells, very sparse at first then gradually a little brighter, slow steady tempo, no drums, no sudden dynamics, cold still air at dawn in late autumn with first frost, a few distant birds, cold turning warm, minimal
```
**④ Suno — Exclude** ✅原本
```
vocals, drums, percussion, alarm sounds, sudden onset, buildup, climax, bright synths, crickets, insects
```

**⑤ Gemini — 動画用背景** ✅原本（**⚠️初回生成は34と同一シーンの誤りだったため再生成した。以下は原本プロンプト**）
```
A photorealistic view of a quiet traditional Japanese garden at dawn in late autumn, shot at eye level, front view. A worn dark wooden deck edge fills the foreground, touched with white frost, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale dawn light comes from the left, still dim, the sky just beginning to lighten from cold blue toward pale gold. Beyond the deck, moss and fallen maple leaves are covered with a thin white frost, and Japanese maple trees in deep red autumn colour stand in the cold morning air, softly blurred. In the blurred background: a stone water basin rimmed with frost, out of focus. Cold blue and white frost against deep red and dark wood, still and quiet. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景** ✅原本
```
A photorealistic view of a quiet traditional Japanese garden at dawn in late autumn, shot at eye level, front view, 16:9. A worn dark wooden deck edge fills the lower foreground, touched with white frost, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale dawn light comes from the left, still dim, the sky just beginning to lighten from cold blue toward pale gold. Beyond the deck, fallen maple leaves covered with thin white frost and maple trees in deep red autumn colour fill the left side, softly blurred. The right third of the frame is dark garden in deep shadow, simple and uncluttered. Cold blue and white frost against deep red and dark wood, high contrast between the pale left side and the shadowed right side. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style.
```
> 再生成後の実ファイル（`35__001.png`）で舞台（初霜の庭）が正しいことを目視確認済み。サムネも同ファイルを流用。

**⑥ サムネ**：主ラベル `目覚め` / バッジ `30 MIN`
**⑦ 茶丸座標（動画背景）**：cx=500, basey=555, th=300

**⑧ ファイル**
- 動画：`初霜の庭で目を覚ます30分.mp4`（108MB / 30:00）
- サムネ：`thumb_35_mezame.png`
- 音源：`初霜の庭で目を覚ます30分.wav` ／ 合成済み背景：`bg35_with_chamaru.png`（採用元 35__001.png・再生成後）

---

## 36 ｜ 集中（紅葉の朝の窓辺・60分）

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | 集中 / 朝 |
| 尺 | 60分（60:00） |
| 舞台 | 窓辺 |
| 主役楽器 | 尺八 |
| 自然音 | 落ち葉・朝の空気 |
| 茶丸 | 片目 |
| 公開目安 | 10/23 |

**① タイトル【日本語】**
```
紅葉の窓辺で集中する60分｜尺八と秋の朝の和のBGM ‑ 作業・勉強用
```

**① タイトル【English】**
```
60 Min Japanese Ambient for Focus | Shakuhachi & Clear Autumn Air | Study & Work
```

**② 概要【日本語】**
```
紅葉の見える窓辺に、澄んだ尺八の音が流れます。
冷たい朝の空気と、落ち葉の音だけを残した、60分の集中用BGMです。

盛り上がりを作らず、最後まで同じ密度で流れるように整えました。
音が意識に上がってこないことを目指しています。

すっきりした秋の朝、作業や勉強のはじまりに置いてみてください。

茶丸の間 / Chamaru
和の集中・休息・安眠BGMを届けるチャンネルです。
茶丸は、この部屋にいるだるまです。

#作業用BGM #集中 #和風BGM #勉強用BGM #尺八 #紅葉 #japaneseambient
```

**② 概要【English】**
```
Clear shakuhachi notes by a window looking out on autumn colour.
A 60-minute ambient track for focus, with cold morning air and dry leaves in the wind.

No build-ups and no sudden dynamics — the density stays even from start to finish.
Designed to stay below your attention rather than draw it.

For crisp autumn mornings, and for the first hour of work or study.

Chamaru / 茶丸の間
Japanese ambient for focus, rest and sleep.
Chamaru is the daruma who lives in this room.

#japaneseambient #studymusic #focusmusic #shakuhachi #autumn
```

**③ タグ**
```
作業用BGM, 集中BGM, 和風BGM, 勉強用BGM, 尺八, 落ち葉, 紅葉, japanese ambient, study music, focus music, shakuhachi
```

**④ Suno — Style** ✅原本
```
Japanese traditional ambient, solo shakuhachi with long breathy sustained notes, sparse repeating pattern, steady slow-medium tempo, no drums, no build-up, cold clear autumn morning air and dry leaves in a light wind, crisp and dry, meditative, minimal
```
**④ Suno — Exclude** ✅原本
```
vocals, drums, percussion, buildup, climax, orchestral swell, synth pads, pop, crickets, insects
```

**⑤ Gemini — 動画用背景** ✅原本（**⚠️初回生成は34と同一シーンの誤りだったため再生成した。以下は原本プロンプト**）
```
A photorealistic interior of a traditional Japanese wa-modern room by a window on a clear autumn morning, shot at eye level, front view. A worn dark wooden window ledge fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft cold clear morning light comes through the open shoji window on the left. Beyond the window, Japanese maple trees in vivid red and orange autumn colour are visible against a pale sky, softly blurred, with a few dry leaves caught on the ledge. In the blurred background: tatami mats, a paper screen, and a small ceramic cup placed off to the side, out of focus. Vivid red and amber against pale sky and warm washi-paper tones, crisp and serene. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景** ✅原本
```
A photorealistic interior of a traditional Japanese wa-modern room by a window on a clear autumn morning, shot at eye level, front view, 16:9. A worn dark wooden window ledge fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft cold clear morning light comes through the open shoji window on the left. Beyond the window, Japanese maple trees in vivid red and orange autumn colour fill the left side against a pale sky, softly blurred, with a few dry leaves caught on the ledge. The right third of the frame is a plain shoji screen in shadow, simple and uncluttered. Vivid red and amber against pale sky and warm washi-paper tones, high contrast between the bright window on the left and the shadowed right side. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style.
```
> 再生成後の実ファイル（`36__001.png`）で舞台（紅葉の窓辺）が正しいことを目視確認済み。サムネも同ファイルを流用。窓の敷居に乗せる構図のため、他話よりbaseyが高め（480）。

**⑥ サムネ**：主ラベル `集中` / バッジ `60 MIN`
**⑦ 茶丸座標（動画背景）**：cx=350, basey=480, th=260

**⑧ ファイル**
- 動画：`紅葉の窓辺で集中する60分.mp4`（169MB / 60:00）
- サムネ：`thumb_36_shuchu.png`
- 音源：`紅葉の窓辺で集中する60分.wav` ／ 合成済み背景：`bg36_with_chamaru.png`（採用元 36__001.png・再生成後）

---

## 37 ｜ 画面疲れ（苔庭の夕暮れの縁側・60分）⚠️紅葉なし

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | 画面疲れ / 夕暮れ |
| 尺 | 60分（60:00） |
| 舞台 | 縁側 |
| 主役楽器 | 尺八（低音域のみ） |
| 自然音 | 遠い風・苔庭 |
| 茶丸 | 正面 |
| 公開目安 | 10/26 |

**① タイトル【日本語】**
```
苔庭を眺めて目を休める60分｜和の休息BGM ‑ 画面から離れる時間に
```

**① タイトル【English】**
```
60 Min Japanese Ambient for a Screen Break | Moss Garden at Dusk | Low Shakuhachi
```

**② 概要【日本語】**
```
夕暮れの縁側から、静かな苔庭が見えています。
尺八の低音域だけを使い、高い音を抑えて設計しました。

一日中画面を見たあとの時間に、
画面を消して、音だけを流しておくための60分です。

盛り上がりを作らず、彩度の低い薄暗い庭とともに。
目と耳を休める時間に置いてみてください。

茶丸の間 / Chamaru
和の集中・休息・安眠BGMを届けるチャンネルです。
茶丸は、この部屋にいるだるまです。

#休息BGM #デジタルデトックス #和風BGM #目の休息 #尺八 #苔庭 #japaneseambient
```

**② 概要【English】**
```
A quiet moss garden, seen from a veranda at dusk.
Only the low register of the shakuhachi — the high frequencies are deliberately held back.

Sixty minutes for the hour after a full day of screens.
Turn the screen off and leave only the sound playing.

No build-ups, alongside a dim garden with very little colour.
For the time you set aside to rest your eyes and ears.

Chamaru / 茶丸の間
Japanese ambient for focus, rest and sleep.
Chamaru is the daruma who lives in this room.

#japaneseambient #screenbreak #digitaldetox #eyerest #shakuhachi
```

**③ タグ**（`紅葉` は入れない）
```
休息BGM, デジタルデトックス, 和風BGM, 目の休息, 尺八, 苔庭, japanese ambient, screen break, digital detox, eye rest
```

**④ Suno — Style** ✅原本
```
Japanese ambient, solo shakuhachi in the low register only with long breathy sustained notes, very slow, spacious, lots of silence, a still overcast dusk and a faint distant wind over a moss garden, warm dark tones, no high frequencies, gentle and dim, contemplative
```
**④ Suno — Exclude** ✅原本
```
vocals, drums, percussion, rhythm, melody hooks, buildup, bright synths, high frequencies, sharp transients, crickets, insects
```
**後処理**：6.5kHz程度のローパスを軽くかける（`chamaru_build.py` の `lowpass_hz: 6500` で対応済み）

**⑤ Gemini — 動画用背景** ✅原本 ⚠️紅葉なし（**⚠️初回生成は34と同一シーンの誤りだったため再生成した。以下は原本プロンプト**）
```
A photorealistic view of a traditional Japanese engawa veranda at dusk under an overcast autumn sky, shot at eye level, front view. A worn dark wooden veranda floor fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft dim grey light comes from the open side on the left, low and weak, the garden settling into shadow. Beyond the veranda, a quiet moss garden with evergreen bamboo, weathered stone and a stone lantern is visible, softly blurred, with no autumn colour — only deep greens and greys. In the blurred background: wooden pillars and a paper screen, out of focus. Muted grey-green and dark wood, very low saturation, dim and restful. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景** ✅原本 ⚠️紅葉なし
```
A photorealistic view of a traditional Japanese engawa veranda at dusk under an overcast autumn sky, shot at eye level, front view, 16:9. A worn dark wooden veranda floor fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft dim grey light comes from the open side on the left, low and weak. Beyond the veranda, a quiet moss garden with evergreen bamboo, weathered stone and a stone lantern is visible on the left, softly blurred, with no autumn colour — only deep greens and greys. The right third of the frame is a dark wooden pillar and a paper screen in deep shadow, simple and uncluttered. Muted grey-green and dark wood, very low saturation, dim and restful. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style.
```
> `with no autumn colour — only deep greens and greys` を消さないこと。**37と38は同じ縁側だが、色をわざと正反対にする設計**（37＝灰緑・低彩度／38＝紅葉の暖色）。再生成後の実ファイル（`37__001.png`）で紅葉なし・苔庭であることを目視確認済み。サムネも同ファイルを流用。

**⑥ サムネ**：主ラベル `目を休める` / バッジ `60 MIN`
**⑦ 茶丸座標（動画背景）**：cx=500, basey=555, th=300

**⑧ ファイル**
- 動画：`苔庭を眺めて目を休める60分.mp4`（179MB / 60:00）
- サムネ：`thumb_37_screen.png`
- 音源：`苔庭を眺めて目を休める60分.wav` ／ 合成済み背景：`bg37_with_chamaru.png`（採用元 37__001.png・再生成後）

---

## 38 ｜ 安眠（秋の夜長の縁側・90分）

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | 安眠 / 宵〜夜 |
| 尺 | 90分（90:00） |
| 舞台 | 縁側 |
| 主役楽器 | 尺八 |
| 自然音 | 秋の雨（秋の夜長） |
| 茶丸 | 正面 |
| 公開目安 | 10/30 |

**① タイトル【日本語】**
```
秋の夜長に雨を聴きながら眠る90分｜和のスリープBGM ‑ 睡眠・瞑想
```

**① タイトル【English】**
```
90 Min Japanese Ambient for Sleep | Long Autumn Night & Quiet Rain | Shakuhachi
```

**② 概要【日本語】**
```
秋の夜長の縁側に、静かな雨が降り続いています。
軒を打つ雨だれと、遠くでゆれる尺八の音だけを残した、90分の睡眠用BGMです。

盛り上がりを作らず、少しずつ静かになっていくように整えました。
音が意識に残らないことを目指しています。

布団に入ってから、灯りを落としたあとに、
小さな音量で流しておいてください。

茶丸の間 / Chamaru
和の集中・休息・安眠BGMを届けるチャンネルです。
茶丸は、この部屋にいるだるまです。

#睡眠用BGM #安眠 #和風BGM #秋の夜長 #雨の音 #尺八 #japaneseambient
```

**② 概要【English】**
```
Quiet rain falls through a long autumn night, seen from a veranda.
A 90-minute sleep ambient track with water dripping from the eaves and a distant shakuhachi.

No build-ups — it grows quieter little by little toward the end.
Designed to leave nothing behind in your attention.

For nights after a day with too much input.
Play it at a low volume after you are in bed and the lights are out.

Chamaru / 茶丸の間
Japanese ambient for focus, rest and sleep.
Chamaru is the daruma who lives in this room.

#japaneseambient #sleepmusic #rainsounds #shakuhachi #nightambient
```

**③ タグ**
```
睡眠用BGM, 安眠BGM, 和風BGM, 寝る前BGM, 秋の夜長, 尺八, 雨の音, 紅葉, japanese ambient, sleep music, rain sounds, night ambient, overwhelm, overstimulation
```

**④ Suno — Style** ✅原本
```
Japanese sleep ambient, low warm drone, solo shakuhachi occasional and distant with long breathy notes, extremely slow, almost no melody, steady quiet autumn rain on the eaves through a long night, dark and still, fading into quiet
```
**④ Suno — Exclude** ✅原本
```
vocals, drums, percussion, tempo, buildup, bright tones, high frequencies, crickets, insects
```

**⑤ Gemini — 動画用背景** ✅原本（**⚠️初回生成は34と同一シーンの誤りだったため再生成した。以下は原本プロンプト**）
```
A photorealistic view of a traditional Japanese engawa veranda at night in autumn during steady rain, shot at eye level, front view. A worn dark wooden veranda floor fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft dim warm light comes from a small paper andon lantern on the left, the veranda mostly in gentle shadow. Beyond the veranda, a dark garden with Japanese maple trees in deep red autumn colour is visible in the rain, softly blurred, with water dripping from the eaves and wet fallen leaves on the stone. In the blurred background: wooden pillars and a single red maple leaf resting on the floor to the side, out of focus. Deep red and warm lantern tones against dark wood and night, humid and still. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景** ✅原本
```
A photorealistic view of a traditional Japanese engawa veranda at night in autumn during steady rain, shot at eye level, front view, 16:9. A worn dark wooden veranda floor fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft dim warm light comes from a small paper andon lantern on the left, the veranda mostly in gentle shadow. Beyond the veranda, a dark garden with Japanese maple trees in deep red autumn colour is visible in the rain on the left, softly blurred, with wet fallen leaves on the stone. The right third of the frame is a dark wooden pillar and a paper screen in deep shadow, simple and uncluttered. Deep red and warm lantern tones against dark wood and night, high contrast between the lit left side and the shadowed right side. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style.
```
> 再生成後の実ファイル（`38__001.png`）で紅葉・夜雨の舞台が正しいことを目視確認済み。サムネも同ファイルを流用。37と対になる縁側回（37＝灰緑・低彩度／38＝紅葉の暖色）。

**⑥ サムネ**：主ラベル `安眠` / バッジ `90 MIN`
**⑦ 茶丸座標（動画背景）**：cx=450, basey=555, th=300

**⑧ ファイル**
- 動画：`秋の夜長に雨を聴きながら眠る90分.mp4`（281MB / 90:00）
- サムネ：`thumb_38_anmin.png`
- 音源：`秋の夜長に雨を聴きながら眠る90分.wav` ／ 合成済み背景：`bg38_with_chamaru.png`（採用元 38__001.png・再生成後）
