"""
茶丸の間 / Chamaru — 動画背景への茶丸合成スクリプト

背景画像に固定キャラ「茶丸」の透過PNGを合成する（サムネ用ではなく動画背景用）。
make_thumb.py の合成ロジック（影・リムライト・無加工合成）を流用し、
1280x720へのクロップ／テロップ描画は行わない（背景の解像度をそのまま保つ）。

使い方:
    python composite_chamaru.py --bg path/to/bg.png --cutout oneeye --cx 450 --basey 560 --th 340 --out path/to/bg_with_chamaru.png

--cutout: "oneeye"（片目） or "master"（正面）
--cx / --basey / --th: 話ごとに手動調整する茶丸の配置（中心X・接地Y・高さpx）
"""

import argparse
import os
import sys
from PIL import Image, ImageFilter, ImageDraw

BANNER_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "バナー関連")
CUTOUTS = {
    "oneeye": os.path.join(BANNER_DIR, "chamaru_oneeye_cutout.png"),
    "master": os.path.join(BANNER_DIR, "chamaru_master_cutout.png"),
}


def composite(bg_path, cutout_key, cx, basey, th, out_path):
    cutout_path = CUTOUTS[cutout_key]
    for p in (bg_path, cutout_path):
        if not os.path.exists(p):
            sys.exit("ファイルが見つかりません: " + p)

    bg = Image.open(bg_path).convert("RGBA")
    W, H = bg.size
    canvas = bg.copy()

    # --- 茶丸 ---
    ch = Image.open(cutout_path).convert("RGBA")
    sc = th / ch.height
    ch = ch.resize((max(1, int(ch.width * sc)), max(1, int(ch.height * sc))), Image.LANCZOS)
    cw, chh = ch.size
    x = cx - cw // 2
    y = basey - chh

    # 接地影
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ew, eh = int(cw * 0.88), int(cw * 0.19)
    ecx, ecy = x + cw // 2, basey - 4
    ImageDraw.Draw(sh).ellipse(
        [ecx - ew // 2, ecy - eh // 2, ecx + ew // 2, ecy + eh // 2],
        fill=(15, 10, 6, 165),
    )
    canvas = Image.alpha_composite(canvas, sh.filter(ImageFilter.GaussianBlur(max(4, int(th * 0.037)))))

    # 左窓からのリムライト
    alpha = ch.split()[3]
    glow_src = Image.new("RGBA", (cw, chh), (255, 232, 195, 255))
    glow_src.putalpha(alpha)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for dx, dy, blur, op in [(-10, -6, 22, 150), (-4, -2, 10, 110)]:
        g = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        g.alpha_composite(glow_src, (x + dx, y + dy))
        g = g.filter(ImageFilter.GaussianBlur(blur))
        g.putalpha(g.split()[3].point(lambda v: int(v * op / 255)))
        glow = Image.alpha_composite(glow, g)
    canvas = Image.alpha_composite(canvas, glow)

    # 茶丸本体（無加工）
    canvas.alpha_composite(ch, (x, y))

    out_dir = os.path.dirname(os.path.abspath(out_path))
    os.makedirs(out_dir, exist_ok=True)
    canvas.convert("RGB").save(out_path)
    print(f"→ {out_path}  ({W}x{H}, 茶丸 h={chh}px @ ({x},{y}))")


def main():
    p = argparse.ArgumentParser(description="茶丸の間 動画背景合成")
    p.add_argument("--bg", required=True)
    p.add_argument("--cutout", choices=list(CUTOUTS), required=True)
    p.add_argument("--cx", type=int, required=True)
    p.add_argument("--basey", type=int, required=True)
    p.add_argument("--th", type=int, required=True)
    p.add_argument("--out", required=True)
    a = p.parse_args()
    composite(a.bg, a.cutout, a.cx, a.basey, a.th, a.out)


if __name__ == "__main__":
    main()
