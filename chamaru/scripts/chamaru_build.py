#!/usr/bin/env python3
"""
茶丸の間 — Suno 4バリエーションの分析・選定・組み立てスクリプト

毎月ハードコードし直さずに済むよう、話数ごとの設定を JSON に外出ししている。

使い方:
    # 1) 分析（36曲ぶんの t1/t2/t3・rng・hf_ratio を出して JSON に保存）
    python chamaru_build.py analyze --indir ./suno_oct --out analysis_oct.json

    # 2) 組み立て（分析結果と設定を読んで、目標尺ちょうどの wav を書き出す）
    python chamaru_build.py build --config oct.json --analysis analysis_oct.json --indir ./suno_oct --outdir ./out

入力ファイルの命名:
    {indir}/30_main.wav, 30_1.wav, 30_2.wav, 30_3.wav
    （Suno が 1 プロンプトから出す 4 曲。プレフィックスが話数）

依存:
    numpy, soundfile, scipy（scipy はローパスにのみ使用）
"""

import argparse
import json
import math
import os
import sys
from glob import glob

import numpy as np
import soundfile as sf


# ---------------------------------------------------------------- 定数

WIN_SEC = 10.0          # RMS 解析の窓（重なりなし）
HF_CUTOFF_HZ = 2000.0   # hf_ratio の境界
BINAURAL_L_HZ = 200.0
BINAURAL_R_HZ = 240.0
BINAURAL_GAIN = 0.05    # 上げすぎると音楽を邪魔する


# ---------------------------------------------------------------- 入出力

def load_wav(path):
    """(samples, channels) の float64 と sr を返す。モノラルもステレオ化する。"""
    x, sr = sf.read(path, always_2d=True, dtype="float64")
    if x.shape[1] == 1:
        x = np.repeat(x, 2, axis=1)
    return x, sr


def save_wav(path, x, sr):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    sf.write(path, x, sr, subtype="PCM_16")


def to_mono(x):
    return x.mean(axis=1)


# ---------------------------------------------------------------- 分析

def rms_db_series(mono, sr, win_sec=WIN_SEC):
    """10秒窓・重なりなしで RMS(dB) の系列を返す。"""
    n = int(win_sec * sr)
    if n <= 0 or len(mono) < n:
        return np.array([20 * math.log10(np.sqrt(np.mean(mono ** 2)) + 1e-12)])
    count = len(mono) // n
    frames = mono[: count * n].reshape(count, n)
    rms = np.sqrt(np.mean(frames ** 2, axis=1))
    return 20 * np.log10(rms + 1e-12)


def thirds(series):
    """系列を3等分して各区間の平均（t1/t2/t3）を返す。

    np.array_split を使うのは、割り切れないときに末尾が空配列にならないようにするため
    （空だと mean が nan になり、安眠の t3 最小・目覚めの t1 最小の選定が静かに壊れる）。
    """
    if len(series) < 3:
        v = float(np.mean(series))
        return v, v, v
    a, b, c = np.array_split(series, 3)
    return float(np.mean(a)), float(np.mean(b)), float(np.mean(c))


