# 【自動生成用 引継ぎプロンプト】神々の温泉宿（全10曲）

このプロンプトを自動生成チャットに貼り、1曲ずつ9点セットを生成してください。共通部を各曲に連結して使います。

# ■ 役割・ブランド
音楽図書館（@ongakutoshokan）の専属プロデューサー兼クリエイティブディレクター。BGMではなく「幻想世界を旅するブランド」を育てる。サムネ0.5秒で「音楽図書館だ」と分かる統一感が最優先。

# ■ シリーズ世界観：神々の温泉宿
音楽図書館の一冊「湯宿の記」を開くと辿り着く、妖と神々が夜だけ訪れる湯けむりの隠れ宿。到着から夜明けまで、一晩の湯宿でひたすら癒される。
- 用途：睡眠・癒し・入眠前・リラックス（巨大な睡眠市場）。**滞在時間（視聴維持）を稼ぐ設計**。

# ■ 出力ルール
必ずコードブロック。長ければPart分割。省略しない。9点セット＝①タイトル②概要欄③Suno完全版④サムネ⑤動画画像5枚⑥タグ⑦固定コメント⑧SEO改善⑨シリーズ繋がり。`{{幻想プレイリストURL}}`は実URLに置換。

# ■ タイトルルール
`神々の温泉宿 {曲名}｜{説明}【幻想和風LoFi】作業用BGM｜Sleep・Relax・Healing`

# ■ 看板モチーフ（毎回）
六角の和風ランタン（木＋和紙、琥珀の灯り＋青い芯、和紙に細い三日月、銀金具）を、サムネの同じ位置＋本編に必ず配置。

# ■ 音の方向（全曲共通）
幻想和風LoFi × 和楽器の質感 × 温かいノスタルジー × 控えめシネマティック。**睡眠・癒し特化で"何時間でも流せる没入"を最優先。**
- 60〜65 BPM。琴・尺八・篠笛・琵琶・鈴・木魚＋LoFi Beat・とても温かいWarm Bass・Warm Analog Vinyl。ボーカルなし。
- 弦パッド/ドローン/広いリバーブは極薄（restrained cinematic）。メロディも控えめ・反復に耐える。
- **湯の音・湯気・遠い水音・虫の音**を薄く。
- **0秒フル音量**（無音/フェードイン禁止・ただしやわらかく）＝ループ継ぎ目が自然。シームレスループ前提（Booth睡眠/リラックス素材に転用可）。
- Suno冒頭：必ず `Begins immediately with`。10秒で世界観完成。`Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.`

# ■ 概要欄 共通フッター（各曲の物語イントロの下に連結）
```
──────────────────
【神々の温泉宿】シリーズ｜音楽図書館
妖と神々が夜だけ訪れる、湯けむりの隠れ宿。到着から夜明けまで、一晩の癒しのBGM。
① 湯宿の灯り ② 湯けむりの露天 ③ 縁側の夜風 ④ 客間の安らぎ ⑤ 中庭の月
⑥ 遠い湯の音 ⑦ 火照りと休息 ⑧ 真夜中の内湯 ⑨ まどろみの床 ⑩ 夜明けの湯宿

▶ 音楽図書館の他の世界も旅する
{{幻想プレイリストURL}}
──────────────────
こんな時間に：Sleep・Relax・Healing・Reading・Deep Rest・Spa・Meditation（＋作業の休憩に）
──────────────────
Fantasy Japanese LoFi from a hidden hot-spring inn where gods and spirits rest at night.
Perfect for Sleep, Relaxation, Healing, Reading, Meditation and Deep Rest.
Let the warm water and lantern light melt the day away until dawn.
──────────────────
#幻想和風LoFi #睡眠用BGM #神々の温泉宿 #SleepMusic #JapaneseLoFi #Relaxing #Healing #Onsen #DeepSleep #ASMR
```

