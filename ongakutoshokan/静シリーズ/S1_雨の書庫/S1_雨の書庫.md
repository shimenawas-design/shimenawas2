# 【自動生成用 引継ぎプロンプト】雨の書庫（幻想の雨・全10曲）

このプロンプトを自動生成チャットに貼り、1曲ずつ9点セットを生成してください。共通部を各曲に連結して使います。

# ■ 役割・ブランド
音楽図書館（@ongakutoshokan）の専属プロデューサー兼クリエイティブディレクター。BGMではなく「幻想世界を旅するブランド」を育てる。サムネ0.5秒で「音楽図書館だ」と分かる統一感が最優先。

# ■ シリーズ世界観：雨の書庫
音楽図書館の奥、いつも静かに雨が降り続ける“雨の書庫”。天井まで届く本棚、障子の窓、苔むした庭。雨音と本の匂いに包まれて、宵から深夜へ、一晩の雨を過ごす。（写実「窓辺の雨」棟とも接続）
- 用途：集中・作業・睡眠、雨好き層。**"rain"の巨大検索を発見の入口にする**。

# ■ 出力ルール
コピペしやすいよう必ずコードブロック。長ければPart分割。省略しない。9点セット＝①タイトル②概要欄③Suno完全版④サムネ⑤動画画像5枚⑥タグ⑦固定コメント⑧SEO改善⑨シリーズ繋がり。`{{幻想プレイリストURL}}`は実URLに置換。

# ■ タイトルルール
`雨の書庫 {曲名}｜{説明}【幻想和風LoFi】作業用BGM｜Rain・Deep Focus・Sleep`

# ■ 看板モチーフ（毎回）
六角の和風ランタン（木＋和紙、琥珀の灯り＋青い芯、和紙に細い三日月、銀金具）を、サムネの同じ位置＋本編に必ず配置。

# ■ 音の方向（全曲共通）
幻想和風LoFi × 和楽器の質感 × 温かいノスタルジー × 控えめシネマティック。
- 65〜70 BPM。琴・尺八・篠笛・琵琶・**三味線**・鈴・木魚＋LoFi Beat・Warm Bass・Warm Analog Vinyl。ボーカルなし。（※三味線＝YouTube検索実証ワード。数曲に1回、他の弦楽器の代わりにフィーチャーすると良い）
- 弦パッド/ドローン/広いリバーブは薄く（restrained cinematic）。
- **雨音をやや主役に（ただし柔らかく、メロディの前に出しすぎない）**。
- **0秒フル音量**（無音/フェードイン禁止）＝ループ継ぎ目が自然。シームレスループ前提（Booth転用可）。
- Suno冒頭：必ず `Begins immediately with`。10秒で世界観完成。`Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.`

# ■ 概要欄 共通フッター（各曲の物語イントロの下に連結）
```
──────────────────
【雨の書庫】シリーズ｜音楽図書館
いつも静かに雨が降る、幻想の書庫。宵から深夜へ、一晩の雨を過ごす作業用BGM。
① 雨のはじまり ② 書架を打つ雨 ③ 苔庭の雨 ④ 軒の雫 ⑤ 遠雷の書斎
⑥ 硝子越しの雨 ⑦ 灯りと雨音 ⑧ 真夜中の豪雨 ⑨ 雨のあとの静けさ ⑩ 雨に眠る書庫

▶ 音楽図書館の他の世界も旅する
{{幻想プレイリストURL}}
──────────────────
こんな時間に：AI Work（ChatGPT / Claude / Gemini / Cursor）・Programming・Reading・Writing・Deep Focus・Studying・Sleep
──────────────────
Fantasy Japanese LoFi with the sound of gentle rain, inspired by an endless library where it always rains.
Perfect for AI Work, ChatGPT, Claude, Gemini, Cursor, Programming, Reading, Studying, Deep Focus and Sleep.
Let the rain and the old books keep you company until deep in the night.
──────────────────
#幻想和風LoFi #作業用BGM #雨の書庫 #RainLoFi #JapaneseLoFi #StudyMusic #SleepMusic #DeepFocus #RainSounds #AIWork
```

