# Level Trim マスタードキュメント

**作成日：2026-08-24**（ローカルセッションでの音源制作作業をまとめたもの）
関連：[handoff-2026-08-23.md](./handoff-2026-08-23.md)（配信戦略・規約確認）／[prompts.md](./prompts.md)（プロンプト集の原本）／[release-plan.md](./release-plan.md)（リリース計画）

> **⚠️ 本書に対するレビュー結果あり** → [review-2026-08-24.md](./review-2026-08-24.md)
> Warm Cacheのカット位置・結合手法の妥当性・Thread Poolの扱いについて、リリース前に対処すべき指摘が5件ある。

---

## 1. プロジェクト概要（要約）

| 項目 | 値 |
|---|---|
| アーティスト名義 | `Level Trim` |
| 用途 | エンジニアの作業用集中BGM（プログラミング・CAD・報告書作成） |
| ジャンル | Electronic / IDM（ウォーム・グリッチ寄り） |
| ディストリビューター | RouteNote（Ongaku Toshokanと同一アカウント、名義のみ分離） |
| 曲構成 | 6曲、BPMを62〜100で梯子状に配置。各曲「動かす変数」を1つだけ割り当てる設計 |

詳しい配信戦略・規約確認・リリースカレンダーは [handoff20260823.md](./handoff20260823.md) を参照。

### 曲一覧

| # | 曲名 | BPM | 動かした変数 | リリース予定 |
|---|---|---|---|---|
| 1 | `Idle Loop` | 70 | （基準）デチューン・テープワブル | 9/6（RouteNote提出済み・Pending Moderation） |
| 2 | `Warm Cache` | 82 | 飽和・持続・ブラウンノイズ層 | 10/11 |
| 3 | `Long Poll` | 62 | 密度 — 最も疎、ほぼビートレス | 11/1 |
| 4 | `Thread Pool` | 90 | ポリリズム | 11/22 |
| 5 | `Backpressure` | 76 | 低域と帯域 | 12/13 |
| 6 | `Hot Path` | 100 | 推進力 | 1/3 |

---

## 2. Sunoプロンプト（全曲）

全曲で据え置く語（＝アルゴリズム上の指紋）：
`warm` / `analog synth pads` / `glitch` / `nostalgic muted tone` / `understated and non-intrusive` / `no build-up` / `no climax` / `instrumental, no vocals, no singing, no lyrics`

### #1 `Idle Loop` — 70bpm（リリース済み）
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

### 運用ルール
- 歌詞欄：`[Instrumental]` のみ（※ただしWarm Cacheはボーカル/ハミングが混入したため例外。詳細は4章）
- UIのInstrumentalトグル：ON（Warm Cacheは要OFF、4章参照）
- 長尺化：Extendで `[Intro]→[Development A]→[Subtle Variation]→[Sustain]→[Outro - slow fade]`

---

## 3. Gemini画像プロンプト

### 共通の視覚システム
ウォームアンバー／カッパー × ディープチャコール。マクロ撮影、浅い被写界深度、微細なグリッチ・走査線、フィルムグレイン。曲ごとに構図を変えて60×60pxサムネでも区別がつくようにする。

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
- 文字は入れない（DSPは表記の完全一致を要求するため）
- 実在ブランドのロゴ・型番が写り込んでいないか目視確認
- 出力後Canvaで3000×3000にリサイズ
- 人物・顔が入ったら再生成
- **画像はまだ未生成**（このセッションでは着手していない。次のタスク）

---

## 4. このセッションでの作業ログ（2026-08-24）

### 4.1 Sunoからのダウンロード

Suno（`shimenawas`アカウント、`https://suno.com/me`）から#2〜#6をWAV形式でダウンロードし、`RouteNote/Level Trim/<曲名>/`配下に振り分け。

| 曲 | 取得テイク数 | 備考 |
|---|---|---|
| #2 Warm Cache | 2 | — |
| #3 Long Poll | 2 | — |
| #4 Thread Pool | 2 | 尺が短い（4:15/4:40）。Extend再生成を試みたが伸びず、断念してこの尺のまま採用 |
| #5 Backpressure | 2 | 初回確認時は1テイクしか見えなかったが、後から2テイク目が存在すると判明し追加取得 |
| #6 Hot Path | 2 | — |

