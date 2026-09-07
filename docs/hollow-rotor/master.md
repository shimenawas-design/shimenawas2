# Hollow Rotor マスタードキュメント

**作成日：2026-09-07**（現状の状態のみを載せた軽量版）
関連：[../policy.md](../policy.md)（規約・配信先、全プロジェクト共通）／[prompts.md](./prompts.md)（Suno・Gemini両方のプロンプト原本）

---

## 1. プロジェクト概要

| 項目 | 値 |
|---|---|
| アーティスト名義 | `Hollow Rotor` |
| 用途 | ジム・ワークアウト向け高強度BGM（ドリフト・ゲーム編集用途も想定） |
| ジャンル | Phonk（Drift/Gym Phonk系統）、インストゥルメンタル限定 |
| ディストリビューター | RouteNote（Level Trim・Ongaku Toshokan・Vermilion Gateと同一アカウント、名義のみ分離） |
| C/Pライン | 本名（川上悟志 / Satoshi Kawakami、他プロジェクトと共通） |
| 命名由来 | 「空虚さ(Hollow)」+「エンジンの機械部品(Rotor)」。Phonkの反復的・催眠的な質感との対応を意図 |

「チャート逆算」手法（プラットフォーム分析→要素分解→プロンプト構築→試聴→最終チェック→配信）の、既存ジャンル拡張ではなく**新ジャンル立ち上げへの初適用**として設計。Level Trimと違い、既存カタログの保護が不要なためSTEP1のジャンル探索を制約なく実施した。

## 2. STEP1-2 調査結果サマリ

- **ジャンル**: Phonk（2026年時点で「Phonk」と言うとほぼこれを指すDrift/Gym Phonk系統）
- **BPM**: 130〜160。ジム/ワークアウト用途は140〜160が最適
- **楽器・音色**: カウベル（最重要の識別音）／歪んで唸るピッチダウン808ベース／パンチの効いたキック・シャープなスネア・busy hi-hatロール／ローファイなカセット・ヴァイナル質感（クリッピング・歪みは意図的な仕様）
- **ムード**: Dark, aggressive, hypnotic, relentless（反復的で執拗なエネルギー）
- **ボーカル方針**: インスト（ボーカルなし）版の需要が明確に存在することを確認済み。ボーカルAIのvoice cloningリスクを回避できるジャンル選択（Vermilion Gateのヴォカリーズ許容方針とは対照的に、こちらは完全排除の方針）
- **需要の裏付け**: Spotifyプレイリスト「GYM PHONK 2026」（Magic Records）が287曲・180万セーブ（実測エンゲージメント数値）

## 3. 名義選定の経緯

1. 「空虚さ+エンジン機械音」の方向で10案作成 → 第一候補「Hollow Engine」
2. 「Hollow Engine」はSpotify/Bandcamp/Facebookに実在するNY拠点の活動中バンド（EP・複数アルバムをリリース済み）と重複することが判明し却下
3. 同コンセプトで追加5案から「Hollow Rotor」を選定。Spotify/Apple Music/Bandcamp/Wikipedia検索で完全一致する既存アーティスト・バンド・アルバムなし（確認日: 2026-09-05、Web検索経由の間接確認）

**⚠️ 未実施**: RouteNote登録の直前に、Spotify/Apple Musicで直接検索する一次確認をもう一度行うこと。

## 4. 曲一覧・現在の状態（2026-09-07時点）

| # | 曲名 | BPM | 音源 | 画像 | 状態 |
|---|---|---|---|---|---|
| 1 | Torque Lock | 150 | `.flac`変換済み（44.1kHz、`-map_metadata -1`でSuno埋め込みメタデータ削除済み） | `jacket.png`（3000×3000リサイズ済み、Gemini透かし除去済み） | リスニング確認OK（①〜④全項目クリア、2026-09-07） |

## 5. Suno生成で確定した既知のクセ（再発防止・汎用知見）

**「no vocals」だけではワードレス・ボーカライズ（ハミング/オーオー系）を防げない。** Instrumentalトグル ON + 徹底した否定プロンプト（`no vocals, no humming, no oohs, no ahs, no wordless vocals, no vocal chops, no vocal ad-libs, no choir`）を両方使ってもTrack #1初回生成では声が残った。

**確定した原因**: `phonk`というジャンル名の単語自体が、メンフィス・ラップ由来のボーカル方向への強いバイアスを学習データに持っており、トグルや否定プロンプトを上書きしていた。**ジャンル名を完全に外し、音の特徴だけで記述したところ声が消えることを確認済み**（詳細は[prompts.md](./prompts.md)）。

この教訓は汎用化できる：今後別ジャンルでも、トグルON+否定プロンプトで声が消えない場合は、まずジャンル名の単語自体を外してみる。

## 6. 残タスク（優先順）

1. **名義の重複最終確認**（RouteNote登録直前にSpotify/Apple Musicで直接検索）
2. **RouteNoteでの名義登録**（他3プロジェクトと同一アカウント、名義のみ分離）
3. Track #2以降の設計（[prompts.md](./prompts.md)の確定版テンプレートをベースにBPM/テクスチャのみ変える、1曲=1変数ルール）

## 7. ファイル配置

ドキュメントは**リポジトリの `docs/` が唯一の正**（リポジトリ直下の `CLAUDE.md` 参照）。音源・画像は `.gitignore` 対象でローカルにのみ存在する。

```
RouteNote/                      ← ここでgit管理
├── CLAUDE.md
├── docs/hollow-rotor/          ← ドキュメントはすべてここ
└── Hollow Rotor/                ← .gitignore対象
    └── 01_Torque Lock/          (take1).wav / .flac / jacket_raw.png / jacket_clean_1024.png / jacket.png
```
