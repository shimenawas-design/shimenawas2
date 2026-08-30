# ⑧ 音楽図書館｜シネマティック・スコア層 仕様（正式採用トレンド）

2026年トレンド「シネマティック化」を**正式採用**。LoFiを「映画のサウンドトラック」に一段引き上げる。
**大原則：シネマティック＝奥行きと物語。音量や劇的さではない。作業・読書・睡眠BGMとして"感じるが前に出ない"（felt, not foreground / restrained cinematic）。**

---

## 既存の共通楽器（維持）に"足す"層
篠笛・琴・尺八・琵琶・木魚・鈴・優しい太鼓・LoFi Beat・Warm Bass・Warm Analog Vinyl（ボーカルなし）
　＋
- **温かい弦のパッド**（チェロ/ストリングス、ボウイング。スタッカート禁止。低めの音量で情緒の土台）
- **静かなスウェル**（場面転換で緩やかなクレッシェンド／デクレッシェンド＝物語のアーク）
- **ドローン/サブパッド**（巨大木造ホールの空気感。深い余韻）
- **広いホール・リバーブ**（"映画背景レベル"の空間。奥行きを音で作る）

## Suno 追記キーワード（既存プロンプトに足す）
```
cinematic Japanese lofi, warm cinematic strings, subtle orchestral swells, emotional narrative arc, spacious wooden-hall reverb, deep atmospheric pad, felt not foreground, restrained and calm, immersive, soft dynamic swell, no dramatic peaks, no loud transients
```
※既存のSunoルール（`Begins immediately with` / 最初5秒 / 10秒で世界観完成 / `Avoid long ambient-only intros. Avoid slow build-up. Keep the first 10 seconds emotionally engaging while remaining calm and immersive.`）はそのまま維持。上記を足すだけ。

## 1曲の情緒アーク（映画の一場面として）
- **0〜10秒**：世界観立ち上げ（風/ページ/鈴/篠笛 → メインメロディ → LoFi Beat＋Bass）※既存ルール
- **中盤**：弦パッドがそっと入る → 緩やかなスウェルで「物語が進む」感
- **後半3分の1**：やわらかな山（温かさが増す）→ 静かに収束
- **全編**：1h/3h/8h版にループできる構造。音量は0:00からフル（維持率ルール）。奥行きは**リバーブとパッドで作る／トランジェントを大きくしない**。

## 映像との連動（Gemini画像にも足す）
シネマティックな音は「映画背景レベル」の画と対で効く。画像プロンプトに追記：
```
cinematic depth of field, volumetric moonlight, atmospheric haze, dust motes in light, film still, anamorphic mood
```
（既存の「人物なし・文字なし・16:9・超高精細・青×銀×琥珀・障子・灯籠・誰もいない」は維持）

## 既存20曲（黄昏・神々）の扱い
- **作り直さない。** シネマティック層は**月夜の図書館以降の新標準**とする。
- 既存は当面「サムネ統一＋タイトル整備＋3h/8h/ベスト版に束ねる」＝包み直しを優先。
- 望むなら後日「シネマティック・リマスター版」を別途出す選択肢もあるが、優先度は低い。

## 適用範囲
- ✅ 月夜の図書館（フラッグシップ）＝最初からこの層で作る
- ✅ 以降の全新シリーズ（神々の温泉宿／白狐茶屋 等）
- ✅ 写実「窓辺の四季」棟にも薄く適用可（現し世を図書館から眺める＝奥行きのある額装サウンド）

## 品質チェック（各曲）
- [ ] 弦・スウェルが**前に出すぎていない**（作業/睡眠を妨げない）
- [ ] 劇的なピーク・大きなトランジェントがない
- [ ] 0:00からフル音量でメロディ（冒頭の崖なし）
- [ ] 10秒以内に世界観が立つ
- [ ] 1時間ループで違和感がない（アークがループ境界で途切れない）
