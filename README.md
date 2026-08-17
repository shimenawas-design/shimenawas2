# shimenawas2

データドリブンなLINEスタンプ制作（後出しジャンケン制作法）のワークスペース。

## 現在のテスト案

| 項目 | 内容 |
|---|---|
| ターゲット界隈 | 推し活・現場通い界隈（全通、実質無料などのスラングを日常使用する層） |
| キャラクターデザイン | 無感情な工業用オブジェクト（ボルト、歯車などの3DCG風） |
| コンセプト | 振り切れた推し活スラングを、無表情・無機質な工業部品に言わせる違和感とシュールな笑い |
| レイアウト厳守ルール | テキストは必ず**上側**、イラストは下側 |

## 進行状況

- [x] ステップ1〜3：市場調査 / 生データ抽出 / スタンプ設計図40個
- [x] ステップ4：画像生成用プロンプトの型を構築 → `docs/step4_prompt_design.md`
- [x] ステップ4.1：v1をGeminiで実測 → 写実的すぎて不採用。型をv2（スタイライズ3Dアイコン）へ改訂
- [x] ステップ4.2：v2を01番で実測 → 技術要件は全通過も「アイコン止まり」。STAGINGブロックを新設しv3へ
- [ ] ステップ5：画像生成 → 背景透過 → テキスト合成
- [ ] ステップ6：LINE Creators Market 申請

## ファイル構成

```
data/stamps_40.json          40個の設計図（日本語文言 + 英語SUBJECT）
scripts/build_prompts.py     設計図からプロンプトを組み立てる
prompts/gemini.md            Gemini用 40本
prompts/midjourney.txt       Midjourney用 40本
prompts/dalle3.md            DALL-E 3 / GPT Image用 40本
prompts/stable_diffusion.txt Stable Diffusion用 40本（Positive/Negative分離）
prompts/main_and_tab.md      メイン画像(240x240) / タブ画像(96x74)用
docs/step4_prompt_design.md  プロンプトの型の設計思想と運用ルール
```

## 再生成

```bash
python3 scripts/build_prompts.py
```

`data/stamps_40.json` を編集して再実行すれば、4エンジン分のプロンプトが更新される。
