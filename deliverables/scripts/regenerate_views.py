#!/usr/bin/env python3
"""
160曲の「Sunoプロンプトだけ一括コピペしたい」「タイトル/概要/タグを一覧で見たい」といった
一時的なニーズのために、正本（series_*/HANDOFF_*.md）から都度ビューを生成するスクリプト。

設計方針：
- 正本は series_*/HANDOFF_*_自動生成用.md の16ファイルだけ。ここが唯一のソース。
- 派生ビュー（Suno一括・タイトル一覧など）は「常設ファイルとして repo に置かない」。
  必要な時にこのスクリプトで生成し、使い終わったら消してよい。
  （常設すると正本との二重管理になり、更新時に片方だけ直して不整合が起きるため）

使い方：
    python3 regenerate_views.py suno   > /tmp/全曲_suno.md
    python3 regenerate_views.py titles > /tmp/全曲_タイトル一覧.md
"""
import re, os, sys

BASE = os.path.join(os.path.dirname(__file__), "..")

SERIES = [
    ("S1", "雨の書庫", "series_雨の書庫/HANDOFF_雨の書庫_自動生成用.md"),
    ("S2", "神々の温泉宿", "series_神々の温泉宿/HANDOFF_神々の温泉宿_自動生成用.md"),
    ("S3", "異界列車", "series_異界列車/HANDOFF_異界列車_自動生成用.md"),
    ("S4", "雪灯りの宿", "series_雪灯りの宿/HANDOFF_雪灯りの宿_自動生成用.md"),
    ("S5", "神域の滝", "series_神域の滝/HANDOFF_神域の滝_自動生成用.md"),
    ("S6", "蛍火の沢", "series_蛍火の沢/HANDOFF_蛍火の沢_自動生成用.md"),
    ("S7", "囲炉裏の間", "series_囲炉裏の間/HANDOFF_囲炉裏の間_自動生成用.md"),
    ("S8", "潮騒の社", "series_潮騒の社/HANDOFF_潮騒の社_自動生成用.md"),
    ("D1", "剣戟の写本", "series_剣戟の写本/HANDOFF_剣戟の写本_自動生成用.md"),
    ("D2", "鬼哭の戦記", "series_鬼哭の戦記/HANDOFF_鬼哭の戦記_自動生成用.md"),
    ("D3", "陣太鼓の号令", "series_陣太鼓の号令/HANDOFF_陣太鼓の号令_自動生成用.md"),
    ("D4", "忍びの影", "series_忍びの影/HANDOFF_忍びの影_自動生成用.md"),
    ("D5", "神風の刃", "series_神風の刃/HANDOFF_神風の刃_自動生成用.md"),
    ("D6", "龍神の逆鱗", "series_龍神の逆鱗/HANDOFF_龍神の逆鱗_自動生成用.md"),
    ("D7", "妖刀奇譚", "series_妖刀奇譚/HANDOFF_妖刀奇譚_自動生成用.md"),
    ("D8", "祭囃子の乱", "series_祭囃子の乱/HANDOFF_祭囃子の乱_自動生成用.md"),
]


def parse_series(relpath):
    path = os.path.join(BASE, relpath)
    with open(path, encoding="utf-8") as f:
        text = f.read()

    m = re.search(r'# ■ タグ\s*共通.*?\n```\n(.*?)\n```', text, re.DOTALL)
    tags = m.group(1).strip() if m else None

    parts = re.split(r'\n## ', text)
    tracks = []
    for p in parts[1:11]:
        lines = p.split("\n")
        heading = lines[0].strip()
        body = "\n".join(lines[1:])

        # title: either "【タイトル】\n```\n...\n```" or "タイトル：..." plain line
        title = None
        m1 = re.search(r'【タイトル】\n```\n(.*?)\n```', body, re.DOTALL)
        if m1:
            title = m1.group(1).strip()
        else:
            m2 = re.search(r'^タイトル：(.*)', body, re.MULTILINE)
            if m2:
                title = m2.group(1).strip()

        # story
        story = None
        m3 = re.search(r'^物語：(.*)', body, re.MULTILINE)
        if m3:
            story = m3.group(1).strip()
        else:
            m4 = re.search(r'【物語イントロ】\n```\n(.*?)\n```', body, re.DOTALL)
            if m4:
                story = m4.group(1).strip().replace("\n", " ")

        # suno: either 【Suno完全版】marker or first code block after title/story lines
        suno = None
        m5 = re.search(r'【Suno完全版】\s*\n```\n(.*?)\n```', body, re.DOTALL)
        if m5:
            suno = m5.group(1).strip()
        else:
            m6 = re.search(r'```\n(.*?)\n```', body, re.DOTALL)
            if m6:
                suno = m6.group(1).strip()

        tracks.append({"heading": heading, "title": title, "story": story, "suno": suno})

    return {"tags": tags, "tracks": tracks}


def build_suno_view():
    out = ["# 全160曲｜Sunoプロンプト（このスクリプトで都度生成・常設しない）\n"]
    for code, name, relpath in SERIES:
        d = parse_series(relpath)
        kind = "静" if code.startswith("S") else "動"
        out.append(f"\n## {code}｜{name}（{kind}）\n")
        for t in d["tracks"]:
            out.append(f"### {t['heading']}")
            out.append("```")
            out.append(t["suno"] or "!!! NOT FOUND !!!")
            out.append("```")
    return "\n".join(out)


def build_titles_view():
    out = ["# 全160曲｜タイトル・概要・タグ（このスクリプトで都度生成・常設しない）\n"]
    for code, name, relpath in SERIES:
        d = parse_series(relpath)
        kind = "静" if code.startswith("S") else "動"
        out.append(f"\n## {code}｜{name}（{kind}）\n")
        out.append(f"**タグ（全曲共通）**\n```\n{d['tags']}\n```\n")
        for t in d["tracks"]:
            out.append(f"### {t['heading']}")
            out.append(f"**タイトル**：{t['title'] or '!!! NOT FOUND !!!'}")
            out.append(f"**概要**：{t['story'] or '!!! NOT FOUND !!!'}")
            out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "suno"
    if mode == "suno":
        print(build_suno_view())
    elif mode == "titles":
        print(build_titles_view())
    else:
        print("Usage: regenerate_views.py [suno|titles]", file=sys.stderr)
        sys.exit(1)
