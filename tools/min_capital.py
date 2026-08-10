#!/usr/bin/env python3
"""単元株（100株）で運用するために必要な資金を逆算する。

必要資金は2つの制約の大きいほうで決まる。

    リスク制約 : 株価 × 単元 × 損切り幅%  ≦  資金 × 1トレードリスク%
    建玉制約   : 株価 × 単元              ≦  資金 × 1銘柄建玉上限%

使用例:
    python3 tools/min_capital.py
    python3 tools/min_capital.py --risk 0.5 --stop 7 --max-position 25
    python3 tools/min_capital.py --prices 1000,2000,3000 --risk 1.0
"""

import argparse
import sys

DEFAULT_PRICES = [500, 1000, 1500, 2000, 3000, 4000, 5000, 8000]
DEFAULT_RISKS = [0.5, 1.0, 1.65, 5.0]


def required_capital(price, unit, stop_pct, risk_pct, max_pos_pct):
    """(必要資金, どちらの制約で決まったか) を返す。"""
    cost = price * unit
    c_risk = cost * (stop_pct / 100) / (risk_pct / 100)
    c_pos = cost / (max_pos_pct / 100)
    return (c_risk, "リスク") if c_risk >= c_pos else (c_pos, "建玉")


def yen(v):
    """万円単位に丸めて読みやすくする。"""
    man = v / 10_000
    return f"{man:,.1f}万円" if man < 100 else f"{man:,.0f}万円"


def main() -> int:
    p = argparse.ArgumentParser(description="単元株運用に必要な資金を逆算する")
    p.add_argument("--unit", type=int, default=100, help="単元株数（既定 100）")
    p.add_argument("--stop", type=float, default=7.0, help="損切り幅%%（既定 7.0）")
    p.add_argument(
        "--max-position", type=float, default=25.0, help="1銘柄あたり建玉の上限%%（既定 25.0）"
    )
    p.add_argument("--prices", help="株価をカンマ区切りで指定（例 1000,2000,3000）")
    p.add_argument("--risk", type=float, help="1トレードあたりリスク%%（単一指定）")
    a = p.parse_args()

    prices = DEFAULT_PRICES
    if a.prices:
        try:
            prices = [float(x) for x in a.prices.split(",") if x.strip()]
        except ValueError:
            print("エラー: --prices は数値のカンマ区切りで指定してください。", file=sys.stderr)
            return 1
    risks = [a.risk] if a.risk is not None else DEFAULT_RISKS
    if any(r <= 0 for r in risks) or a.stop <= 0 or a.max_position <= 0:
        print("エラー: リスク率・損切り幅・建玉上限は正の値で指定してください。", file=sys.stderr)
        return 1

    print(f"単元株数 {a.unit}株 / 損切り幅 {a.stop}% / 1銘柄建玉上限 {a.max_position}%")
    print()
    header = "  株価   | " + " | ".join(f"リスク{r:>5.2f}%" for r in risks)
    print(header)
    print("-" * len(header))
    for price in prices:
        cells = []
        for r in risks:
            cap, _ = required_capital(price, a.unit, a.stop, r, a.max_position)
            cells.append(f"{yen(cap):>11}")
        print(f"{price:>7,.0f}円 | " + " | ".join(cells))

    print()
    print("※ 上表は「1銘柄を建てるのに最低限必要な資金」。")
    print("  分散して同時に複数銘柄を持つには、さらに建玉総額の余力が必要になる。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
