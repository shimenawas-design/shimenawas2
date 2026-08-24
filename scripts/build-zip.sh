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
STAGE_DIR="$DIST_DIR/${PACKAGE_NAME}-v${VERSION}"
ZIP_PATH="$DIST_DIR/${PACKAGE_NAME}-v${VERSION}.zip"

echo "バージョン $VERSION のZIPを作成します…"

rm -rf "$STAGE_DIR" "$ZIP_PATH"
mkdir -p "$STAGE_DIR"

# Chromeの動作に必要なファイルだけをコピーする
# （.git や README、ビルドスクリプト自体は含めない）
cp manifest.json background.js content.js popup.html popup.css popup.js "$STAGE_DIR/"
cp -r icons "$STAGE_DIR/"

# 非技術者向けのインストール手順書も同梱する
# （ファイル名はASCII文字にしておく。日本語ファイル名はZIPの文字コード
# 　方式の違いにより、環境によっては文字化けすることがあるため）
cp "docs/INSTALL_README.txt" "$STAGE_DIR/"

# ---------------------------------------------------------------------
# 重要: ZIPの中身は「フォルダで包まない」で、ファイルをアーカイブの
# 直下に直接格納する。
#
# 理由: Windowsの「すべて展開」機能は、ZIP名と同じ名前の
# フォルダを自動的に新規作成してから展開する。もしZIPの中に
# さらに同名のフォルダが入っていると、
#   展開先フォルダ/展開先フォルダ/manifest.json ...
# のように二重にネストしてしまい、Chromeの「拡張機能を読み込む」
# ダイアログで一番外側のフォルダを選ぶと manifest.json が
# 見つからない、という混乱を招く。
# ファイルを直下に置くことで、展開したフォルダ＝そのまま選択する
# フォルダになり、迷わない構成にしている。
# ---------------------------------------------------------------------
(cd "$STAGE_DIR" && zip -r -X "$ZIP_PATH" . -x '.*')

echo "完了しました: $ZIP_PATH"