# ■ タグ共通（英7:日3。曲ごとに湯/宿の場面語を1〜2差し替え）
```
sleep music, japanese lofi, relaxing music, healing music, onsen, deep sleep, meditation music, spa music, ambient sleep, reading music, lofi hip hop, fantasy lofi, 幻想和風lofi, 睡眠用bgm, 神々の温泉宿, 癒しbgm
```

# ■ 画像 共通サフィックス（各画像の場面行に連結）
```
Japanese fantasy anime background art, no people, no text, a wooden fantasy hot-spring inn at night, rising steam, moonlit open-air bath, tatami rooms, veranda, warm amber and deep blue palette, cinematic depth of field, volumetric moonlight, soft steam haze, film still, ultra detailed, 16:9
```
# ■ 共通ネガティブ
```
people, person, human, text, watermark, logo, daytime, harsh light, steampunk, neon, oversaturated, cluttered, modern hotel
```
※サムネ画像（各曲1番）だけ末尾に `clear empty negative space on the left third for title text` を足す。
※**看板ランタンは生成に含めない。** 生成後に**固定ランタンPNGを後付けオーバーレイ**で毎回同じ位置に合成する（絵のブレ防止）。プロンプト内に出る "lantern/灯り" は情景の灯りであり、ブランドの固定ランタンではない。

# ■ SEO改善 共通
世界観を先頭・SEO用途語（Sleep/Relax/Healing）を後ろ。サムネ文字は左3分の1＋明朝＋ランタン。0秒フル音量（やわらかく）で維持率↑。睡眠は長時間再生が付きやすい＝滞在時間の武器。タイトル/タグに sleep / relax / onsen を必ず含める。公開2週間後に検索キーワード反映。

# ■ シリーズ繋がり 共通
終了画面に次曲＋プレイリスト。カードでプレイリストへ。概要欄で「音楽図書館の湯宿の記から入る宿」と明示し既存シリーズと同じ世界だと示す。全10曲でサムネ様式（湯宿＋湯気＋ランタン＋琥珀×青＋左に明朝）を固定。10曲後：3h/8h睡眠版・焚火/湯音ライブ・季節版へ拡張。

# ■ 固定コメント共通テンプレ（{HOOK}差し替え）
```
♨ {HOOK}
ここは音楽図書館の「湯宿の記」から辿り着く、夜だけの隠れ宿です。
今夜は、ゆっくり休んでください。おやすみなさい。
🎧 神々の温泉宿シリーズはこちら {{幻想プレイリストURL}}
A hidden hot-spring inn for gods and spirits. Rest well tonight. Good night.
```

═══════════════════════════════
# 各曲 差分（①〜⑩）
═══════════════════════════════

## ① 湯宿の灯り
【タイトル】
```
神々の温泉宿 湯宿の灯り｜夜だけ開く、癒しの隠れ宿【幻想和風LoFi】作業用BGM｜Sleep・Relax・Healing
```
【物語イントロ】
```
夜。湯けむりの向こうに、ぽつりと宿の灯りが見えてくる。
妖も神々も、ここでは肩の力を抜く。ようこそ、今夜の隠れ宿へ。
```
【Suno完全版】
```
Begins immediately with a soft warm koto melody over gentle steam ambience and a very mellow lofi beat, warm and immersive from the very first second.
Style: cinematic Japanese lofi, arriving at a hidden hot-spring inn at night, warm and welcoming, deeply relaxing.
Instruments: koto, shakuhachi, shinobue flute, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, deep warm bass, warm analog vinyl crackle.
Cinematic layer: very soft warm strings, deep warm pad, spacious reverb, gentle emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: gentle rising steam, faint distant water, soft wind, warm inn room-tone — all very soft under the melody.
Structure: 0-2s soft wind + a sliding shoji + suzu bell + koto; 2-5s main melody enters; 4-5s mellow lofi beat and deep warm bass join; full world within 10 seconds.
Mood: warm, welcoming, unwinding, the relief of arrival.
62 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, aggressive drums, EDM, bright cheerful tones, harsh sounds.
```
【画像5枚】
```
1（サムネ兼用）A wooden hot-spring inn glowing warm through night steam, lantern-lit entrance, moonlit mountains behind, inviting and cozy,
2（別角度）The inn approach lit by stone lanterns and rising steam, warm noren curtain at the entrance,
3（客間/縁側）A warm tatami guest room seen from the doorway, a low lamp, shoji open to steam beyond,
4（内湯/回廊）A lantern-lit wooden corridor leading toward the baths, steam drifting, warm glow,
5（全景/外観）Wide view of the whole hot-spring inn nestled in a moonlit valley, warm windows, steam rising into a starry sky,
```
【HOOK】
```
湯けむりの向こうに、今夜の宿の灯りが見える。
```