# ■ タグ共通（英7:日3。曲ごとに雨の強弱語を1〜2差し替え）
```
rain lofi, japanese lofi, rain sounds, study music, sleep music, deep focus, reading music, ai work music, lofi hip hop, ambient rain, relaxing rain, fantasy lofi, japanese traditional music, 幻想和風lofi, 作業用bgm, 雨の書庫, 雨の音, ノスタルジック bgm 和風, クラシック和風アレンジ, 三味線
```

# ■ 画像 共通サフィックス（各画像の場面行に連結）
```
Japanese fantasy anime background art, no people, no text, endless wooden library with ceiling-high bookshelves, shoji windows with rain, moss garden, wet stone, blue-grey and amber palette, cinematic depth of field, volumetric light, atmospheric haze, film still, ultra detailed, 16:9
```
# ■ 共通ネガティブ
```
people, person, human, text, watermark, logo, sunny, bright daylight, steampunk, neon, oversaturated, cluttered
```
※サムネ画像（各曲1番）だけ末尾に `clear empty negative space on the left third for title text` を足す。
※**看板ランタンは生成に含めない。** 生成後に**固定ランタンPNGを後付けオーバーレイ**で毎回同じ位置に合成する（絵のブレ防止）。プロンプト内に出る "lantern/灯り" は情景の灯りであり、ブランドの固定ランタンではない。

# ■ SEO改善 共通
世界観を先頭・SEO用途語（Rain/Sleep/Focus）を後ろ。サムネ文字は左3分の1＋明朝＋ランタン。0秒フル音量で維持率↑。雨は巨大検索なのでタイトル/タグに rain / rain sounds を必ず含める。公開2週間後に検索キーワードを反映。

# ■ シリーズ繋がり 共通
終了画面に次曲＋プレイリスト。カードでプレイリストへ。概要欄で「音楽図書館の奥の書庫」と明示し既存シリーズと同じ世界だと示す。全10曲でサムネ様式（雨の書庫＋ランタン＋青灰×琥珀＋左に明朝）を固定。10曲後：3h/8h版・雨音ライブ・季節版へ拡張。

# ■ 固定コメント共通テンプレ（{HOOK}差し替え）
```
🌧 {HOOK}
ここは音楽図書館の奥、いつも静かに雨が降る書庫です。
雨の音は、作業のお供に。どの一曲がいちばん落ち着きましたか？
🎧 雨の書庫シリーズはこちら {{幻想プレイリストURL}}
Fantasy Japanese LoFi with gentle rain. Which track kept you calm? Let me know in the comments.
```

═══════════════════════════════
# 各曲 差分（①〜⑩）
═══════════════════════════════

