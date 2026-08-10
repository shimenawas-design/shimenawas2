# shimenawas2

日本株スイングトレードの売買ルールと補助ツール。

## 内容

| ファイル | 説明 |
|---|---|
| [`docs/swing-trading-rules.md`](docs/swing-trading-rules.md) | 売買ルール本体（資金管理・環境フィルタ・エントリー・損切り・利確・記録） |
| [`docs/trade-journal-template.csv`](docs/trade-journal-template.csv) | トレード記録のテンプレート |
| [`tools/position_size.py`](tools/position_size.py) | 発注株数の計算（依存パッケージなし、Python 3.8+） |

## 使い方

```bash
python3 tools/position_size.py --capital 5000000 --risk 0.5 --entry 2500 --stop 2350 --target 2800
```

ルール上の制約（損切り幅8%以内、リスクリワード1.5以上、必要資金の上限）に抵触する場合は警告が出ます。

## 注意

本リポジトリの内容は投資助言ではありません。売買の最終判断は自己責任で行ってください。
記載のパラメータは検証を経て各自の資金規模・リスク許容度に合わせて調整する前提のものです。
