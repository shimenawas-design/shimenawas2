#!/usr/bin/env python3
"""シフトうさぎ（A案）: 40個の差分から Gemini 用プロンプトを組み立てる。

BASE / NEGATIVE は 40 枚すべてで一字一句同じにする。差し替えるのは
{{ACTION}} と {{EXPRESSION}} の 2 箇所だけ。これがキャラのブレを
構造的に防ぐ唯一の方法。

    python3 scripts/build_prompts.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "stamps_40.json"
OUT = ROOT / "prompts"

# ---------------------------------------------------------------------------
# BASE（40枚共通・変更禁止）
# ---------------------------------------------------------------------------
BASE = """A simple flat-illustration LINE sticker of a chibi white rabbit character.

[CHARACTER — must stay identical in every image]
A 3-head-tall chibi white rabbit, round plump body, short stubby arms and legs,
long slightly droopy ears.
Eyes: small solid black dot eyes, NO white highlight, NO shine, NO sparkle,
always half-lidded and lifeless. Faint dark shadows (eye bags) under both eyes.
Mouth: one small thin horizontal line, minimal.
Line art: thin, even-weight, dark grey outlines (not pure black).
Clothing: muted mint-green short-sleeve caregiver polo shirt, a small blank white
name badge on the chest (no letters on it), navy chino pants.
Color: low-saturation muted pastel palette, flat colors, minimal shading,
no gradients, no texture.

[COMPOSITION — strict layout rule]
The character is placed in the LOWER-CENTER of the frame and occupies only the
bottom 65-70% of the canvas.
The TOP 30% of the canvas must be completely empty flat background — it is
reserved space for text. Nothing may enter it: no ears, no raised hands, no
effect marks, no props.
Arms are never raised above shoulder height.

[POSE]
{{ACTION}}

[EXPRESSION]
{{EXPRESSION}}

[FORMAT]
Square canvas. Pure white background. No border, no frame, no ground shadow.
No text, no letters, no numbers, no watermark.
Style: clean minimal kawaii sticker illustration, thin line art, deadpan
dead-eyed comedic tone."""

# ---------------------------------------------------------------------------
# NEGATIVE（40枚共通・変更禁止）
# ---------------------------------------------------------------------------
NEGATIVE = """realistic, 3d render, glossy eyes, eye highlights, catchlight, sparkle, big shiny
eyes, moe anime eyes, gradient, heavy shading, detailed background, scenery, text,
letters, japanese characters, watermark, signature, extra limbs, extra fingers,
arms raised above the head, ears cropped by the frame, character filling the whole
canvas, cluttered composition, high saturation, vivid colors"""


def prompt_for(stamp: dict) -> str:
    return BASE.replace("{{ACTION}}", stamp["action_en"]).replace(
        "{{EXPRESSION}}", stamp["expression_en"]
    )


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    stamps = data["stamps"]
    OUT.mkdir(exist_ok=True)

    # --- BASE / NEGATIVE を単体で出力（コピペ用・これが唯一の正） -----------
    (OUT / "_base.md").write_text(
        "# BASE / NEGATIVE（40枚共通・変更禁止）\n\n"
        "`scripts/build_prompts.py` が唯一の正。手で編集しないこと。\n\n"
        f"## BASE\n\n```text\n{BASE}\n```\n\n"
        f"## NEGATIVE\n\n```text\n{NEGATIVE}\n```\n",
        encoding="utf-8",
    )

    # --- 40本の完成プロンプト ---------------------------------------------
    lines = [
        f"# {data['project']} — Gemini用プロンプト 40本\n",
        f"- ターゲット: {data['target']}\n"
        f"- 絵柄: {data['art_direction']}\n"
        f"- レイアウト: {data['layout_rule']}\n",
        "生成した画像は `raw/` に `01_*.png` 〜 `40_*.png` の名前で置き、`compose.py` にかける。\n",
    ]
    current = None
    for s in stamps:
        if s["category"] != current:
            current = s["category"]
            lines.append(f"\n---\n\n# カテゴリ：{current}\n")
        hero = "（看板コマ）" if s.get("is_hero") else ""
        lines.append(f"\n## {s['id']:02d}／{s['text']}{hero}\n")
        lines.append(f"```text\n{prompt_for(s)}\n```\n")
        lines.append(f"Negative prompt: `{NEGATIVE.replace(chr(10), ' ')}`\n")
    (OUT / "gemini_40.md").write_text("".join(lines), encoding="utf-8")

    # --- テキスト載せ用の一覧（改行位置つき） -------------------------------
    spec = data["text_spec"]
    rows = ["# テキスト一覧（改行位置つき）\n",
            f"\nフォント {spec['font_px']}px 固定 / 1行 {spec['max_chars_per_line']} 文字以内 / "
            f"行送り {spec['line_height_px']}px / 配置ゾーン 上端 {spec['zone_top_px']}〜{spec['zone_bottom_px']}px\n",
            "\n| # | セリフ | 1行目 | 2行目 | 最長行 |\n|---|---|---|---|---|\n"]
    over = []
    for s in stamps:
        l1 = s["lines"][0]
        l2 = s["lines"][1] if len(s["lines"]) > 1 else ""
        longest = max(len(x) for x in s["lines"])
        if longest > spec["max_chars_per_line"]:
            over.append((s["id"], s["text"], longest))
        rows.append(f"| {s['id']:02d} | {s['text']} | {l1} | {l2} | {longest} |\n")
    if over:
        rows.append("\n## 文字数超過（要修正）\n\n")
        for i, t, n in over:
            rows.append(f"- {i:02d} {t} — 最長 {n} 文字\n")
    else:
        rows.append(f"\n全40個が1行 {spec['max_chars_per_line']} 文字以内に収まっている。\n")
    (OUT / "texts_40.md").write_text("".join(rows), encoding="utf-8")

    # --- タグ一覧 ----------------------------------------------------------
    rows = ["# タグ一覧（40個）\n\n原則：汎用語1個 + 界隈語2個\n\n",
            "| # | セリフ | タグ1（汎用） | タグ2 | タグ3 |\n|---|---|---|---|---|\n"]
    for s in stamps:
        rows.append(f"| {s['id']:02d} | {s['text']} | {' | '.join(s['tags'])} |\n")
    (OUT / "tags_40.md").write_text("".join(rows), encoding="utf-8")

    n_over = len(over)
    print(f"generated {len(stamps)} prompts -> {OUT}")
    print(f"  _base.md / gemini_40.md / texts_40.md / tags_40.md")
    print(f"  文字数超過: {n_over} 件")


if __name__ == "__main__":
    main()
