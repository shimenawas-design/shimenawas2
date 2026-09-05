# 話別詳細 — 雪 39〜48（11月分）

> 統合マスター_YYMMDD.md（インデックス）から分割。共通ルール・タグ設計・要対応リストはインデックス側を参照。

**進行中（2026-09-06時点：Gemini背景プロンプトのみ作成。音源組み立て・画像生成・合成・サムネ・動画エンコード・①〜④⑥〜⑧はこれから）。** テーマは雪。10月＝紅葉からの切り替え。11月分専用の指示書ドキュメントは存在しないため、①〜④⑥〜⑧は今後の作業で作成する。

### この10本の狙い

- 状態配分が10月と異なる（集中1・リセット1・安眠1・目覚め2・ブレインフォグ3・画面疲れ2、詳細はインデックスの「11月分（39〜48）素材到着・フォルダ分け」参照）
- **画面疲れ（47・48）は10月の「紅葉なし」ルールに相当する処理として、暖色を抑える**：⑤のプロンプトに `with no warm colour — only deep blue and grey` 相当の指定を入れ、彩度を落として目を休める構図にする（47は残照の暖色を排除、48は熾火の暖色だけを残しそれ以外を寒色に絞る）
- **43〜48は各2テイクしかない**が、目覚め・ブレインフォグ・画面疲れの選定ロジックはもともと2曲だけ使う設計のため問題なし（インデックス参照）

### 茶丸の使い分け（状態別テンプレートどおり）

- **片目版**（`chamaru_oneeye_cutout.png`）：39（集中）・42・43（目覚め）・44・45・46（ブレインフォグ）
- **正面版**（`chamaru_master_cutout.png`）：40（リセット）・41（安眠）・47・48（画面疲れ）

### 出力先

```
39_集中_雪の朝の茶室\
40_リセット_雪の午後の縁側\
41_安眠_雪の宵の囲炉裏端\
42_目覚め_雪明けの囲炉裏端\
43_目覚め_初雪の窓辺\
44_ブレインフォグ_雪の朝の縁側\
45_ブレインフォグ_粉雪の午後の庭\
46_ブレインフォグ_火鉢の午後の茶室\
47_画面疲れ_雪の夕暮れの窓辺\
48_画面疲れ_熾火の夕暮れの囲炉裏端\
```

---

## 39 ｜ 集中（雪の朝の茶室・60分）

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | 集中 / 朝 |
| 尺 | 60分 |
| 舞台 | 茶室 |
| 茶丸 | 片目 |

**⑤ Gemini — 動画用背景**
```
A photorealistic interior of a traditional Japanese wa-modern tea room on a clear snowy winter morning, shot at eye level, front view. A worn dark wooden table surface fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft clear cold morning light comes from a shoji window on the left. Beyond the window, a snow-covered garden with a stone lantern capped in snow and bare tree branches dusted with fresh snow is visible, softly blurred, quiet and still. In the blurred background: tatami mats and a plain shoji screen, out of focus, with very few objects. Muted white and pale blue-grey against dark wood, crisp and serene. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景**
```
A photorealistic interior of a traditional Japanese wa-modern tea room on a clear snowy winter morning, shot at eye level, front view, 16:9. A worn dark wooden table surface fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft clear cold morning light comes from a shoji window on the left. Beyond the window, a snow-covered garden with a stone lantern capped in snow is visible on the left, softly blurred. The right third of the frame is a plain shoji screen in shadow, simple and uncluttered. Muted white and pale blue-grey against dark wood, high contrast between the bright window on the left and the shadowed right side. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style.
```

---

## 40 ｜ リセット（雪の午後の縁側・90分）

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | リセット / 午後 |
| 尺 | 90分 |
| 舞台 | 縁側 |
| 茶丸 | 正面 |

**⑤ Gemini — 動画用背景**
```
A photorealistic view of a traditional Japanese engawa veranda on a quiet snowy winter afternoon, shot at eye level, front view. A worn dark wooden veranda floor fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale afternoon light comes from the open side on the left. Beyond the veranda, snow is falling gently over a quiet garden, with a stone lantern and pine branches capped in white, softly blurred. In the blurred background: wooden pillars and a paper screen, out of focus. Soft white and pale blue against dark wood, calm and even. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景**
```
A photorealistic view of a traditional Japanese engawa veranda on a quiet snowy winter afternoon, shot at eye level, front view, 16:9. A worn dark wooden veranda floor fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale afternoon light comes from the open side on the left. Beyond the veranda, snow is falling gently over a quiet garden with a stone lantern and pine branches capped in white, visible on the left, softly blurred. The right third of the frame is a dark wooden pillar and a paper screen in shadow, simple and uncluttered. Soft white and pale blue against dark wood, calm and even, gentle contrast between the pale left side and the shadowed right side. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style.
```

