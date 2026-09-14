# -*- coding: utf-8 -*-
r"""
シフトうさぎ（A案）LINEスタンプ 仕上げ一括処理

Gemini が出力した生画像 → 背景透過 → キャラを基準サイズに正規化 →
テキスト載せ → LINE規定サイズで書き出し（01.png〜40.png / main.png / tab.png）

使い方:
    python compose.py                      # raw\ を読んで out\ に書き出す
    python compose.py --placeholder        # 生画像なしでレイアウトだけ検証
    python compose.py --thresh 230         # 背景の白判定を緩める（背景が薄グレーの時）
    python compose.py --only 30            # 1枚だけ処理して確認

生画像のファイル名は先頭2桁が番号であること（例: 01_xxx.png, 30.png）
"""
import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy.ndimage import distance_transform_edt

ROOT = Path(__file__).resolve().parent
FONT_PATH = ROOT / "fonts" / "ZenMaruGothic-Bold.ttf"

# ---- LINE規定 & レイアウト定数（A案） ----
W, H = 370, 320          # スタンプ画像サイズ
TEXT_ZONE_H = 110        # 上部テキスト領域の高さ
TEXT_CENTER_Y = 58       # テキストブロックの縦中心
FONT_SIZE = 36           # 全40個で固定（統一感の要）
LINE_GAP = 42            # 2行時の行送り
SIDE_MARGIN = 12
STROKE = 5               # 白フチ
TEXT_COLOR = (74, 74, 74, 255)      # #4A4A4A
STROKE_COLOR = (255, 255, 255, 255)
EDGE_MARGIN = 10         # LINE規定の透明マージン
CHAR_W = W - EDGE_MARGIN * 2                  # 350
CHAR_H = H - TEXT_ZONE_H - EDGE_MARGIN        # 200

MAIN_SIZE = (240, 240)
TAB_SIZE = (96, 74)
COVER_NO = 30            # メイン/タブ画像に使う番号（看板コマ）

# ---- セリフ（改行位置を明示指定：36px固定・1行9文字以内） ----
TEXTS = {
    1:  ["おつかれさまです"],
    2:  ["おはようございます"],
    3:  ["夜勤入ります"],
    4:  ["明けました"],
    5:  ["了解です"],
    6:  ["ありがとう", "ございます"],
    7:  ["すみません遅れます"],
    8:  ["今から向かいます"],
    9:  ["お先に失礼します"],
    10: ["確認しました"],
    11: ["今夜ワンオペ"],
    12: ["センサー鳴りやまん"],
    13: ["巡視いってきます"],
    14: ["記録まだ真っ白"],
    15: ["仮眠、取れんかった"],
    16: ["明けの3時間睡眠"],
    17: ["今夜の面子、神"],
    18: ["残業、確定しました"],
    19: ["トランスで腰やった"],
    20: ["コール2つ", "同時は無理"],
    21: ["入浴介助、汗だく"],
    22: ["オムツ交換ラッシュ"],
    23: ["また起き上がってる"],
    24: ["検温まだ", "終わってない"],
    25: ["委員会の資料、", "できてません"],
    26: ["腰、そろそろ限界"],
    27: ["人手、", "足りてます？（笑）"],
    28: ["有給って何ですか"],
    29: ["心が無になりました"],
    30: ["笑顔だけは", "死んでない"],
    31: ["もう帰りたい", "（始業5分）"],
    32: ["この給料でこの仕事"],
    33: ["私、何の仕事", "してたっけ"],
    34: ["数えるのやめました"],
    35: ["ナイス介助"],
    36: ["生きて帰ろう"],
    37: ["それは大変だったね"],
    38: ["無理しないでね"],
    39: ["ほんと助かった"],
    40: ["お互い生き延びよう"],
}
assert len(TEXTS) == 40


# ---------------- 背景透過 ----------------
def _grow(mask, allowed, iters=None):
    """maskをallowedの内側だけに拡張する。itersがNoneなら収束まで。"""
    n = 0
    while True:
        g = mask.copy()
        g[1:, :] |= mask[:-1, :]
        g[:-1, :] |= mask[1:, :]
        g[:, 1:] |= mask[:, :-1]
        g[:, :-1] |= mask[:, 1:]
        g &= allowed
        n += 1
        if np.array_equal(g, mask) or (iters is not None and n >= iters):
            return g
        mask = g


