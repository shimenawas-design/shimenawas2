# shimenawas2

日本株スイングトレードの売買ルールと補助ツール。

**前提**: 運用資金20万円／SBI証券のS株（単元未満株）／現物のみ／保有1〜2週間

## 内容

| ファイル | 説明 |
|---|---|
| [`docs/swing-trading-rules.md`](docs/swing-trading-rules.md) | 売買ルール本体（資金管理・環境フィルタ・エントリー・損切り・利確・記録） |
| [`docs/sbi-setup.md`](docs/sbi-setup.md) | SBI証券での執行設定、S株を選ぶ理由、20年前からの制度変更点 |
| [`docs/trade-journal-template.csv`](docs/trade-journal-template.csv) | トレード記録のテンプレート |
| [`tools/position_size.py`](tools/position_size.py) | 発注株数の計算とルール抵触チェック |
| [`tools/review_journal.py`](tools/review_journal.py) | トレード記録の集計（期待値・勝率・遵守率など） |
| [`tools/min_capital.py`](tools/min_capital.py) | 単元株（100株）運用に必要な資金の逆算 |

いずれも依存パッケージなし（Python 3.8+）。

## 使い方

### 発注前：株数を計算する

```bash
python3 tools/position_size.py -c 200000 -r 1.65 -e 2980 -s 2772 -t 3300 -u 1
```

損切り幅7%超、リスクリワード1.5未満、1銘柄建玉25%超のいずれかに該当すると警告が出ます。

### 週末：記録を集計する

```bash
python3 tools/review_journal.py my-journal.csv --from 2026-08-01 --to 2026-08-31
```

### 単元株に必要な資金を調べる

```bash
python3 tools/min_capital.py --prices 1500,3000,5000 --risk 1.0
```

## 現在の運用パラメータ

| 項目 | 値 |
|---|---|
| 運用資金 | 200,000円 |
| 同時保有の合計リスク上限 | 5.0%（10,000円） |
| 同時保有銘柄数 | 3銘柄 |
| 1トレードあたりリスク | 1.65%（3,300円） |
| 1銘柄あたり建玉上限 | 50,000円 |
| 建玉総額の上限 | 150,000円（残り25%は現金） |
| 損切り幅の上限 | 7% |
| 保有期間 | 最大10営業日 |

## 注意

本リポジトリの内容は投資助言ではありません。売買の最終判断は自己責任で行ってください。
記載のパラメータは検証を経て各自の資金規模・リスク許容度に合わせて調整する前提のものです。