---

## 41 ｜ 安眠（雪の宵の囲炉裏端・90分）

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | 安眠 / 夜 |
| 尺 | 90分 |
| 舞台 | 囲炉裏端 |
| 茶丸 | 正面 |

**⑤ Gemini — 動画用背景**
```
A photorealistic interior of a traditional Japanese wa-modern room beside a sunken irori hearth on a snowy winter evening, shot at eye level, front view. A worn dark wooden floor beside the hearth fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. A soft warm glow from the low burning hearth fire comes from the left, the room settling into deep shadow. Through a small window, snow is falling quietly in the dark outside, softly blurred. In the blurred background: a hanging iron kettle and tatami mats, out of focus, with very few objects. Warm amber firelight against deep blue-black night and dark wood, still and hushed. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景**
```
A photorealistic interior of a traditional Japanese wa-modern room beside a sunken irori hearth on a snowy winter evening, shot at eye level, front view, 16:9. A worn dark wooden floor beside the hearth fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. A soft warm glow from the low burning hearth fire comes from the left, the room settling into deep shadow. Through a small window, snow falling quietly in the dark is visible on the left, softly blurred. The right third of the frame is a dark wooden pillar and tatami in deep shadow, simple and uncluttered. Warm amber firelight against deep blue-black night and dark wood, high contrast between the glowing left side and the shadowed right side. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style.
```

---

## 42 ｜ 目覚め（雪明けの囲炉裏端・30分）

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | 目覚め / 明け方 |
| 尺 | 30分 |
| 舞台 | 囲炉裏端 |
| 茶丸 | 片目 |

**⑤ Gemini — 動画用背景**
```
A photorealistic interior of a traditional Japanese wa-modern room beside a sunken irori hearth just before dawn after overnight snowfall, shot at eye level, front view. A worn dark wooden floor beside the hearth fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale blue-white light reflected off fresh snow comes through a window on the left, with the last embers glowing faintly in the hearth. Beyond the window, a snow-covered garden is visible in the pale pre-dawn light, softly blurred. In the blurred background: a hanging iron kettle and tatami mats, out of focus, with very few objects. Pale blue-white snow light against warm dying embers and dark wood, quiet and still. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景**
```
A photorealistic interior of a traditional Japanese wa-modern room beside a sunken irori hearth just before dawn after overnight snowfall, shot at eye level, front view, 16:9. A worn dark wooden floor beside the hearth fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale blue-white light reflected off fresh snow comes through a window on the left, with the last embers glowing faintly in the hearth. Beyond the window, a snow-covered garden is visible on the left in the pale pre-dawn light, softly blurred. The right third of the frame is plain tatami and a dark wall in shadow, simple and uncluttered. Pale blue-white snow light against warm dying embers and dark wood, gentle contrast between the pale left side and the shadowed right side. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style.
```

---

## 43 ｜ 目覚め（初雪の窓辺・30分）

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | 目覚め / 明け方 |
| 尺 | 30分 |
| 舞台 | 窓辺 |
| 茶丸 | 片目 |

