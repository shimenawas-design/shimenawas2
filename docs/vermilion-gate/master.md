# Vermilion Gate マスタードキュメント

**作成日：2026-08-30**（現状の状態のみを載せた軽量版）
関連：[../policy.md](../policy.md)（規約・配信先・AI環境、両プロジェクト共通）

---

## 1. プロジェクト概要

| 項目 | 値 |
|---|---|
| アーティスト名義 | `Vermilion Gate` |
| ジャンル | ファンタジー風・和風。エピック/シネマティック |
| 音源の来歴 | 既に YouTube に公開済みの楽曲群（AI生成・Suno）。今回 RouteNote 経由でのストリーミング配信を追加する |
| ディストリビューター | RouteNote（Level Trim / Ongaku Toshokan と同一アカウント、名義のみ分離） |
| C/Pライン | 本名（川上悟志 / Satoshi Kawakami） |
| YouTubeチャンネルの収益化（YPP） | **されていない**（2026-08-30 確認済み） |

### 他プロジェクトとの違い（重要）

Level Trim / Ongaku Toshokan は`no build-up, no climax`が設計DNAだが、**このプロジェクトは逆に、盛り上がり（ビルドアップ・クライマックス）があってこそ成立するジャンル**。プロンプト設計・審査観点ともに他2プロジェクトの流用ができない。

---

## 2. 名義の決定経緯

`Yugen`→`Tatara`→`Kumiko`→`Ninth Torii`を検討し、いずれも既存アーティストとの衝突・類似名の乱立で却下。**`Vermilion Gate`は2026-08-30時点のWeb検索で完全一致なし。**

⚠️ **これは検索エンジン経由の簡易確認にとどまる。RouteNote入稿画面またはSpotify/Apple Musicアプリ内検索での直接確認はまだ済んでいない。入稿前に必ず実施すること。**

---

## 3. ボーカルテクスチャの扱い（決定事項）

音源の一部に**ハミング程度の、歌詞のないヴォーカルテクスチャ**が混入していることが判明（2026-08-30）。

**Level Trimのハミング混入とは扱いが異なる**：Level Trimの設計DNA（`instrumental, no vocals`）への違反だったのに対し、ファンタジー/エピック系劇伴では**歌詞のないヴォーカル（エセリアル・コーラス／ヴォカリーズ）は正統な様式**（『ロード・オブ・ザ・リング』等の劇伴で多用される技法）。よって「欠陥」ではなく「活かせる要素」として扱う。

### 運用ルール

| 項目 | 値 |
|---|---|
| **ジャンル**（全曲共通） | Soundtrack / Cinematic（統一する。曲によって変えない） |
| **Instrumentalフラグ** | **全70曲ON で確定（2026-09-06）**。歌詞のないヴォーカル（ハミング/ヴォカリーズ/コーラス）はDSP業界共通で「Instrumental」の対象外に含まれない、との判断（RouteNote一次情報に直接の定義記事はなし、映画音楽での一般的な扱いに準拠）。曲ごとの試聴判定は不要 |

**ジャンルを統一し、フラグだけを曲ごとに変える**のが要点。ジャンル欄自体を曲によって変えると、Spotify等のアルゴリズムに対して分類信号が割れる（Level Trimで警戒したのと同じ問題）。RouteNoteの入稿画面に「Instrumental」が独立したジャンル選択肢としてしか存在しない仕様だった場合は、この運用を再検討する（**入稿画面の実際の項目構成は未確認**）。

### 判断基準（新曲・既存曲とも）
実際に聴いて「神秘的・幻想的に聞こえるか」「不自然・チープに聞こえるか」で判断する。前者ならそのまま活かす。後者ならLevel Trim/Warm Cacheと同様の除去処理を検討する。

---

## 4. リスク管理

### 🔴 最優先：既存YouTube動画とのContent ID衝突
音源は**既に公開済みのYouTube動画**として存在する。RouteNoteはAI楽曲のためContent ID登録の対象外だが（[../policy.md](../policy.md)参照）、**入稿時にYouTube Content IDのチェックを外し忘れると、この既存動画と衝突してクレームが発生し得る**。Level Trim/Ongaku Toshokanの新曲（まだYouTubeに存在しない）とは異なり、**衝突相手が実在する**点が今回特有のリスク。

