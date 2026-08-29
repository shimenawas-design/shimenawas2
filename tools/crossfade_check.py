#!/usr/bin/env python3
"""
クロスフェードの継ぎ目で、2つのテイクのキー／テンポが合っているかを検査する。

Sunoの2テイクは同じプロンプトから生成されていても互いに独立で、キーもテンポも
揃っている保証がない。acrossfade は継ぎ目を滑らかにするが、重なった区間で
キーが衝突していれば「濁り」として残る。バイト単位比較では検出できない。

このスクリプトは継ぎ目の前後を取り出して比較し、**聴くべき箇所を絞り込む**。
最終判断は必ず耳で行うこと。

必要なもの: ffmpeg のみ（numpy/librosa 不要）

使い方:
    python3 crossfade_check.py "04 Thread Pool (combined).wav" --joins 90 150 255
    python3 crossfade_check.py in.wav --joins 180 210 --xfade 5 --window 8
"""

import argparse
import math
import struct
import subprocess
import sys

SR = 22050          # 解析用サンプルレート（ダウンサンプルして軽くする）
PITCH_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def decode(path, start, dur):
    """ffmpeg で [start, start+dur) を mono/SR/float に展開する。"""
    cmd = [
        "ffmpeg", "-v", "error",
        "-ss", f"{start:.3f}", "-t", f"{dur:.3f}", "-i", path,
        "-ac", "1", "-ar", str(SR), "-f", "s16le", "-",
    ]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = len(raw) // 2
    return [s / 32768.0 for s in struct.unpack(f"<{n}h", raw[: n * 2])]


def goertzel(x, freq):
    """単一周波数の強度を求める。FFT全体を回すより軽い。"""
    k = 2.0 * math.cos(2.0 * math.pi * freq / SR)
    s1 = s2 = 0.0
    for v in x:
        s0 = v + k * s1 - s2
        s2, s1 = s1, s0
    return s1 * s1 + s2 * s2 - k * s1 * s2


def chroma(x):
    """12音のピッチクラス分布。C2(MIDI36)〜C6(MIDI84) を集計して1オクターブに畳む。"""
    if not x:
        return [0.0] * 12
    # 直流除去（オフセットがあるとGoertzelが歪む）
    m = sum(x) / len(x)
    x = [v - m for v in x]

    out = [0.0] * 12
    for midi in range(36, 85):
        f = 440.0 * (2.0 ** ((midi - 69) / 12.0))
        out[midi % 12] += math.sqrt(max(0.0, goertzel(x, f)))
    total = sum(out)
    return [v / total for v in out] if total > 0 else out


def cosine(a, b):
    na = math.sqrt(sum(v * v for v in a))
    nb = math.sqrt(sum(v * v for v in b))
    if na == 0 or nb == 0:
        return 0.0
    return sum(p * q for p, q in zip(a, b)) / (na * nb)


def tempo(x, lo=40.0, hi=200.0):
    """RMSエンベロープの自己相関からBPMを推定する。返り値 (bpm, 相関の強さ)。"""
    hop = 256
    env = []
    for i in range(0, len(x) - hop, hop):
        w = x[i : i + hop]
        env.append(math.sqrt(sum(v * v for v in w) / hop))
    if len(env) < 32:
        return None, 0.0

    m = sum(env) / len(env)
    env = [v - m for v in env]
    fps = SR / hop

    best_bpm, best_r = None, 0.0
    lag_lo = max(1, int(fps * 60.0 / hi))
    lag_hi = min(len(env) - 1, int(fps * 60.0 / lo))
    denom = sum(v * v for v in env) or 1e-12
    for lag in range(lag_lo, lag_hi + 1):
        r = sum(env[i] * env[i + lag] for i in range(len(env) - lag)) / denom
        if r > best_r:
            best_r, best_bpm = r, 60.0 * fps / lag
    return best_bpm, best_r


def top_notes(c, n=3):
    idx = sorted(range(12), key=lambda i: c[i], reverse=True)[:n]
    return " ".join(f"{PITCH_NAMES[i]}({c[i]*100:.0f}%)" for i in idx)


def duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", path],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return float(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("--joins", type=float, nargs="+", required=True,
                    help="クロスフェード中心の秒数（changelog.md の構成を参照）")
    ap.add_argument("--xfade", type=float, default=3.0, help="クロスフェード長（秒）")
    ap.add_argument("--window", type=float, default=6.0, help="前後それぞれの解析窓（秒）")
    ap.add_argument("--key-threshold", type=float, default=0.80)
    ap.add_argument("--tempo-threshold", type=float, default=3.0, help="許容するBPM差(%)")
    a = ap.parse_args()

    total = duration(a.audio)
    half = a.xfade / 2.0
    print(f"\n{a.audio}  （長さ {int(total//60)}:{total%60:04.1f}）")
    print(f"クロスフェード {a.xfade}s / 解析窓 前後 {a.window}s ずつ\n")

    flagged = []
    for t in a.joins:
        b_start, a_start = t - half - a.window, t + half
        if b_start < 0 or a_start + a.window > total:
            print(f"  {t:7.1f}s  ✗ 範囲外（窓が音源からはみ出す）")
            continue

        before = decode(a.audio, b_start, a.window)
        after = decode(a.audio, a_start, a.window)

        cb, ca = chroma(before), chroma(after)
        sim = cosine(cb, ca)
        tb, rb = tempo(before)
        ta, ra = tempo(after)

        mm, ss = divmod(t, 60)
        print(f"  ── {int(mm)}:{ss:04.1f} の継ぎ目 ──")
        print(f"     前  {top_notes(cb)}")
        print(f"     後  {top_notes(ca)}")

        issues = []
        mark = "OK " if sim >= a.key_threshold else "要確認"
        print(f"     キー一致度 {sim:.3f}  [{mark}]")
        if sim < a.key_threshold:
            issues.append("キー")

        if tb and ta and rb > 0.15 and ra > 0.15:
            diff = abs(tb - ta) / ((tb + ta) / 2) * 100
            mark = "OK " if diff <= a.tempo_threshold else "要確認"
            print(f"     テンポ {tb:.1f} / {ta:.1f} BPM  差 {diff:.1f}%  [{mark}]")
            if diff > a.tempo_threshold:
                issues.append("テンポ")
        else:
            print("     テンポ 判定不能（拍が弱くアンビエント寄り。耳で確認）")

        if issues:
            flagged.append((t, "・".join(issues)))
        print()

    print("─" * 52)
    if flagged:
        print("⚠️  以下を優先して聴くこと：")
        for t, why in flagged:
            mm, ss = divmod(t, 60)
            print(f"     {int(mm)}:{ss:04.1f} 付近（{why}）")
    else:
        print("✅ 数値上の衝突は検出されず。ただし最終判断は耳で行うこと。")
    print()


if __name__ == "__main__":
    sys.exit(main())
