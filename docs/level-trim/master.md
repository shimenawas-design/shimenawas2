# Level Trim マスタードキュメント

**作成日：2026-08-24**（現状の状態のみを載せた軽量版。経緯・判断理由は [changelog.md](./changelog.md) 参照）
関連：[../policy.md](../policy.md)（規約・配信先）／[prompts.md](./prompts.md)（Sunoプロンプト原本）（Geminiプロンプトも同ファイル）

---

## 1. プロジェクト概要

| 項目 | 値 |
|---|---|
| アーティスト名義 | `Level Trim` |
| 用途 | エンジニアの作業用集中BGM（プログラミング・CAD・報告書作成） |
| ジャンル | Electronic / IDM（ウォーム・グリッチ寄り） |
| ディストリビューター | RouteNote（Ongaku Toshokanと同一アカウント、名義のみ分離） |
| 曲構成 | 6曲、BPMを62〜100で梯子状に配置。各曲「動かす変数」を1つだけ割り当てる設計 |

配信戦略・規約確認は [../policy.md](../policy.md)、リリースカレンダーは [../ongaku-toshokan/master.md](../ongaku-toshokan/master.md) を参照。

## 2. 曲一覧・現在の状態（2026-09-19更新）

| # | 曲名 | BPM | 最終尺 | 音源 | 画像 | 状態 |
|---|---|---|---|---|---|---|
| 1 | Idle Loop | 70 | — | — | — | **審査中**（リリース日 9/6） |
| 2 | Warm Cache | 82 | 5:12 | `.flac`変換済み | 3000×3000済み | **審査中**（入稿 8/29） |
| 3 | Long Poll | 62 | 7:59 | `.flac`変換済み | 3000×3000済み | **審査中**（入稿 9/12） |
| 4 | Thread Pool | 90 | 4:30 | `.flac`変換済み | 3000×3000済み | リスニング確認OK・**再生成しない（2026-09-20決定）**。12月分として入稿予定 |
| 5 | Backpressure | 76 | 7:53 | `.flac`変換済み | 3000×3000済み（2026-09-08） | **入稿完了・審査中**（2026-09-19、UPC 5064140279851、Sales Start Date 2026-11-21） |
| 6 | Hot Path | 100 | 7:59 | `.flac`変換済み | 3000×3000済み（2026-09-08） | **入稿完了・審査中**（2026-09-19、UPC 5064140790288、Sales Start Date 2026-11-28） |

音源はすべて2テイクを組み合わせ／選定して作成（`#<番号> <曲名> (combined).wav`＝48kHz、`#<番号> <曲名>.flac`＝44.1kHz入稿用）。組み合わせ方の詳細・変更履歴は [changelog.md](./changelog.md) を参照。

**UPC（審査中の3曲、2026-09-12 RouteNote画面で確認）**：Idle Loop = 5064115821122／Warm Cache = 5064115892511／Long Poll = 5064140758363

Long Pollの入稿ではジャケットが当初PNGでリジェクトされ、JPGに変換して再アップロードして解決（アートワーク仕様はJPG必須の可能性あり、他曲の入稿時も要注意）。YouTube Content IDのチェックは外して入稿済み。

## 3. 残タスク（優先順）

1. ~~ジャケット画像を3000×3000にリサイズ~~ → **全6曲完了（2026-09-08）**
2. ~~Thread Poolを再生成するか判断~~ → **再生成しない（2026-09-20決定）**。4:30のまま12月分として入稿する
3. RouteNoteへの入稿（[../policy.md](../policy.md)のチェックリスト参照）。**Backpressure・Hot Pathは2026-09-19に入稿完了**。残りはThread Poolのみ

4. **次バッチ（#7〜）の方向性**：[market-research-2026-08.md](./market-research-2026-08.md) 4章の候補②「マカーム旋法×ウォームIDM」に決定（2026-09-20、設計中）。ブラウンノイズ層（候補③）は#2 Warm Cacheで実施済み。

全曲リスニング確認済み（2026-08-24、問題なし）。

### 3.1 入稿スケジュール（2026-09-17決定：入稿はまとめて、公開日だけ分散）

在庫解消のため、Backpressure・Hot Pathは**2026-09-19に入稿済み**（Sales Start Dateを指定。公開ペースは従来の週2〜3件を維持）（[../policy.md](../policy.md) 5章、[routenote-release スキル](../../.claude/skills/routenote-release/SKILL.md)参照）。

| # | 曲名 | Sales Start Date（公開予定） | 入稿 |
|---|---|---|---|
| 5 | Backpressure | 2026-11-21 | 2026-09-19完了 |
| 6 | Hot Path | 2026-11-28 | 2026-09-19完了 |

Thread Poolは再生成しないと決定（2026-09-20）。12月分として追加する（Sales Start Dateは入稿時に決定）。

## 4. ファイル配置

ドキュメントは**リポジトリの `docs/` が唯一の正**（リポジトリ直下の `CLAUDE.md` 参照）。音源・画像は `.gitignore` 対象でローカルにのみ存在する。

```
RouteNote/                     ← ここでgit管理
├── CLAUDE.md
├── docs/level-trim/           ← ドキュメントはすべてここ
└── Level Trim/                ← .gitignore対象
    ├── 済/01_Idle Loop/       リリース済み（アーカイブ）
    ├── 済/02_Warm Cache/      アーカイブ（jacket3000×3000済み）
    ├── 03_Long Poll/          （combined).wav / .flac / jacket.png=3000×3000済み
    ├── 04_Thread Pool/        同様の構成（jacket (alt).pngあり／jacket.png=3000×3000済み）
    ├── 05_Backpressure/       同様の構成（jacket.png=3000×3000済み）
    └── 06_Hot Path/           同様の構成（jacket.png=3000×3000済み）
```