現在YPP未収益化のため、衝突しても凍結される広告収益はない。ただし動画へのクレーム表示自体は起こり得るため、チェック解除は必須作業として扱う。

### 🟡 要確認：ヴォーカルテクスチャの実在アーティストとの類似
RouteNoteの2026年1月AIポリシーは「実在アーティストの声を模倣・混同させる内容」を拒否対象としている（[../policy.md](../policy.md)参照）。歌詞のないハミングのため該当リスクは低いが、特定の歌手の声質に酷似していないか一度確認すること。

---

## 5. 曲一覧（2026-09-06 棚卸し確定・全70曲）

`main`ブランチ `ongakutoshokan/動シリーズ` `/静シリーズ` にBPM解析によるテイク選定結果あり（`_選定結果.md`）。**同一素材だが、ジャンル信号を汚さないようVermilion Gate名義で配信する。**

**ユーザー判断（2026-09-06）**：曲ごとのヴォーカルテクスチャ試聴・取捨選択はせず、このまま全曲出す方針。

| シリーズ | 曲数 | 各曲尺目安 | 選定元 |
|---|---|---|---|
| D1 剣戟の写本 | 10 | フルアルバム72.9分÷10 | `ongakutoshokan/動シリーズ/D1_剣戟の写本/_選定結果.md`(main) |
| D2 鬼哭の戦記 | 10 | フルアルバム53.4分÷10 | 同上フォルダ |
| D3 陣太鼓の号令 | 10 | フルアルバム49.9分÷10 | 同上フォルダ |
| D4 忍びの影 | 10 | フルアルバム51.1分÷10 | 同上フォルダ |
| S1 雨の書庫 | 10 | フルアルバム61.4分÷10 | `ongakutoshokan/静シリーズ/S1_雨の書庫/_選定結果.md`(main) |
| S2 神々の温泉宿 | 10 | フルアルバム61.4分÷10 | 同上フォルダ |
| S3 異界列車 | 10 | フルアルバム64.2分÷10 | 同上フォルダ |
| **合計** | **70** | | |

### RouteNote Track Title（英語+日本語原題併記、2026-09-06確定）

Ongaku Toshokanと同じ「English (原題)」方式。ソースは各シリーズ`_選定版/`フォルダ（`番号_曲名.wav/mp3`）。

**D1 剣戟の写本 / Chronicle of Blades**
1. Sealed Gate (封印の扉)
2. Drawing the Blade (抜刀)
3. Strike of the Swift Wind (疾風の一撃)
4. Blade Lock (鍔迫り合い)
5. Duel Under the Full Moon (満月の決闘)
6. Crimson Camellia Strike (紅椿の一閃)
7. Echo of Twin Blades (二刀の残響)
8. Flash Within the Storm (嵐中の一閃)
9. Decisive Blow (決着)
10. The Manuscript Closes (写本は閉じられて)

**D2 鬼哭の戦記 / War Record of the Weeping Oni**
1. Rising Menace (鬼気迫る)
2. The Roar (咆哮)
3. Formation of Demon Fire (鬼火の陣)
4. Strike of the Iron Club (金棒の一撃)
5. Wailing of the Demons (鬼哭啾々)
6. The Shattered Horn (角の砕ける音)
7. Rage of the Bloodline (血脈の怒り)
8. Facing the Demon God (鬼神との対峙)
9. Hour of Subjugation (討伐の刻)
10. The Demon Departs (鬼は去りて)

**D3 陣太鼓の号令 / Call of the War Drum**
1. The Conch Horn Sounds (法螺貝が鳴る)
2. Forming the Ranks (陣を敷く)
3. Vanguard Charge (先鋒突撃)
4. Battle of Arrows (矢戦)
5. The Full Assault (総攻撃)
6. Banners Unfurled (旗の翻る)
7. Single Combat (一騎打ち)
8. Pushing Back the Tide (押し返す)
9. Cry of Victory (勝鬨)
10. Breaking Camp (陣を払う)

**D4 忍びの影 / Shadow of the Shinobi**
1. Lurking in the Shadows (影に潜む)
2. Crossing the Rooftops (屋根を渡る)
3. Vanishing Presence (気配を消す)
4. Wind of the Shuriken (手裏剣の風)
5. The Waiting Trap (罠の間)
6. Footsteps of the Pursuers (追手の足音)
7. Smoke Bomb (煙玉)
8. Confrontation in the Rafters (屋根裏の対峙)
9. The Withdrawal (撤収)
10. The Shadow Vanishes (影は消えて)