**⑤ Gemini — 動画用背景**
```
A photorealistic interior of a traditional Japanese wa-modern room by a window at dawn during the season's first snowfall, shot at eye level, front view. A worn dark wooden window ledge fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale cold dawn light comes through the open shoji window on the left. Beyond the window, the season's first snow is falling gently over bare tree branches against a pale grey sky, softly blurred. In the blurred background: tatami mats, a paper screen, and a small ceramic cup placed off to the side, out of focus. Pale white and grey against dark wood and warm washi-paper tones, crisp and quiet. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景**
```
A photorealistic interior of a traditional Japanese wa-modern room by a window at dawn during the season's first snowfall, shot at eye level, front view, 16:9. A worn dark wooden window ledge fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale cold dawn light comes through the open shoji window on the left. Beyond the window, the season's first snow is falling gently over bare tree branches, visible on the left against a pale grey sky, softly blurred. The right third of the frame is a plain shoji screen in shadow, simple and uncluttered. Pale white and grey against dark wood and warm washi-paper tones, high contrast between the bright window on the left and the shadowed right side. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style.
```

> 43は窓の敷居に乗せる構図になる想定（36と同様、baseyを高めに調整する見込み。実際の座標は合成時に決定）。

---

## 44 ｜ ブレインフォグ（雪の朝の縁側・60分）✅40Hz

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | ブレインフォグ / 朝 |
| 尺 | 60分 |
| 舞台 | 縁側 |
| 茶丸 | 片目 |

**⑤ Gemini — 動画用背景**
```
A photorealistic view of a traditional Japanese engawa veranda on a quiet snowy winter morning, shot at eye level, front view. A worn dark wooden veranda floor fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale cold morning light comes from the open side on the left. Beyond the veranda, a snow-covered garden is visible, softly blurred, still and empty. The scene is deliberately sparse and uncluttered. In the blurred background: a single wooden pillar and a paper screen, out of focus, with very few objects. Muted white and pale grey-blue against dark wood, still and quiet. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景**
```
A photorealistic view of a traditional Japanese engawa veranda on a quiet snowy winter morning, shot at eye level, front view, 16:9. A worn dark wooden veranda floor fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale cold morning light comes from the open side on the left. Beyond the veranda, a snow-covered garden is visible on the left, softly blurred, still and empty. The right third of the frame is a plain wooden pillar and paper screen in shadow, simple and uncluttered. Muted white and pale grey-blue against dark wood, gentle contrast between the pale left side and the shadowed right side. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style.
```

> ブレインフォグ回は静かで情報量の少ない絵にする（小物を増やさない、34・45・46と同方針）。

---

## 45 ｜ ブレインフォグ（粉雪の午後の庭・60分）✅40Hz

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | ブレインフォグ / 午後 |
| 尺 | 60分 |
| 舞台 | 庭 |
| 茶丸 | 片目 |

**⑤ Gemini — 動画用背景**
```
A photorealistic view of a quiet traditional Japanese garden on a winter afternoon with fine powder snow falling, shot at eye level, front view. A worn dark wooden deck edge fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale afternoon light comes from the left. Beyond the deck, fine powder snow drifts over moss, stepping stones and bare trees, softly blurred. The scene is deliberately sparse and uncluttered. In the blurred background: a stone water basin, out of focus, with very few objects. Muted white and pale grey against dark wood and moss green, still and quiet. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景**
```
A photorealistic view of a quiet traditional Japanese garden on a winter afternoon with fine powder snow falling, shot at eye level, front view, 16:9. A worn dark wooden deck edge fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale afternoon light comes from the left. Beyond the deck, fine powder snow drifts over moss and bare trees, visible on the left, softly blurred. The right third of the frame is a plain dark wooden wall in shadow, simple and uncluttered. Muted white and pale grey against dark wood and moss green, gentle contrast between the pale left side and the shadowed right side. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style.
```

---

## 46 ｜ ブレインフォグ（火鉢の午後の茶室・60分）✅40Hz

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | ブレインフォグ / 午後 |
| 尺 | 60分 |
| 舞台 | 茶室 |
| 茶丸 | 片目 |

**⑤ Gemini — 動画用背景**
```
A photorealistic interior of a traditional Japanese wa-modern tea room beside a small charcoal hibachi brazier on a quiet winter afternoon, shot at eye level, front view. A worn dark wooden table surface fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale afternoon light comes from a shoji window on the left, with a faint warm glow from the hibachi coals. Beyond the window, a snow-covered garden is visible, softly blurred. The scene is deliberately sparse and uncluttered. In the blurred background: tatami mats and a plain shoji screen, out of focus, with very few objects. Muted amber glow against pale white snow light and dark wood, still and quiet. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景**
```
A photorealistic interior of a traditional Japanese wa-modern tea room beside a small charcoal hibachi brazier on a quiet winter afternoon, shot at eye level, front view, 16:9. A worn dark wooden table surface fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft pale afternoon light comes from a shoji window on the left, with a faint warm glow from the hibachi coals on the left. Beyond the window, a snow-covered garden is visible on the left, softly blurred. The right third of the frame is a plain shoji screen in shadow, simple and uncluttered. Muted amber glow against pale white snow light and dark wood, gentle contrast between the lit left side and the shadowed right side. Shallow depth of field, gentle natural lighting, fine grain, high-detail craft photography style.
```