ダウンロードは各テイクとも48kHz/16bit stereo WAV。ファイル名に`(take1)`/`(take2)`を付与して区別。

### 4.2 2テイクの結合方針と手法

**背景**：同一プロンプトから生成された2テイクを、良い区間だけ組み合わせて1曲にしたいという要望。

**採用手法**：
1. 30秒（曲によっては60秒）単位のセグメントに分割
2. 各セグメントについて`ffmpeg -af volumedetect`で平均音量（mean_volume）を測定し、両テイクを比較
3. 音量差が明確な区間（目安1dB以上）だけ「密度が高い方」を採用。差が僅少な区間は前の選択を維持（頻繁な切り替えを避けるヒステリシス）
4. 選んだブロックを`acrossfade`フィルタ（3秒、triangularカーブ）で実際に音を重ねてブレンド。単純なフェードイン/アウト＋concatではテンポ・音量の継ぎ目が不自然になることが判明したため、この方式に変更（4.3参照）
5. 最終ファイルは`-map_metadata -1`で"made with suno"の埋め込みメタデータを除去

**判明した限界**：
- 密度（音量）だけでは「良い区間」を判断できない場合がある（Long Poll・Hot Pathは差がノイズレベルで機械選択が機能せず、take1を単体採用）
- ボーカル・ハミングの混入は音量分析やスペクトログラム画像では検出できなかった。**実際に聴いたユーザーからの報告に依存**している

### 4.3 発生した問題と対応

**問題1：継ぎ目でテンポ・音量が急変する**
- 原因：初回は各セグメントを0.15秒の短いフェードで書き出してから単純concatしていたため、実質的に「フェードアウト→無音→フェードイン」に近く、テンポ/音量の断絶が聴感上目立った
- 対応：`acrossfade`フィルタで3秒間、実際に2つの音声を重ねてクロスフェードする方式に変更

**問題2：Warm Cacheの後半にボーカル/ハミングが混入**
- take2の6:30以降にボーカルらしきものが混入していると報告があり、その区間をtake1に差し替えて再構築
- しかし差し替え後も「ボーカルが消えていない」との報告 → バイト単位のPCM比較で検証したところ、該当区間はtake1の音声と完全一致（差分0）と確認。**つまりtake1自体にも同じ区間にハミングが入っていた**
- 最終的にユーザーが実際に聴いて特定：**take1は5:30以降、take2は6:00以降にハミングあり**
- 対応：take1を0:00-3:00、take2を3:00-6:00で使用し、3秒クロスフェードで結合。6:00以降は完全にカット（尺は7:59→5:57に短縮）
- **この曲はInstrumentalとして扱えない可能性がある**（4.5参照）

### 4.4 検証手法（バイト単位比較）
音声を実際に聴けないため、「意図した音源に差し替わっているか」は以下の方法で数値的に検証した：
```bash
ffmpeg -ss <出力側の時刻> -t 3 -i "combined.wav" -f s16le -ar 48000 -ac 2 out.pcm
ffmpeg -ss <ソース側の対応時刻> -t 3 -i "take1.wav" -f s16le -ar 48000 -ac 2 src.pcm
cmp -l out.pcm src.pcm | wc -l   # 0なら完全一致
```
今回の全ての結合作業で、この検証により意図通りの音源が使われていることを確認済み。

### 4.5 最終結果一覧

| 曲 | 手法 | 構成 | 最終尺 | 元の尺 | 特記事項 |
|---|---|---|---|---|---|
| #2 Warm Cache | 結合 | take1(0:00-3:00) → 3秒クロスフェード → take2(3:00-6:00) | 5:57 | 7:59 | **ハミングを除外するため尺を短縮。Instrumentalトグルは要検討（4.6参照）** |
| #3 Long Poll | 単体採用 | take1のみ | 7:59 | 7:59 | 密度差がノイズレベルのため機械選択せず |
| #4 Thread Pool | 結合 | take1(0-90s)→take2(90-150s)→take1(150-254.8s)→take2(254.8-279.9s)、各3秒クロスフェード | 4:31 | take1:4:15 / take2:4:40 | 尺が短いまま採用（Extend再生成断念） |
| #5 Backpressure | 結合 | take2(0-180s)→take1(180-210s)→take2(210-479s)、各3秒クロスフェード | 7:53 | 7:59 | — |
| #6 Hot Path | 単体採用 | take1のみ | 7:59 | 7:59 | 明確な密度差がないため機械選択せず |

