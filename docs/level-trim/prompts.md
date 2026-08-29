# Suno / Gemini プロンプト集（#1〜#6）

関連：[handoff-2026-08-23.md](./archive/handoff-2026-08-23.md) / [release-plan.md](./release-plan.md)

---

## 設計方針

BPMを梯子状に配置し、**各曲に「動かす変数」を1つだけ割り当てる**。

| # | 曲名 | BPM | 動かした変数 | リリース |
|---|---|---|---|---|
| 1 | `Idle Loop` | 70 | （基準）デチューン・テープワブル | 9/6 |
| 2 | `Warm Cache` | 82 | 飽和・持続・ブラウンノイズ層 | 10/11 |
| 3 | `Long Poll` | 62 | **密度** — 最も疎、ほぼビートレス | 11/1 |
| 4 | `Thread Pool` | 90 | **ポリリズム** — 長さの違うループの位相 | 11/22 |
| 5 | `Backpressure` | 76 | **低域と帯域** — 重心が低く上が塞がれている | 12/13 |
| 6 | `Hot Path` | 100 | **推進力** — 最も前進的、グリッチが硬質 | 1/3 |

62〜100BPMで作業時間帯を一巡する。

### 全曲で据え置く語（＝アルゴリズム上の指紋）
`warm` / `analog synth pads` / `glitch` / `nostalgic muted tone` / `understated and non-intrusive` / `no build-up` / `no climax` / `instrumental, no vocals, no singing, no lyrics`

これを維持する限りジャンル信号は割れない。**新曲を追加する際も必ず踏襲すること。**

---

## Suno スタイル欄

### #1 `Idle Loop` — 70bpm（リリース済み・参考）
```
instrumental warm melancholic IDM, detuned analog synth pads, subtle glitch percussion textures, nostalgic muted tone, slow tempo around 70bpm, tape warble, understated and non-intrusive, no build-up, no climax, instrumental, no vocals, no singing, no lyrics
```

### #2 `Warm Cache` — 82bpm
```
instrumental warm IDM, saturated analog synth pads, gentle tape saturation, sparse glitch percussion, soft brown noise bed, sustained and unchanging, slow tempo around 82bpm, nostalgic muted tone, understated and non-intrusive, no build-up, no climax, instrumental, no vocals, no singing, no lyrics
```

### #3 `Long Poll` — 62bpm
```
instrumental warm ambient IDM, sparse detuned analog synth pads, very long decay, wide empty space between notes, occasional faint glitch clicks, almost beatless, slow tempo around 62bpm, nostalgic muted tone, patient and still, understated and non-intrusive, no build-up, no climax, instrumental, no vocals, no singing, no lyrics
```

### #4 `Thread Pool` — 90bpm
```
instrumental warm IDM, interlocking polyrhythmic loops of different lengths slowly phasing, muted analog synth pads, dry glitch percussion, gently shifting patterns, steady tempo around 90bpm, nostalgic muted tone, understated and non-intrusive, no build-up, no climax, instrumental, no vocals, no singing, no lyrics
```

### #5 `Backpressure` — 76bpm
```
instrumental warm IDM, deep rounded sub bass, low-pass filtered analog synth pads, muffled high end, dense compressed texture, restrained glitch percussion, slow tempo around 76bpm, nostalgic muted tone, heavy but calm, understated and non-intrusive, no build-up, no climax, instrumental, no vocals, no singing, no lyrics
```

### #6 `Hot Path` — 100bpm
```
instrumental warm IDM, crisp precise glitch percussion, steady forward pulse, bright detuned analog synth pads, clean tight groove, tempo around 100bpm, nostalgic muted tone, understated and non-intrusive, no build-up, no climax, instrumental, no vocals, no singing, no lyrics
```

### 全曲共通の運用
- **歌詞欄**：`[Instrumental]` のみ
- **UIのInstrumentalトグル**：ON
- **長尺化**：Extendで `[Intro]→[Development A]→[Subtle Variation]→[Sustain]→[Outro - slow fade]`

