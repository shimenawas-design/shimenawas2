# shimenawas2 — LINEスタンプ制作（後出しジャンケン制作法）

作り手の主観を捨て、「キャラクターデザイン（絵柄）× ニッチ市場」の組み合わせ自体を
市場テストして、売れるスタンプを発掘・資産化するためのワークスペース。

**このリポジトリは作業用**（プロンプト生成・画像処理・出品実務）。
戦略判断・市場分析・販売データの解釈は別チャットで行う。

## 厳守ルール

**スタンプ内のテキストは画像の下側ではなく「上側」に配置する。** この前提で構図を設計する。

## 現在のテスト：A案「シフトうさぎ」

| 項目 | 内容 |
|---|---|
| ターゲット | 介護施設の夜勤スタッフ（特養・老健・グループホーム） |
| 絵柄 | ゆるかわ系だが目が完全に死んでいる3頭身の白ウサギ |
| タイトル | `介護士の夜勤うさぎ【目が死んでる】` |
| 価格 | 120円固定 |

詳細は `docs/A_shift-usagi_spec.md`、判定ラインは `docs/test_design.md`。

## 進捗

| 項目 | 状態 |
|---|---|
| 3案の策定・生データ抽出 | 完了 |
| A案の40個設計図（セリフ・構図・表情） | 完了 |
| 画像生成プロンプト40本 | 完了 |
| ストア情報・タグ40個分 | 完了 |
| 判定ライン設計 | 完了 |
| 文字入れレイアウト・スクリプト（`compose.py`） | **収録済み**（フチ描画をPIL標準の`stroke_width`から距離変換方式に変更し、複雑な漢字内の黒抜け・ジャギーを解消） |
| **Geminiでの画像生成** | **完了**（40枚。`raw/`はリポジトリ未収録、ローカルのみ） |
| 合成・文字入れ | **完了**（`out/`にmain.png/tab.png/コンタクトシート含め40枚。リポジトリ未収録、ローカルのみ） |
| 出品 | LINE Creators Marketへの入力作業中（タイトル・説明文・タグ等は確定済み） |
| 次の界隈候補の追加調査 | 完了。`docs/next_niche_candidates_260915.md` 参照 |

## ファイル構成

```
data/stamps_40.json           40個の単一の真実（セリフ・改行・ACTION・EXPRESSION・タグ）
scripts/build_prompts.py      BASE + 差分 → prompts/ を生成
prompts/_base.md              BASE / NEGATIVE（コピペ用・生成物）
prompts/gemini_40.md          完成プロンプト40本（生成物）
prompts/texts_40.md           テキスト一覧 + 1行9文字以内の検証（生成物）
prompts/tags_40.md            タグ一覧40個分（生成物）
compose.py                    生画像 → 背景透過 → 文字入れ → LINE規定サイズ書き出し
docs/A_shift-usagi_spec.md    A案の全仕様
docs/test_design.md           3案の位置づけ・合否判定ライン・禁止事項
docs/next_niche_candidates_260915.md
                               後出しジャンケン制作法の次の界隈候補（NotebookLM横断調査）
```

`compose.py` はリポジトリと同じ階層に `raw/`（生画像）・`out/`（出力）・`fonts/ZenMaruGothic-Bold.ttf`
（Zen Maru Gothic、SIL OFLライセンス）を置いて実行する。`raw/`・`out/`・フォントは容量の関係でリポジトリには含めていない。

```bash
python compose.py --only 30   # 1枚だけ確認
python compose.py             # raw/ を全部読んで out/ に一括書き出し
```

`prompts/` は生成物なので手で編集しない。`data/stamps_40.json` を編集して再生成する。

## 再生成

```bash
python3 scripts/build_prompts.py
```

セリフの追加・差し替え・改行位置の変更は `data/stamps_40.json` を編集して再実行する。
1行9文字を超えた項目は `prompts/texts_40.md` の末尾に列挙される。