## ② 湯けむりの露天
【タイトル】
```
神々の温泉宿 湯けむりの露天｜月夜の露天風呂で【幻想和風LoFi】作業用BGM｜Sleep・Relax・Healing
```
【物語イントロ】
```
月を映す露天の湯。立ちのぼる湯けむりに、一日の疲れが溶けていく。
ただ、湯の音に身をゆだねる。
```
【Suno完全版】
```
Begins immediately with a gentle koto and shakuhachi melody over soft water and steam and a very mellow lofi beat, soothing and immersive from the very first second.
Style: cinematic Japanese lofi, a moonlit open-air hot spring, soothing and warm, deeply relaxing.
Instruments: koto, shakuhachi, shinobue flute, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, deep warm bass, warm analog vinyl crackle.
Cinematic layer: very soft warm strings, deep warm pad, spacious reverb, gentle emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: soft lapping hot-spring water, gentle steam, occasional water drips on stone, distant night insects — all very soft.
Structure: 0-2s soft water + suzu bell + koto; 2-5s main melody enters; 4-5s mellow lofi beat and deep warm bass join; full world within 10 seconds.
Mood: soothing, melting tension, warm moonlit calm.
61 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, aggressive drums, EDM, bright cheerful tones, harsh sounds.
```
【画像5枚】
```
1（サムネ兼用）A moonlit open-air hot spring wrapped in steam, stone rim and lanterns, reflection of the moon on the water, warm and serene,
2（別角度）The open-air bath from the side, steam curling up toward a starry sky, warm lantern glow on wet stone,
3（客間/縁側）A veranda beside the bath, a folded towel and a warm lantern, steam drifting past,
4（内湯/回廊）Stone steps into the steaming bath, lanterns lighting the way, moonlight and steam,
5（全景/外観）Wide view of the open-air bath in a moonlit mountain garden, steam rising, warm lantern-lit inn behind,
```
【HOOK】
```
月を映す湯に、一日の疲れが溶けていく。
```

## ③ 縁側の夜風
【タイトル】
```
神々の温泉宿 縁側の夜風｜湯上がりの、涼しい夜風【幻想和風LoFi】作業用BGM｜Sleep・Relax・Healing
```
【物語イントロ】
```
湯上がり。縁側に腰かけて、火照った肌に夜風を受ける。
虫の声と、遠い湯の音。ただ、心地よい。
```
【Suno完全版】
```
Begins immediately with a warm koto melody over a gentle night breeze and soft insects and a mellow lofi beat, breezy and immersive from the very first second.
Style: cinematic Japanese lofi, a cool night breeze on the veranda after a bath, breezy and content, relaxing.
Instruments: koto, shinobue flute, shakuhachi, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, warm bass, warm analog vinyl crackle.
Cinematic layer: very soft warm strings, deep warm pad, spacious reverb, gentle emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: gentle night breeze, soft insects, a faint wind chime, distant water, warm veranda room-tone.
Structure: 0-2s breeze + wind chime + suzu bell + koto; 2-5s main melody enters; 4-5s mellow lofi beat and warm bass join; full world within 10 seconds.
Mood: content, breezy, the pleasant cool after warmth.
62 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, aggressive drums, EDM, bright cheerful tones, harsh sounds.
```
【画像5枚】
```
1（サムネ兼用）A wooden veranda of the inn at night, a warm lantern and a small wind chime, moonlit garden and drifting steam beyond,
2（別角度）The veranda along the inn, tatami and shoji, night garden and stone lantern beyond,
3（客間/縁側）Close view of the veranda edge, a cushion and warm lantern, cool night garden beyond,
4（内湯/回廊）A corridor opening onto the veranda, warm lanterns, night breeze implied by a swaying chime,
5（全景/外観）Wide view of the inn's veranda wrapping a moonlit garden, warm lanterns, faint steam from the baths,
```
【HOOK】
```
火照った肌に、涼しい夜風が心地よい。
```

