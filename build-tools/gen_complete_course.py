#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate btf-Pt3 Complete Course.md from p3_lessons.py, matching the
Pt1/Pt2 Complete Course markdown pattern exactly.
Run from the biblefoundations folder root.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from p3_lessons import LESSONS

SECTION_NAMES = {
    'A': "Living in the Spirit's Power",
    'B': 'Living Among Others',
    'C': 'Living Free from Law and Sin',
    'D': 'Living as a Disciple',
}

def teaching_md(items):
    out = []
    for it in items:
        k = it[0]
        if k == 'h3':
            out.append(f'#### {it[1]}\n')
        elif k == 'p':
            out.append(f'{it[1]}\n')
        elif k == 'scripture':
            out.append(f'**{it[1]}**\n> *{it[2]}*\n')
        elif k == 'callout':
            label = {'note': 'Note', 'depth': 'Going Deeper', 'caution': 'Caution', 'tip': 'Practical Tip'}[it[1]]
            out.append(f'**{label}:** {it[2]}\n')
    return '\n'.join(out)

def lesson_md(L):
    out = []
    out.append(f"# Lesson {L['num']:02d}: {L['title']}\n")
    out.append(f"*Lesson {L['num']} of 16  |  Section {L['section']}: {L['section_name']}*\n")
    out.append("\n### Opening Question\n")
    out.append(f"**{L['opening']}**\n")
    out.append("\n### Key Scripture\n")
    out.append(f"**{L['ks_ref']}**\n> *{L['ks_text']}*\n")
    out.append(f"\n*{L['ks_note']}*\n")
    out.append("\n### Core Truth\n")
    out.append(f"**{L['core']}**\n")
    out.append("\n### Bible Teaching\n\n")
    out.append(teaching_md(L['teaching']))
    out.append("\n\n### Key Discovery Questions\n\n")
    for i, q in enumerate(L['kdq'], 1):
        out.append(f"{i}. {q}\n\n")
    out.append("### Group Discussion Questions\n\n")
    for i, q in enumerate(L['gdq'], 1):
        out.append(f"{i}. {q}\n\n")
    out.append("### Application\n\n")
    out.append(f"{L['app_intro']}\n\n")
    for label, text in L['app']:
        out.append(f"- **{label}.** {text}\n\n")
    out.append("### Revision Cards\n\n")
    for c in L['cards']:
        ref_part = f" ({c['ref']})" if c.get('ref') else ''
        out.append(f"- **Q:** {c['front']}{ref_part}  \n")
        if c['back_type'] == 'verse':
            out.append(f"  **A:** {c['back']} {c['back_ref']}\n\n")
        else:
            out.append(f"  **A:** {c['back']}\n\n")
    return ''.join(out)

def build_toc():
    out = []
    for sec in ['A', 'B', 'C', 'D']:
        lessons_in_sec = [L for L in LESSONS if L['section'] == sec]
        out.append(f"#### Section {sec}: {SECTION_NAMES[sec]}\n\n")
        for L in lessons_in_sec:
            out.append(f"- **L{L['num']:02d}** {L['title']}\n")
        out.append("\n")
    return ''.join(out)

def main():
    parts = []
    parts.append("# Bible Truth Foundations\n")
    parts.append("## Part 3 of 3: Serving in Christ\n")
    parts.append("### The Well Shrewsbury\n\n")
    parts.append("---\n\n")
    parts.append("> This is the complete course text for Part 3. All scripture quotations throughout the series are taken from the New King James Version. Based on the Discipleship Evangelism Programme by Andrew Wommack and Don W. Krow, courtesy of delessons.org, used with permission for discipleship purposes, free of charge.\n\n\n")
    parts.append("### Lessons\n\n\n")
    parts.append(build_toc())
    parts.append("---\n\n\n")
    for L in LESSONS:
        parts.append(lesson_md(L))
        parts.append("\n\n---\n\n\n")

    content = ''.join(parts)
    out_path = 'btf-Pt3 Complete Course.md'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Written: {out_path} ({len(content)} chars)")

if __name__ == '__main__':
    main()
