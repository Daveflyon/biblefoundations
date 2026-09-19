# BTF lesson builder (part-aware). Clones the CURRENT btf-p1-l01 boilerplate,
# splices lesson content from a dict. Works for any part: set part/subtitle in the dict.
# Usage: from builder import build; build(L)  where L has num, slug, title, part,
# subtitle, section, section_name, opening, ks_ref, ks_text, ks_note, core,
# teaching[], kdq[], gdq[], app_intro, app[], cards[].
import re, os
TPL = os.path.expanduser('~/mnt/biblefoundations/btf-p1-l01-eternal-life.html')
OUT = os.path.expanduser('~/mnt/biblefoundations')
CALLOUT_LABEL = {'note':'Note','depth':'Going Deeper','tip':'Practical Tip','caution':'Caution'}

def scripture(ref, text):
    return ('  <div class="scripture-block">\n    <p class="scripture-ref">%s</p>\n'
            '    <p class="scripture-text">%s</p>\n  </div>\n') % (ref, text)

def callout(kind, text):
    return ('  <div class="callout %s">\n    <p class="callout-label">%s</p>\n'
            '    <p>%s</p>\n  </div>\n') % (kind, CALLOUT_LABEL[kind], text)

def teaching_html(items):
    out = []
    for it in items:
        k = it[0]
        if k == 'h3': out.append('  <h3>%s</h3>\n' % it[1])
        elif k == 'p': out.append('  <p>%s</p>\n' % it[1])
        elif k == 'scripture': out.append(scripture(it[1], it[2]))
        elif k == 'callout': out.append(callout(it[1], it[2]))
    return ''.join(out)

def sec_toggle(sec_id, label):
    return ('<section id="%s">\n  <button class="section-toggle" aria-expanded="false" '
            'aria-controls="%s-body" id="%s-btn">\n    %s <span class="section-chevron" '
            'aria-hidden="true">&#9660;</span>\n  </button>\n  <div class="section-body" id="%s-body">\n'
            ) % (sec_id, sec_id, sec_id, label, sec_id)

def end_sec(): return '  </div><!-- end section-body -->\n</section>'

def kdq_section(L):
    ns = 'p%d-l%02d' % (L['part'], L['num'])
    rows = []
    for i, q in enumerate(L['kdq'], 1):
        rows.append('        <tr>\n          <td>%s</td>\n'
          '          <td><div class="fillable" contenteditable="true" data-key="%s-q%d-answer" data-placeholder="Type your answer here&hellip;"></div></td>\n'
          '          <td><div class="fillable" contenteditable="true" data-key="%s-q%d-notes" data-placeholder="Group notes&hellip;"></div></td>\n        </tr>' % (q, ns, i, ns, i))
    return (sec_toggle('discovery-questions','Key Discovery Questions')
      + '  <p>Work through these on your own before your group meets. Type your answers directly into the table below. Your answers are saved automatically in your browser.</p>\n\n'
      + '  <div class="answers-toolbar">\n    <button id="download-btn">&#8595; Download my answers</button>\n    <button class="clear-btn" id="clear-btn">Clear all answers</button>\n  </div>\n'
      + '  <p class="answers-note">Note: answers are saved to your browser on this device. If you are viewing this inside Google Sites, open the file directly in your browser for reliable saving.</p>\n\n'
      + '  <div class="table-wrap">\n    <table>\n      <thead>\n        <tr>\n          <th style="width:38%">Question</th>\n          <th style="width:31%">My Answer</th>\n          <th style="width:31%">Group Discussion Notes</th>\n        </tr>\n      </thead>\n      <tbody>\n'
      + '\n'.join(rows) + '\n      </tbody>\n    </table>\n  </div>\n' + end_sec())

def gdq_section(L):
    items = ''.join('    <li style="margin-bottom:16px;">%s</li>\n' % q for q in L['gdq'])
    return (sec_toggle('group-discussion','Group Discussion Questions')
      + '  <p>These questions are designed for open conversation at any level of experience. There are no trick questions and no single correct answer.</p>\n\n  <ol>\n'
      + items + '  </ol>\n' + end_sec())

def app_section(L):
    rows = ''.join('        <tr>\n          <td class="label-cell">%s</td>\n          <td>%s</td>\n        </tr>\n' % (c, t) for c, t in L['app'])
    return (sec_toggle('application','Application')
      + '  <p>%s</p>\n\n  <div class="table-wrap">\n    <table>\n      <thead>\n        <tr>\n          <th style="width:22%%">Context</th>\n          <th>How I Apply This</th>\n        </tr>\n      </thead>\n      <tbody>\n' % L['app_intro']
      + rows + '      </tbody>\n    </table>\n  </div>\n' + end_sec())

