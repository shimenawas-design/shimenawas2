# 【自動生成用 引継ぎプロンプト】剣戟の写本（全10曲）

このプロンプトを自動生成チャットに貼り、1曲ずつ9点セットを生成してください。共通部を各曲に連結して使います。
**Sunoは文字数制限に収まるコンパクト版（各200〜250字）を最初から使用しています。**

# ■ 役割・ブランド
音楽図書館（@ongakutoshokan）の専属プロデューサー兼クリエイティブディレクター。BGMではなく「幻想世界を旅するブランド」を育てる。サムネ0.5秒で「音楽図書館だ」と分かる統一感が最優先。

# ■ シリーズ世界観：剣戟の写本
図書館の最奥、普段は閉ざされている禁書区画。伝説の剣豪たちの決闘を記した写本群。一冊を開けば、その一戦が音となって蘇る。写本が閉じられれば、また静かな図書館の夜へ戻る。
**このシリーズは音楽図書館で唯一の"動・かっこいい"路線。** 他シリーズ（静・restrained）とは音の作り方が逆転する。詳細は `00_series_bible.md` 参照。

# ■ 出力ルール
必ずコードブロック。長ければPart分割。省略しない。9点セット＝①タイトル②概要欄③Suno完全版④サムネ⑤動画画像5枚⑥タグ⑦固定コメント⑧SEO改善⑨シリーズ繋がり。`{{幻想プレイリストURL}}`は実URLに置換。

# ■ タイトルルール
`剣戟の写本 {曲名}｜{説明}【幻想和風LoFi】ハイテンポBGM｜Gaming・Workout・Motivation`

# ■ 看板モチーフ（毎回）
- **共通（他シリーズと完全に同じ）**：六角の和風ランタン（木＋和紙、琥珀の灯り＋青い芯、和紙に細い三日月、銀金具）。**生成には含めず、後付けPNG合成**で毎回同位置。
- **このシリーズ固有の副モチーフ**：床に突き立てられた一振りの刀身（鞘なし、人物・手は描かない）。5枚のどこかに配置。

# ■ 人物なしルール（最重要・厳守）
戦いは環境描写のみで語る：斬られて宙を舞う花弁、飛び散る墨、破れた巻物、床に刺さった刀、斬撃の残光。**人物・手・シルエットは一切描かない。**

# ■ 音の方向（全曲共通・他シリーズと逆転）
幻想和風LoFi × 三味線を主役級に × ドラマチックなシネマティック（**このシリーズだけピークを歓迎**）。
- 100〜122 BPM（曲ごとに指定）。篠笛・琴・尺八・三味線（主役）・琵琶（鋭いストップ音）・太鼓（強打）・鈴＋LoFi Beat寄りのトラップ的リズム・深いサブベース。ボーカルなし。
- **ドラマチックなピーク・鋭いトランジェントを積極的に使う**（他シリーズの `no dramatic peaks` を反転）。ただしミックスはクリーン、デジタル歪みは避ける。
- **0秒フル音量・0秒からインパクトのある開始**（このシリーズと特に相性がいい）。
- Suno冒頭：必ず `Begins immediately with`。10秒で世界観完成。

# ■ 概要欄 共通フッター（各曲の物語イントロの下に連結）
```
──────────────────
【剣戟の写本】シリーズ｜音楽図書館
図書館の禁書区画に眠る、伝説の剣豪たちの決闘記録。一冊を開けば、一戦が音となって蘇る。
① 封印の扉 ② 抜刀 ③ 疾風の一撃 ④ 鍔迫り合い ⑤ 満月の決闘
⑥ 紅椿の一閃 ⑦ 二刀の残響 ⑧ 嵐中の一閃 ⑨ 決着 ⑩ 写本は閉じられて

▶ 音楽図書館の他の世界も旅する
{{幻想プレイリストURL}}
──────────────────
こんな時間に：Gaming・Workout・Motivation・Programming・Hype Focus・Creative Work
──────────────────
High-tempo Fantasy Japanese LoFi with shamisen and taiko, inspired by forbidden chronicles of legendary duels.
Perfect for Gaming, Workout, Motivation, Programming and Hype Focus.
Open the chronicle, and the duel begins.
──────────────────
#幻想和風LoFi #和風BGM #剣戟の写本 #かっこいいBGM #三味線BGM #JapaneseLoFi #GamingMusic #WorkoutMusic #SamuraiLofi #EpicJapanese
```

