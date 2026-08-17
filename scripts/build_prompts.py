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

# [1] MEDIUM: 画風の支配力が最も強い位置。
#     v1 では "catalog product shot / octane render / 8k" と書いたため、
#     AIが「工業製品のリアル写真」を正しく生成してしまい、370x320 に縮小すると
#     判別不能・透過不能・サムネイル一覧で区別不能という三重の不合格になった。
#     写実をやめ、スタイライズされた3Dアイコンに転換する。
MEDIUM = (
    "simple stylized 3D icon, clean minimal 3D render of a vinyl toy miniature, "
    "chunky simplified geometry, bold readable silhouette, messenger sticker art"
)

# [2] TONE: 「無感情・無機質」は維持。ただし全面グレーは禁止し、差し色を1点だけ入れる。
TONE = (
    "an industrial machine part, cold emotionless inorganic object, "
    "absolutely no face and no eyes, not anthropomorphized, not a mascot, deadpan and lifeless, "
    "simplified matte metal with smooth soft gray shading, minimal surface detail, "
    "one single vivid orange accent color used sparingly on the focal point, "
    "strong value contrast between the object and the background"
)

# [2.5] STAGING: v2 の 01番テストで判明した課題への対策。
#     技術要件を全部満たしても「ストック3D素材」にしか見えず、スタンプとして機能しなかった。
#     原因は物体が何もしていないこと。感情を顔で出せない以上、
#     感情は「その物体に今まさに起きている物理現象」でしか表現できない。
#     よって全40枚を「事件の最高潮の一瞬」として演出することを固定ルールにする。
STAGING = (
    "the object is captured at the single most extreme peak instant of what is happening to it, "
    "theatrical exaggerated cartoon physics, clear and obvious action, "
    "slightly exaggerated proportions with the key feature oversized, "
    "all of the drama comes from the physical state of the object itself and never from any facial expression"
)

# [3] COMPOSITION: 【厳守ルール】上部35%の確保 + スタンプとして成立する「閉じた輪郭」。
#     v1 では被写体がフレーム外へ続いてしまい、背景透過に必要なシルエットが得られなかった。
COMPOSITION = (
    "one single isolated object, the entire object fits completely inside the frame "
    "with clear margin on every side, nothing is cropped and nothing touches the edges, "
    "the object sits entirely in the lower two thirds of the frame, "
    "wide empty headroom across the top 35 percent of the image, "
    "nothing at all in the upper area, generous negative space above the subject reserved for a caption, "
    "centered horizontally, slightly low camera angle looking at the object"
)

# [4] LIGHTING: 被写界深度は捨てる。縮小時にボケは情報の損失にしかならない。
LIGHTING = (
    "soft even studio lighting, gentle ambient occlusion, one simple soft drop shadow directly under the object, "
    "everything in sharp focus, no depth of field blur"
)

# [5] BACKGROUND: キーイングで抜くため、純白のフラット背景に固定する。
BACKGROUND = (
    "pure flat white background, completely empty, no environment, no floor, no walls, no machinery behind, "
    "the object floats cleanly, die cut sticker style with crisp clean edges"
)

# [6] QUALITY: 「高精細」ではなく「縮小に耐える」を品質の定義にする。
QUALITY = (
    "simple and bold, minimal detail, high contrast, thick clean edges, "
    "instantly readable when shrunk down to 370x320 pixels, iconic and graphic"
)

# [7] NEGATIVE: 文字は後から合成するので一切描かせない。写実化とトリミングも全力で潰す。
NEGATIVE = [
    "text", "letters", "words", "captions", "watermark", "signature", "logo",
    "numbers",
    "human", "person", "face", "eyes", "mouth", "hands",
    "cute character", "mascot", "anime",
    "photorealistic", "photograph", "hyperrealistic", "octane render", "8k", "macro", "close up",
    "cropped object", "cut off edges", "object touching the frame",
    "cluttered machinery", "hoses", "wires", "pipes in the background", "factory environment",
    "gray background", "gradient background", "busy background", "low contrast", "monochrome",
    "tiny details", "fine surface texture", "depth of field", "bokeh",
    "border", "frame", "vignette",
    "static and lifeless pose", "nothing happening", "stock 3d asset", "clip art icon",
]