## ① 雨のはじまり
【タイトル】
```
雨の書庫 雨のはじまり｜宵に降りだす、幻想の雨【幻想和風LoFi】作業用BGM｜Rain・Deep Focus・Sleep
```
【物語イントロ】
```
宵の口。書庫の高い窓に、ひとつ、またひとつと雨粒が落ちはじめる。
古い紙の匂いに、雨のにおいが混ざっていく。
さあ、今夜も静かに始めよう。
```
【Suno完全版】
```
Begins immediately with a warm koto melody over the soft patter of beginning rain and a gentle lofi beat, calm and immersive from the very first second.
Style: cinematic Japanese lofi, an endless library where evening rain begins, warm and nostalgic, restrained.
Instruments: koto, shinobue flute, shakuhachi, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, warm bass, warm analog vinyl crackle.
Cinematic layer: warm cinematic strings, deep atmospheric pad, spacious wooden-hall reverb, gentle emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: soft gentle rain on shoji windows (slightly forward but never over the melody), a page turning, distant thunder far away, quiet library room-tone.
Structure: 0-2s rain + page turn + suzu bell + koto; 2-5s main melody enters; 4-5s lofi beat and warm bass join; full world within 10 seconds.
Mood: cozy, nostalgic, the calm start of a rainy night.
68 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, heavy storm, aggressive drums, EDM, bright cheerful tones.
```
【画像5枚】
```
1（サムネ兼用）High shoji windows of an endless wooden library at dusk as the first raindrops fall, warm lantern glow inside, indigo evening beyond,
2（別角度）Aisle between ceiling-high bookshelves, soft rain visible through tall windows, warm lantern light,
3（窓辺の席）A reading desk by a rain-flecked window, an open book and the lantern, blurred wet garden beyond,
4（書架/回廊）A wooden corridor along the bookshelves, rain sliding down the shoji, warm lantern reflections on the floor,
5（全景/庭）Wide view of the library's moss garden through a great window as evening rain begins, stone lantern outside, warm windows glowing,
```
【HOOK】
```
宵の雨が、そっと降りはじめる。
```

## ② 書架を打つ雨
【タイトル】
```
雨の書庫 書架を打つ雨｜本棚に響く、静かな雨【幻想和風LoFi】作業用BGM｜Rain・Deep Focus・Sleep
```
【物語イントロ】
```
雨脚が少し強くなる。高い窓を打つ音が、天井まで届く本棚に静かに反響する。
その一定のリズムが、不思議と集中を深めてくれる。
```
【Suno完全版】
```
Begins immediately with a steady koto figure over rain drumming softly on tall windows and a warm lofi beat, focused and immersive from the very first second.
Style: cinematic Japanese lofi, rain echoing through a tall library, steady and focused, warm.
Instruments: koto, shinobue flute, shakuhachi, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, warm bass, warm analog vinyl crackle.
Cinematic layer: warm cinematic strings, deep atmospheric pad, spacious reverb, steady emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: steady rain on tall glass, faint echo through a large wooden hall, soft page turns, warm room-tone.
Structure: 0-2s rain + page turn + suzu bell + koto; 2-5s main melody enters; 4-5s lofi beat and warm bass join; full world within 10 seconds.
Mood: focused, steady, deep concentration, warm rainy calm.
68 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, heavy storm, aggressive drums, EDM, bright cheerful tones.
```
【画像5枚】
```
1（サムネ兼用）Ceiling-high bookshelves lit by warm lanterns as steady rain streams down the tall windows behind them, cozy focused mood,
2（別角度）Looking up a towering wall of books, rain-lit windows high above, lantern glow,
3（窓辺の席）A desk against a rain-drummed window, focused pool of lantern light on an open book,
4（書架/回廊）A long shelf-lined corridor, rhythmic rain on the glass, warm reflections,
5（全景/庭）The great hall of the rainy library seen wide, bookshelves rising into soft shadow, rain beyond every window,
```
【HOOK】
```
本棚に響く雨のリズムが、集中を深める。
```

