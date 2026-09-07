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
- **既知の注意点**: Gemini生成画像には右下付近に小さな透かし（星マーク）が入ることがある。周囲が単色背景の場合はその領域を背景色で塗りつぶして除去できる（Track #1で確認済み、ffmpeg/PILでの後処理）

### #1 `Torque Lock` 用プロンプト
```
Extreme close-up of a hollow, cutaway rotary engine rotor suspended in a dark empty garage space, deep black void background, dramatic crimson red and amber metallic rim lighting reflecting off brushed steel and carbon surfaces, faint wisps of engine smoke drifting through the hollow center, gritty industrial texture with subtle scratches and grime, cinematic movie-poster lighting, hyper-detailed photorealistic render, moody aggressive atmosphere, tension and stillness, no text, no people, no hands, no silhouettes, no logos, square 1:1 aspect ratio, ultra high detail, 8k quality
```

生成後、透かし除去 → 3000×3000リサイズ（Track #1はPIL/ffmpegで実施、`LANCZOS`リサンプリング）。
