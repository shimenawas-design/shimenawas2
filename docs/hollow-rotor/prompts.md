# Hollow Rotor プロンプト原本

全曲共通シグネチャ（据え置く語、Level Trimの「warm/analog/glitch」に相当）：
`cowbell` / `distorted pitched-down 808` / `dark and hypnotic` / `relentless` / `lo-fi tape saturation` / `instrumental` / `no vocals`

BPMとテクスチャの微調整だけを曲ごとに動かす（1曲=1変数の原則、Level Trimと共通）。

---

## #1 `Torque Lock`（確定版・声の混入なしを確認済み）

### 経緯
初回プロンプトは`phonk`という単語を含んでおり、Instrumentalトグル ON + 徹底した否定プロンプトを使ってもハミング等のワードレス・ボーカルが後半に混入した。`phonk`という単語自体を外し、音の特徴だけで記述したところ声が消えることを確認（2026-09-06）。詳細は[master.md](./master.md)5章参照。

### ❌ 初回版（声が混入・不採用）
```
instrumental drift phonk, aggressive cowbell pattern, distorted pitched-down 808 bass, punchy kick, sharp snare, busy hi-hat rolls, lo-fi cassette tape saturation, gritty vinyl crackle, dark and hypnotic, relentless driving energy, tempo around 150bpm, explosive full-volume start from 0:00, no long intro, seamless loop, strictly instrumental, no vocals, no singing, no lyrics, no humming, no oohs, no ahs, no wordless vocals, no vocal chops, no vocal ad-libs, no choir
```
Exclude Styles: `rap vocals, spoken word, chanting, ad-libs, melodic singing, choir, humming, wordless vocals, vocal chops`

### ✅ 確定版（Style of Music、声の混入なし）
```
dark aggressive electronic instrumental, cowbell-driven percussion groove, distorted pitched-down sub-bass with pitch bends, punchy kick, sharp snare, busy hi-hat rolls, gritty lo-fi tape and vinyl texture, hypnotic repetitive loop, relentless mechanical energy, tempo 150bpm, explosive full-volume start from 0:00, no long intro, seamless loop, purely instrumental track, absolutely no vocal content, no voice of any kind, no human voice, no singing, no humming, no vocal samples
```

Lyrics欄（Custom Mode）: `[Instrumental]`のみ + UIのInstrumentalトグルをON

**Extend使用時の注意**: 区間ごとにこの全文を再入力すること。最初の1回だけだと後半にかけて禁止指定の効力が薄れる。

---

## Gemini画像プロンプト（ジャケット共通ルール）

- **色調**: 黒×深紅（crimson）×琥珀色の金属光沢。Level Trim（シアン×琥珀）、Ongaku Toshokan（青×銀×琥珀）とは区別
- **識別アンカー**: 「中空（hollow）のロータリーエンジン部品」を毎回中央〜近景に配置。空洞から光が漏れる・煙がうっすら立ち込める演出で「空虚さ」を視覚化
- **共通制約**: 人物なし・手なし・シルエットなし・文字なし、ダーク・攻撃的・シネマティック、超高精細、正方形1:1指定
- **既知の注意点**: Gemini生成画像には右下付近に小さな透かし（星マーク）が入ることがある（Track #1・#3で発生、#2は透かしなし）。生成のたびに右下を確認すること。除去方法は周囲の背景次第で使い分ける：**単色に近い背景なら背景色で塗りつぶすだけで十分**（Track #1）。**周囲に模様・グラデーションがある背景では単純な塗りつぶしだと不自然に浮くため、`opencv-python-headless`の`cv2.inpaint`（TELEA法）で周辺テクスチャから自然に補完する**（Track #3、`pip install opencv-python-headless`が必要）。
- **生成方法（2026-09-12実施）**: Gemini本体（gemini.google.com）にプロンプトを直接貼り付けて生成。出力アスペクト比は必ずしも指定通り1:1にならない（Track #1は1024×1024、Track #2は2048×2048と幅高さは一致したが、生成前に毎回確認要）。「フルサイズでダウンロード」ボタンを使うこと（サムネイルサイズの誤ダウンロードに注意）

### #1 `Torque Lock` 用プロンプト
```
Extreme close-up of a hollow, cutaway rotary engine rotor suspended in a dark empty garage space, deep black void background, dramatic crimson red and amber metallic rim lighting reflecting off brushed steel and carbon surfaces, faint wisps of engine smoke drifting through the hollow center, gritty industrial texture with subtle scratches and grime, cinematic movie-poster lighting, hyper-detailed photorealistic render, moody aggressive atmosphere, tension and stillness, no text, no people, no hands, no silhouettes, no logos, square 1:1 aspect ratio, ultra high detail, 8k quality
```

生成後、透かし除去 → 3000×3000リサイズ（Track #1はPIL/ffmpegで実施、`LANCZOS`リサンプリング）。

---