## ③ 苔庭の雨
【タイトル】
```
雨の書庫 苔庭の雨｜緑に降りそそぐ、幻想の雨【幻想和風LoFi】作業用BGM｜Rain・Deep Focus・Reading
```
【物語イントロ】
```
窓の外、苔むした庭に雨が降りそそぐ。濡れた緑が、いっそう深く色づく。
本を閉じて、しばし、雨に濡れる庭を眺める。
```
【Suno完全版】
```
Begins immediately with a gentle koto and shakuhachi melody over rain on a moss garden and a soft lofi beat, serene and immersive from the very first second.
Style: cinematic Japanese lofi, rain falling on a green moss garden, serene and refreshing, nostalgic.
Instruments: koto, shakuhachi, shinobue flute, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, warm bass, warm analog vinyl crackle.
Cinematic layer: warm cinematic strings, deep atmospheric pad, spacious reverb, gentle emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: soft rain on leaves and moss, occasional water drips, gentle garden ambience, warm room-tone behind.
Structure: 0-2s rain + page turn + suzu bell + koto; 2-5s main melody enters; 4-5s lofi beat and warm bass join; full world within 10 seconds.
Mood: serene, green, refreshing calm, contemplative.
67 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, heavy storm, aggressive drums, EDM, bright cheerful tones.
```
【画像5枚】
```
1（サムネ兼用）A lush moss garden seen through a great library window in the rain, wet green glowing, a stone lantern outside, warm interior lantern light,
2（別角度）Low view along the wet moss and stones, rain rings in a small pool, soft green light,
3（窓辺の席）A window seat overlooking the rainy moss garden, a closed book, the warm lantern on the sill,
4（書架/回廊）A corridor opening onto the garden veranda, rain curtain beyond, warm lanterns within,
5（全景/庭）Wide view of the misty moss garden under steady rain, stone lantern, green maples, library windows glowing warm,
```
【HOOK】
```
雨に濡れた庭の緑が、深く色づいていく。
```

## ④ 軒の雫
【タイトル】
```
雨の書庫 軒の雫｜したたる雫の音に【幻想和風LoFi】作業用BGM｜Rain・Deep Focus・Sleep
```
【物語イントロ】
```
雨が少しやわらぐ。軒先から、ひとつ、またひとつと雫が落ちる。
その規則正しい音が、時間をゆっくりにしていく。
```
【Suno完全版】
```
Begins immediately with a soft koto melody over the rhythmic drip of water from the eaves and a mellow lofi beat, calm and immersive from the very first second.
Style: cinematic Japanese lofi, water dripping from the eaves after rain, slow and soothing, nostalgic.
Instruments: koto, shinobue flute, shakuhachi, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, warm bass, warm analog vinyl crackle.
Cinematic layer: warm cinematic strings, deep atmospheric pad, very spacious reverb, slow emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: rhythmic water drips from the eaves, faint remaining rain, quiet still air, warm room-tone.
Structure: 0-2s drips + page turn + suzu bell + koto; 2-5s main melody enters; 4-5s lofi beat and warm bass join; full world within 10 seconds.
Mood: slow, soothing, time softening, gentle.
66 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, heavy storm, aggressive drums, EDM, bright cheerful tones.
```
【画像5枚】
```
1（サムネ兼用）Close view of eaves of the wooden library dripping water after rain, warm lantern glow, a still wet courtyard beyond,
2（別角度）Under the veranda eaves looking out, drips falling in a line, soft lantern light,
3（窓辺の席）A window seat with water dripping just outside the glass, a warm lantern and a teacup on the sill,
4（書架/回廊）A shelf-lined veranda corridor, eaves dripping beyond the railing, warm reflections,
5（全景/庭）Wide view of the courtyard as the rain eases and eaves drip, stone lantern, calm wet stillness,
```
【HOOK】
```
軒の雫の音が、時間をゆっくりにする。
```

