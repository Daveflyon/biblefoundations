#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert Part 3 sections into index.html, matching the exact pattern used
for Part 1 and Part 2, and update footer/TOC/title accordingly.
Run from the biblefoundations folder root.
"""
import re

with open('index.html', encoding='utf-8') as f:
    content = open('index.html', encoding='utf-8').read()

# --- Lesson data (title, slug, num) per section, matching p3_lessons.py ---
SECTIONS = [
    ("p3-section-a", "Section A &mdash; Living in the Spirit's Power",
     "Lessons 1&ndash;3. The divine flow of God's love, using spiritual gifts to minister, and why miracles exist to glorify God.",
     [
        (1, "the-divine-flow", "The Divine Flow"),
        (2, "using-the-gifts-to-minister", "Using the Gifts to Minister"),
        (3, "miracles-glorify-god", "Miracles Glorify God"),
     ]),
    ("p3-section-b", "Section B &mdash; Living Among Others",
     "Lessons 4&ndash;6. The power of godly relationships, facing persecution, and understanding the King and His Kingdom.",
     [
        (4, "the-power-of-godly-relationships", "The Power of Godly Relationships"),
        (5, "persecution", "Persecution"),
        (6, "the-king-and-his-kingdom", "The King and His Kingdom"),
     ]),
    ("p3-section-c", "Section C &mdash; Living Free from Law and Sin",
     "Lessons 7&ndash;11. The true object of saving faith, the proper use of God's Law, grace instead of law, no more consciousness of sin, and being fully loved.",
     [
        (7, "the-object-of-saving-faith", "The Object of Saving Faith"),
        (8, "the-proper-use-of-gods-law", "The Proper Use of God's Law"),
        (9, "not-under-law-but-under-grace", "Not Under Law, but Under Grace"),
        (10, "no-more-consciousness-of-sin", "No More Consciousness of Sin"),
        (11, "i-am-loved-i-am-pretty", "I Am Loved, I Am Pretty"),
     ]),
    ("p3-section-d", "Section D &mdash; Living as a Disciple",
     "Lessons 12&ndash;16. The fruit that proves genuine faith, the call to make disciples, using your testimony, and mobilising every believer's gifts.",
     [
        (12, "the-fruit-of-salvation-part-1", "The Fruit of Salvation (Part 1)"),
        (13, "the-fruit-of-salvation-part-2", "The Fruit of Salvation (Part 2)"),
        (14, "a-call-to-discipleship", "A Call to Discipleship"),
        (15, "how-to-use-your-testimony", "How to Use Your Testimony"),
        (16, "using-everyones-gifts-to-disciple", "Using Everyone's Gifts to Disciple"),
     ]),
]

def lesson_item(num, slug, title):
    fname = f"btf-p3-l{num:02d}-{slug}.html"
    return (f'      <a class="lesson-item" href="{fname}">\n'
            f'        <span class="lesson-num">{num:02d}</span>\n'
            f'        <div class="lesson-info"><p class="lesson-title">{title}</p></div>\n'
            f'        <span class="lesson-arrow" aria-hidden="true">&#8250;</span>\n'
            f'      </a>\n')

def section_block(sec_id, btn_title, btn_desc, lessons):
    items = ''.join(lesson_item(n, s, t) for n, s, t in lessons)
    return (f'<!-- Part 3 {sec_id} -->\n'
            f'<div class="part-section" id="{sec_id}">\n'
            f'  <button type="button" class="part-btn" aria-expanded="false" aria-controls="{sec_id}-body">\n'
            f'    <span class="part-btn-label">\n'
            f'      <span class="part-btn-title">{btn_title}</span>\n'
            f'      <span class="part-btn-desc">{btn_desc}</span>\n'
            f'    </span>\n'
            f'    <span class="part-chevron" aria-hidden="true">&#9660;</span>\n'
            f'  </button>\n'
            f'  <div class="part-body" id="{sec_id}-body">\n'
            f'    <div class="lesson-list">\n'
            f'{items}'
            f'    </div>\n'
            f'  </div>\n'
            f'</div>\n\n')

part3_html = '\n<h2 id="part3" style="margin-top:48px;">Part 3 &middot; Serving in Christ</h2>\n\n'
for sec_id, title, desc, lessons in SECTIONS:
    part3_html += section_block(sec_id, title, desc, lessons)

# --- 1. Insert Part 3 sections after Part 2's last section, before the section-controls div ---
marker = '<div class="btf-section-controls">'
assert marker in content, "section-controls marker not found"
content = content.replace(marker, part3_html + marker, 1)

# --- 2. Update page footer ---
old_footer = '<p>Bible Truth Foundations &middot; Parts 1 and 2 of 3 &middot; The Well Shrewsbury</p>'
new_footer = '<p>Bible Truth Foundations &middot; Parts 1, 2 and 3 of 3 &middot; The Well Shrewsbury</p>'
assert old_footer in content, "footer text not found"
content = content.replace(old_footer, new_footer, 1)

# --- 3. Update floating TOC with Part 3 links ---
old_toc_end = '''    <a href="#p2-section-d">Part 2: Provision and Prayer</a>
<a href="#" class="toc-back-top">&#8593; Back to top</a>'''
new_toc_end = '''    <a href="#p2-section-d">Part 2: Provision and Prayer</a>
    <a href="#p3-section-a">Part 3: Living in the Spirit's Power</a>
    <a href="#p3-section-b">Part 3: Living Among Others</a>
    <a href="#p3-section-c">Part 3: Living Free from Law and Sin</a>
    <a href="#p3-section-d">Part 3: Living as a Disciple</a>
<a href="#" class="toc-back-top">&#8593; Back to top</a>'''
assert old_toc_end in content, "TOC end marker not found"
content = content.replace(old_toc_end, new_toc_end, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully.")
print(f"Part 3 HTML block length: {len(part3_html)} chars")
