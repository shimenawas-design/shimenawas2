#!/usr/bin/env python3
"""トレード記録CSVを集計する（docs/swing-trading-rules.md §8）。

月次・週次のレビューで使う。標準ライブラリのみで動作する。

使用例:
    python3 tools/review_journal.py docs/trade-journal-template.csv
    python3 tools/review_journal.py my-journal.csv --from 2026-08-01 --to 2026-08-31
"""

import argparse
import csv
import sys
from collections import defaultdict

# §8 の目安
TARGET_EXPECTANCY = 0.2  # 平均R
TARGET_PAYOFF = 1.5  # 平均勝ちR ÷ 平均負けR
TARGET_COMPLIANCE = 90.0  # ルール遵守率(%)


def load(path, date_from, date_to):
    rows = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            if not (row.get("entry_date") or "").strip():
                continue
            d = row["entry_date"].strip()
            if (date_from and d < date_from) or (date_to and d > date_to):
                continue
            raw_r = (row.get("pnl_r") or "").strip()
            if not raw_r:
                continue  # 決済前のトレードは集計対象外
            try:
                row["_r"] = float(raw_r)
            except ValueError:
                print(f"警告: {i}行目の pnl_r が数値ではありません: {raw_r!r}", file=sys.stderr)
                continue
            rows.append(row)
    return rows


def stats(rs):
    """勝ち負けの分離と各指標。ゼロ除算は None を返す。"""
    wins = [r["_r"] for r in rs if r["_r"] > 0]
    losses = [r["_r"] for r in rs if r["_r"] < 0]
    n = len(rs)
    expectancy = sum(r["_r"] for r in rs) / n if n else None
    win_rate = len(wins) / n * 100 if n else None
    avg_win = sum(wins) / len(wins) if wins else None
    avg_loss = sum(losses) / len(losses) if losses else None
    payoff = avg_win / abs(avg_loss) if avg_win is not None and avg_loss else None
    return n, expectancy, win_rate, avg_win, avg_loss, payoff


def max_drawdown_r(rs):
    """entry_date 順の累積R曲線における最大下落幅（R単位）。"""
    peak = 0.0
    equity = 0.0
    mdd = 0.0
    for r in sorted(rs, key=lambda x: x["entry_date"]):
        equity += r["_r"]
        peak = max(peak, equity)
        mdd = min(mdd, equity - peak)
    return mdd


def fmt(v, unit="", nd=2):
    return "―" if v is None else f"{v:.{nd}f}{unit}"


def main() -> int:
    p = argparse.ArgumentParser(description="トレード記録CSVを集計する")
    p.add_argument("csv_path", help="トレード記録CSVのパス")
    p.add_argument("--from", dest="date_from", help="集計開始日 (YYYY-MM-DD)")
    p.add_argument("--to", dest="date_to", help="集計終了日 (YYYY-MM-DD)")
    a = p.parse_args()

    try:
        rows = load(a.csv_path, a.date_from, a.date_to)
    except FileNotFoundError:
        print(f"エラー: ファイルが見つかりません: {a.csv_path}", file=sys.stderr)
        return 1

    if not rows:
        print("集計対象のトレードがありません（pnl_r が未記入のものは除外されます）。")
        return 0

    n, expectancy, win_rate, avg_win, avg_loss, payoff = stats(rows)
    total_yen = sum(float(r["pnl_yen"]) for r in rows if (r.get("pnl_yen") or "").strip())
    mdd = max_drawdown_r(rows)
    complied = sum(1 for r in rows if (r.get("rule_compliance") or "").strip().upper() == "Y")
    compliance = complied / n * 100

    print(f"■ 集計結果  （{n} トレード）")
    print("-" * 46)
    print(f"  期待値（平均R）    : {fmt(expectancy, 'R')}   目安 > +{TARGET_EXPECTANCY}R")
    print(f"  勝率               : {fmt(win_rate, '%', 1)}")
    print(f"  平均勝ち           : {fmt(avg_win, 'R')}")
    print(f"  平均負け           : {fmt(avg_loss, 'R')}")
    print(f"  ペイオフレシオ     : {fmt(payoff)}   目安 > {TARGET_PAYOFF}")
    print(f"  最大ドローダウン   : {fmt(mdd, 'R')}")
    print(f"  累計損益           : {total_yen:,.0f} 円")
    print(f"  ルール遵守率       : {compliance:.1f}%   目安 > {TARGET_COMPLIANCE}%")

    by_setup = defaultdict(list)
    for r in rows:
        by_setup[(r.get("setup") or "?").strip() or "?"].append(r)
    if len(by_setup) > 1:
        print()
        print("■ セットアップ別")
        print("-" * 46)
        for key in sorted(by_setup):
            sn, se, sw, _, _, sp = stats(by_setup[key])
            print(
                f"  {key}: {sn:3d}件  期待値 {fmt(se, 'R')}  "
                f"勝率 {fmt(sw, '%', 1)}  ペイオフ {fmt(sp)}"
            )

    print()
    print("■ 判定")
    print("-" * 46)
    if compliance < TARGET_COMPLIANCE:
        print(f"  ルール遵守率が {compliance:.1f}% で目安を下回っています。")
        print("  → §8 の通り、遵守率が90%を超えるまで手法を変更しないこと。")
        print("    成績が悪い原因が手法かメンタルかを切り分けられません。")
    elif expectancy is not None and expectancy > TARGET_EXPECTANCY:
        print("  遵守率・期待値ともに目安を満たしています。§9 のフェーズ移行を検討可。")
    else:
        print("  遵守率は十分ですが期待値が目安に届いていません。")
        print("  → セットアップ別の成績を見て、劣るほうを停止することを検討。")

    violations = [r for r in rows if (r.get("rule_compliance") or "").strip().upper() == "N"]
    if violations:
        print()
        print("■ ルール違反トレード（必ず読み返すこと）")
        print("-" * 46)
        for r in violations:
            print(
                f"  {r['entry_date']} {r.get('code', '')} {r.get('name', '')} "
                f"({r['_r']:+.2f}R): {r.get('note', '')}"
            )

    return 0


if __name__ == "__main__":
    sys.exit(main())