**S1 雨の書庫 / The Rain-Soaked Archive**
1. The Rain Begins (雨のはじまり)
2. Rain on the Bookshelves (書架を打つ雨)
3. Rain on the Moss Garden (苔庭の雨)
4. Drops from the Eaves (軒の雫)
5. Study of Distant Thunder (遠雷の書斎)
6. Rain Through the Glass (硝子越しの雨)
7. Lamplight and Rainfall (灯りと雨音)
8. Midnight Downpour (真夜中の豪雨)
9. Stillness After the Rain (雨のあとの静けさ)
10. The Archive Asleep in Rain (雨に眠る書庫)

**S2 神々の温泉宿 / The Hot Spring Inn of the Gods**
1. Lantern Light of the Inn (湯宿の灯り)
2. Steam Over the Open Bath (湯けむりの露天)
3. Night Breeze on the Veranda (縁側の夜風)
4. Comfort of the Guest Room (客間の安らぎ)
5. Moon Over the Courtyard (中庭の月)
6. Distant Sound of the Spring (遠い湯の音)
7. Warmth and Rest (火照りと休息)
8. Midnight Indoor Bath (真夜中の内湯)
9. Bed of Slumber (まどろみの床)
10. The Inn at Dawn (夜明けの湯宿)

**S3 異界列車 / The Otherworld Train**
1. The Midnight Departure (始発は真夜中)
2. The Lantern Car (提灯の車両)
3. Station in the Fog (霧の停車場)
4. Crossing the Sea of Stars (星原を渡る夜)
5. Station of the Spirits (妖たちの停車駅)
6. Rain on the Iron Bridge (雨の鉄橋)
7. Passing the Glowing Shore (夜光の海辺を過ぎて)
8. Tunnel of the Torii (鳥居のトンネル)
9. Dawn Through the Window (夜明けの車窓)
10. Final Stop: The Library (終着、図書館へ)

※S4〜S8・D5〜D8は企画書のみで音源未制作（対象外）

## 6. 残タスク（優先順）

1. **アーティスト名の直接重複確認**（RouteNote入稿画面 or Spotify/Apple Musicアプリ）
2. ~~既存YouTube楽曲の棚卸し~~ → **完了（上記5章、全70曲）**。ヴォーカルテクスチャの有無は曲ごとに確認せず、全曲そのまま出す方針
3. ~~英語タイトルの用意~~ → **完了（上記5章、全70曲）**。Ongaku Toshokanと同じ「英語 (原題)」併記方式を採用
4. ~~音源フォーマット確認~~ → **完了（2026-09-06）**。全70曲を44.1kHzに変換、`RouteNote/Vermilion Gate/<シリーズ>-<番号>_<英語タイトル>/`に配置
   - **⚠️ 品質上限に注意**：D2・D3・D4・S2・S3の一部（計48曲）は元がWAVでなく約190kbpsのMP3のみで、320kbps FLACへの変換元WAVが存在しない。今回は320kbps/44.1kHzへ**形式上変換**したが、実際の音質は190kbps相当のまま（ユーザー判断・2026-09-06）
   - D1・S1・S3一部（計22曲）はWAVソースがあり、無劣化で44.1kHz FLAC化できている
5. ~~Instrumental判定~~ → **完了（2026-09-06）**。全70曲Instrumental=ONで統一（3章参照）
6. RouteNote入稿（[../policy.md](../policy.md)のAI楽曲チェックリスト参照。**YouTube Content ID解除を最優先で確認**）。入稿カレンダー`RouteNote/入稿予定/<日付>/`に5週分（9/12〜10/10）作成済み。各日付フォルダ内に曲ごとのサブフォルダを作り、音源・ジャケットの実体コピーを配置済み
7. **ジャケット画像・アートワークの準備 — 進行中（2026-09-06）**。動シリーズ（D1〜D4、計40曲）は元YouTube動画の既存サムネを`jacket_source`として転用可能と確認し、`RouteNote/Vermilion Gate/`および入稿カレンダー各曲フォルダに配置済み。静シリーズはS3の1〜3のみ確認済み（配置済み）、S1・S2・S3の4〜10は未確認。**全曲共通で、Canva 3000×3000へのリサイズは未実施**（ユーザー操作待ち）