# ■ タグ共通（英7:日3。曲ごとに場面語を1〜2差し替え）
```
japanese battle music, samurai lofi, gaming music, workout music, epic japanese music, shamisen music, taiko drums, motivation music, epic fantasy lofi, japanese traditional music, かっこいい bgm 和風, 和風bgm アップテンポ, 三味線 かっこいい bgm, 和風 盛り上がる 曲, 剣戟の写本, 和風bgm 重低音
```

# ■ 画像 共通サフィックス（各画像の場面行に連結）
```
Japanese fantasy anime background art, no people, no hands, no silhouettes, a forbidden archive of duel chronicles within a great library, torn scrolls, scattered ink, a single blade standing upright in the floor, cut flower petals caught in motion, moonlight, blue and silver palette with a single accent of deep crimson, cinematic depth of field, dynamic motion blur, dramatic lighting, film still, ultra detailed, 16:9
```
# ■ 共通ネガティブ
```
people, person, human, hand, silhouette, text, watermark, logo, explicit gore, blood pooling, modern weapons, steampunk, neon, oversaturated
```
※サムネ画像（各曲1番）だけ末尾に `clear empty negative space on the left third for title text` を足す。
※看板ランタンは生成に含めない（後付け合成）。

# ■ SEO改善 共通
世界観を先頭・英語SEO用途語（Gaming/Workout/Motivation）を後ろ。「かっこいい」「アップテンポ」「三味線」はYouTube検索実証ワード＝タグとタイトル説明部に必ず反映。サムネは他シリーズ同様、左3分の1に文字＋ランタン。ドラマチックなピークが視聴維持のフックになりやすい（このジャンルは"掴み"が強いほど良い、静シリーズとは逆）。

# ■ シリーズ繋がり 共通
終了画面に次曲＋プレイリスト。①は「禁書区画へ入る」、⑩は「写本が閉じ図書館へ戻る」で他シリーズと同じ"一晩の物語"構造に接続。概要欄で「音楽図書館の禁書区画」と明示。全10曲でサムネ様式（禁書区画＋刀身＋青銀×琥珀+差し色の紅＋ランタン＋左に明朝タイトル）を固定。

# ■ 固定コメント共通テンプレ（{HOOK}差し替え）
```
⚔️ {HOOK}
この写本は、音楽図書館の禁書区画に眠っていたものです。
どの一戦がいちばん心に残りましたか？コメントで教えてください。
🎧 剣戟の写本シリーズはこちら {{幻想プレイリストURL}}
A forbidden chronicle of legendary duels. Which duel struck you the most?
```

═══════════════════════════════
# 各曲 差分（①〜⑩）
═══════════════════════════════

## ① 封印の扉
【タイトル】
```
剣戟の写本 封印の扉｜禁書区画へ、足を踏み入れる【幻想和風LoFi】ハイテンポBGM｜Gaming・Workout・Motivation
```
【物語イントロ】
```
図書館の最奥、鎖の巻かれた扉。封印を解くと、冷たい空気が流れ出す。
禁書区画――伝説の剣豪たちの記録が眠る場所。今宵、一冊を開く。
```
【Suno（コンパクト版）】
```
cinematic Japanese lofi, entering a forbidden archive, shamisen+taiko hit, biwa stabs, driving lofi-trap beat, deep sub bass, dramatic orchestral hit, dynamic and bold, 100 BPM, instrumental, no vocals, explosive full-volume start from 0:00
```
【画像5枚（場面行）】
```
1（サムネ兼用）A heavy sealed archive door within the great library, chains breaking apart, cold light spilling out, a single blade standing just inside the threshold,
2（別角度）Looking down a corridor of the forbidden archive as the door opens, scrolls lining the walls, dust catching moonlight,
3（写本机）A stone desk with an ancient chronicle opening itself, ink swirling off the page, a blade resting beside it,
4（書架）Towering shelves of duel chronicles in the archive, torn scroll ends drifting, dim cold light,
5（全景）Wide view of the forbidden archive chamber, the broken seal on the floor, moonlight through a high window,
```
【HOOK】
```
封印が解かれ、禁書区画への扉が開く。
```

