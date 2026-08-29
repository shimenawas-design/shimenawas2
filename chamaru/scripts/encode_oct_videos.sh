#!/bin/bash
# 茶丸の間 10月分（30〜38）動画エンコード。統合マスターの付録「制作フロー」記載の
# ffmpeg zoompanパラメータどおりに実行する。

set -e
cd "C:/Users/shime/Downloads/茶丸"

encode() {
  local id="$1" dir="$2" bg="$3" audio="$4" out="$5" duration="$6" d="$7" zinc="$8" fade_st="$9" loop="${10}"
  local bgpath="$dir/$bg"
  local audiopath="$dir/$audio"
  local outpath="$dir/$out"
  local W=$(python -c "from PIL import Image; print(Image.open(r'$bgpath').width)")
  local H=$(python -c "from PIL import Image; print(Image.open(r'$bgpath').height)")
  local cw=$(python -c "print((int($H*16/9)//2)*2)")

  echo "=== [$id] encoding -> $outpath (crop=${cw}:${H}, d=$d, loop=$loop) ==="

  if [ "$loop" = "yes" ]; then
    ffmpeg -y -i "$bgpath" -stream_loop -1 -i "$audiopath" -t "$duration" \
      -vf "crop=${cw}:${H},zoompan=z=zoom+${zinc}:d=${d}:x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):s=1920x1080:fps=24,format=yuv420p" \
      -r 24 -map 0:v:0 -map 1:a:0 -c:v libx264 -preset veryfast -crf 21 -pix_fmt yuv420p \
      -c:a aac -b:a 192k -af "afade=t=in:st=0:d=3,afade=t=out:st=${fade_st}:d=15" -movflags +faststart \
      "$outpath" 2>&1 | tail -5
  else
    ffmpeg -y -i "$bgpath" -i "$audiopath" -t "$duration" \
      -vf "crop=${cw}:${H},zoompan=z=zoom+${zinc}:d=${d}:x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):s=1920x1080:fps=24,format=yuv420p" \
      -r 24 -map 0:v:0 -map 1:a:0 -c:v libx264 -preset veryfast -crf 21 -pix_fmt yuv420p \
      -c:a aac -b:a 192k -af "afade=t=in:st=0:d=3,afade=t=out:st=${fade_st}:d=15" -movflags +faststart \
      "$outpath" 2>&1 | tail -5
  fi
  echo "=== [$id] done ==="
}

# id dir bg audio out duration d zinc fade_st loop
encode 30 "30_集中_紅葉の朝の庭"               "bg30_with_chamaru.png" "紅葉の庭で集中する60分.wav"           "紅葉の庭で集中する60分.mp4"           3600 86400  0.00000092593 3585 yes
encode 31 "31_安眠_紅葉の宵の庭"               "bg31_with_chamaru.png" "紅葉の庭が暮れていく90分.wav"          "紅葉の庭が暮れていく90分.mp4"          5400 129600 0.00000061728 5385 yes
encode 32 "32_リセット_紅葉の午後の窓辺"        "bg32_with_chamaru.png" "午後の窓辺で紅葉を眺める90分.wav"       "午後の窓辺で紅葉を眺める90分.mp4"       5400 129600 0.00000061728 5385 yes
encode 33 "33_画面疲れ_雨の夕暮れの茶室"        "bg33_with_chamaru.png" "雨の夕暮れに目を休める60分.wav"         "雨の夕暮れに目を休める60分.mp4"         3600 86400  0.00000092593 3585 yes
encode 34 "34_ブレインフォグ_紅葉の午後の囲炉裏端" "bg34_with_chamaru.png" "頭が回らない秋の午後に60分.wav"         "頭が回らない秋の午後に60分.mp4"         3600 86400  0.00000092593 3585 yes
# 35は動作確認テストで既に生成済み（スキップ）
encode 36 "36_集中_紅葉の朝の窓辺"              "bg36_with_chamaru.png" "紅葉の窓辺で集中する60分.wav"           "紅葉の窓辺で集中する60分.mp4"           3600 86400  0.00000092593 3585 yes
encode 37 "37_画面疲れ_苔庭の夕暮れの縁側"      "bg37_with_chamaru.png" "苔庭を眺めて目を休める60分.wav"         "苔庭を眺めて目を休める60分.mp4"         3600 86400  0.00000092593 3585 yes
encode 38 "38_安眠_秋の夜長の縁側"              "bg38_with_chamaru.png" "秋の夜長に雨を聴きながら眠る90分.wav"   "秋の夜長に雨を聴きながら眠る90分.mp4"   5400 129600 0.00000061728 5385 yes

echo "ALL_DONE"
