"""
茶丸の間 / Chamaru — サムネイル生成スクリプト（バッジ形式・26〜38用）

背景画像に固定キャラ「茶丸」の透過PNGを合成し、
主ラベル＋区切り線＋バッジ（丸ピル）＋右下ロゴの構成でテロップを入れて
1280x720 のサムネイルを書き出す。茶丸のピクセルは加工しない。

01〜25 の3行構成（タイトル/時間帯・尺/ジャンル・季節）は make_thumb.py を使う。
こちらは26〜29で採用したバッジ形式（例: 頭のもや / 40Hz・60 MIN）。

使い方 (Windows):
    python make_thumb_badge.py --bg bg30_with_chamaru.png --label 集中 --badges "60 MIN" --out thumb_30_shuchu.png
    python make_thumb_badge.py --bg bg34_with_chamaru.png --label 頭のもや --badges "40Hz,60 MIN" --out thumb_34_brainfog.png

--badges はカンマ区切りで複数指定可（1〜2個）。
"""

import argparse
import os
import sys
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance

# ---------------------------------------------------------------- 設定

W, H = 1280, 720

DEFAULTS = {
    "cutout": "chamaru_master_cutout.png",
    "label": "集中",
    "badges": "60 MIN",
    "logo": "茶丸の間",
    "out": "chamaru_thumb_badge.png",
}

CREAM = (250, 246, 236, 255)
GOLD = (206, 176, 106, 255)
PILL_DARK = (85, 83, 80, 255)

TX = 640          # テロップの左端
SUBJECT_H = 430   # 茶丸の高さ(px)
SUBJECT_CX = 285  # 茶丸の中心X
BASE_Y = 672      # 茶丸の底が卓面に接するY

# バッジ（ピル）のジオメトリ。26〜29の実物サムネを実測して合わせた値
PILL_H = 46
PILL_RADIUS = 23
PILL_GAP = 16
PILL_PAD_X = 28
PILL_BORDER = 2
LINE_Y = 400

FONT_CANDIDATES_BOLD = [
    r"C:\Windows\Fonts\yumindb.ttf",
    r"C:\Windows\Fonts\YuGothB.ttc",
    r"C:\Windows\Fonts\meiryob.ttc",
    r"C:\Windows\Fonts\msgothic.ttc",
    "/System/Library/Fonts/ヒラギノ明朝 ProN.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/usr/share/fonts/opentype/noto/NotoSerifCJK-Black.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc",
]

FONT_CANDIDATES_REG = [
    r"C:\Windows\Fonts\meiryo.ttc",
    r"C:\Windows\Fonts\YuGothR.ttc",
    r"C:\Windows\Fonts\msgothic.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
]


def find_font(candidates):
    for path in candidates:
        if os.path.exists(path):
            return path
    return None


def load_font(path, size):
    if path is None:
        return ImageFont.load_default()
    if path.lower().endswith(".ttc"):
        for idx in range(6):
            try:
                f = ImageFont.truetype(path, size, index=idx)
                if f.getbbox("集") != (0, 0, 0, 0):
                    return f
            except Exception:
                continue
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


# ---------------------------------------------------------------- 描画