## ② 抜刀
【タイトル】
```
剣戟の写本 抜刀｜刃を抜く、緊張の解放【幻想和風LoFi】ハイテンポBGM｜Gaming・Workout・Motivation
```
【物語イントロ】
```
写本のページに、鞘走る音が刻まれている。一息、間があって――抜刀。
その一瞬に、すべての緊張が解き放たれる。
```
【Suno（コンパクト版）】
```
cinematic Japanese lofi, the moment of drawing a blade, sharp shamisen stab, taiko hit, biwa accent, driving lofi-trap beat, deep sub bass, tense release, 108 BPM, instrumental, no vocals, explosive full-volume start from 0:00
```
【画像5枚（場面行）】
```
1（サムネ兼用）A single blade caught mid-draw, motion blur streak of silver light, torn page fragments frozen in the air, moonlit dojo floor,
2（別角度）Close view of a scabbard lying empty on tatami, the blade's motion trail leading away from it,
3（写本机）A chronicle page showing an illustration of a draw, ink still wet, a real blade resting beside the book,
4（書架）A dojo-like hall within the archive, wooden floor, a single blade planted upright, dust motes in a shaft of light,
5（全景）Wide view of a moonlit training hall inside the library, the blade's silver trail frozen in the air, no one present,
```
【HOOK】
```
鞘を走る音、一瞬の抜刀。
```

## ③ 疾風の一撃
【タイトル】
```
剣戟の写本 疾風の一撃｜疾い最初の斬り合い【幻想和風LoFi】ハイテンポBGM｜Gaming・Workout・Motivation
```
【物語イントロ】
```
風のように速い、最初の交錯。写本の上で、線が幾重にも重なっていく。
息をのむ間もなく、次の一撃が来る。
```
【Suno（コンパクト版）】
```
cinematic Japanese lofi, first fast clash of blades, rapid shamisen riff, driving taiko, biwa stabs, fast lofi-trap beat, deep sub bass, dramatic swells, high energy, 118 BPM, instrumental, no vocals, explosive full-volume start from 0:00
```
【画像5枚（場面行）】
```
1（サムネ兼用）Two blades' motion trails crossing in mid-air above a wooden dojo floor, sparks of silver light, petals scattering, no figures,
2（別角度）Fast motion-blur streaks crossing a moonlit courtyard, cut leaves suspended in the air,
3（写本机）A chronicle page depicting crossed blade trails, ink smeared with speed, the desk trembling,
4（書架）Scrolls falling from shelves as if from a gust, motion blur, dim archive light,
5（全景）Wide view of a courtyard duel scene frozen mid-motion, crossed silver trails, petals in flight, no people,
```
【HOOK】
```
息をのむ間もなく、次の一撃が交錯する。
```

## ④ 鍔迫り合い
【タイトル】
```
剣戟の写本 鍔迫り合い｜拮抗する力、押し合う間【幻想和風LoFi】ハイテンポBGM｜Gaming・Workout・Motivation
```
【物語イントロ】
```
刃と刃が鍔で止まる。動かない、けれど張り詰めた一瞬。
写本の筆致さえ、震えて止まっている。
```
【Suno（コンパクト版）】
```
cinematic Japanese lofi, blade lock tension, grinding shamisen drone, taiko pulse, biwa tremolo, driving lofi-trap beat, deep sub bass, tense standoff energy, 112 BPM, instrumental, no vocals, explosive full-volume start from 0:00
```
【画像5枚（場面行）】
```
1（サムネ兼用）Two blades locked together at the hilt, sparks caught frozen at the point of contact, tense moonlit courtyard, no figures,
2（別角度）Close view of the locked blade point, silver sparks, deep shadow around it,
3（写本机）The chronicle page showing a locked-blade illustration, ink trembling as if under pressure,
4（書架）The archive hall with dust frozen mid-fall, tense stillness, a locked-blade motif etched on a scroll,
5（全景）Wide view of the standoff moment, two motion trails frozen at a single point, courtyard stones cracked beneath,
```
【HOOK】
```
動かない、けれど張り詰めた一瞬。
```