def cards_section(L):
    cards = []
    for c in L['cards']:
        front = '          <p class="fc-prompt">%s</p>\n' % c['front']
        if c.get('ref'): front += '          <p class="fc-ref">%s</p>\n' % c['ref']
        if c['back_type'] == 'verse':
            back = ('          <p class="fc-verse">%s</p>\n          <p class="fc-ref-back">%s</p>\n'
                    ) % (c['back'], c['back_ref'])
        else:
            back = '          <p class="fc-def">%s</p>\n' % c['back']
        cards.append('    <div class="flashcard" role="button" tabindex="0" aria-label="Revision card: %s">\n'
          '      <div class="flashcard-inner">\n        <div class="flashcard-front">\n%s        </div>\n'
          '        <div class="flashcard-back">\n%s        </div>\n      </div>\n    </div>\n' % (c['front'], front, back))
    return (sec_toggle('revision-cards','Revision Cards')
      + '  <p class="flashcard-hint">Tap each card to reveal the answer.</p>\n\n  <div class="flashcard-grid">\n\n'
      + '\n'.join(cards) + '\n  </div><!-- end flashcard-grid -->\n' + end_sec())

def teaching_section(L):
    return (sec_toggle('bible-teaching','Bible Teaching') + '\n'
            + teaching_html(L['teaching']) + '\n' + end_sec())

def replace_section(html, sec_id, new):
    a = html.index('<section id="%s">' % sec_id)
    b = html.index('</section>', a) + len('</section>')
    return html[:a] + new + html[b:]

def swap(html, sec_id, cls, new, tag='p'):
    a = html.index('<section id="%s">' % sec_id)
    b = html.index('</section>', a)
    seg = html[a:b]
    seg2 = re.sub(r'(<%s class="%s">).*?(</%s>)' % (tag, cls, tag),
                  lambda m: m.group(1) + new + m.group(2), seg, count=1, flags=re.S)
    return html[:a] + seg2 + html[b:]

def build(L):
    part = L['part']; sub = L['subtitle']
    h = open(TPL, encoding='utf-8').read()
    nn = '%02d' % L['num']
    fname = 'btf-p%d-l%s-%s.html' % (part, nn, L['slug'])
    h = h.replace('<title>Lesson 01: Eternal Life – Bible Truth Foundations Part 1</title>',
                  '<title>Lesson %s: %s – Bible Truth Foundations Part %d</title>' % (nn, L['title'], part))
    h = h.replace('<p class="series-part">Part 1 of 3: New Life in Christ</p>',
                  '<p class="series-part">Part %d of 3: %s</p>' % (part, sub))
    h = h.replace('<h1>Eternal Life</h1>', '<h1>%s</h1>' % L['title'])
    h = h.replace('<p class="lesson-meta">Lesson 1 of 16 &nbsp;|&nbsp; Section A: The Gospel Foundation</p>',
                  '<p class="lesson-meta">Lesson %d of 16 &nbsp;|&nbsp; Section %s: %s</p>' % (L['num'], L['section'], L['section_name']))
    h = h.replace('Part 1 of 3: New Life in Christ &middot; Lesson 01: Eternal Life',
                  'Part %d of 3: %s &middot; Lesson %s: %s' % (part, sub, nn, L['title']))
    h = swap(h, 'opening-question', 'question-text', L['opening'])
    h = swap(h, 'key-scripture', 'scripture-ref', L['ks_ref'])
    h = swap(h, 'key-scripture', 'scripture-text', L['ks_text'])
    a = h.index('<section id="key-scripture">'); b = h.index('</section>', a)
    seg = h[a:b]
    seg = re.sub(r'(<p class="scripture-note"><em>).*?(</em></p>)',
                 lambda m: m.group(1) + L['ks_note'] + m.group(2), seg, count=1, flags=re.S)
    h = h[:a] + seg + h[b:]
    h = swap(h, 'core-truth', 'core-truth-statement', L['core'])
    h = replace_section(h, 'bible-teaching', teaching_section(L))
    h = replace_section(h, 'discovery-questions', kdq_section(L))
    h = replace_section(h, 'group-discussion', gdq_section(L))
    h = replace_section(h, 'application', app_section(L))
    h = replace_section(h, 'revision-cards', cards_section(L))
    assert '(NKJV)' not in h.split('</head>')[1], 'NKJV label leaked into body'
    open(os.path.join(OUT, fname), 'w', encoding='utf-8').write(h)
    return fname