## ④ 客間の安らぎ
【タイトル】
```
神々の温泉宿 客間の安らぎ｜灯りのともる客間で【幻想和風LoFi】作業用BGM｜Sleep・Relax・Healing
```
【物語イントロ】
```
客間に戻る。畳の匂い、やわらかな灯り、敷かれた床。
もう、何も考えなくていい。ただ、安らぐ。
```
【Suno完全版】
```
Begins immediately with a soft warm koto melody over a quiet tatami room-tone and a very mellow lofi beat, safe and immersive from the very first second.
Style: cinematic Japanese lofi, the calm of a lantern-lit guest room, safe and cozy, deeply restful.
Instruments: koto, shinobue flute, shakuhachi, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, deep warm bass, warm analog vinyl crackle.
Cinematic layer: very soft warm strings, deep warm pad, spacious reverb, gentle emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: very quiet tatami room-tone, faint distant water, a soft sliding shoji, warm stillness.
Structure: 0-2s soft shoji + suzu bell + koto; 2-5s main melody enters; 4-5s mellow lofi beat and deep warm bass join; full world within 10 seconds.
Mood: safe, cozy, nothing to worry about, deep rest.
61 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, aggressive drums, EDM, bright cheerful tones, harsh sounds.
```
【画像5枚】
```
1（サムネ兼用）A warm tatami guest room lit by a single soft lantern, folded bedding, shoji glowing with moonlight, deeply cozy,
2（別角度）The guest room from the corner, a low table and lamp, shoji to a moonlit garden,
3（客間/縁側）Close view of the bedding and a warm lantern on the tatami, gentle shadows,
4（内湯/回廊）A quiet corridor to the rooms, warm lanterns, tatami and wood,
5（全景/外観）Wide view of the inn's rooms glowing warm behind shoji, moonlit garden, faint steam,
```
【HOOK】
```
やわらかな灯りの客間で、ただ安らぐ。
```

## ⑤ 中庭の月
【タイトル】
```
神々の温泉宿 中庭の月｜静かな中庭を照らす月【幻想和風LoFi】作業用BGM｜Sleep・Relax・Healing
```
【物語イントロ】
```
中庭に、月が静かに満ちている。
鹿威しの音がひとつ。あとは、ただ静けさ。
```
【Suno完全版】
```
Begins immediately with a serene koto and shakuhachi melody over a quiet moonlit courtyard and a very mellow lofi beat, tranquil and immersive from the very first second.
Style: cinematic Japanese lofi, a still moonlit courtyard garden, tranquil and clear, relaxing.
Instruments: koto, shakuhachi, shinobue flute, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, warm bass, warm analog vinyl crackle.
Cinematic layer: very soft warm strings, deep warm pad, very spacious reverb, gentle emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: deep courtyard stillness, an occasional shishi-odoshi knock, faint water, soft insects.
Structure: 0-2s stillness + shishi-odoshi + suzu bell + koto; 2-5s main melody enters; 4-5s mellow lofi beat and warm bass join; full world within 10 seconds.
Mood: tranquil, clear, moonlit serenity.
62 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, aggressive drums, EDM, bright cheerful tones, harsh sounds.
```
【画像5枚】
```
1（サムネ兼用）A still moonlit courtyard garden of the inn, a stone lantern and a small pond reflecting the full moon, drifting steam, serene,
2（別角度）The courtyard from the veranda, moss and stones, a shishi-odoshi by the water, warm lanterns around,
3（客間/縁側）A room's shoji open onto the moonlit courtyard, a warm lantern on the sill,
4（内湯/回廊）A corridor around the courtyard, warm lanterns, moonlight on the wooden floor,
5（全景/外観）Wide view of the inn built around a moonlit courtyard garden, warm glowing rooms, steam and stars,
```
【HOOK】
```
中庭に月が満ちる。鹿威しの音がひとつ、あとは静けさ。
```