## ⑤ 満月の決闘
【タイトル】
```
剣戟の写本 満月の決闘｜月下のクライマックス【幻想和風LoFi】ハイテンポBGM｜Gaming・Workout・Motivation
```
【物語イントロ】
```
満月が中天にかかる。戦いは、最も激しい局面へ。
写本のインクが、まるで生きているように奔る。
```
【Suno（コンパクト版）】
```
cinematic Japanese lofi, duel under the full moon, aggressive shamisen lead, powerful taiko hits, biwa stabs, driving lofi-trap beat, deep sub bass, orchestral peak, epic and bold, 120 BPM, instrumental, no vocals, explosive full-volume start from 0:00
```
【画像5枚（場面行）】
```
1（サムネ兼用）A full moon dominating the sky above a courtyard duel, crossed silver motion trails, petals and torn paper caught in the air, no figures,
2（別角度）Close view of the full moon reflected off a spinning blade trail, dramatic contrast,
3（写本机）The chronicle page glowing under moonlight streaming through a window, ink alive with motion,
4（書架）The archive shaking with energy, scrolls flying, moonbeam cutting through dust,
5（全景）Wide epic view of the moonlit courtyard duel at its climax, dynamic motion trails, dramatic sky,
```
【HOOK】
```
満月の下、戦いは最も激しい局面へ。
```

## ⑥ 紅椿の一閃
【タイトル】
```
剣戟の写本 紅椿の一閃｜斬られた椿が舞う【幻想和風LoFi】ハイテンポBGM｜Gaming・Workout・Motivation
```
【物語イントロ】
```
一閃。庭の紅椿が、音もなく斬られて宙に舞う。
その赤だけが、静かな戦いの余韻を語る。
```
【Suno（コンパクト版）】
```
cinematic Japanese lofi, a single decisive strike, sharp shamisen stab, taiko accent, biwa flourish, driving lofi-trap beat, deep sub bass, dramatic and elegant, 116 BPM, instrumental, no vocals, explosive full-volume start from 0:00
```
【画像5枚（場面行）】
```
1（サムネ兼用）Crimson camellia petals cut and scattering through the air above a moonlit courtyard, a single blade trail crossing the frame, elegant not gory,
2（別角度）Close view of camellia petals frozen mid-fall, a thin silver blade trail behind them,
3（写本机）The chronicle page with a painted crimson camellia and a single brushstroke line, ink still glistening,
4（書架）A camellia branch by the archive window, one bloom cut clean, petals drifting into the room,
5（全景）Wide view of a courtyard where a single strike has scattered crimson petals across the stones, serene aftermath,
```
【HOOK】
```
一閃。斬られた紅椿が、音もなく舞う。
```

## ⑦ 二刀の残響
【タイトル】
```
剣戟の写本 二刀の残響｜二刀の応酬、重なる音【幻想和風LoFi】ハイテンポBGM｜Gaming・Workout・Motivation
```
【物語イントロ】
```
一振りではない、二振りの刃が同時に奔る。
音が幾重にも重なり、写本の紙面を埋め尽くしていく。
```
【Suno（コンパクト版）】
```
cinematic Japanese lofi, dual-blade exchange, layered shamisen riffs, complex taiko pattern, biwa counter-stabs, driving lofi-trap beat, deep sub bass, intricate and intense, 118 BPM, instrumental, no vocals, explosive full-volume start from 0:00
```
【画像5枚（場面行）】
```
1（サムネ兼用）Two blades' motion trails weaving together above a dojo floor, layered silver arcs, torn paper swirling, no figures,
2（別角度）Close view of two crossing motion trails forming an X of light, sparks at the intersection,
3（写本机）The chronicle page densely illustrated with overlapping duel lines, ink layered thick,
4（書架）The archive hall with two sets of scroll-pages fluttering as if caught in a dual current,
5（全景）Wide view of the dojo floor with two intertwined silver arcs frozen in dynamic motion,
```
【HOOK】
```
二振りの刃が重なり、音が幾重にも響く。
```