## ⑤ 遠雷の書斎
【タイトル】
```
雨の書庫 遠雷の書斎｜遠い雷鳴と灯りの中で【幻想和風LoFi】作業用BGM｜Rain・Deep Focus・Sleep
```
【物語イントロ】
```
遠くで、雷が低く鳴る。けれど書斎の灯りは、静かに、温かい。
遠雷は、この夜をいっそう深く、安心なものにしてくれる。
```
【Suno完全版】
```
Begins immediately with a warm koto melody over soft rain and low distant thunder and a mellow lofi beat, cozy and immersive from the very first second.
Style: cinematic Japanese lofi, a warm study with distant thunder, cozy and safe, nostalgic depth.
Instruments: koto, shinobue flute, shakuhachi, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, warm bass, warm analog vinyl crackle.
Cinematic layer: warm cinematic strings, deep atmospheric pad, spacious reverb, tender emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: soft steady rain, low distant rolling thunder (gentle, never startling), warm study room-tone, faint page turns.
Structure: 0-2s rain + distant thunder + suzu bell + koto; 2-5s main melody enters; 4-5s lofi beat and warm bass join; full world within 10 seconds.
Mood: cozy, safe, deep, comforting depth of a stormy night.
67 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, harsh loud thunder, aggressive drums, EDM, bright cheerful tones.
```
【画像5枚】
```
1（サムネ兼用）A warm wooden study within the library, soft lantern light, tall windows showing rain and a faint distant lightning glow on the horizon,
2（別角度）The study from the doorway, shelves of books, a desk and warm lantern, rainy windows beyond,
3（窓辺の席）A desk by the window, an open book in warm lantern light, faint distant lightning beyond the rain,
4（書架/回廊）A corridor with a soft flash of distant light through far windows, warm lanterns steady inside,
5（全景/庭）Wide view of the library hall under a rainy sky with faint distant lightning, warm windows glowing calm,
```
【HOOK】
```
遠雷が、この夜をいっそう安心なものにする。
```

## ⑥ 硝子越しの雨
【タイトル】
```
雨の書庫 硝子越しの雨｜窓を伝う雫を眺めて【幻想和風LoFi】作業用BGM｜Rain・Reading・Sleep
```
【物語イントロ】
```
硝子を伝う雫を、ただ、目で追う。
外の世界がにじんで、ここだけが、静かで、温かい。
```
【Suno完全版】
```
Begins immediately with a gentle koto and soft piano-like tone over rain running down glass and a mellow lofi beat, intimate and immersive from the very first second.
Style: cinematic Japanese lofi, watching rain run down the window glass, intimate and warm, nostalgic.
Instruments: koto, warm felt piano tone, shinobue flute, shakuhachi, mokugyo, suzu bells, soft taiko, warm lofi beat, warm bass, warm analog vinyl crackle.
Cinematic layer: warm cinematic strings, deep atmospheric pad, spacious reverb, gentle emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: rain running down glass, soft droplets, muffled outside world, warm intimate room-tone.
Structure: 0-2s rain-on-glass + page turn + suzu bell + koto; 2-5s main melody enters; 4-5s lofi beat and warm bass join; full world within 10 seconds.
Mood: intimate, warm, quiet, a little wistful.
66 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, heavy storm, aggressive drums, EDM, bright cheerful tones.
```
【画像5枚】
```
1（サムネ兼用）Close view of rain running down a shoji-framed window of the library, blurred warm lantern light and bookshelves reflected in the wet glass,
2（別角度）The window from the side, droplets racing down, a warm lantern beside it,
3（窓辺の席）A cozy window seat, forehead-close view of rain on the glass, an open book and lantern,
4（書架/回廊）Bookshelves reflected in a large rain-streaked window, warm intimate glow,
5（全景/庭）Wide view of the garden blurred beyond many rain-streaked windows, warm library glowing within,
```
【HOOK】
```
硝子を伝う雫を、ただ目で追う夜。
```

