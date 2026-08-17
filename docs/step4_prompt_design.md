# ステップ4：画像生成用プロンプトの型（テンプレート）

対象テスト案
- ターゲット界隈：推し活・現場通い界隈
- 絵柄：無感情な工業用オブジェクト（ボルト・歯車などの3DCG風）
- コンセプト：振り切れた推し活スラングを、無表情な工業部品に言わせる違和感とシュール

---

## 0. 大前提：文字はAIに描かせない（二層構造）

【厳守ルール：文字は上側】をAIの気分に委ねると必ず破綻する。理由は3つ。

1. **日本語が読める形で出ない。** MJ / SD は日本語をほぼ描けず、DALL-E 3 も40枚のうち安定して読めるのは体感で数枚。「供給過多で死ぬ」のような長文はまず崩れる。
2. **文字位置が揺れる。** プロンプトで「上」と書いても、40枚の位置・サイズ・書体がバラバラになり、シリーズとしての統一感（＝購買の決め手）が壊れる。
3. **A/Bテストが回らない。** 後出しジャンケン制作法では、絵はそのままで文言だけ差し替えて反応を見たい。焼き込まれた文字は差し替えられない。

したがって本プロジェクトのパイプラインは以下で固定する。

```
[層1] 画像生成AI  → 文字ゼロ・上部35%が空白のイラストのみを生成
[層2] 後工程      → 上部の空白に日本語テキストを合成（フォント・サイズ・縁取りを全40枚で共通化）
```

プロンプト側の役割は「**上部35%を確実に空けさせること**」であり、
【厳守ルール】は層1の構図指示 + 層2の合成座標という二重で担保する。

---

## 1. プロンプトの型：7固定 + 1可変

可変なのは `[SUBJECT]` のみ。残り6ブロックは40枚すべてで一字一句同じにする。
これが「絵柄のブレを構造的に潰す」唯一の方法。

```
[1 MEDIUM]      + [2 SUBJECT(可変)] + [3 TONE] + [4 COMPOSITION]
+ [5 LIGHTING]  + [6 BACKGROUND]    + [7 QUALITY] + [8 PARAMETERS / NEGATIVE]
```

| # | ブロック | 役割 | 中身（固定） |
|---|---|---|---|
| 1 | MEDIUM | 画風の支配権を最初に握る | `3DCG product render, industrial machine part photographed like a catalog product shot` |
| 2 | **SUBJECT** | **★ここだけ40通り差し替える** | 設計図の英訳（`data/stamps_40.json`） |
| 3 | TONE | 無感情・無機質の担保。擬人化を全力で禁止 | `cold emotionless inorganic object, absolutely no face and no eyes, not anthropomorphized, not a mascot, deadpan and lifeless, machined steel and matte aluminum, brushed metal surfaces, subtle scratches and machining marks` |
| 4 | **COMPOSITION** | **★【厳守ルール】上部35%の確保** | `the object sits entirely in the lower two thirds of the frame, wide empty headroom across the top 35 percent of the image, nothing at all in the upper area, generous negative space above the subject reserved for a caption, centered horizontally, slightly low camera angle looking at the object` |
| 5 | LIGHTING | 40枚の光を揃える | `soft large softbox studio lighting, gentle rim light, crisp contact shadow, shallow depth of field` |
| 6 | BACKGROUND | 後工程で透過に抜くためフラット無地 | `plain flat seamless light gray studio background, clean and empty, subject clearly isolated from the background` |
| 7 | QUALITY | 質感 | `physically based rendering, octane render, ultra detailed, 8k, sharp focus` |
| 8 | PARAMETERS / NEGATIVE | 比率と禁止事項 | `--ar 37:32 --style raw --v 7 --no text, letters, words, ...` |

### ブロック4が効く理由（構図指示のコツ）

画像生成AIは「上を空けて」という一言をほぼ無視する。効かせるには
**同じ命令を、視点を変えた3つの言い回しで重ねる**。

1. 被写体の位置で言う → `the object sits entirely in the lower two thirds of the frame`
2. 余白の量で言う → `wide empty headroom across the top 35 percent of the image`
3. 上部の中身で言う → `nothing at all in the upper area`
4. 用途を教える → `negative space above the subject reserved for a caption`

さらに `slightly low camera angle`（あおり）を加えると、被写体が自然にフレーム下側へ落ち、
上部の抜けが安定する。SDでは 3.の要素に `(empty space at the top of the frame:1.4)` と
強調重みを付ける。

---

## 2. エンジン別の書き分け

### Midjourney（`prompts/midjourney.txt`）
- 1行のカンマ区切り。`--ar 37:32`（= 370×320）。
- `--style raw` は必須。付けないとMJが勝手に「エモい」演出を足し、無感情トンマナが崩れる。
- `--no` に禁止語をまとめる。
- 40枚の絵柄をさらに固める場合：まず1枚（推奨は `08. 尊い…`）を確定させ、
  その画像URLを全プロンプト先頭に置いて `--sref <URL>` でスタイル参照を固定する。

### DALL-E 3 / GPT Image（`prompts/dalle3.md`）
- 単語羅列より**命令文**が通る。`Create a ...` から始め、構図は
  `Composition is critical:` と明示的に格上げする。
- プロンプトを勝手に書き換える性質があるため、末尾に
  `Do not render any text, letters, words or logos anywhere in the image.` を必ず付ける。

### Stable Diffusion（`prompts/stable_diffusion.txt`）
- Positive / Negative を分離。重み `(...:1.4)` で構図を強制。
- 生成は 768×664（37:32）で行い、最後に 370×320 へ縮小する。

---

## 3. LINEスタンプ規格との対応

| 用途 | サイズ (px) | アスペクト | 備考 |
|---|---|---|---|
| スタンプ | 370 × 320 | `--ar 37:32` | 40個 |
| メイン画像 | 240 × 240 | `--ar 1:1` | 正方形なので上部余白は35%→30%に縮める |
| タブ画像 | 96 × 74 | `--ar 48:37` | 文字なし。縮小に耐えるシンプルな1点（`01. 実質無料`）を使う |

- 全ファイル PNG・背景透過・1個あたり 1MB 以下。
- 余白：上下左右に10px程度の余白を残す（LINEの審査基準）。

メイン画像・タブ画像のプロンプトは `prompts/main_and_tab.md`。

---

## 4. 後工程（層2）で守ること

- 文字は**上部35%の帯の中に必ず収める**。設計図の文言が長い40番
  「今日も推しが生きていることに感謝」は2行組みにし、帯からはみ出す場合は
  文字サイズではなく**帯を40%に広げて再生成**する（文字を小さくしない＝トーク画面での視認性優先）。
- 書体は全40枚共通。工業っぽさを出すならゴシック体＋等幅寄り、
  白フチ（2〜3px）＋わずかなドロップシャドウで、どの背景色のトーク画面でも読めるようにする。
- 背景透過は、生成時のフラットグレー背景をキーイングで抜く。
  ブロック6を固定しているのは、この抜き処理を40枚で同一設定にするため。

---

## 5. 使い方

```bash
python3 scripts/build_prompts.py
# -> prompts/midjourney.txt / dalle3.md / stable_diffusion.txt / main_and_tab.md
```

文言や被写体を変えたいときは `data/stamps_40.json` の `jp_text` / `subject_en` を編集して
再実行する。テスト案（絵柄）ごと差し替える場合は `scripts/build_prompts.py` の
`MEDIUM` / `TONE` だけを書き換えれば、40枚が丸ごと別の絵柄に移行できる。