## ⑥ 遠い湯の音
【タイトル】
```
神々の温泉宿 遠い湯の音｜どこかで響く、やさしい湯の音【幻想和風LoFi】作業用BGM｜Sleep・Relax・Healing
```
【物語イントロ】
```
床に横たわると、どこか遠くで湯の湧く音がする。
その音は、まるで子守唄のよう。
```
【Suno完全版】
```
Begins immediately with a soft koto melody over faint distant hot-spring water and a very slow mellow lofi beat, drowsy and immersive from the very first second.
Style: cinematic Japanese lofi, the faint distant sound of the baths, drowsy and warm, lullaby-like.
Instruments: koto, shinobue flute, shakuhachi, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, deep warm bass, warm analog vinyl crackle.
Cinematic layer: very soft warm strings, deep warm pad, spacious reverb, gentle emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: faint distant flowing hot-spring water, very soft steam, quiet room-tone, drifting toward sleep.
Structure: 0-2s faint water + suzu bell + koto; 2-5s main melody enters; 4-5s slow lofi beat and deep warm bass join; full world within 10 seconds.
Mood: drowsy, warm, lullaby, sinking toward sleep.
60 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, aggressive drums, EDM, bright cheerful tones, harsh sounds.
```
【画像5枚】
```
1（サムネ兼用）A dim warm guest room at deep night, bedding laid out, faint steam glow from distant baths beyond the shoji, drowsy calm,
2（別角度）The quiet room in low lantern light, shoji faintly glowing with distant bath steam,
3（客間/縁側）Close view of the bedding and a very low lantern, soft warm shadows,
4（内湯/回廊）A dim corridor toward the distant baths, faint steam and low lantern glow,
5（全景/外観）Wide view of the sleeping inn at deep night, one faint glow from the baths, steam and moon,
```
【HOOK】
```
遠くで響く湯の音は、まるで子守唄。
```

## ⑦ 火照りと休息
【タイトル】
```
神々の温泉宿 火照りと休息｜ぬくもりに包まれて【幻想和風LoFi】作業用BGM｜Sleep・Relax・Healing
```
【物語イントロ】
```
湯のぬくもりが、まだ体に残っている。
そのあたたかさに包まれたまま、ゆっくりと休息へ。
```
【Suno完全版】
```
Begins immediately with a warm koto melody over deep cozy warmth and a very mellow lofi beat, warm and immersive from the very first second.
Style: cinematic Japanese lofi, wrapped in lingering warmth and rest, deeply cozy, restful.
Instruments: koto, shinobue flute, shakuhachi, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, deep warm bass, warm analog vinyl crackle.
Cinematic layer: very soft warm strings, deep warm pad, spacious reverb, gentle emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: very warm quiet room-tone, faint distant water, soft steam, a sense of lingering warmth.
Structure: 0-2s soft warmth + suzu bell + koto; 2-5s main melody enters; 4-5s mellow lofi beat and deep warm bass join; full world within 10 seconds.
Mood: cozy, warm, restful, wrapped in warmth.
61 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, aggressive drums, EDM, bright cheerful tones, harsh sounds.
```
【画像5枚】
```
1（サムネ兼用）A deeply cozy tatami room bathed in warm amber lantern light, bedding and a soft glow, faint steam beyond the shoji, restful,
2（別角度）The warm room from above, bedding and a low lantern, gentle amber tones,
3（客間/縁側）Close view of a warm lantern beside the bedding, deep cozy shadows,
4（内湯/回廊）A warm corridor, amber lanterns, faint steam from the baths,
5（全景/外観）Wide view of the inn glowing deeply warm at night, amber windows, steam and moon,
```
【HOOK】
```
湯のぬくもりに包まれたまま、ゆっくり休む。
```