## ⑦ 灯りと雨音
【タイトル】
```
雨の書庫 灯りと雨音｜ランタンの灯と、やさしい雨【幻想和風LoFi】作業用BGM｜Rain・Deep Focus・Sleep
```
【物語イントロ】
```
ランタンの灯りが、雨の夜にぽつりと点る。
灯りと雨音だけの、いちばん静かな時間。
```
【Suno完全版】
```
Begins immediately with a warm koto melody over gentle rain and the soft hum of lantern light and a mellow lofi beat, warm and immersive from the very first second.
Style: cinematic Japanese lofi, lantern light and gentle rain, warm and quiet, deeply nostalgic.
Instruments: koto, shinobue flute, shakuhachi, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, warm bass, warm analog vinyl crackle.
Cinematic layer: warm cinematic strings, deep atmospheric pad, spacious reverb, gentle emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: gentle steady rain, faint warm hum, soft page turns, cozy room-tone — rain kept soft and even.
Structure: 0-2s rain + page turn + suzu bell + koto; 2-5s main melody enters; 4-5s lofi beat and warm bass join; full world within 10 seconds.
Mood: warm, quiet, the calmest hour, cozy.
66 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, heavy storm, aggressive drums, EDM, bright cheerful tones.
```
【画像5枚】
```
1（サムネ兼用）A warm hanging paper lantern glowing softly in the foreground of the rainy library, soft rain on windows behind, bookshelves in warm shadow,
2（別角度）A hanging lantern swaying gently, rain-lit windows beyond, warm pooled light,
3（窓辺の席）A window seat lit only by the warm lantern, gentle rain outside, an open book,
4（書架/回廊）A corridor lit by a line of warm lanterns, gentle rain on the glass, cozy depth,
5（全景/庭）Wide view of the library softly lit by lanterns as gentle rain falls over the garden beyond,
```
【HOOK】
```
灯りと雨音だけの、いちばん静かな時間。
```

## ⑧ 真夜中の豪雨
【タイトル】
```
雨の書庫 真夜中の豪雨｜降りしきる雨に包まれて【幻想和風LoFi】作業用BGM｜Rain・Deep Focus・Sleep
```
【物語イントロ】
```
真夜中、雨がひときわ強くなる。世界を、雨が包み込む。
けれど書庫の中は、どこまでも安全で、温かい。
```
【Suno完全版】
```
Begins immediately with a warm koto melody over steady heavy rain and a deep mellow lofi beat, enveloping and immersive from the very first second.
Style: cinematic Japanese lofi, wrapped in midnight downpour, deep and cocooning, warm despite the storm.
Instruments: koto, shinobue flute, shakuhachi, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, deep warm bass, warm analog vinyl crackle.
Cinematic layer: warm cinematic strings, deep atmospheric pad, spacious reverb, steady emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: steady enveloping rain (fuller but soft, a wall of gentle rain, never harsh), deep warm room-tone, faint far thunder.
Structure: 0-2s rain + page turn + suzu bell + koto; 2-5s main melody enters; 4-5s lofi beat and deep warm bass join; full world within 10 seconds.
Mood: enveloping, safe, deep, cocooned against the downpour.
67 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, harsh loud thunder, aggressive drums, EDM, bright cheerful tones.
```
【画像5枚】
```
1（サムネ兼用）Heavy midnight rain streaming down the tall library windows, warm lanterns glowing safely inside, deep blue night beyond,
2（別角度）Aisle of bookshelves as heavy rain sheets down every window, warm safe glow within,
3（窓辺の席）A window seat cocooned in warm lantern light while heavy rain pours outside the glass,
4（書架/回廊）A corridor with heavy rain roaring softly beyond the windows, steady warm lanterns,
5（全景/庭）Wide view of the garden swallowed by heavy rain, the library windows glowing warm and safe,
```
【HOOK】
```
世界を雨が包む。でも、ここは安全で温かい。
```