def background_mask(rgb, thresh, scale=4):
    """画像の縁と地続きになっている白領域だけを背景と判定する。
    キャラ自身が白いため、単純な白抜きでは体に穴が空く。多段解像度の
    フラッドフィルで、濃いグレーの輪郭線を境界として使う。"""
    h, w = rgb.shape[:2]
    near = rgb.min(axis=2) >= thresh

    small = np.ascontiguousarray(near[::scale, ::scale])
    seed = np.zeros_like(small)
    seed[0, :] = small[0, :]
    seed[-1, :] = small[-1, :]
    seed[:, 0] = small[:, 0]
    seed[:, -1] = small[:, -1]
    small_bg = _grow(seed, small)

    up = np.repeat(np.repeat(small_bg, scale, axis=0), scale, axis=1)[:h, :w]
    return _grow(up & near, near, iters=scale * 8)


def keyout(path, thresh):
    im = Image.open(path).convert("RGBA")
    arr = np.array(im)
    if arr[..., 3].min() < 240:          # 既に透過済みならそのまま使う
        return im

    bg = background_mask(arr[..., :3], thresh)
    bg = _grow(bg, np.ones_like(bg), iters=1)     # 1px広げて白フリンジを除去
    alpha = np.where(bg, 0, 255).astype(np.uint8)

    out = Image.fromarray(np.dstack([arr[..., :3], alpha]))
    out.putalpha(out.getchannel("A").filter(ImageFilter.GaussianBlur(0.6)))
    return out