def hf_ratio(mono, sr, cutoff=HF_CUTOFF_HZ, max_windows=120):
    """2000Hz 以上の FFT エネルギー比率。画面疲れ回の選定に使う。"""
    n = int(WIN_SEC * sr)
    if len(mono) < n:
        n = len(mono)
    count = max(1, len(mono) // n)
    step = max(1, count // max_windows)   # 長尺は間引いて十分
    hi = lo = 0.0
    for i in range(0, count, step):
        seg = mono[i * n : (i + 1) * n]
        if len(seg) < 16:
            continue
        spec = np.abs(np.fft.rfft(seg * np.hanning(len(seg)))) ** 2
        freqs = np.fft.rfftfreq(len(seg), 1.0 / sr)
        hi += float(spec[freqs >= cutoff].sum())
        lo += float(spec.sum())
    return hi / lo if lo > 0 else 0.0


def analyze_file(path):
    x, sr = load_wav(path)
    mono = to_mono(x)
    series = rms_db_series(mono, sr)
    t1, t2, t3 = thirds(series)
    return {
        "file": os.path.basename(path),
        "sr": sr,
        "duration_sec": round(len(mono) / sr, 2),
        "t1": round(t1, 2),
        "t2": round(t2, 2),
        "t3": round(t3, 2),
        "rng": round(float(np.percentile(series, 95) - np.percentile(series, 5)), 2),
        "hf_ratio": round(hf_ratio(mono, sr), 4),
    }


def cmd_analyze(args):
    paths = sorted(glob(os.path.join(args.indir, "*.wav")))
    if not paths:
        sys.exit(f"wav が見つかりません: {args.indir}")

    results = {}
    for p in paths:
        key = os.path.splitext(os.path.basename(p))[0]
        results[key] = analyze_file(p)
        print(f"analyzing… {key}", file=sys.stderr)

    # 表示より先に保存する。`| head` などで途中終了しても分析結果を失わないため。
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"→ {args.out} に保存（{len(results)}曲）\n")
    for key in sorted(results):
        r = results[key]
        flag = ""
        # 実績値の目安から外れるものに印を付ける（Suno が指示から逸れている可能性）
        if not (-18 <= r["t1"] <= -10):
            flag += " ⚠t1"
        if r["rng"] > 14:
            flag += " ⚠rng"
        print(
            f"{key:16s} t1={r['t1']:7.2f} t2={r['t2']:7.2f} t3={r['t3']:7.2f} "
            f"rng={r['rng']:5.2f} hf={r['hf_ratio']:.4f}{flag}"
        )
    print("\n目安: t1 -16〜-12dB / rng 平坦4〜6・起伏8〜12 / hf_ratio 0.02〜0.10")


# ---------------------------------------------------------------- 加工

def crossfade(a, b, sr, sec):
    """a の末尾と b の先頭を線形クロスフェードで繋ぐ。長さ = len(a)+len(b)-sec。"""
    n = int(sec * sr)
    n = min(n, len(a), len(b))
    if n <= 0:
        return np.concatenate([a, b])
    ramp = np.linspace(0.0, 1.0, n)[:, None]
    mid = a[-n:] * (1.0 - ramp) + b[:n] * ramp
    return np.concatenate([a[:-n], mid, b[n:]])


def make_seam(x, sr, sec):
    """末尾 sec 秒を先頭へ線形クロスフェードして、繋ぎ目のないループ素材にする。

    出力長 = len(x) - sec。これを単純に繰り返せば継ぎ目が出ない。
    """
    n = int(sec * sr)
    if n <= 0 or len(x) <= 2 * n:
        return x
    ramp = np.linspace(0.0, 1.0, n)[:, None]
    head = x[-n:] * (1.0 - ramp) + x[:n] * ramp
    return np.concatenate([head, x[n:-n]])


def loop_to(x, sr, target_sec):
    """seam 済みの素材を目標秒数ちょうどに伸ばす（足りなければ繰り返し、余れば切る）。"""
    target = int(target_sec * sr)
    if len(x) == 0:
        raise ValueError("空の音源")
    reps = int(math.ceil(target / len(x)))
    return np.tile(x, (reps, 1))[:target]


def add_binaural_40hz(x, sr):
    """L=200Hz / R=240Hz の正弦波を重ねて差分 40Hz を作る。

    検証済みの ffmpeg チェーンと等価:
        左右を個別に分解 → 個別に混ぜる → join で戻す
        （amix で直接混ぜるとステレオがダウンミックスされ左右分離が壊れる）
    amix(2入力) は 0.5 倍平均、その後 volume=2 で戻すので、実質は単純加算。
    """
    t = np.arange(len(x)) / sr
    out = x.copy()
    out[:, 0] += BINAURAL_GAIN * np.sin(2 * np.pi * BINAURAL_L_HZ * t)
    out[:, 1] += BINAURAL_GAIN * np.sin(2 * np.pi * BINAURAL_R_HZ * t)
    return out


def verify_binaural(x, sr):
    """L に 200Hz、R に 240Hz が立っているか実測して返す（保存前の自己チェック）。"""
    n = min(len(x), sr * 30)
    res = {}
    for ch, name, want in ((0, "L", BINAURAL_L_HZ), (1, "R", BINAURAL_R_HZ)):
        spec = np.abs(np.fft.rfft(x[:n, ch] * np.hanning(n)))
        freqs = np.fft.rfftfreq(n, 1.0 / sr)
        band = (freqs > want - 3) & (freqs < want + 3)
        peak = float(freqs[band][np.argmax(spec[band])]) if band.any() else 0.0
        res[name] = round(peak, 2)
    return res


def lowpass(x, sr, cutoff_hz, order=4):
    """画面疲れ回の仕上げ。Suno は「高域なし」指示に完全には従わないため軽くかける。"""
    from scipy.signal import butter, sosfiltfilt

    sos = butter(order, cutoff_hz / (sr / 2.0), btype="low", output="sos")
    return sosfiltfilt(sos, x, axis=0)


def normalize(x, target_rms_db=-20.0, peak_cap_db=-1.5):
    """RMS を target に合わせる。ピークが cap を超える場合はゲインを下げる（可逆ゲインのみ）。"""
    mono = to_mono(x)
    cur = 20 * math.log10(np.sqrt(np.mean(mono ** 2)) + 1e-12)
    gain = 10 ** ((target_rms_db - cur) / 20.0)
    peak = float(np.max(np.abs(x))) or 1e-12
    cap = 10 ** (peak_cap_db / 20.0)
    if peak * gain > cap:
        gain = cap / peak
    return x * gain


# ---------------------------------------------------------------- 選定

def pick(analysis, keys, state):
    """状態別の選定ロジック。採用する take のキーを順番どおりに返す。

    集中・リセット : rng 最小順に 4 曲すべて
    安眠           : t3 が最小の曲を最後に（締めを静かに）
    ブレインフォグ : rng 最小の 2 曲のみ（均一密度を最優先）
    画面疲れ       : hf_ratio 最小の 2 曲のみ
    目覚め         : 別処理（build_wake を参照）
    """
    if state in ("focus", "reset"):
        return sorted(keys, key=lambda k: analysis[k]["rng"])
    if state == "sleep":
        last = min(keys, key=lambda k: analysis[k]["t3"])
        rest = sorted([k for k in keys if k != last], key=lambda k: analysis[k]["rng"])
        return rest + [last]
    if state == "brainfog":
        return sorted(keys, key=lambda k: analysis[k]["rng"])[:2]
    if state == "screen":
        return sorted(keys, key=lambda k: analysis[k]["hf_ratio"])[:2]
    raise ValueError(f"未知の状態: {state}")


# ---------------------------------------------------------------- 組み立て

def build_looped(paths, sr_expect, target_sec, xfade, seam):
    """集中・リセット・安眠・ブレインフォグ・画面疲れ 共通。

    採用曲を 8 秒クロスフェードで連結 → 6 秒継ぎ目でループ素材化 → 目標尺ちょうどに伸ばす。
    """
    acc = None
    for p in paths:
        x, sr = load_wav(p)
        if acc is None:
            acc, sr_expect = x, sr
        else:
            if sr != sr_expect:
                sys.exit(f"サンプルレート不一致: {p}")
            acc = crossfade(acc, x, sr, xfade)
    acc = make_seam(acc, sr_expect, seam)
    return loop_to(acc, sr_expect, target_sec), sr_expect


def build_wake(first_path, second_path, target_sec, xfade, seam):
    """目覚め専用。

    t1 最小の曲を前半にループ、t3 最大の曲を後半に 1 回だけ繋ぐ。
    ⚠ 全体を通しでループしない（「静か→やや明るい」の一方向の設計を壊すため）。

    尺の計算:
        前半 = target - len(後半) + xfade
        → クロスフェードで xfade ぶん重なるので、合計がちょうど target になる。
    """
    a, sr = load_wav(first_path)
    b, sr_b = load_wav(second_path)
    if sr != sr_b:
        sys.exit("サンプルレート不一致（目覚め回の前半/後半）")

    tail_sec = len(b) / sr
    head_sec = target_sec - tail_sec + xfade
    if head_sec <= xfade:
        sys.exit(f"後半用が長すぎます（{tail_sec:.1f}s）。別テイクを選んでください")

    head = loop_to(make_seam(a, sr, seam), sr, head_sec)
    return crossfade(head, b, sr, xfade), sr


def cmd_build(args):
    with open(args.config, encoding="utf-8") as f:
        cfg = json.load(f)
    with open(args.analysis, encoding="utf-8") as f:
        analysis = json.load(f)

    xfade = cfg.get("crossfade_sec", 8)
    seam = cfg.get("seam_sec", 6)
    target_rms = cfg.get("target_rms_db", -20.0)
    peak_cap = cfg.get("peak_cap_db", -1.5)

    for ep in cfg["episodes"]:
        eid = str(ep["id"])
        state = ep["state"]
        target = ep["duration_sec"]
        excluded = set(ep.get("exclude_takes", []))

        # 耳での不採用（虫が入った・蝉が断続的 等）は設定ファイルの exclude_takes で除く。
        # 数値では判定できないため、ここは人の判断が入る。
        keys = sorted(
            k for k in analysis
            if k.split("_")[0] == eid and k not in excluded
        )
        if not keys:
            print(f"[{eid}] スキップ（該当ファイルなし）")
            continue

        print(f"\n[{eid}] {state} / 目標 {target}s / 候補 {len(keys)}曲"
              + (f" / 除外 {sorted(excluded)}" if excluded else ""))

        if state == "wake":
            # 27 のように前半/後半を別プロンプトで生成した場合はプレフィックスで分ける
            hp = ep.get("first_half_prefix")
            tp = ep.get("second_half_prefix")
            pool_a = [k for k in keys if k.startswith(hp)] if hp else keys
            pool_b = [k for k in keys if k.startswith(tp)] if tp else keys
            ka = min(pool_a, key=lambda k: analysis[k]["t1"])
            kb = max(pool_b, key=lambda k: analysis[k]["t3"])
            print(f"  前半 {ka} (t1={analysis[ka]['t1']}) / 後半 {kb} (t3={analysis[kb]['t3']}) ※通しループなし")
            y, sr = build_wake(
                os.path.join(args.indir, ka + ".wav"),
                os.path.join(args.indir, kb + ".wav"),
                target, xfade, seam,
            )
        else:
            chosen = pick(analysis, keys, state)
            metric = "hf_ratio" if state == "screen" else "rng"
            print("  採用: " + " → ".join(f"{k}({analysis[k][metric]})" for k in chosen))
            y, sr = build_looped(
                [os.path.join(args.indir, k + ".wav") for k in chosen],
                None, target, xfade, seam,
            )

        # ⚠ 40Hz 重ねは必ず音量統一の前
        if ep.get("binaural_40hz"):
            y = add_binaural_40hz(y, sr)
            print(f"  40Hz 重ね → 実測ピーク {verify_binaural(y, sr)}")

        if ep.get("lowpass_hz"):
            y = lowpass(y, sr, ep["lowpass_hz"])
            print(f"  ローパス {ep['lowpass_hz']}Hz")

        y = normalize(y, target_rms, peak_cap)

        out = os.path.join(args.outdir, f"{eid}_final.wav")
        save_wav(out, y, sr)
        print(f"  → {out}  ({len(y)/sr:.2f}s / 目標 {target}s)")


# ---------------------------------------------------------------- CLI

def main():
    p = argparse.ArgumentParser(description="茶丸の間 音源ビルダー")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("analyze", help="Suno 出力を分析して JSON に保存")
    a.add_argument("--indir", required=True)
    a.add_argument("--out", default="analysis.json")
    a.set_defaults(func=cmd_analyze)

    b = sub.add_parser("build", help="選定・組み立て・40Hz・音量統一")
    b.add_argument("--config", required=True)
    b.add_argument("--analysis", required=True)
    b.add_argument("--indir", required=True)
    b.add_argument("--outdir", default="./out")
    b.set_defaults(func=cmd_build)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
