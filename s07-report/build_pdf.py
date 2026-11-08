#!/usr/bin/env python3
"""Build S07_VAPT_Report.html from README.md (styled for PDF printing)."""

import re
import markdown
from pathlib import Path

SRC = Path(__file__).parent / "README.md"
OUT = Path(__file__).parent / "S07_VAPT_Report.html"

md_text = SRC.read_text(encoding="utf-8")

# The printable body starts at the Executive Summary - the title/metadata
# table above it is replaced by the HTML cover page.
body = md_text[md_text.index("# 1. Executive summary"):]
body_html = markdown.markdown(body, extensions=["tables", "fenced_code"])

# Fix image paths so relative Figures/ links resolve when opened from file
body_html = body_html.replace('src="Figures/', 'src="Figures/')

CSS = """
@page { size: A4; margin: 20mm 16mm; }
* { box-sizing: border-box; }
body { font-family: Georgia, 'Times New Roman', serif; color: #1a2332;
       font-size: 10.5pt; line-height: 1.55; margin: 0; }
.cover { page-break-after: always; text-align: center; padding-top: 70mm; }
.cover h1 { font-size: 24pt; border: none; color: #0d3b4f; }
.cover .sub { font-size: 12pt; color: #555; margin-top: 6mm; }
.cover .meta { margin-top: 24mm; font-size: 10.5pt; color: #333;
               display: inline-block; text-align: left; line-height: 2; }
h1 { font-family: 'Segoe UI', Arial, sans-serif; color: #0d3b4f;
     font-size: 16pt; border-bottom: 2.5px solid #17a398;
     padding-bottom: 4px; page-break-before: always; margin-top: 0; }
h1:first-of-type { page-break-before: avoid; }
h2 { font-family: 'Segoe UI', Arial, sans-serif; color: #0d3b4f;
     font-size: 12.5pt; margin-top: 18px; }
h3 { font-family: 'Segoe UI', Arial, sans-serif; color: #12566a; font-size: 11pt; }
table { border-collapse: collapse; width: 100%; margin: 10px 0;
        font-size: 9.5pt; page-break-inside: avoid; }
th { background: #0d3b4f; color: #fff; text-align: left; padding: 5px 8px;
     font-family: 'Segoe UI', Arial, sans-serif; font-size: 9.5pt; }
td { border: 1px solid #b9c4cc; padding: 5px 8px; vertical-align: top; }
tr:nth-child(even) td { background: #f2f6f8; }
code { font-family: Consolas, 'Courier New', monospace; background: #eef2f4;
       padding: 1px 4px; border-radius: 3px; font-size: 9pt; color: #0d3b4f; }
pre { background: #f4f7f9; border: 1px solid #d3dde3; border-left: 4px solid #17a398;
      padding: 9px 12px; overflow-x: auto; page-break-inside: avoid; }
pre code { background: none; padding: 0; font-size: 8.8pt; color: #1a2332; }
blockquote { border-left: 4px solid #17a398; margin: 10px 0; padding: 2px 14px;
             background: #f0f7f6; color: #22505c; }
img { max-width: 100%; border: 1px solid #ccd6dc; margin: 6px 0;
      page-break-inside: avoid; }
em { color: #555; }
hr { border: none; border-top: 1px solid #ccd6dc; margin: 16px 0; }
a { color: #12566a; text-decoration: none; }
"""

COVER = """
<div class="cover">
  <h1>Vulnerability Assessment &amp; Penetration Test Report</h1>
  <div class="sub">Target: Metasploitable 2 at 10.0.2.5</div>
  <div class="meta">
    <b>Prepared by:</b> &lt;STUDENT NAME&gt; - DFCS Bootcamp, Atomcamp<br>
    <b>Date of assessment:</b> &lt;DATE&gt;<br>
    <b>Classification:</b> CONFIDENTIAL - training submission<br>
    <b>Engagement type:</b> Grey-box VA with controlled exploitation
  </div>
</div>
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>S07 VA/PT Report</title>
<style>{CSS}</style>
</head>
<body>
{COVER}
{body_html}
</body>
</html>"""

OUT.write_text(html, encoding="utf-8")
print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
