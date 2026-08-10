#!/usr/bin/env python3
"""発注株数を計算する（docs/swing-trading-rules.md §1.2）。

損切り価格からリスク幅を求め、そこから株数を逆算する。
株数を先に決めてはいけない。

使用例:
    python3 tools/position_size.py --capital 5000000 --risk 0.5 --entry 2500 --stop 2350
    python3 tools/position_size.py -c 5000000 -r 0.5 -e 2500 -s 2350 -t 2800
"""

import argparse
import sys

# ルール上の制約（docs/swing-trading-rules.md v0.2）
MAX_STOP_PCT = 7.0  # §5.3 損切り幅の上限（エントリー価格比）
MAX_POSITION_PCT = 25.0  # §1.1 1銘柄あたり建玉の上限（運用資金比）
MIN_RR = 1.5  # §6.1 最低リスクリワード

# 境界値ちょうど（損切り幅7.00%など）が浮動小数点誤差で超過判定されないための許容誤差
EPS = 1e-9


def main() -> int:
    p = argparse.ArgumentParser(
        description="スイングトレードの発注株数を計算する",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("-c", "--capital", type=float, required=True, help="運用資金（円）")
    p.add_argument(
        "-r", "--risk", type=float, default=0.5, help="1トレードあたりリスク率（%%、既定 0.5）"
    )
    p.add_argument("-e", "--entry", type=float, required=True, help="エントリー価格（円）")
    p.add_argument("-s", "--stop", type=float, required=True, help="損切り価格（円）")
    p.add_argument("-t", "--target", type=float, help="目標価格（円、任意）")
    p.add_argument("-u", "--unit", type=int, default=100, help="単元株数（既定 100）")
    p.add_argument(
        "-m",
        "--max-position",
        type=float,
        default=MAX_POSITION_PCT,
        help=f"1銘柄あたり建玉の上限（%%、既定 {MAX_POSITION_PCT:.0f}）。5銘柄構成なら 15",
    )
    a = p.parse_args()

    if a.stop >= a.entry:
        print("エラー: 損切り価格はエントリー価格より低く設定してください。", file=sys.stderr)
        return 1
    if a.capital <= 0 or a.risk <= 0 or a.unit <= 0:
        print("エラー: 資金・リスク率・単元株数は正の値で指定してください。", file=sys.stderr)
        return 1

    risk_amount = a.capital * a.risk / 100
    risk_per_share = a.entry - a.stop
    stop_pct = risk_per_share / a.entry * 100
    shares = int(risk_amount / risk_per_share) // a.unit * a.unit

    print(f"運用資金          : {a.capital:>15,.0f} 円")
    print(f"リスク率          : {a.risk:>15.2f} %")
    print(f"許容リスク額 (1R) : {risk_amount:>15,.0f} 円")
    print("-" * 40)
    print(f"エントリー価格    : {a.entry:>15,.1f} 円")
    print(f"損切り価格        : {a.stop:>15,.1f} 円")
    print(f"1株あたりリスク幅 : {risk_per_share:>15,.1f} 円  ({stop_pct:.2f} %)")
    print("-" * 40)

    warnings = []
    if stop_pct > MAX_STOP_PCT + EPS:
        warnings.append(
            f"損切り幅が {stop_pct:.2f}% で上限 {MAX_STOP_PCT}% を超過 → §5.3 によりこのトレードは見送り"
        )

    if shares == 0:
        min_risk = risk_per_share * a.unit
        warnings.append(
            f"最小単元({a.unit}株)でもリスクが {min_risk:,.0f} 円となり許容額 {risk_amount:,.0f} 円を超過 → 見送り"
        )
        print(f"発注株数          : {'0 株（発注不可）':>18}")
    else:
        cost = a.entry * shares
        actual_risk = risk_per_share * shares
        print(f"発注株数          : {shares:>13,d} 株")
        print(f"必要資金          : {cost:>15,.0f} 円  (資金比 {cost / a.capital * 100:.1f} %)")
        print(
            f"実際のリスク額    : {actual_risk:>15,.0f} 円  "
            f"(資金比 {actual_risk / a.capital * 100:.2f} %)"
        )
        max_cost = a.capital * a.max_position / 100
        if cost > max_cost + EPS:
            warnings.append(
                f"必要資金 {cost:,.0f} 円が1銘柄の建玉上限 {max_cost:,.0f} 円"
                f"（資金の{a.max_position:.0f}%）を超過 → §1.3 によりこの銘柄は見送り"
                "（株数を減らして損切りを浅くしてはいけない）"
            )

    if a.target is not None:
        if a.target <= a.entry:
            warnings.append("目標価格がエントリー価格以下です。")
        else:
            rr = (a.target - a.entry) / risk_per_share
            print("-" * 40)
            print(f"目標価格          : {a.target:>15,.1f} 円")
            print(f"リスクリワード    : {rr:>15.2f} : 1")
            if shares:
                print(f"目標到達時の利益  : {(a.target - a.entry) * shares:>15,.0f} 円")
            if rr < MIN_RR:
                warnings.append(
                    f"リスクリワードが {rr:.2f} で下限 {MIN_RR} 未満 → §6.1 によりこのトレードは見送り"
                )
    else:
        print("-" * 40)
        print(f"※ 目標価格 (-t) 未指定。§6.1 のリスクリワード {MIN_RR} 以上の確認を忘れずに。")

    if warnings:
        print()
        print("【ルール抵触】")
        for w in warnings:
            print(f"  ! {w}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
