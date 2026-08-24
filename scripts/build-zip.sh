#!/usr/bin/env bash
# =====================================================================
# build-zip.sh
# ---------------------------------------------------------------------
# 「誰でもダウンロードしてすぐ使える」ように、拡張機能一式を
# 1つのZIPファイルにまとめるビルドスクリプトです。
#
# 使い方:
#   ./scripts/build-zip.sh
#
# dist/ フォルダの中に、バージョン番号入りのZIPファイル
# （例: gemini-image-bulk-downloader-v1.0.0.zip）が作られます。
# 中身をChromeの「パッケージ化されていない拡張機能を読み込む」で
# そのまま読み込める構成になっています。
# =====================================================================

set -euo pipefail

# このスクリプトが置かれている場所からリポジトリのルートを求める
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$ROOT_DIR"

# manifest.json からバージョン番号を読み取る
VERSION=$(python3 -c "import json; print(json.load(open('manifest.json'))['version'])")

PACKAGE_NAME="gemini-image-bulk-downloader"
DIST_DIR="$ROOT_DIR/dist"
STAGE_DIR="$DIST_DIR/$PACKAGE_NAME"
ZIP_PATH="$DIST_DIR/${PACKAGE_NAME}-v${VERSION}.zip"

echo "バージョン $VERSION のZIPを作成します…"

rm -rf "$STAGE_DIR" "$ZIP_PATH"
mkdir -p "$STAGE_DIR"

# Chromeの動作に必要なファイルだけをコピーする
# （.git や README、ビルドスクリプト自体は含めない）
cp manifest.json background.js content.js popup.html popup.css popup.js "$STAGE_DIR/"
cp -r icons "$STAGE_DIR/"

# 非技術者向けのインストール手順書も同梱する
cp "docs/はじめにお読みください.txt" "$STAGE_DIR/"

cd "$DIST_DIR"
zip -r -X "$(basename "$ZIP_PATH")" "$PACKAGE_NAME" -x '.*'

echo "完了しました: $ZIP_PATH"
