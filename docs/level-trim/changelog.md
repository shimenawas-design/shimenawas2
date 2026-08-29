# Level Trim 作業ログ（2026-08-24）

現状の要点だけ知りたい場合は [master20260824.md](./master20260824.md) を見れば十分。本書は経緯・判断理由の記録用（普段は読み込み不要）。

---

## Sunoプロンプト・Gemini画像プロンプト

原本は [prompts.md](./prompts.md)（Suno）／[gemini_prompts_copyready.md](./gemini_prompts_copyready.md)（Gemini、コピペ専用）を参照。全曲で据え置く語（アルゴリズム上の指紋）：
`warm` / `analog synth pads` / `glitch` / `nostalgic muted tone` / `understated and non-intrusive` / `no build-up` / `no climax` / `instrumental, no vocals, no singing, no lyrics`

歌詞欄：`[Instrumental]`のみ。UIのInstrumentalトグル：ON。長尺化：Extendで`[Intro]→[Development A]→[Subtle Variation]→[Sustain]→[Outro - slow fade]`。

---

## 1. Sunoからのダウンロード

Suno（`shimenawas`アカウント、`https://suno.com/me`）から#2〜#6をWAV形式でダウンロードし、`RouteNote/Level Trim/<曲名>/`配下に振り分け。

| 曲 | 取得テイク数 | 備考 |
|---|---|---|
| #2 Warm Cache | 2 | — |
| #3 Long Poll | 2 | — |
| #4 Thread Pool | 2 | 尺が短い（4:15/4:40）。Extend再生成を試みたが伸びず、断念してこの尺のまま採用 |
| #5 Backpressure | 2 | 初回確認時は1テイクしか見えなかったが、後から2テイク目が存在すると判明し追加取得 |
| #6 Hot Path | 2 | — |

ダウンロードは各テイクとも48kHz/16bit stereo WAV。ファイル名に`(take1)`/`(take2)`を付与して区別。

## 2. 2テイクの結合方針と手法

**背景**：同一プロンプトから生成された2テイクを、良い区間だけ組み合わせて1曲にしたいという要望。

**採用手法**：
1. 30秒（曲によっては60秒）単位のセグメントに分割
2. 各セグメントについて`ffmpeg -af volumedetect`で平均音量（mean_volume）を測定し、両テイクを比較
3. 音量差が明確な区間（目安1dB以上）だけ「静かな方」を採用。差が僅少な区間は前の選択を維持（頻繁な切り替えを避けるヒステリシス）。**当初は「密度が高い方」を採用していたが、設計思想（understated and non-intrusive）と逆行すると指摘され、2026-08-24に反転した（4章参照）**
4. 選んだブロックを`acrossfade`フィルタ（3〜5秒、triangularカーブ）で実際に音を重ねてブレンド。単純なフェードイン/アウト＋concatではテンポ・音量の継ぎ目が不自然になることが判明したため、この方式に変更（3章参照）
5. 最終ファイルは`-map_metadata -1`で"made with suno"の埋め込みメタデータを除去

**判明した限界**：
- 密度（音量）だけでは「良い区間」を判断できない場合がある（Long Poll・Hot Pathは差がノイズレベルで機械選択が機能せず、片方のテイクを単体採用）
- ボーカル・ハミングの混入は音量分析やスペクトログラム画像では検出できなかった。**実際に聴いたユーザーからの報告に依存**している
- クロスフェードのバイト比較検証は「意図した音源が使われているか」は確認できるが、**テイク間のキー/テンポ衝突は検証できない**（4章の指摘3、未解決）

## 3. 発生した問題と対応

**問題1：継ぎ目でテンポ・音量が急変する**
- 原因：初回は各セグメントを0.15秒の短いフェードで書き出してから単純concatしていたため、実質的に「フェードアウト→無音→フェードイン」に近く、テンポ/音量の断絶が聴感上目立った
- 対応：`acrossfade`フィルタで実際に2つの音声を重ねてクロスフェードする方式に変更