## ⑧ 真夜中の内湯
【タイトル】
```
神々の温泉宿 真夜中の内湯｜誰もいない、真夜中の湯【幻想和風LoFi】作業用BGM｜Sleep・Relax・Healing
```
【物語イントロ】
```
真夜中、そっと内湯へ。木の湯船に、湯がやさしく満ちている。
誰もいない、静かな湯を、独り占め。
```
【Suno完全版】
```
Begins immediately with a soft koto and shakuhachi melody over gentle indoor bath water and a very mellow lofi beat, hushed and immersive from the very first second.
Style: cinematic Japanese lofi, a quiet indoor wooden bath at midnight, hushed and warm, deeply relaxing.
Instruments: koto, shakuhachi, shinobue flute, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, deep warm bass, warm analog vinyl crackle.
Cinematic layer: very soft warm strings, deep warm pad, spacious reverb with soft echo, gentle emotional arc, felt not foreground, soft swell, no dramatic peaks, no loud transients.
Sound design: gentle indoor bath water with a soft wooden echo, faint steam drips, hushed midnight room-tone.
Structure: 0-2s soft water echo + suzu bell + koto; 2-5s main melody enters; 4-5s mellow lofi beat and deep warm bass join; full world within 10 seconds.
Mood: hushed, private, warm midnight calm.
60 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, aggressive drums, EDM, bright cheerful tones, harsh sounds.
```
【画像5枚】
```
1（サムネ兼用）A quiet indoor wooden hot-spring bath at midnight, warm lanterns, steam rising over still water, hushed and private,
2（別角度）The wooden bath hall from the doorway, lanterns reflected in the still water, steam,
3（客間/縁側）A changing nook beside the bath, a folded towel and warm lantern, steam drifting,
4（内湯/回廊）Steps down into the indoor bath, warm lantern glow on wet wood, soft steam,
5（全景/外観）Wide view of the wooden indoor bath house glowing warm at midnight, steam against dark timber,
```
【HOOK】
```
誰もいない真夜中の湯を、独り占め。
```

## ⑨ まどろみの床
【タイトル】
```
神々の温泉宿 まどろみの床｜眠りへ落ちていく【幻想和風LoFi】作業用BGM｜Sleep・Relax・Healing
```
【物語イントロ】
```
床につく。まぶたが重くなる。
湯のぬくもりと、遠い水の音に包まれて、意識がやさしくほどけていく。
```
【Suno完全版】
```
Begins immediately with a very soft koto melody over deep warm stillness and a slow gentle lofi beat, drowsy and immersive from the very first second.
Style: cinematic Japanese lofi, drifting into sleep in warm bedding, a tender lullaby, deeply restful.
Instruments: koto, shinobue flute, shakuhachi, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, deep warm bass, warm analog vinyl crackle.
Cinematic layer: very soft warm strings, deep warm pad, spacious reverb, gentle emotional arc, felt not foreground, no dramatic peaks, no loud transients.
Sound design: deep warm stillness, very faint distant water, the softest steam, consciousness gently unwinding.
Structure: 0-2s deep hush + suzu bell + koto; 2-5s main melody enters; 4-5s slow lofi beat and deep warm bass join; full world within 10 seconds.
Mood: drowsy, tender, unwinding into sleep.
60 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, aggressive drums, EDM, bright cheerful tones, harsh sounds.
```
【画像5枚】
```
1（サムネ兼用）Warm bedding in a dim tatami room at deepest night, a single very low lantern, faint moonlit shoji, drifting toward sleep,
2（別角度）The dim room fading into warm dark, bedding and the low lantern glow,
3（客間/縁側）Very close view of the bedding and the dim warm lantern, soft heavy calm,
4（内湯/回廊）A corridor sinking into sleep-dark, one dim lantern, faint steam,
5（全景/外観）Wide view of the inn almost dark, a single dim warm window, moon and quiet steam,
```
【HOOK】
```
湯のぬくもりに包まれて、意識がやさしくほどけていく。
```

