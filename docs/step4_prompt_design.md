# ステップ4：画像生成用プロンプトの型（テンプレート）— v2

対象テスト案
- ターゲット界隈：推し活・現場通い界隈
- 絵柄：無感情な工業用オブジェクト（ボルト・歯車などの3DCG風）
- コンセプト：振り切れた推し活スラングを、無表情な工業部品に言わせる違和感とシュール

---

## 0. 大前提：文字はAIに描かせない（二層構造）

【厳守ルール：文字は上側】をAIの気分に委ねると必ず破綻する。理由は3つ。

1. **日本語が読める形で出ない。** MJ / SD は日本語をほぼ描けず、他エンジンでも「供給過多で死ぬ」級の長文はまず崩れる。
2. **文字位置が揺れる。** プロンプトで「上」と書いても、40枚の位置・サイズ・書体がバラバラになり、シリーズとしての統一感（＝購買の決め手）が壊れる。
3. **A/Bテストが回らない。** 後出しジャンケン制作法では、絵はそのままで文言だけ差し替えて反応を見たい。焼き込まれた文字は差し替えられない。

```
[層1] 画像生成AI  → 文字ゼロ・上部35%が空白のイラストのみを生成
[層2] 後工程      → 上部の空白に日本語テキストを合成（フォント・サイズ・縁取りを全40枚で共通化）
```

---

## 1. v1 の失敗ログ（テスト結果の記録）

Gemini で 05「喜んでATMになります」を3枚生成し、実測した結果は **不採用**。

v1 の MEDIUM / QUALITY ブロックはこう書いていた。

```
MEDIUM : 3DCG product render, industrial machine part photographed like a catalog product shot
QUALITY: physically based rendering, octane render, ultra detailed, 8k, sharp focus
```

AIはこれを正確に実行した。出てきたのは「工業製品のリアル写真」であり、指示通りである。
つまりこれは生成側の失敗ではなく、**型の設計ミス**。

| 観点 | 結果 | 内容 |
|---|---|---|
| 上部35%の確保 | △ | 3枚中2枚は25〜30%確保。構図ブロック自体は届いていた |
| 370×320での判別 | **×** | ホース・配管・ボルト頭が実寸で完全に潰れ、何の絵か分からない |
| 閉じたシルエット | **×** | 被写体がフレーム外へ続き、背景透過に必要な輪郭が存在しない |
| 背景の抜きやすさ | **×** | 背景も被写体も同じグレー。キーイング不可 |
| 一覧での識別性 | **×** | 全40枚が「灰色の金属」になり、サムネイル一覧で区別不能 |

**学び：スタンプにおける「高品質」とは、高精細のことではなく「縮小に耐えること」である。**
v2 では品質の定義そのものを差し替えた。

---

## 2. プロンプトの型：7固定 + 1可変

可変なのは `[SUBJECT]` のみ。残り6ブロックは40枚すべてで一字一句同じにする。

```
[1 MEDIUM]      + [2 SUBJECT(可変)] + [3 TONE] + [4 COMPOSITION]
+ [5 LIGHTING]  + [6 BACKGROUND]    + [7 QUALITY] + [8 PARAMETERS / NEGATIVE]
```

| # | ブロック | 役割 | v2での方針 |
|---|---|---|---|
| 1 | MEDIUM | 画風の支配権を最初に握る | **写実→スタイライズ3Dアイコンへ転換。** `simple stylized 3D icon, clean minimal 3D render of a vinyl toy miniature, chunky simplified geometry, bold readable silhouette, messenger sticker art` |
| 2 | **SUBJECT** | **★ここだけ40通り差し替える** | `data/stamps_40.json` |
| 3 | TONE | 無感情・無機質の担保 + 全面グレー回避 | 擬人化の全面禁止は維持。加えて `one single vivid orange accent color used sparingly on the focal point` で焦点色を1色だけ導入 |
| 4 | **COMPOSITION** | **★上部35%確保 + 閉じた輪郭** | `the entire object fits completely inside the frame with clear margin on every side, nothing is cropped and nothing touches the edges` を追加 |
| 5 | LIGHTING | 光を揃える | **被写界深度を捨てた。** 縮小時のボケは情報の損失にしかならない。`everything in sharp focus, no depth of field blur` |
| 6 | BACKGROUND | 透過に抜くため | グレー→**純白**。`no environment, no floor, no walls, no machinery behind` + `die cut sticker style` |
| 7 | QUALITY | 品質の定義 | `8k / octane render` を削除し、`instantly readable when shrunk down to 370x320 pixels, iconic and graphic` に置換 |
| 8 | NEGATIVE | 禁止事項 | `photorealistic / hoses / cropped object / gray background / tiny details / depth of field` などを追加 |

### 構図指示を効かせるコツ

画像生成AIは「上を空けて」を単発ではほぼ無視する。
**同じ命令を、視点を変えた4つの言い回しで重ねる。**