---

## 47 ｜ 画面疲れ（雪の夕暮れの窓辺・60分）⚠️暖色を抑える

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | 画面疲れ / 夕暮れ |
| 尺 | 60分 |
| 舞台 | 窓辺 |
| 茶丸 | 正面 |

**⑤ Gemini — 動画用背景**
```
A photorealistic interior of a traditional Japanese wa-modern room by a window at dusk during a quiet snowfall, shot at eye level, front view. A worn dark wooden window ledge fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft dim grey-blue light comes through the shoji window on the left, low and weak, the room settling into shadow. Beyond the window, snow is falling quietly over a dim garden, softly blurred, with no warm colour — only deep blue and grey. In the blurred background: tatami mats and a paper screen, out of focus, with very few objects. Muted grey-blue and dark wood, very low saturation, dim and restful. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景**
```
A photorealistic interior of a traditional Japanese wa-modern room by a window at dusk during a quiet snowfall, shot at eye level, front view, 16:9. A worn dark wooden window ledge fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. Soft dim grey-blue light comes through the shoji window on the left, low and weak. Beyond the window, snow is falling quietly over a dim garden, visible on the left, softly blurred, with no warm colour — only deep blue and grey. The right third of the frame is a plain shoji screen in deep shadow, simple and uncluttered. Muted grey-blue and dark wood, very low saturation, dim and restful. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style.
```

> `with no warm colour — only deep blue and grey` を消さないこと（10月の33・37における「紅葉なし」と同じ狙い＝彩度を上げない）。

---

## 48 ｜ 画面疲れ（熾火の夕暮れの囲炉裏端・60分）⚠️暖色を抑える

| 項目 | 内容 |
|---|---|
| 状態 / 時間帯 | 画面疲れ / 夕暮れ |
| 尺 | 60分 |
| 舞台 | 囲炉裏端 |
| 茶丸 | 正面 |

**⑤ Gemini — 動画用背景**
```
A photorealistic interior of a traditional Japanese wa-modern room beside a sunken irori hearth at dusk during a quiet snowfall, shot at eye level, front view. A worn dark wooden floor beside the hearth fills the foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. A dim glow from the low dying embers comes from the left, the room settling into shadow. Through a small window, snow is falling quietly in the fading light outside, softly blurred, with no warm colour beyond the embers — only deep blue and grey. In the blurred background: a hanging iron kettle and tatami mats, out of focus, with very few objects. Muted ember-glow amber against deep blue-grey dusk and dark wood, very low saturation, dim and restful. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style. 16:9.
```

**⑤ Gemini — サムネ用背景**
```
A photorealistic interior of a traditional Japanese wa-modern room beside a sunken irori hearth at dusk during a quiet snowfall, shot at eye level, front view, 16:9. A worn dark wooden floor beside the hearth fills the lower foreground, with an empty clear space in the center foreground where a small object will sit — nothing placed in the center. A dim glow from the low dying embers comes from the left, the room settling into shadow. Through a small window, snow falling quietly in the fading light is visible on the left, softly blurred, with no warm colour beyond the embers — only deep blue and grey. The right third of the frame is plain tatami and a dark wall in deep shadow, simple and uncluttered. Muted ember-glow amber against deep blue-grey dusk and dark wood, very low saturation, dim and restful. Shallow depth of field, low-key gentle lighting, fine grain, high-detail craft photography style.
```

> `with no warm colour beyond the embers — only deep blue and grey` を消さないこと。47と48は同じ「暖色を抑える」方針だが、48だけ熾火の暖色を画面内の唯一のアクセントとして残す設計（37・38が同じ縁側で色を対比させたのと同様、47＝寒色のみ／48＝熾火の暖色1点だけ許容）。

---
