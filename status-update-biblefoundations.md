# status-update-biblefoundations.md

**Project:** Bible Truth Foundations (3-part discipleship series, The Well Shrewsbury)
**Last updated:** 18 September 2026 (evening: Part 2 fully built)

---

## What this file is

Open this file first, in any session, before touching this project. It tells you what every other file in this folder is for, what is built, what is live, and what is next, so you never need to re-derive any of it from git history or the site itself.

## What every file in this folder is for

- `index.html` — the site's homepage/hub. Lists all parts and sections, links out to every lesson file. Deployed live.
- `btf-p1-l01-eternal-life.html` through `btf-p1-l16-the-benefits-of-speaking-in-tongues.html` — the 16 Part 1 lesson pages. Each is a complete, self-contained study session (Opening Question through Revision Cards).
- `btf-site.css` — shared stylesheet for every page on the site (index and all lessons). One file, used everywhere. Do not fork it per lesson.
- `btf-site.js` — shared JavaScript engine for every page: sticky audio panel, text-to-speech playback (whole-page and per-section), collapsible sections with auto-inserted minimise buttons, Expand All/Minimise All, floating table-of-contents, responsive table labelling. One file, used everywhere. This is the file that makes the site interactive; see the Part 2 build instructions (in chat, 18 Sep 2026) for a full functional breakdown.
- `Bible Truth Foundation Pt1 - Teachers Guide.html` — standalone teacher-facing guide for Part 1, kept separate from student-facing lesson files (per the project's Teaching Tips rule: teacher content never appears in student pages).
- `btf-Pt1 Complete Course.md` — master markdown file containing the full text of all 16 Part 1 lessons in one document. Useful for review/read-through without opening 16 separate HTML files.
- `favicon.ico` — shared site favicon, linked from every page.
- `.git/` — this folder is a git repository, connected to GitHub.

## Where it lives and how it deploys

- **Local folder (this one):** `...\CREATE\bible-teachings\biblefoundations`
- **GitHub:** `Daveflyon/biblefoundations` (origin, branch `main`)
- **Live site:** https://biblefoundations.pages.dev/ — Cloudflare Pages, connected to the GitHub repo. Deploys automatically within a minute or two of every push to `main`. No build step, no wrangler.toml, no manual deploy action needed; push and it goes live.
- **Not related to this project:** https://delessons.org/ — this is Discipleship Evangelism's own ministry site (Andrew Wommack / Don W. Krow), the *source material* Part 1 and Part 2 are adapted from, used with permission. It is not where this build is hosted.

## What's built and confirmed live (Part 1 of 3)

**"New Life in Christ"** — 16 lessons across four sections:
- Section A, Gospel Foundation (L01–L03): Eternal Life, Salvation by Grace, Righteousness by Grace
- Section B, Knowing God (L04–L05): Relationship with God, The Nature of God
- Section C, Response and Commitment (L06–L08): Repentance, Commitment, Water Baptism
- Section D, Life in Christ (L09–L16): Identity in Christ (Parts 1–2), What Happens When a Christian Sins, Integrity of God's Word, God's Not Guilty, The Power of a Spirit-Filled Life, How to Receive the Holy Spirit, The Benefits of Speaking in Tongues

Verified live at biblefoundations.pages.dev on 18 September 2026; homepage and structure match the local files exactly.

**Every lesson has:** Opening Question, Key Scripture, Core Truth, Bible Teaching (with Note/Depth/Tip/Caution callouts), Key Discovery Questions (fillable, autosaving, downloadable, clearable), Group Discussion Questions, Application, Revision Cards (flip cards, keyboard accessible).

**Site-wide functionality (confirmed via source inspection, not just visually):** sticky audio panel with browser text-to-speech (whole-page and per-section play/pause, five speed settings saved across visits), auto-inserted per-section minimise buttons, Expand All/Minimise All, floating "Jump to section" table of contents, responsive tables on mobile, autosaving fillable answers per lesson, answer download-as-text, clear-all-answers with confirmation.

## Git state as of 18 September 2026

Branch `main`, up to date with `origin/main` (13 commits).

**Uncommitted at last check:** `btf-site.css`, `btf-site.js`, `index.html` have local edits not yet committed. `Bible Truth Foundation Pt1 - Teachers Guide.html` and `btf-Pt1 Complete Course.md` are untracked; they have never been committed to git at all, despite existing on disk.

**Action needed before Part 2 work starts:** commit all of the above to get a clean, complete baseline. Do this first, in its own commit, before any Part 2 files are added.

## What's next: Part 2 of 3

Source: Level 2 of the Discipleship Evangelism Programme (16 lessons; self-centredness, meditation, renewing the mind, the local church, deliverance, authority of the believer, healing, forgiveness, marriage, God's kind of love, finances, unanswered prayer).

A full build-instruction document was written on 18 September 2026, reverse-engineering every interactive behaviour from the live Part 1 site (not just the original CLAUDE.md project brief, which describes some things, an "arc bar," a scroll-triggered sticky bar, that don't match what was actually built). It covers: the arc/section grouping proposal, the exact template structure, every JS-driven behaviour (audio engine, collapsibles, TOC, flashcards, fillable answers), file naming, content rules, and the git/deploy workflow. It is meant to be pasted into a fresh Claude Code session to build Part 2 with far fewer iterations than Part 1 needed, since every functional requirement is specified upfront rather than discovered through review cycles.

**Decisions locked 18 Sep 2026:** arc approved (A Mind and Word 1-3, B Church and Authority 4-6, C Healing and Relationships 7-13, D Provision and Prayer 14-16); subtitle "Growing in Christ"; local lesson numbering with p2-lNN-qM-answer keys; one Teacher's Guide and Complete Course file per part; working docs committed to public repo by choice; source fetched from delessons.org per lesson; build running in Cowork session (Fable 5).

## Dated changelog

- **18 Sep 2026** — Recap and audit performed. Confirmed live site matches local Part 1 build. Confirmed hosting chain (GitHub, Cloudflare Pages; not delessons.org). Reverse-engineered full functional spec from btf-site.js/btf-site.css/live HTML for Part 2 build instructions. Identified uncommitted Part 1 changes and never-committed Teacher's Guide/Complete Course files. Created this status file.
- **18 Sep 2026 (later)** — Part 2 kicked off in Cowork session on Fable 5 (Claude Code only offers Fable 5.1, which bypasses promo credits). Arc, subtitle, numbering, file-per-part and source decisions locked (see above). Baseline commit made: pending line-ending-only changes to css/js/index plus four previously untracked files (Teacher's Guide, Complete Course, CLAUDE.md, this file).

- **18 Sep 2026 (evening)** — PART 2 BUILT IN FULL, in the Cowork session on Fable 5. Delivered: 16 lesson files (btf-p2-l01 through btf-p2-l16, sections A Mind and Word / B Church and Authority / C Healing and Relationships / D Provision and Prayer), index.html updated with Part 1 and Part 2 group headings, four new collapsible Part 2 sections, series-level NKJV declaration added to the attribution, footer and title updated to series level; "btf-Pt2 Complete Course.md" (full course text, 125KB); "Bible Truth Foundation Pt2 - Teachers Guide.html" (Parts A/B/C structure: how to use, per-lesson facilitator guide with aims, watch-fors and pastoral notes, quick reference table). All lessons reuse btf-site.css/btf-site.js unchanged; answer keys namespaced p2-lNN-qM; no NKJV labels on individual verses (note: Part 1 files still carry them; optional cleanup later). Full red-flag sweep passed: 8 sections per lesson, page attributes, shared assets, data-keys, download filenames, TOC, 5+ revision cards, unique opening questions, all 16 index links resolve. NOT YET COMMITTED: three stale git lock files (.git/HEAD.lock, .git/index.lock, .git/objects/maintenance.lock) block git; David must delete them manually, then commit and push (or push via VS Code Sync). Nothing is live until pushed. Build scripts and content sources live in the session only; the generated files in this folder are the deliverables.

- **18 Sep 2026 (late evening)** — Push was rejected: GitHub held 10 newer commits from an earlier Claude Code session (audio overhaul: speed dropdown, read-along highlighting, sentence-level resume; per-lesson scripts moved into new shared btf-lesson-page.js; shared callout CSS; index polish). Resolved without git merge machinery: took their css/js/favicon.svg/all 16 Part 1 lessons/btf-lesson-page.js wholesale, re-applied Part 2 sections onto their index.html, patched btf-lesson-page.js download-slug regex from btf-p1-only to btf-p(any)-l(NN) so Part 2 answer downloads name correctly, regenerated all 16 Part 2 lessons from the NEW Part 1 template (speed dropdown, no inline scripts, both shared JS files). Full sweep re-passed. Local git branch is 2 commits ahead of a stale base; David runs the reset-and-recommit block from the chat on his machine (fetch, reset --mixed origin/main, add, commit, push), which lands everything as one commit on top of the remote work. VM git is avoided from now on: it cannot delete its own lock files.