## #2 `Rev Limiter`（確定・2026-09-08、音源・画像とも完成2026-09-12）

動かす変数はBPMのみ（150→160）。他はTrack #1の確定版から一切変更しない。

**生成結果**：Suno初回テイクは声が混入、2回目のテイクで声なしを確認し2回目を採用（プロンプト自体の問題ではなく通常の生成ランダム性）。Gemini画像は1回目の生成で2048×2048・透かしなしの結果が得られ、そのまま採用。

### Style of Music
```
dark aggressive electronic instrumental, cowbell-driven percussion groove, distorted pitched-down sub-bass with pitch bends, punchy kick, sharp snare, busy hi-hat rolls, gritty lo-fi tape and vinyl texture, hypnotic repetitive loop, relentless mechanical energy, tempo 160bpm, explosive full-volume start from 0:00, no long intro, seamless loop, purely instrumental track, absolutely no vocal content, no voice of any kind, no human voice, no singing, no vocal samples
```

Lyrics欄: `[Instrumental]`のみ + Instrumentalトグル ON。`phonk`という単語は入れない（Track #1で声混入の原因と特定済み）。Extend使用時は区間ごとに全文を再入力。

### Gemini画像プロンプト
```
A hollow cutaway turbine rotor spinning at speed inside a dark industrial test chamber, deep black void background, intense crimson red and amber light streaking through the hollow center from motion, radial motion blur on the outer edge while the core stays sharp, heat shimmer and thin smoke trails, scratched brushed steel and carbon texture, cinematic movie-poster lighting, hyper-detailed photorealistic render, aggressive high-speed atmosphere, no text, no people, no hands, no silhouettes, no logos, square 1:1 aspect ratio, ultra high detail, 8k quality
```

---

## #3 `Dead Weight`（確定・2026-09-12、音源・画像とも完成）

動かす変数はBPM（150→148、経緯は下記）と③808処理（重く獰猛に）。**当初BPM140で設計したが、声混入の原因がBPM自体にあると判明し148に変更した。** 詳細な検証経緯は[master.md](./master.md)5章を参照。

### ❌ 試行錯誤（すべて140bpm、声混入解消せず）
1. `dark aggressive phonk instrumental` + `growling/guttural`表記 → 声が「がっつり」増加
2. `dark aggressive electronic instrumental`（phonkなし）+ `crushing sub-bass with deep pitch drops`表記 → 改善せず、むしろ増加
3. 808をTrack #1の確定版そのまま + BPM140維持 → 改善せず（冒頭から声）
4. BPM145に変更 → 改善したが声は残る

### ✅ 確定版（Style of Music、BPM148で声なしを2テイクで確認）
```
dark aggressive electronic instrumental, cowbell-driven percussion groove, heavily distorted crushing sub-bass with deep pitch drops, punchy kick, sharp snare, busy hi-hat rolls, gritty lo-fi tape and vinyl texture, hypnotic repetitive loop, relentless mechanical energy, tempo 148bpm, explosive full-volume start from 0:00, no long intro, seamless loop, purely instrumental track, absolutely no vocal content, no voice of any kind, no human voice, no singing, no vocal samples, no trap beat, no rap, no hip-hop vocals, no R&B, no soul
```

Lyrics欄: `[Instrumental]`のみ + Instrumentalトグル ON。**140〜145付近のBPMは避ける**（トラップの定番テンポ域でボーカル連想が強い）。低めのBPMを狙う曲では`no trap beat, no rap, no hip-hop vocals, no R&B, no soul`を標準装備にする。

### Gemini画像プロンプト（生成済み。透かしは`cv2.inpaint`で除去）
```
A massive hollow cutaway engine rotor under extreme compressive strain inside a dark industrial press chamber, deep black void background, dramatic crimson red and amber light glowing from stress fractures and the hollow core, heavy metal groaning under load, thick scratched steel and carbon texture, sparks and embers falling, cinematic movie-poster lighting, hyper-detailed photorealistic render, monumental and crushing atmosphere, no text, no people, no hands, no silhouettes, no logos, square 1:1 aspect ratio, ultra high detail, 8k quality
```

---

## #4 `Firing Order`（確定・2026-09-14、音源・画像とも完成）

動かす変数はBPM（150→155）と②カウベル処理（密に）。**当初はTrack #1の808表現を土台にしたが3テイク連続で声混入し、Track #3の確定版（808=crushing/pitch drops＋trap/rap/R&B除外）を土台に変えたら初回テイクで解消した。** 詳細は[master.md](./master.md)5章を参照。

### ❌ 試行錯誤（すべて155bpm、Track #1ベースの808表現、3テイクとも声混入）
1. `relentless dense 16th-note cowbell pattern` + Track #1の808表現そのまま → 3テイク連続で声混入