## ⑩ 夜明けの湯宿
【タイトル】
```
神々の温泉宿 夜明けの湯宿｜朝の光と、別れの湯けむり【幻想和風LoFi】作業用BGM｜Sleep・Relax・Healing
```
【物語イントロ】
```
夜が明ける。障子が白み、湯けむりが朝の光にきらめく。
一晩の癒しも、これで終わり。また、夜になったら。
```
【Suno完全版】
```
Begins immediately with the main koto theme returning softly over gentle morning steam and a mellow lofi beat, tender and immersive from the very first second.
Style: cinematic Japanese lofi, dawn at the hot-spring inn, a gentle farewell and warm afterglow, restful and hopeful.
Instruments: koto, shinobue flute, shakuhachi, biwa, mokugyo, suzu bells, soft taiko, warm lofi beat, deep warm bass, warm analog vinyl crackle.
Cinematic layer: warm cinematic strings with a soft sunrise swell that recalls the first track, deep warm pad, spacious reverb, conclusive emotional arc, felt not foreground, no dramatic peaks, no loud transients.
Sound design: gentle morning steam glittering, faint first birdsong far away, soft water, a sliding shoji, warm dawn room-tone.
Structure: 0-2s soft morning + sliding shoji + suzu bell + koto theme; 2-5s main melody returns; 4-5s mellow lofi beat and deep warm bass join; full world within 10 seconds.
Mood: tender, warm afterglow, a gentle farewell at dawn.
62 BPM, instrumental, no vocals.
Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.
Exclude: vocals, aggressive drums, EDM, bright cheerful tones, harsh sounds.
```
【画像5枚】
```
1（サムネ兼用）The hot-spring inn at dawn, shoji glowing soft amber, steam glittering in the first light, warm and peaceful farewell,
2（別角度）The open-air bath at dawn, steam catching pink-gold light, lanterns dimming,
3（客間/縁側）A guest room at dawn, folded bedding, warm sunrise through the shoji, a cooled lantern,
4（内湯/回廊）A corridor filled with soft golden dawn light and gentle steam, lanterns nearly out,
5（全景/外観）Wide view of the whole inn in a dawn valley, steam rising into a pink-amber sky, warm and calm,
```
【HOOK】
```
一晩の癒しも、これで終わり。また、夜になったら。
```

═══════════════════════════════
# 自動生成チャットへの指示
①共通ルールを踏まえ各曲9点セットを生成。②概要欄＝物語イントロ＋共通フッター。③タグ＝共通＋湯/宿の場面語1〜2。④サムネ＝各曲画像1＋共通サフィックス＋余白指定＋ネガティブ。⑤動画画像＝各行＋共通サフィックス＋ネガティブ。⑥固定コメント＝共通テンプレ＋各曲HOOK。⑦SEO・⑧シリーズ繋がりは共通、次動画は次番号（⑩は①へ）。必ずコードブロック、省略しない、「続けて」で次曲。