# LINEスタンプ規格（W x H）
SPEC = {
    "stamp": (370, 320),
    "main": (240, 240),
    "tab": (96, 74),
}


def negatives_for(stamp: dict) -> list[str]:
    """被写体そのものがネガティブ語と衝突する数枚だけ、該当語を外す。

    例: 03「供給過多で死ぬ」はパイプが主役なので "pipes in the background" を外す。
        29「詳細なレポ助かる」は寸法数値が主役なので "numbers" を外す。
    """
    dropped = set(stamp.get("negative_exceptions", []))
    if stamp.get("allow_numbers"):
        dropped.add("numbers")
    return [n for n in NEGATIVE if n not in dropped]


def core(stamp: dict) -> str:
    """可変ブロック [SUBJECT] を固定ブロックで挟んだ本体。"""
    return ", ".join(
        [MEDIUM, stamp["subject_en"], STAGING, TONE, COMPOSITION, LIGHTING, BACKGROUND, QUALITY]
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
        f"Staging: {STAGING}. "
        f"Art direction: {TONE}. "
        f"Composition is critical: {COMPOSITION}. "
        f"Lighting: {LIGHTING}. Background: {BACKGROUND}. Quality: {QUALITY}. "
        "Do not render any text, letters, words or logos anywhere in the image. "
        "Do not add a border or frame. Aspect ratio 37:32 (wide)."
    )


def gemini(stamp: dict) -> str:
    """Gemini 系は用途を先に宣言すると絵柄が一気に安定する。

    「これはメッセージアプリのスタンプだ」と最初に言い切るのが最大のレバー。
    これを言わないと、工業製品のリアル写真を作りに行ってしまう。
    """
    return (
        "This image is a sticker for a messaging app. It will be displayed at only "
        "370x320 pixels, so it must be extremely simple, bold and instantly readable at that tiny size. "
        "It is NOT a photograph and NOT a realistic product render.\n\n"
        f"Draw a {MEDIUM} of {stamp['subject_en']}.\n\n"
        f"Staging (what makes or breaks this image): {STAGING}.\n"
        f"Style: {TONE}.\n"
        f"Composition (this is the most important requirement): {COMPOSITION}.\n"
        f"Lighting: {LIGHTING}.\n"
        f"Background: {BACKGROUND}.\n"
        f"Quality target: {QUALITY}.\n\n"
        "Absolute rules:\n"
        "- Keep the top 35 percent of the image completely empty. A Japanese caption will be "
        "placed there later, so nothing may appear in that area.\n"
        "- Show the whole object. Never crop it or let it touch the edges of the frame.\n"
        "- Do not draw any text, letters, words, numbers or logos.\n"
        "- Do not draw any background machinery, hoses, pipes, floor or factory interior. "
        "The background must be plain white and totally empty.\n"
        "- Do not make it photorealistic.\n"
        "- The object must clearly be in the middle of something happening. A static object just sitting there is a failure.\n"
        "Aspect ratio: 37:32 (slightly wider than tall)."
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

    # --- Gemini -----------------------------------------------------------
    lines = [f"# Gemini 用プロンプト（{data['project']}）\n"]
    for s in stamps:
        lines.append(f"\n## {s['id']:02d}. {s['jp_text']}\n\n> {s['concept_ja']}\n")
        lines.append(f"```\n{gemini(s)}\n```")
    (OUT / "gemini.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

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

    print(f"generated {len(stamps)} prompts x 4 engines -> {OUT}")


if __name__ == "__main__":
    main()