1. 被写体の位置で言う → `the object sits entirely in the lower two thirds of the frame`
2. 余白の量で言う → `wide empty headroom across the top 35 percent of the image`
3. 上部の中身で言う → `nothing at all in the upper area`
4. 用途を教える → `negative space above the subject reserved for a caption`

さらに `slightly low camera angle`（あおり）を加えると被写体が自然にフレーム下へ落ちる。
SDでは 2. に `(empty space at the top of the frame:1.4)` と強調重みを付ける。

### 「用途の宣言」が最大のレバー（Gemini系）

Gemini など指示追従型のエンジンでは、プロンプト冒頭で**用途を言い切る**のが最も効く。

```
This image is a sticker for a messaging app. It will be displayed at only 370x320 pixels,
so it must be extremely simple, bold and instantly readable at that tiny size.
It is NOT a photograph and NOT a realistic product render.
```

これを言わないと、AIは自分の知る「最も上手い絵」＝工業製品のリアル写真を作りに行く。

---

## 3. エンジン別の書き分け

| ファイル | エンジン | 形式 |
|---|---|---|
| `prompts/gemini.md` | Gemini | 用途宣言 + 命令文 + Absolute rules の箇条書き |
| `prompts/dalle3.md` | DALL-E 3 / GPT Image | 命令文。`Composition is critical:` で構図を格上げ |
| `prompts/midjourney.txt` | Midjourney | 1行カンマ区切り + `--ar 37:32 --style raw --v 7 --no ...` |
| `prompts/stable_diffusion.txt` | Stable Diffusion | Positive / Negative 分離 + 重み `(...:1.4)` |

Midjourney の `--style raw` は必須。付けないとMJが勝手に情緒的な演出を足し、無感情トンマナが崩れる。
絵柄を固めたい場合は、採用した1枚のURLを `--sref <URL>` で全40本に流し込む。

### ネガティブ語の例外処理

被写体そのものがネガティブ語と衝突する数枚だけ、`data/stamps_40.json` の
`negative_exceptions` / `allow_numbers` で該当語を外している。

| id | 文言 | 外した語 | 理由 |
|---|---|---|---|
| 02 | 全通します | cropped object 系 | チェーンが画面奥から手前へ続く構図が本質 |
| 03 | 供給過多で死ぬ | pipes in the background | パイプが主役 |
| 10 / 21 / 29 / 37 | 図面・計器系 | numbers | 寸法・目盛が主役 |
| 30 | 物販待機列 | cropped object 系 | 列が奥へ続く構図が本質 |
| 32 | 夜行バスで帰る | low contrast | 暗い車体が本質 |
| 40 | 今日も推しが〜 | factory environment | 現場の照明が本質 |

なお 32 / 40 は元設計が「風景」だったため、純白背景と両立するよう
**被写体をオブジェクト単体に描き直した**（台車単体 / 水銀灯単体）。

---

## 4. LINEスタンプ規格との対応

| 用途 | サイズ (px) | アスペクト | 備考 |
|---|---|---|---|
| スタンプ | 370 × 320 | `--ar 37:32` | 40個 |
| メイン画像 | 240 × 240 | `--ar 1:1` | 正方形なので上部余白は35%→30%に縮める |
| タブ画像 | 96 × 74 | `--ar 48:37` | 文字なし。最もシンプルな1点（`01. 実質無料`）を使う |

全ファイル PNG・背景透過・1個あたり 1MB 以下。上下左右に10px程度の余白を残す。

---

## 5. 採否の判定手順（毎回これで測る）

主観で「良い/悪い」を決めない。以下を実測する。

1. 生成画像を **370×320 px に縮小**して見る。ここで何の絵か分からなければ即不採用。
2. 96×74（タブサイズ）まで縮めて、**シルエットだけで**区別がつくか。
3. 白背景・濃色背景の両方に置いて、沈まないか。
4. 上部35%に文字帯を仮置きして、被写体と干渉しないか。
5. 候補を5枚並べて、**一覧で区別がつくか**。これが最終関門。

---

## 6. 後工程（層2）で守ること

- 文字は**上部35%の帯の中に必ず収める**。40番「今日も推しが生きていることに感謝」は2行組み。
  はみ出す場合は文字を小さくせず、**帯を40%に広げて再生成**する（視認性優先）。
- 書体は全40枚共通。白フチ2〜3px + わずかなドロップシャドウで、どの背景色のトーク画面でも読めるようにする。
- 背景透過は、純白背景をキーイングで抜く。ブロック6を固定しているのはこの処理を40枚で同一設定にするため。

---

## 7. 使い方

```bash
python3 scripts/build_prompts.py
# -> prompts/gemini.md / dalle3.md / midjourney.txt / stable_diffusion.txt / main_and_tab.md
```

文言や被写体を変えたいときは `data/stamps_40.json` を編集して再実行する。
テスト案（絵柄）ごと差し替える場合は `scripts/build_prompts.py` の `MEDIUM` / `TONE` だけを
書き換えれば、40枚が丸ごと別の絵柄に移行できる。