---

## Gemini 画像プロンプト

### 共通の視覚システム
ウォームアンバー／カッパー × ディープチャコール。マクロ撮影、浅い被写界深度、微細なグリッチ・走査線、フィルムグレイン。
**構図を曲ごとに変える**ことで、60×60pxのサムネイルでも区別がつくようにしている（中央発光 / 暗闇の一点 / 平行線 / 高密度 / 斜めの一本）。

### #2 `Warm Cache`
```
Extreme macro photograph of an aluminium heatsink, warm amber light glowing from deep between the fins, radiating outward from the centre. Deep charcoal-navy background. Shallow depth of field, soft bokeh. Subtle horizontal scanline artifacts and fine film grain. Warm copper and burnt orange palette. Abstract, calm, no text, square composition.
```

### #3 `Long Poll`
```
A single small amber indicator LED glowing in the far distance down a long dark corridor of server racks. Vast negative space, most of the frame in deep charcoal shadow. Extreme depth of field falloff, heavy bokeh. Faint scanline artifacts and film grain. Minimal warm amber accent against near-black. Quiet, patient, abstract, no text, square composition.
```

### #4 `Thread Pool`
```
Macro photograph of many parallel ribbon cables and fibre optic strands running side by side, slightly offset from each other, warm amber light travelling along them at different points. Deep charcoal-navy background. Shallow depth of field. Subtle glitch displacement artifacts and film grain. Warm copper palette. Rhythmic, repeating, abstract, no text, square composition.
```

### #5 `Backpressure`
```
Tight macro photograph of densely packed electrolytic capacitors and stacked circuit layers, compressed tightly into the frame with almost no empty space. Dim warm amber light struggling through from behind. Deep charcoal-navy, darker and heavier than usual. Shallow depth of field, subtle glitch artifacts, film grain. Muted copper palette, low contrast. Dense, weighty, abstract, no text, square composition.
```

### #6 `Hot Path`
```
A single bright amber circuit trace cutting diagonally across a dark printed circuit board, glowing hot, with subtle motion blur along its length. All other traces dim and out of focus. Deep charcoal-navy background. Shallow depth of field, crisp glitch artifacts, fine film grain. Warm copper and bright orange palette. Fast, directional, abstract, no text, square composition.
```

### 生成時の注意
- **文字は入れない** — Geminiの文字描画は不正確で、DSPは表記の完全一致を要求する。曲名が読める必要はない
- **実在ブランドのロゴ・型番の写り込みを目視確認** — マクロ撮影風だと基板の刻印が生成されることがある
- 出力後に Canva で **3000×3000** にリサイズ（#1と同じ手順）
- 人物・顔が入ったら再生成

### 既存の素材
- **#1 `Idle Loop`**：Gemini生成「回路基板・ウォームアンバー・グリッチ」構図（使用済み）
- **予備案**：「ワークスペースのぼかし」構図 — 上記の系統と合わないため、使うなら別シリーズ／YouTube長尺用に回す

---

## 音源書き出し後の処理（毎回同じ）

```bash
# ファイル名は必ず英数字にする（日本語だとffmpegでエンコードエラー）
ffmpeg -i "Warm Cache.wav" -af "aresample=resampler=soxr:precision=28" \
  -ar 44100 -map_metadata -1 "Warm Cache.flac"
```

- RouteNoteは **MP3(320kbps/44.1kHz) か FLAC(44.1kHz)** のみ受付。Sunoの48kHz WAVは要変換
- **`-map_metadata -1`** で "made with suno" の埋め込みメタデータを削除（必須）
- 48000→44100 は整数比でないため **リサンプラー（soxr）を明示する**
- リリースタイトルのIME誤変換に注意（過去にカタカナ「アイドルループ」になった事例あり）