## ⑧ 嵐中の一閃
【タイトル】
```
剣戟の写本 嵐中の一閃｜嵐の中のクライマックス【幻想和風LoFi】ハイテンポBGM｜Gaming・Workout・Motivation
```
【物語イントロ】
```
嵐が吹き荒れる中、最後の局面へ。雨と風が写本のページを叩く。
それでも、筆は止まらない。
```
【Suno（コンパクト版）】
```
cinematic Japanese lofi, duel in a raging storm, intense shamisen lead, thunderous taiko, biwa stabs, wind and rain texture, driving lofi-trap beat, deep sub bass, peak energy, 122 BPM, instrumental, no vocals, explosive full-volume start from 0:00
```
【画像5枚（場面行）】
```
1（サムネ兼用）A storm-lashed courtyard duel scene, rain streaking through motion-blurred blade trails, lightning behind a torii silhouette, no figures,
2（別角度）Close view of rain hitting a blade planted in the ground, lightning flash reflected on the metal,
3（写本机）The chronicle page soaked at the edges, ink running in the rain, a storm outside the archive window,
4（書架）Scrolls whipping in a windstorm inside the archive as a window has blown open, rain entering,
5（全景）Wide dramatic view of the storm duel climax, lightning, rain, crossed motion trails filling the sky,
```
【HOOK】
```
嵐の中、それでも筆は止まらない。
```

## ⑨ 決着
【タイトル】
```
剣戟の写本 決着｜最後の一撃、決着の重み【幻想和風LoFi】ハイテンポBGM｜Gaming・Workout・Motivation
```
【物語イントロ】
```
嵐が止む。最後の一撃が、静かに、けれど確かに刻まれる。
写本のページに、決着の一文字が記される。
```
【Suno（コンパクト版）】
```
cinematic Japanese lofi, the final decisive blow, weighty shamisen chord, single powerful taiko hit, biwa resonance, driving lofi-trap beat, deep sub bass, heavy and conclusive, 110 BPM, instrumental, no vocals, explosive full-volume start from 0:00
```
【画像5枚（場面行）】
```
1（サムネ兼用）A single blade standing upright in cracked stone ground after the storm, calm moonlight breaking through clearing clouds, no figures,
2（別角度）Close view of the blade's edge catching the first clear moonlight after the storm,
3（写本机）The chronicle page finished, final brushstroke drying, the archive quiet again,
4（書架）The archive hall settling back into stillness, scrolls resting, dust slowly falling,
5（全景）Wide view of the courtyard after the duel, cracked stone, scattered petals and paper, calm returning,
```
【HOOK】
```
嵐が止み、最後の一撃が静かに刻まれる。
```

## ⑩ 写本は閉じられて
【タイトル】
```
剣戟の写本 写本は閉じられて｜図書館の静けさへ【幻想和風LoFi】ハイテンポBGM｜Gaming・Workout・Motivation
```
【物語イントロ】
```
写本が、静かに閉じられる。禁書区画の扉もまた、鎖に戻る。
今宵の一戦は、また写本の中で眠りにつく。図書館は、いつもの静けさへ。
```
【Suno（コンパクト版）】
```
cinematic Japanese lofi, closing the chronicle and returning to the quiet library, shamisen theme softening, taiko fading, gentle biwa, mellow lofi beat, deep warm bass, calm resolution, 90 BPM, instrumental, no vocals, full-volume melody from 0:00
```
【画像5枚（場面行）】
```
1（サムネ兼用）An ancient chronicle closing itself on a stone desk, the last ink settling, the forbidden archive dimming into calm blue-silver light,
2（別角度）The archive door closing, chains wrapping back around it, quiet returning,
3（写本机）Close view of the closed chronicle with a single blade laid flat beside it now at rest,
4（書架）The towering shelves calm and still, dust settling, soft moonlight,
5（全景）Wide view of the archive returning to silence, the library beyond glowing warm through a distant doorway,
```
【HOOK】
```
写本が閉じ、また静かな図書館の夜へ。
```

═══════════════════════════════
# 自動生成チャットへの指示
①共通ルールを踏まえ各曲9点セットを生成。②概要欄＝物語イントロ＋共通フッター。③タグ＝共通＋場面語1〜2。④サムネ＝各曲画像1＋共通サフィックス＋余白指定＋ネガティブ。⑤動画画像＝各行＋共通サフィックス＋ネガティブ。⑥固定コメント＝共通テンプレ＋各曲HOOK。⑦SEO・⑧シリーズ繋がりは共通、次動画は次番号（⑩は①へ、または他シリーズへの導線）。**Sunoは必ずコンパクト版（表記の文字数目安）のまま使用し、長文化しない。** 必ずコードブロック、省略しない、「続けて」で次曲。
