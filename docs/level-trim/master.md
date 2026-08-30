# Level Trim マスタードキュメント

**作成日：2026-08-24**（現状の状態のみを載せた軽量版。経緯・判断理由は [changelog20260824.md](./changelog20260824.md) 参照）
関連：[handoff20260823.md](./handoff20260823.md)（配信戦略・規約確認）／[prompts.md](./prompts.md)（Sunoプロンプト原本）／[gemini_prompts_copyready.md](./gemini_prompts_copyready.md)（Geminiプロンプト、コピペ専用）

---

## 1. プロジェクト概要

| 項目 | 値 |
|---|---|
| アーティスト名義 | `Level Trim` |
| 用途 | エンジニアの作業用集中BGM（プログラミング・CAD・報告書作成） |
| ジャンル | Electronic / IDM（ウォーム・グリッチ寄り） |
| ディストリビューター | RouteNote（Ongaku Toshokanと同一アカウント、名義のみ分離） |
| 曲構成 | 6曲、BPMを62〜100で梯子状に配置。各曲「動かす変数」を1つだけ割り当てる設計 |

詳しい配信戦略・規約確認・リリースカレンダーは [handoff20260823.md](./handoff20260823.md) を参照。

## 2. 曲一覧・現在の状態（2026-08-24時点）

| # | 曲名 | BPM | 最終尺 | 音源 | 画像 | 状態 |
|---|---|---|---|---|---|---|
| 1 | Idle Loop | 70 | — | — | — | リリース済み・審査中（9/6） |
| 2 | Warm Cache | 82 | 5:12 | `.flac`変換済み | jacket.png（Canvaリサイズ待ち） | **入稿済み（8/29）** |
| 3 | Long Poll | 62 | 7:59 | `.flac`変換済み | jacket.png（Canvaリサイズ待ち） | リスニング確認OK |
| 4 | Thread Pool | 90 | 4:30 | `.flac`変換済み | jacket.png（Canvaリサイズ待ち） | リスニング確認OK・再生成要否は未決定 |
| 5 | Backpressure | 76 | 7:53 | `.flac`変換済み | jacket.png（Canvaリサイズ待ち） | リスニング確認OK |
| 6 | Hot Path | 100 | 7:59 | `.flac`変換済み | jacket.png（Canvaリサイズ待ち） | リスニング確認OK |

音源はすべて2テイクを組み合わせ／選定して作成（`#<番号> <曲名> (combined).wav`＝48kHz、`#<番号> <曲名>.flac`＝44.1kHz入稿用）。組み合わせ方の詳細・変更履歴は [changelog20260824.md](./changelog20260824.md) を参照。

## 3. 残タスク（優先順）

1. **ジャケット画像5枚をCanvaで3000×3000にリサイズ**（画像自体は#2〜#6すべて生成・振り分け済み）
2. **Thread Poolを再生成するか判断**（4:30と短尺。3ヶ月の余裕があるため再生成も選択肢）
3. RouteNoteへの入稿（[handoff20260823.md](./handoff20260823.md)のチェックリスト参照）

全曲リスニング確認済み（2026-08-24、問題なし）。

## 4. ファイル配置

```
RouteNote/Level Trim/
├── master20260824.md            本書（現状のみ）
├── changelog20260824.md         経緯・判断理由の詳細ログ
├── handoff20260823.md           配信戦略・規約確認
├── prompts.md                   Sunoプロンプト原本（#1〜#6）
├── gemini_prompts_copyready.md  Geminiプロンプト（コピペ専用）
├── 01_Idle Loop/                 リリース済み
├── 02_Warm Cache/                (take1).wav / (take2).wav / (combined).wav / .flac / jacket.png
├── 03_Long Poll/                 同様の構成
├── 04_Thread Pool/                同様の構成（jacket (alt).pngあり）
├── 05_Backpressure/               同様の構成
└── 06_Hot Path/                  同様の構成
```