# ---------------- 合成 ----------------
def fit_into(img, size, bg=(0, 0, 0, 0)):
    canvas = Image.new("RGBA", size, bg)
    k = min(size[0] / img.width, size[1] / img.height)
    r = img.resize((max(1, int(img.width * k)), max(1, int(img.height * k))), Image.LANCZOS)
    canvas.alpha_composite(r, ((size[0] - r.width) // 2, (size[1] - r.height) // 2))
    return canvas


TEXT_SS = 4   # テキストのスーパーサンプリング倍率（縁取りのガタつき防止）


def compose(art, lines, font, font_path):
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))

    bbox = art.getbbox()
    if bbox:
        art = art.crop(bbox)
    k = min(CHAR_H / art.height, CHAR_W / art.width)
    art = art.resize((max(1, int(art.width * k)), max(1, int(art.height * k))), Image.LANCZOS)
    canvas.alpha_composite(art, ((W - art.width) // 2, H - EDGE_MARGIN - art.height))

    # ---- テキストは高解像度の文字マスク＋距離変換で縁取りを作り、縮小してフチの
    # ジャギーや内部の小さな囲み（例:「顔」の目の部分）が黒く抜ける不具合を防ぐ。
    # PIL純正のstroke_widthは複雑な字形の小さな囲みを塗り残すことがあるため使わない。
    ss = TEXT_SS
    font_ss = ImageFont.truetype(font_path, FONT_SIZE * ss)
    mask_im = Image.new("L", (W * ss, TEXT_ZONE_H * ss), 0)
    d = ImageDraw.Draw(mask_im)
    y0 = TEXT_CENTER_Y - (len(lines) - 1) * LINE_GAP / 2
    for i, line in enumerate(lines):
        if d.textlength(line, font=font) > W - SIDE_MARGIN * 2:
            print(f"    ! 文字がはみ出します: 「{line}」")
        d.text((W * ss // 2, (y0 + i * LINE_GAP) * ss), line, font=font_ss, fill=255,
               anchor="mm")

    ink = np.array(mask_im) > 127
    stroke = distance_transform_edt(~ink) <= STROKE * ss
    px = np.zeros((*ink.shape, 4), dtype=np.uint8)
    px[stroke] = STROKE_COLOR
    px[ink] = TEXT_COLOR
    text_layer = Image.fromarray(px, "RGBA").resize((W, TEXT_ZONE_H), Image.LANCZOS)
    canvas.alpha_composite(text_layer, (0, 0))
    return canvas


def placeholder_art():
    """生画像がない時のダミー（背景透過処理の検証も兼ねて白背景で作る）"""
    im = Image.new("RGB", (1024, 1024), (255, 255, 255))
    d = ImageDraw.Draw(im)
    grey, mint = (110, 115, 120), (168, 208, 190)
    d.ellipse([430, 380, 594, 520], fill=(255, 255, 255), outline=grey, width=6)   # 頭
    d.ellipse([452, 300, 486, 400], fill=(255, 255, 255), outline=grey, width=6)   # 耳
    d.ellipse([538, 300, 572, 400], fill=(255, 255, 255), outline=grey, width=6)
    d.ellipse([478, 440, 492, 454], fill=(40, 40, 40))                            # 目
    d.ellipse([532, 440, 546, 454], fill=(40, 40, 40))
    d.rounded_rectangle([446, 510, 578, 640], radius=40, fill=mint, outline=grey, width=6)
    d.rounded_rectangle([460, 636, 564, 720], radius=24, fill=(90, 100, 130), outline=grey, width=6)
    return im


def find_raw(raw_dir, num):
    for ext in ("png", "PNG", "jpg", "jpeg", "webp"):
        hits = sorted(raw_dir.glob(f"{num:02d}*.{ext}"))
        if hits:
            return hits[0]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="raw")
    ap.add_argument("--out", default="out")
    ap.add_argument("--thresh", type=int, default=236)
    ap.add_argument("--placeholder", action="store_true")
    ap.add_argument("--only", type=int, default=None)
    ap.add_argument("--font", default=str(FONT_PATH))
    args = ap.parse_args()

    raw_dir = (ROOT / args.input).resolve()
    out_dir = (ROOT / args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    font = ImageFont.truetype(args.font, FONT_SIZE)

    targets = [args.only] if args.only else list(range(1, 41))
    done, missing = {}, []

    for n in targets:
        lines = TEXTS[n]
        if args.placeholder:
            art = keyout_from_image(placeholder_art(), args.thresh)
        else:
            src = find_raw(raw_dir, n)
            if src is None:
                missing.append(n)
                continue
            art = keyout(src, args.thresh)

        sticker = compose(art, lines, font, args.font)
        sticker.save(out_dir / f"{n:02d}.png")
        done[n] = (sticker, art)
        print(f"  {n:02d}.png  「{'／'.join(lines)}」")

    if COVER_NO in done:
        sticker, art = done[COVER_NO]
        fit_into(sticker, MAIN_SIZE).save(out_dir / "main.png")
        head = art.crop(art.getbbox())
        head = head.crop((0, 0, head.width, int(head.height * 0.45)))   # 顔まわりのみ
        fit_into(head, TAB_SIZE).save(out_dir / "tab.png")
        print(f"  main.png / tab.png （#{COVER_NO} から生成）")

    if done and not args.only:
        cols, rows = 8, 5
        sheet = Image.new("RGB", (cols * W, rows * H), (236, 239, 241))
        for i, n in enumerate(sorted(done)):
            sheet.paste(done[n][0], ((i % cols) * W, (i // cols) * H), done[n][0])
        sheet.save(out_dir / "_contactsheet.png")
        print("  _contactsheet.png （全体の統一感チェック用）")

    print(f"\n完了: {len(done)}枚 → {out_dir}")
    if missing:
        print(f"生画像が見つからない番号: {missing}")
        print(f"  {raw_dir} に 01〜40 で始まる画像を置いてください")


def keyout_from_image(im, thresh):
    arr = np.array(im.convert("RGBA"))
    bg = background_mask(arr[..., :3], thresh)
    bg = _grow(bg, np.ones_like(bg), iters=1)
    alpha = np.where(bg, 0, 255).astype(np.uint8)
    out = Image.fromarray(np.dstack([arr[..., :3], alpha]))
    out.putalpha(out.getchannel("A").filter(ImageFilter.GaussianBlur(0.6)))
    return out


if __name__ == "__main__":
    main()