**問題2：Warm Cacheの後半にボーカル/ハミングが混入**
- take2の6:30以降にボーカルらしきものが混入していると報告があり、その区間をtake1に差し替えて再構築
- しかし差し替え後も「ボーカルが消えていない」との報告 → バイト単位のPCM比較で検証したところ、該当区間はtake1の音声と完全一致（差分0）と確認。**つまりtake1自体にも同じ区間にハミングが入っていた**
- 最終的にユーザーが実際に聴いて特定：**take1は5:30以降、take2は6:00以降にハミングあり**
- 対応：ハミング混入区間を除外して結合。最終的にInstrumentalとして扱う判断が確定（Instrumentalトグル ON）

**検証手法（バイト単位比較）**：音声を実際に聴けないため、「意図した音源に差し替わっているか」は以下の方法で数値的に検証した：
```bash
ffmpeg -ss <出力側の時刻> -t 3 -i "combined.wav" -f s16le -ar 48000 -ac 2 out.pcm
ffmpeg -ss <ソース側の対応時刻> -t 3 -i "take1.wav" -f s16le -ar 48000 -ac 2 src.pcm
cmp -l out.pcm src.pcm | wc -l   # 0なら完全一致
```

## 4. GitHubレビュー指摘と対応（2026-08-24）

GitHubリポジトリ `shimenawas-design/shimenawas2`（ブランチ`claude/new-session-8v0hvp`）の `docs/level-trim/review-2026-08-24.md` に、別セッションによる品質レビューが存在すると判明。指摘5項目すべてに対応した。

| # | 指摘 | 対応 |
|---|---|---|
| 1 | Warm Cacheのカット位置(6:00)がハミング開始点と一致していて精度不足 | take1側の使用終端を5:15に短縮（ハミング開始5:30まで15秒マージン）、末尾4秒フェードアウトを追加 |
| 2 | **選定基準が設計思想（understated and non-intrusive）と逆行**：「密度が高い方＝音量が大きい方」を機械選択で採用していた | **全曲、選定基準を「静かな方を優先」に反転して再構築**（2章参照） |
| 3 | クロスフェードはバイト比較で「意図した音源か」は検証できるが、テイク間のキー/テンポ衝突は未検証 | Thread Poolのクロスフェードを3秒→5秒に延長。**ただしキー/テンポの一致そのものはffmpegでは検証できず、実際に聴いての確認が引き続き必要**（未解決） |
| 4 | Thread Poolが4:31と短尺。3ヶ月の余裕があるためSunoでの再生成を推奨 | **アシスタントでは対応不可**（Suno生成はユーザー操作必須）。現状は継ぎ接ぎ版のまま。再生成するかは要判断 |
| 5 | 48kHz→44.1kHz変換時、リサンプラーが未指定（デフォルト＝低品質になりうる） | `-af aresample=resampler=soxr:precision=28` を明示して全曲再変換済み |

軽微な指摘（ファイル名の`#`使用、状態表記の不整合、ドキュメント二重管理）のうち、**ドキュメント二重管理**はgh CLI環境を整備し、GitHub側`master.md`をローカル版で上書きすることで解消済み（2026-08-24）。

## 5. 指摘3の解決：全曲リスニング確認（2026-08-24）

GitHub側に別セッションが用意した [listening-check.md](https://github.com/shimenawas-design/shimenawas2/blob/claude/new-session-8v0hvp/docs/level-trim/listening-check.md) の手順（継ぎ目位置の特定→3通りの聴き方→問題があれば段階的に対処）に沿って、ユーザーが全曲を実際に聴いて確認。**Thread Pool（継ぎ目3回、最優先対象）を含め、全曲問題なし。** review-2026-08-24.mdの指摘3を対応済みに更新し、GitHubへpush済み。
