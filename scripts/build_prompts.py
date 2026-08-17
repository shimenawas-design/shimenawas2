#!/usr/bin/env python3
"""ステップ4: 40個の設計図から、画像生成AI用プロンプトを機械的に組み立てる。

プロンプトは 7 レイヤーの固定ブロック + 1 レイヤーの可変ブロックで構成する。
可変なのは [SUBJECT] のみ。他の 6 ブロックは 40 枚すべてで完全固定にすることで、
絵柄のブレ（＝トンマナ崩壊）を構造的に潰す。

    python3 scripts/build_prompts.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "stamps_40.json"
OUT = ROOT / "prompts"

# ---------------------------------------------------------------------------
# 固定ブロック（40枚共通・絶対に変更しない）
# ---------------------------------------------------------------------------

# [1] MEDIUM: 3DCGレンダーであることを最初に宣言する（画風の支配力が最も強い位置）
MEDIUM = (
    "3DCG product render, industrial machine part photographed like a catalog product shot"
)

# [2] TONE: 「無感情・無機質」を担保する。擬人化を全力で禁止する。
TONE = (
    "cold emotionless inorganic object, absolutely no face and no eyes, "
    "not anthropomorphized, not a mascot, deadpan and lifeless, "
    "machined steel and matte aluminum, brushed metal surfaces, subtle scratches and machining marks"
)

# [3] COMPOSITION: 【厳守ルール】テキストを上に置くため、上部35%を強制的に空ける。
#     同じ意味の指示を 3 通りの言い回しで重ねるのが、構図指示を効かせる最大のコツ。
COMPOSITION = (
    "the object sits entirely in the lower two thirds of the frame, "
    "wide empty headroom across the top 35 percent of the image, "
    "nothing at all in the upper area, generous negative space above the subject reserved for a caption, "
    "centered horizontally, slightly low camera angle looking at the object"
)

# [4] LIGHTING
LIGHTING = (
    "soft large softbox studio lighting, gentle rim light, crisp contact shadow, "
    "shallow depth of field"
)

# [5] BACKGROUND: 後工程で透過PNGに抜くため、フラットな無地に固定する。
BACKGROUND = (
    "plain flat seamless light gray studio background, clean and empty, "
    "subject clearly isolated from the background"
)

# [6] QUALITY
QUALITY = "physically based rendering, octane render, ultra detailed, 8k, sharp focus"

# [7] NEGATIVE: 文字は後から合成するので、AIには一切描かせない。
NEGATIVE = [
    "text", "letters", "words", "captions", "watermark", "signature", "logo",
    "numbers",
    "human", "person", "face", "eyes", "mouth", "hands",
    "cute character", "mascot", "anime", "illustration", "2d",
    "cluttered background", "busy background", "props", "multiple panels",
    "border", "frame", "vignette",
]

# LINEスタンプ規格（W x H）
SPEC = {
    "stamp": (370, 320),
    "main": (240, 240),
    "tab": (96, 74),
}


def negatives_for(stamp: dict) -> list[str]:
    """図面系など、数字が画に必要な数枚だけ numbers をネガティブから外す。"""
    neg = list(NEGATIVE)
    if stamp.get("allow_numbers"):
        neg.remove("numbers")
    return neg


def core(stamp: dict) -> str:
    """可変ブロック [SUBJECT] を固定ブロックで挟んだ本体。"""
    return ", ".join(
        [MEDIUM, stamp["subject_en"], TONE, COMPOSITION, LIGHTING, BACKGROUND, QUALITY]
    )


def midjourney(stamp: dict, ar: str = "37:32") -> str:
    return f"{core(stamp)} --ar {ar} --style raw --v 7 --no {', '.join(negatives_for(stamp))}"


def stable_diffusion(stamp: dict) -> str:
    pos = f"{core(stamp)}, (empty space at the top of the frame:1.4), (subject in lower half:1.3)"
    neg = ", ".join(negatives_for(stamp) + ["lowres", "jpeg artifacts", "blurry", "extra objects"])
    return f"Positive: {pos}\nNegative: {neg}\nSize: 768x664 (=370x320 と同じ 37:32。生成後に縮小)"


def dalle3(stamp: dict) -> str:
    """DALL-E 3 / GPT Image は命令文のほうが通る。禁止事項を文で明示する。"""
    return (
        f"Create a {MEDIUM} of {stamp['subject_en']}. "
        f"Art direction: {TONE}. "
        f"Composition is critical: {COMPOSITION}. "
        f"Lighting: {LIGHTING}. Background: {BACKGROUND}. Quality: {QUALITY}. "
        "Do not render any text, letters, words or logos anywhere in the image. "
        "Do not add a border or frame. Aspect ratio 37:32 (wide)."
    )


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    stamps = data["stamps"]
    OUT.mkdir(exist_ok=True)

    header = (
        f"# {data['project']}\n"
        f"# 絵柄: {data['art_direction']}\n"
        f"# レイアウト: {data['layout_rule']}\n"
        f"# 出力: {SPEC['stamp'][0]}x{SPEC['stamp'][1]} px / 透過PNG / 文字は後工程で上部に合成\n"
    )

    # --- Midjourney -------------------------------------------------------
    lines = [header]
    for s in stamps:
        lines.append(f"\n# --- {s['id']:02d}. {s['jp_text']}  ({s['concept_ja']})")
        lines.append(midjourney(s))
    (OUT / "midjourney.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # --- Stable Diffusion -------------------------------------------------
    lines = [header]
    for s in stamps:
        lines.append(f"\n# --- {s['id']:02d}. {s['jp_text']}  ({s['concept_ja']})")
        lines.append(stable_diffusion(s))
    (OUT / "stable_diffusion.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # --- DALL-E 3 ---------------------------------------------------------
    lines = [f"# DALL-E 3 / GPT Image 用プロンプト（{data['project']}）\n"]
    for s in stamps:
        lines.append(f"\n## {s['id']:02d}. {s['jp_text']}\n\n> {s['concept_ja']}\n")
        lines.append(f"```\n{dalle3(s)}\n```")
    (OUT / "dalle3.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # --- メイン画像 / タブ画像 ---------------------------------------------
    hero = next(s for s in stamps if s["id"] == 8)   # 尊い… = 世界観を最も象徴する1枚
    tab = next(s for s in stamps if s["id"] == 1)    # 実質無料 = 最もシンプルで縮小に強い
    tab_core = dict(tab)
    tab_core["subject_en"] = tab["subject_en"] + ", extremely simple silhouette, readable at thumbnail size"
    (OUT / "main_and_tab.md").write_text(
        "# メイン画像 / タブ画像用プロンプト\n\n"
        f"## メイン画像 {SPEC['main'][0]}x{SPEC['main'][1]} px（正方形なので上部余白は 30% に縮める）\n\n"
        f"```\n{midjourney(hero, ar='1:1')}\n```\n\n"
        f"## タブ画像 {SPEC['tab'][0]}x{SPEC['tab'][1]} px（文字なし・オブジェクト単体で作る）\n\n"
        f"```\n{midjourney(tab_core, ar='48:37')}\n```\n",
        encoding="utf-8",
    )

    print(f"generated {len(stamps)} prompts x 3 engines -> {OUT}")


if __name__ == "__main__":
    main()
