#!/usr/bin/env python3
"""Build dist/index.html (a standalone page) from src/clipflow.html (the artifact fragment).

The fragment starts with <title>, <link> and <style> tags, which are moved into <head>.
Everything after them becomes <body>.
"""
import re
from pathlib import Path

root = Path(__file__).parent
src = (root / "src" / "clipflow.html").read_text(encoding="utf-8")

head_parts = []
for pattern in (r"<title>.*?</title>", r"<link\b[^>]*>", r"<style>.*?</style>"):
    for m in re.finditer(pattern, src, flags=re.S):
        head_parts.append(m.group(0))
        src = src.replace(m.group(0), "", 1)
body = src.strip()

icon = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
    "%3Crect width='32' height='32' rx='9' fill='%23F97316'/%3E"
    "%3Cpath d='M12.5 9.5v13L23 16z' fill='%23fff' stroke='%23fff' stroke-width='2' stroke-linejoin='round'/%3E%3C/svg%3E"
)

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="ClipFlow is an AI-powered short-form content production system. Plan clips, track them from idea to ready, and score quality before you publish.">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="{icon}">
<style>
:root{{padding-block:env(safe-area-inset-top,0px) env(safe-area-inset-bottom,0px)}}
body{{margin:0}}
img{{max-width:100%}}
[hidden]{{display:none!important}}
</style>
{chr(10).join(head_parts)}
</head>
<body>
{body}
</body>
</html>
"""

out = root / "dist"
out.mkdir(exist_ok=True)
(out / "index.html").write_text(page, encoding="utf-8")
print(f"wrote {out / 'index.html'} ({len(page):,} bytes)")