### ✅ 確定版（Style of Music、Track #3ベースに切替。初回テイクで声なしを確認）
```
dark aggressive electronic instrumental, relentless dense 16th-note cowbell pattern, heavily distorted crushing sub-bass with deep pitch drops, punchy kick, sharp snare, busy hi-hat rolls, gritty lo-fi tape and vinyl texture, hypnotic repetitive loop, relentless mechanical energy, tempo 155bpm, explosive full-volume start from 0:00, no long intro, seamless loop, purely instrumental track, absolutely no vocal content, no voice of any kind, no human voice, no singing, no vocal samples, no trap beat, no rap, no hip-hop vocals, no R&B, no soul
```

Lyrics欄: `[Instrumental]`のみ + Instrumentalトグル ON。**この一件以降、Track #5・#6もTrack #3の確定版（808=crushing/pitch drops＋trap/rap/R&B除外）を土台にし、副変数だけ載せる方式に統一する。**

### Gemini画像プロンプト（生成済み、透かしなし）
```
A hollow cutaway engine rotor captured in rapid strobe-like multiple exposure showing repeated pulses of motion, dark industrial chamber, deep black void background, dramatic crimson red and amber light flashing in rhythmic bursts from the hollow core, sharp mechanical repetition, scratched brushed steel and carbon texture, sparks firing in quick successive bursts, cinematic movie-poster lighting, hyper-detailed photorealistic render, intense rapid-fire atmosphere, no text, no people, no hands, no silhouettes, no logos, square 1:1 aspect ratio, ultra high detail, 8k quality
```

---

## #5 `Direct Drive`（2026-09-19、音源完成・ジャケット未生成）

当初は⑤空間処理（ドライで近接感）を副変数にする計画だったが、声が混入。副変数を外したBPMのみ版でも声が残り、**非歌詞のボーカライズ（「だだだだ」系）が残るままユーザー判断で採用**。詳細は[master.md](./master.md)5章を参照。

### ❌ 副変数あり（声混入）
Track #3確定版に `dry and tight mix with minimal reverb, close and immersive in-your-face presence` を追加、`tempo 152bpm`。

### 採用版（Track #3確定版のテンポのみ変更、非歌詞ボーカライズが残る）
```
dark aggressive electronic instrumental, cowbell-driven percussion groove, heavily distorted crushing sub-bass with deep pitch drops, punchy kick, sharp snare, busy hi-hat rolls, gritty lo-fi tape and vinyl texture, hypnotic repetitive loop, relentless mechanical energy, tempo 152bpm, explosive full-volume start from 0:00, no long intro, seamless loop, purely instrumental track, absolutely no vocal content, no voice of any kind, no human voice, no singing, no vocal samples, no trap beat, no rap, no hip-hop vocals, no R&B, no soul
```

### Gemini画像プロンプト案（未生成）
```
Extreme macro close-up on the interlocking teeth of a hollow rotor gear mechanism, shallow depth of field with only the foreground teeth in sharp focus, deep black void background, intense crimson red and amber light glowing from between the gear teeth, tight and claustrophobic framing, scratched brushed steel and carbon texture, cinematic movie-poster lighting, hyper-detailed photorealistic render, focused and intense atmosphere, no text, no people, no hands, no silhouettes, no logos, square 1:1 aspect ratio, ultra high detail, 8k quality
```

---

## #6 `Oxide Layer`（2026-09-19、音源完成・ジャケット未生成）

当初は④ローファイ質感の強化を副変数にする計画だったが、声が混入。#5と同様、副変数を外したBPMのみ版でも声が残り、非歌詞のボーカライズが残るままユーザー判断で採用。

### ❌ 副変数あり（声混入）
Track #3確定版の `gritty lo-fi tape and vinyl texture` を `heavily saturated lo-fi tape hiss and crackling vinyl noise, degraded warm analog grit` に置換、`tempo 158bpm`。

### 採用版（Track #3確定版のテンポのみ変更、非歌詞ボーカライズが残る）
```
dark aggressive electronic instrumental, cowbell-driven percussion groove, heavily distorted crushing sub-bass with deep pitch drops, punchy kick, sharp snare, busy hi-hat rolls, gritty lo-fi tape and vinyl texture, hypnotic repetitive loop, relentless mechanical energy, tempo 158bpm, explosive full-volume start from 0:00, no long intro, seamless loop, purely instrumental track, absolutely no vocal content, no voice of any kind, no human voice, no singing, no vocal samples, no trap beat, no rap, no hip-hop vocals, no R&B, no soul
```

### Gemini画像プロンプト案（未生成）
```
A weathered hollow cutaway rotor covered in warm rust and oxidation patina, dark dusty workshop background, deep black void, warm amber and muted crimson light glowing softly through the hollow, worn scratched surface with age and grime, soft warm haze and dust particles drifting in the light, cinematic moody lighting, hyper-detailed photorealistic render, nostalgic weathered atmosphere, no text, no people, no hands, no silhouettes, no logos, square 1:1 aspect ratio, ultra high detail, 8k quality
```
