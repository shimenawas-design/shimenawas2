# Level Trim マスタードキュメント

**作成日：2026-08-24**（このセッションでの音源制作作業をまとめたもの）
関連：[handoff20260823.md](./handoff20260823.md)（配信戦略・規約確認）／[prompts.md](./prompts.md)（プロンプト集の原本）

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
| 1 | `Idle Loop` | 70 | （基準）デチューン・テープワブル | 9/6（リリース済み・審査中） |
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
- 歌詞欄：`[Instrumental]` のみ
- UIのInstrumentalトグル：ON（**Warm Cacheもハミング混入区間は除外済みのため、Instrumentalとして扱う方針で確定**。判断の経緯は4.6参照）
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
- コピペ専用の統合版プロンプトシートを [gemini_prompts_copyready.md](./gemini_prompts_copyready.md) に用意済み
- **生成状況（2026-08-24）**：#2〜#6すべて生成・振り分け完了。各曲フォルダ直下に`<曲名> jacket.png`（Thread Poolのみ予備の`(alt).png`もあり）。**Canvaでの3000×3000リサイズはまだ未実施**

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
- **判断（2026-08-24確定）**：ハミング混入区間を完全に除外できたため、Instrumentalとして扱う。UIのInstrumentalトグルはON、歌詞欄は`[Instrumental]`のまま他曲と統一

### 4.4 検証手法（バイト単位比較）
音声を実際に聴けないため、「意図した音源に差し替わっているか」は以下の方法で数値的に検証した：
```bash
ffmpeg -ss <出力側の時刻> -t 3 -i "combined.wav" -f s16le -ar 48000 -ac 2 out.pcm
ffmpeg -ss <ソース側の対応時刻> -t 3 -i "take1.wav" -f s16le -ar 48000 -ac 2 src.pcm
cmp -l out.pcm src.pcm | wc -l   # 0なら完全一致
```
今回の全ての結合作業で、この検証により意図通りの音源が使われていることを確認済み。

### 4.5 最終結果一覧

| 曲 | 手法 | 構成 | 最終尺 |
|---|---|---|---|
| #2 Warm Cache | 結合 | take2(0:00-3:00) → 3秒クロスフェード → take1(3:00-5:15) → 4秒フェードアウト | 5:12 |
| #3 Long Poll | 単体採用 | take2のみ（全体平均-15.3dBでtake1より静か） | 7:59 |
| #4 Thread Pool | 結合 | take2(0-90s)→take1(90-150s)→take2(150-279.9s)、各5秒クロスフェード | 4:30 |
| #5 Backpressure | 結合 | take1(0-180s)→take2(180-210s)→take1(210-479s)、各3秒クロスフェード | 7:53 |
| #6 Hot Path | 単体採用 | take2のみ（後半ほど顕著にtake1より静か） | 7:59 |

最終ファイル名は`#<番号> <曲名> (combined).wav`（48kHz/16bit）。入稿用に`#<番号> <曲名>.flac`（44.1kHz、soxrリサンプラー明示）へ変換済み。

### 4.6 GitHub上のレビュー指摘と対応（2026-08-24）

GitHubリポジトリ `shimenawas-design/shimenawas2`（ブランチ`claude/new-session-8v0hvp`）の `docs/level-trim/review-2026-08-24.md` に、本書とは別セッションによる品質レビューが存在することが判明。指摘5項目すべてに対応した。

| # | 指摘 | 対応 |
|---|---|---|
| 1 | Warm Cacheのカット位置(6:00)がハミング開始点と一致していて精度不足 | take1側の使用終端を5:15に短縮（ハミング開始5:30まで15秒マージン）、末尾4秒フェードアウトを追加 |
| 2 | **選定基準が設計思想（understated and non-intrusive）と逆行**：「密度が高い方＝音量が大きい方」を機械選択で採用していた | **全曲、選定基準を「静かな方を優先」に反転して再構築**。Long Poll・Hot Pathはtake1→take2に、Backpressureはtake1/take2の担当区間が入れ替わり、Warm Cache・Thread Poolも同様に再構成 |
| 3 | クロスフェードはバイト比較で「意図した音源か」は検証できるが、テイク間のキー/テンポ衝突は未検証 | Thread Pool（切り替え回数が最多）のクロスフェードを3秒→5秒に延長し、変化をより緩やかに。**ただしキー/テンポの一致そのものはffmpegでは検証できず、実際に聴いての確認が引き続き必要**（未解決、要リスニング） |
| 4 | Thread Poolが4:31と短尺。3ヶ月の余裕があるためSunoでの再生成を推奨 | **アシスタントでは対応不可**（Suno生成はユーザー操作必須、[handoff20260823.md](./handoff20260823.md)の制約通り）。現状は継ぎ接ぎ版（4:30）のまま。再生成するかは要判断 |
| 5 | 48kHz→44.1kHz変換時、リサンプラーが未指定（デフォルト＝低品質になりうる） | `-af aresample=resampler=soxr:precision=28` を明示して全曲再変換済み |

軽微な指摘（ファイル名の`#`使用、状態表記の不整合、ドキュメント二重管理）は未対応。特に**ドキュメント二重管理**（本書とGitHub版`master.md`が別内容）は、このセッションにgh CLI・git環境がないため解消できていない。GitHubへの反映が必要ならユーザー側での対応、またはgh CLIが使える環境での作業が必要。

### 4.7 残タスク

1. **全曲を再度リスニング確認**：選定基準を反転したため、旧版で確認済みだった内容は無効。特にThread Poolのキー/テンポ一致（指摘3）は要確認
2. **Thread Poolを再生成するか判断**（指摘4）
3. **ジャケット画像5枚をCanvaで3000×3000にリサイズ**（画像自体は#2〜#6すべて生成・各フォルダへ振り分け済み。リサイズのみ未実施）
4. GitHub側ドキュメントとの整合（要gh CLI環境）

---

## 5. ファイル配置

```
RouteNote/Level Trim/
├── master20260824.md         本書
├── handoff20260823.md        配信戦略・規約確認
├── prompts.md                プロンプト集の原本（#1〜#6）
├── gemini_prompts_copyready.md  ジャケット用プロンプト（コピペ専用）
├── 01_Idle Loop/              リリース済み
├── 02_Warm Cache/
│   ├── #2 Warm Cache (take1).wav
│   ├── #2 Warm Cache (take2).wav
│   ├── #2 Warm Cache (combined).wav   48kHz・編集済み音源
│   └── #2 Warm Cache.flac             44.1kHz・入稿用
│   └── Warm Cache jacket.png
├── 03_Long Poll/               同様の構成 + Long Poll jacket.png
├── 04_Thread Pool/              同様の構成 + Thread Pool jacket.png / (alt).png
├── 05_Backpressure/             同様の構成 + Backpressure jacket.png
└── 06_Hot Path/                同様の構成 + Hot Path jacket.png
```

※ 2026-08-24、フォルダ名に番号を付与済み（`01_〜06_`）。#2〜#6のジャケット画像も生成・振り分け完了。

---

## 6. 次にやること（優先順）

1. **全曲を再度リスニング確認**（4.7-1）— 選定基準を反転したため再確認必須。特にThread Poolの継ぎ目
2. **ジャケット画像5枚をCanvaで3000×3000にリサイズ**（4.7-3）
3. **Thread Poolを再生成するか判断**（4.7-2）
4. RouteNoteへの入稿（[handoff20260823.md](./handoff20260823.md)のチェックリスト参照）— 音源(`.flac`)・Instrumental設定・C/Pライン等