全曲、最終ファイル名は`#<番号> <曲名> (combined).wav`、保存先は`RouteNote/Level Trim/<曲名>/`。

### 4.6 ⚠️ 未解決・要確認事項

1. **全曲、実際に聴いての最終確認がまだ済んでいない。** 特にThread Pool（3回クロスフェード）・Backpressure（2回クロスフェード）は継ぎ目が多いため、テンポ/音量の違和感がないか要確認
2. **Warm Cacheのボーカル/ハミング問題**：ハミングは除外したが、そもそも"instrumental, no vocals"という全曲共通の設計方針にこの曲だけ抵触するリスクがある。RouteNote入稿時、Instrumentalトグルの扱いをどうするか要判断
3. **サンプルレート未対応**：現在の`(combined).wav`は全曲48kHz/16bit。RouteNoteの受付規格はMP3(320kbps/44.1kHz)かFLAC(44.1kHz)なので、**入稿前に44.1kHzへの変換が必要**（未実施）
4. **ジャケット画像が#2〜#6すべて未生成**：Geminiプロンプトは3章の通り確定しているが、実際の画像生成・Canvaでの3000×3000リサイズはまだ着手していない
5. **Thread Poolの尺が他曲より大幅に短い**（4:31 vs 他曲7:53〜7:59）。シリーズ内での尺の統一感が崩れている点、リリース判断に影響する可能性

---

## 5. ファイル配置

**ドキュメントはリポジトリの `docs/level-trim/` が唯一の正。ローカルにコピーを作らないこと**（詳細はリポジトリ直下の `CLAUDE.md` を参照）。
音源は `.gitignore` 対象でローカルにのみ存在する。

```
RouteNote/                          ← ここでgit管理
├── CLAUDE.md
├── docs/level-trim/
│   ├── master.md                   本書
│   ├── review-2026-08-24.md        本書へのレビュー
│   ├── handoff-2026-08-23.md       配信戦略・規約確認
│   ├── release-plan.md             リリース計画
│   ├── prompts.md                  プロンプト集の原本（#1〜#6）
│   └── market-research-2026-08.md  市場調査
└── Level Trim/                     ← .gitignore対象（音源）
    ├── Idle Loop/                  提出済み
    ├── Warm Cache/
    │   ├── 02 Warm Cache (take1).wav
    │   ├── 02 Warm Cache (take2).wav
    │   └── 02 Warm Cache (combined).wav   ← 最終候補
    ├── Long Poll/                  同様の構成
    ├── Thread Pool/                同様の構成
    ├── Backpressure/               同様の構成
    └── Hot Path/                   同様の構成
```

※ ファイル名の先頭は `#2` ではなく `02` にすること。`#` はシェルでコメント開始文字として扱われ、クォートを忘れると事故る。

---

## 6. 次にやること（優先順）

**[review-2026-08-24.md](./review-2026-08-24.md) の指摘を反映済みの順序。**

1. **Warm Cache の末尾を 5:45 に詰める** — ハミング開始点とカット位置が一致しており安全余裕がない（レビュー指摘1）
2. **全曲を実際に聴いて確認**（4.6-1）— 特にThread Pool（クロスフェード3回）・Backpressure（同2回）の継ぎ目
3. **Thread Pool を作り直すか判断**（レビュー指摘4）— 尺4:31、つぎはぎ4セグメント。リリースは11/22で猶予あり
4. **Warm Cacheのinstrumental扱いを判断**（4.6-2）
5. **44.1kHzへの変換**（4.6-3）— リサンプラーを明示すること：
   ```bash
   ffmpeg -i in.wav -af "aresample=resampler=soxr:precision=28" -ar 44100 -map_metadata -1 out.flac
   ```
6. **ジャケット画像生成**（4.6-4）— Gemini（3章のプロンプト）→ Canvaで3000×3000
7. RouteNoteへの入稿（[handoff-2026-08-23.md](./handoff-2026-08-23.md)のチェックリスト参照）