def build(bg_path, cutout_path, label, badges, logo, out_path):
    for p in (bg_path, cutout_path):
        if not os.path.exists(p):
            sys.exit("ファイルが見つかりません: " + p)

    # --- 背景: 1280x720 にトリミングし、少しぼかして暗く落とす ---
    bg = Image.open(bg_path).convert("RGBA")
    s = max(W / bg.width, H / bg.height)
    bg = bg.resize((int(bg.width * s), int(bg.height * s)), Image.LANCZOS)
    left = (bg.width - W) // 2
    top = (bg.height - H) // 2
    bg = bg.crop((left, top, left + W, top + H))

    bg = bg.filter(ImageFilter.GaussianBlur(2.2))
    bg = ImageEnhance.Brightness(bg).enhance(0.80)
    bg = ImageEnhance.Color(bg).enhance(0.92)

    vig = Image.new("L", (W, H), 0)
    ImageDraw.Draw(vig).ellipse([-W * 0.25, -H * 0.35, W * 1.25, H * 1.35], fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(180))
    darker = Image.alpha_composite(bg, Image.new("RGBA", (W, H), (10, 8, 6, 110)))
    canvas = Image.composite(bg, darker, vig)

    # --- 茶丸 ---
    ch = Image.open(cutout_path).convert("RGBA")
    sc = SUBJECT_H / ch.height
    ch = ch.resize((int(ch.width * sc), int(ch.height * sc)), Image.LANCZOS)
    cw, chh = ch.size
    cx = SUBJECT_CX - cw // 2
    cy = BASE_Y - chh

    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ew, eh = int(cw * 0.88), int(cw * 0.19)
    ecx, ecy = cx + cw // 2, BASE_Y - 4
    ImageDraw.Draw(sh).ellipse(
        [ecx - ew // 2, ecy - eh // 2, ecx + ew // 2, ecy + eh // 2],
        fill=(15, 10, 6, 165),
    )
    canvas = Image.alpha_composite(canvas, sh.filter(ImageFilter.GaussianBlur(16)))

    alpha = ch.split()[3]
    glow_src = Image.new("RGBA", (cw, chh), (255, 232, 195, 255))
    glow_src.putalpha(alpha)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for dx, dy, blur, op in [(-10, -6, 22, 150), (-4, -2, 10, 110)]:
        g = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        g.alpha_composite(glow_src, (cx + dx, cy + dy))
        g = g.filter(ImageFilter.GaussianBlur(blur))
        g.putalpha(g.split()[3].point(lambda v: int(v * op / 255)))
        glow = Image.alpha_composite(glow, g)
    canvas = Image.alpha_composite(canvas, glow)

    canvas.alpha_composite(ch, (cx, cy))

    # --- テロップ ---
    bold_path = find_font(FONT_CANDIDATES_BOLD)
    reg_path = find_font(FONT_CANDIDATES_REG) or bold_path
    if bold_path is None:
        print("警告: 日本語フォントが見つかりません。文字が化ける可能性があります。")

    right_margin = 40
    avail_w = W - TX - right_margin

    def fit_font(path, base_size, text, min_size):
        f = load_font(path, base_size)
        w = f.getlength(text)
        if w > avail_w:
            f = load_font(path, max(min_size, int(base_size * avail_w / w)))
        return f

    f_main = fit_font(bold_path, 172, label, 96)
    f_badge = load_font(bold_path, 34)
    f_logo = load_font(bold_path, 34)

    d = ImageDraw.Draw(canvas)

    def shadowed(xy, text, font, fill, anchor="la", blur=10, sh_a=190):
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(layer).text(
            (xy[0] + 4, xy[1] + 6), text, font=font, fill=(0, 0, 0, sh_a), anchor=anchor
        )
        canvas.alpha_composite(layer.filter(ImageFilter.GaussianBlur(blur)))
        d.text(xy, text, font=font, fill=fill, anchor=anchor)

    # 主ラベル
    shadowed((TX, 196), label, f_main, CREAM)

    # 区切り線
    d.line([(TX + 4, LINE_Y), (TX + 128, LINE_Y)], fill=GOLD, width=4)

    # バッジ（ピル）: LINE_Y の下に横並び
    pill_top = LINE_Y + 30
    x = TX
    for badge_text in badges:
        tw = f_badge.getlength(badge_text)
        pill_w = int(tw + PILL_PAD_X * 2)
        box = [x, pill_top, x + pill_w, pill_top + PILL_H]

        shadow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(shadow_layer).rounded_rectangle(
            [box[0] + 3, box[1] + 4, box[2] + 3, box[3] + 4],
            radius=PILL_RADIUS, fill=(0, 0, 0, 140),
        )
        canvas.alpha_composite(shadow_layer.filter(ImageFilter.GaussianBlur(8)))

        d.rounded_rectangle(box, radius=PILL_RADIUS, fill=PILL_DARK, outline=GOLD, width=PILL_BORDER)
        cx_text = (box[0] + box[2]) / 2
        cy_text = (box[1] + box[3]) / 2
        d.text((cx_text, cy_text), badge_text, font=f_badge, fill=CREAM, anchor="mm")

        x += pill_w + PILL_GAP

    # 右下ロゴ
    shadowed((W - 44, H - 60), logo, f_logo, GOLD, anchor="ra", blur=8)

    out_dir = os.path.dirname(os.path.abspath(out_path))
    os.makedirs(out_dir, exist_ok=True)
    canvas.convert("RGB").save(out_path, quality=95)
    print("保存しました: " + out_path)


# ---------------------------------------------------------------- CLI

def main():
    p = argparse.ArgumentParser(description="茶丸の間 サムネイル生成（バッジ形式）")
    p.add_argument("--bg", required=True, help="背景画像のパス（茶丸合成済みでも未合成でも可。茶丸は本スクリプトが重ねて配置する）")
    p.add_argument("--cutout", default=DEFAULTS["cutout"], help="茶丸の透過PNG")
    p.add_argument("--label", default=DEFAULTS["label"], help="主ラベル（大・日本語）")
    p.add_argument("--badges", default=DEFAULTS["badges"], help="バッジ文言（カンマ区切りで複数可）")
    p.add_argument("--logo", default=DEFAULTS["logo"], help="右下の署名")
    p.add_argument("--out", default=DEFAULTS["out"], help="出力先")
    a = p.parse_args()
    badges = [b.strip() for b in a.badges.split(",") if b.strip()]
    build(a.bg, a.cutout, a.label, badges, a.logo, a.out)


if __name__ == "__main__":
    main()
