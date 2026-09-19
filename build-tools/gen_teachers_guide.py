#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 'Bible Truth Foundation Pt3 - Teachers Guide.html' matching the
exact structure/CSS of the Pt1/Pt2 Teacher's Guide files.
Run from the biblefoundations folder root.
"""
import sys, os, html as htmlmod
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p3_lessons import LESSONS
from p3_teacher_notes import TEACHER_NOTES

SECTION_NAMES = {
    'A': "Living in the Spirit's Power",
    'B': 'Living Among Others',
    'C': 'Living Free from Law and Sin',
    'D': 'Living as a Disciple',
}

CSS = ("*,*::before,*::after{box-sizing:border-box}body{margin:0;padding:0 16px;font-family:Arial,Helvetica,sans-serif;"
"font-size:15px;line-height:1.6;color:#1c1c1e;background:#fff}@media(min-width:640px){body{padding:0 32px}}"
"@media(min-width:900px){body{max-width:900px;margin:0 auto}}\n"
"h1{font-size:26px;font-weight:700;color:#1F3864;text-align:center;margin:40px 0 4px}"
"h2{font-size:22px;font-weight:700;color:#1F3864;text-transform:uppercase;letter-spacing:.07em;margin-top:40px}"
"h3{font-size:18px;font-weight:700;color:#1F3864;margin-top:28px;border-bottom:1px solid #ccc;padding-bottom:4px}\n"
".sub{text-align:center;font-size:19px;font-weight:400;color:#1F3864;margin:0 0 4px}"
".church{text-align:center;font-size:13px;color:#777;margin:0 0 16px}"
".rule{border:none;border-top:2px solid #1F3864;margin:12px auto 32px}\n"
"table{border-collapse:collapse;width:100%;font-size:14px}th{background:#1F3864;color:#fff;font-weight:700;"
"letter-spacing:.04em;padding:10px 14px;text-align:left}td{border:1px solid #ccc;padding:10px 14px;vertical-align:top}"
"tr:nth-child(even) td{background:#f2f2f2}\n"
".twrap{overflow-x:auto}.aim{border-left:4px solid #d97706;background:#fffbf0;padding:12px 16px;margin:16px 0}"
".aim b{color:#1F3864}\n"
".core{background:#1F3864;color:#fff;padding:14px 18px;border-radius:4px;margin:14px 0}"
".core .lbl{color:#f0b429;font-size:11px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;margin:0 0 6px}"
".core p{margin:0}\n"
"ul{padding-left:20px}li{margin-bottom:8px}.pastoral{background:#f0f4fb;border-left:4px solid #1F3864;padding:12px 16px;margin:14px 0}"
".pastoral .lbl{font-size:11px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:#1F3864;margin:0 0 6px}"
".pastoral p{margin:0}\n"
".foot{font-size:13px;color:#888;text-align:center;border-top:1px solid #ccc;padding:24px 0 40px;margin-top:40px}"
"@media print{body{background:#fff}}")

def lesson_block(L):
    notes = TEACHER_NOTES[L['num']]
    watch_items = ''.join(f'<li>{w}</li>' for w in notes['watch_for'])
    return (
        f"<h3>Lesson {L['num']:02d}: {L['title']}</h3>\n"
        f"<div class=\"aim\"><b>Facilitator’s aim:</b> {notes['aim']}</div>\n"
        f"<p><b>Key Scripture:</b> {L['ks_ref']} &mdash; <em>{L['ks_text']}</em></p>\n"
        f"<div class=\"core\"><p class=\"lbl\">Core Truth</p><p>{L['core']}</p></div>\n"
        f"<p><b>Watch for:</b></p><ul>{watch_items}</ul>\n"
        f"<div class=\"pastoral\"><p class=\"lbl\">Pastoral note</p><p>{notes['pastoral']}</p></div>\n"
    )

def build_body():
    out = []
    out.append('<h2>Part A: How to Use This Guide</h2>\n')
    out.append('<p>This guide accompanies the sixteen student lessons of Part 3 and is for facilitators only; it is never distributed with the student files. Each lesson entry below gives the facilitator’s aim, the key scripture and core truth as they appear in the student material, specific things to watch for in the room, and a pastoral note. The student lesson carries the full teaching text; your role is not to re-teach it but to steward the discussion it opens.</p>\n')
    out.append('<p>Suggested session shape (75&ndash;90 minutes): open with the Opening Question cold, before any teaching (10 minutes); read the Key Scripture aloud and let the group sit with it (5); walk the Bible Teaching section together, expanding where the room needs it (25&ndash;30); Group Discussion Questions (20); Application and prayer (15). Key Discovery Questions are completed by members at home before the session; begin discussion by asking what they found.</p>\n')
    out.append('<p>All scripture in the series is New King James Version, declared once at series level. British English throughout. Lessons build in order; resist requests to jump ahead, especially into Section C (Lessons 7&ndash;11), which depends on the freedom-in-Christ foundation of Sections A and B.</p>\n')
    out.append('<h2>Part B: Per-Lesson Guide</h2>\n')
    for sec in ['A', 'B', 'C', 'D']:
        out.append(f'<h3 style="border:none;background:#f2f2f2;padding:8px 12px;">Section {sec} &mdash; {SECTION_NAMES[sec]}</h3>\n')
        for L in [x for x in LESSONS if x['section'] == sec]:
            out.append(lesson_block(L))
    out.append('<h2>Part C: Quick Reference Table</h2>\n')
    out.append('<div class="twrap"><table>\n<thead><tr><th>Lesson</th><th>Title</th><th>Section</th><th>Key Scripture</th><th>Anchor of the session</th></tr></thead>\n<tbody>\n')
    for L in LESSONS:
        notes = TEACHER_NOTES[L['num']]
        out.append(f"<tr><td>{L['num']:02d}</td><td>{L['title']}</td><td>{L['section']}: {SECTION_NAMES[L['section']]}</td><td>{L['ks_ref']}</td><td>{notes['aim']}</td></tr>\n")
    out.append('</tbody></table></div>\n')
    return ''.join(out)

def main():
    body = build_body()
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Teacher’s Guide &ndash; Bible Truth Foundations Part 3 | The Well Shrewsbury</title>
<style>{CSS}</style>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
</head>
<body>
<h1>Teacher’s Guide</h1>
<p class="sub">Bible Truth Foundations &ndash; Part 3 of 3: Serving in Christ</p>
<p class="church">The Well Shrewsbury</p>
<hr class="rule">
{body}<p class="foot">Bible Truth Foundations &middot; Part 3 of 3: Serving in Christ &middot; Teacher’s Guide &middot; The Well Shrewsbury<br>Based on the Discipleship Evangelism Programme by Andrew Wommack and Don W. Krow. Courtesy of delessons.org. Used with permission.</p>
</body>
</html>
"""
    out_path = 'Bible Truth Foundation Pt3 - Teachers Guide.html'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(doc)
    print(f"Written: {out_path} ({len(doc)} chars)")

if __name__ == '__main__':
    main()