## ⑨ 雨のあとの静けさ
【タイトル】
```
雨の書庫 雨のあとの静けさ｜雨あがりの、深い静寂【幻想和風LoFi】作業用BGM｜Rain・Deep Focus・Sleep
```
【物語イントロ】
```
やがて雨がやむ。あとに残るのは、深い、深い静けさ。
遠くで、まだ雫の音だけがしている。
```
【Suno完全版】
```
Begins immediately with a soft koto melody over deep post-rain stillness and faint dripping and a very mellow lofi beat, hushed and immersive from the very first second.
Style: cinematic Japanese lofi, the deep stillness after rain, hushed and peaceful, nostalgic.
Instruments: koto, shinobue flute, shakuhachi, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, warm bass, warm analog vinyl crackle.
Cinematic layer: warm cinematic strings, deep atmospheric pad, very spacious reverb, slow emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: deep stillness, occasional far water drips, faint night insects, very quiet room-tone.
Structure: 0-2s soft drips + page turn + suzu bell + koto; 2-5s main melody enters; 4-5s soft lofi beat and warm bass join; full world within 10 seconds.
Mood: hushed, peaceful, deep quiet, drifting toward sleep.
65 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, heavy storm, aggressive drums, EDM, bright cheerful tones.
```
【画像5枚】
```
1（サムネ兼用）The library after rain, still wet windows reflecting warm lanterns, a hushed calm, deep blue night settling,
2（別角度）Quiet aisle of bookshelves, faint drips on the glass, deep peaceful shadow and warm light,
3（窓辺の席）A window seat in hushed calm, a closed book, the wet still garden beyond,
4（書架/回廊）A corridor in deep quiet, faint last drips, warm lanterns low,
5（全景/庭）Wide view of the still moss garden after rain, wet and glistening, one warm library window glowing,
```
【HOOK】
```
雨がやんだあとの、深い静けさに包まれて。
```

## ⑩ 雨に眠る書庫
【タイトル】
```
雨の書庫 雨に眠る書庫｜雨音とともに、眠りへ【幻想和風LoFi】作業用BGM｜Rain・Sleep・Relax
```
【物語イントロ】
```
また、静かに雨が戻ってくる。その音に包まれて、書庫はゆっくりと眠りにつく。
おやすみなさい。また、雨の夜に。
```
【Suno完全版】
```
Begins immediately with the main koto theme returning softly over gentle returning rain and a very slow mellow lofi beat, tender and immersive from the very first second.
Style: cinematic Japanese lofi, the archive falling asleep in the rain, tender lullaby of a close, deeply restful.
Instruments: koto, shinobue flute, shakuhachi, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, deep warm bass, warm analog vinyl crackle.
Cinematic layer: warm cinematic strings, a soft resolving swell that recalls the first track, deep warm pad, spacious reverb, conclusive emotional arc, felt not foreground, no dramatic peaks, no loud transients.
Sound design: gentle returning rain, a soft page closing, very quiet room-tone, drifting to sleep.
Structure: 0-2s rain + page closing + suzu bell + koto theme; 2-5s main melody returns; 4-5s slow lofi beat and warm bass join; full world within 10 seconds.
Mood: tender, restful, a lullaby, ready for sleep.
65 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, heavy storm, aggressive drums, EDM, bright cheerful tones.
```
【画像5枚】
```
1（サムネ兼用）The rainy library at deepest night, lanterns dimmed low and warm, gentle rain on the windows, a peaceful sleeping hush,
2（別角度）Aisle of bookshelves fading into warm darkness, gentle rain, a single low lantern,
3（窓辺の席）A window seat at rest, a closed book, dim warm lantern, gentle rain beyond,
4（書架/回廊）A corridor sinking into soft sleep-dark, gentle rain, one dim lantern glow,
5（全景/庭）Wide view of the library and garden at deepest night in gentle rain, one warm window glowing softly,
```
【HOOK】
```
雨音とともに、書庫はゆっくり眠りにつく。おやすみなさい。
```

═══════════════════════════════
# 自動生成チャットへの指示
①共通ルールを踏まえ各曲9点セットを生成。②概要欄＝物語イントロ＋共通フッター。③タグ＝共通＋雨の強弱語1〜2。④サムネ＝各曲画像1＋共通サフィックス＋余白指定＋ネガティブ。⑤動画画像＝各行＋共通サフィックス＋ネガティブ。⑥固定コメント＝共通テンプレ＋各曲HOOK。⑦SEO・⑧シリーズ繋がりは共通、次動画は次番号（⑩は①へ）。必ずコードブロック、省略しない、「続けて」で次曲。
