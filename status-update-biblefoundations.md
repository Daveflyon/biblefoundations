# status-update-biblefoundations.md

**Project:** Bible Truth Foundations (3-part discipleship series, The Well Shrewsbury)
**Last updated:** 19 September 2026

---

## What this file is

Open this file first, in any session, before touching this project. It tells you what every other file in this folder is for, what is built, what is live, and what is next, so you never need to re-derive any of it from git history or the site itself.

## What every file in this folder is for

- `index.html` — the site's homepage/hub. Lists all parts and sections, links out to every lesson file. Deployed live, includes all three parts.
- `btf-p1-l01-eternal-life.html` through `btf-p1-l16-the-benefits-of-speaking-in-tongues.html` — the 16 Part 1 lesson pages.
- `btf-p2-l01-self-centredness.html` through `btf-p2-l16-what-to-do-when-your-prayers-seem-unanswered.html` — the 16 Part 2 lesson pages.
- `btf-p3-l01-the-divine-flow.html` through `btf-p3-l16-using-everyones-gifts-to-disciple.html` — the 16 Part 3 lesson pages.
- `btf-site.css` — shared stylesheet for every page on the site. One file, used everywhere.
- `btf-site.js` — shared JavaScript engine for sticky audio panel, collapsibles, Expand All/Minimise All, floating TOC, responsive tables. One file, used everywhere.
- `btf-lesson-page.js` — shared JavaScript engine added by a later audio-engine overhaul: speed dropdown, read-along text highlighting during playback, sentence-level resume for Play Lesson. Referenced alongside `btf-site.js` on every lesson page.
- `favicon.svg` — shared site favicon (replaced `favicon.ico` in the same overhaul).
- `Bible Truth Foundation Pt1 - Teachers Guide.html` / `Bible Truth Foundation Pt2 - Teachers Guide.html` / `Bible Truth Foundation Pt3 - Teachers Guide.html` — standalone teacher-facing guides, one per part, kept separate from student-facing lesson files.
- `btf-Pt1 Complete Course.md` / `btf-Pt2 Complete Course.md` / `btf-Pt3 Complete Course.md` — master markdown files containing the full text of each part's 16 lessons.
- `build-tools/builder.py` — generalised, part-aware Python HTML builder. Clones the *current* `btf-p1-l01-eternal-life.html` as its template (so any new lesson automatically inherits the live audio engine) and takes a content dict keyed by `part`, `subtitle`, plus all the usual fields. Used to build all 16 Part 3 lesson files.
- `build-tools/p3_lessons.py` — the Part 3 lesson content, translated into `builder.py`'s schema (16-entry `LESSONS` list).
- `build-tools/p3_teacher_notes.py` — Part 3 facilitator notes (aim, watch-for, pastoral note per lesson), used only by the Teacher's Guide generator.
- `build-tools/run_p3_build.py`, `build-tools/gen_complete_course.py`, `build-tools/gen_teachers_guide.py`, `build-tools/update_index.py` — one-off generator scripts that produced the Part 3 HTML files, Complete Course markdown, Teacher's Guide, and `index.html` update respectively. Kept in-repo for reference/reuse on a future part.
- `build-tools/part3/btf-p3-content-draft.md` — the approved Phase 2A/2B content draft Part 3's HTML was built from.
- `.git/` — this folder is a git repository, connected to GitHub.

## Where it lives and how it deploys

- **Local folder (this one):** `...\CREATE\bible-teachings\biblefoundations`
- **GitHub:** `Daveflyon/biblefoundations` (origin, branch `main`)
- **Live site:** https://biblefoundations.pages.dev/ — Cloudflare Pages, connected to the GitHub repo. Deploys automatically within a minute or two of every push to `main`.
- **Not related to this project:** https://delessons.org/ — Discipleship Evangelism's own ministry site (Andrew Wommack / Don W. Krow), the *source material* all three parts are adapted from, used with permission. Not where this build is hosted.

## What's built and confirmed live

**Part 1 of 3, "New Life in Christ"** — 16 lessons across four sections (Gospel Foundation, Knowing God, Response and Commitment, Life in Christ). Live and confirmed.

**Part 2 of 3, "Growing in Christ"** — 16 lessons (self-centredness, meditation, renewing the mind, the local church, deliverance, authority of the believer, healing, forgiveness, marriage, God's kind of love, finances, unanswered prayer, and others). Built, committed (`e194054`), pushed, and confirmed live on 18 September 2026 after resolving a remote-divergence issue (see Dated changelog).

**Part 3 of 3, "Serving in Christ"** — 16 lessons across four sections (Living in the Spirit's Power, Living Among Others, Living Free from Law and Sin, Living as a Disciple). Built, committed, and pushed on 19 September 2026 (see Dated changelog). All 9 components (N.1-N.9) present in every lesson; `index.html`, Complete Course markdown, and standalone Teacher's Guide all updated/added.

**Every lesson has:** Opening Question, Key Scripture, Core Truth, Bible Teaching (Note/Depth/Caution callouts), Key Discovery Questions (fillable, autosaving, downloadable, clearable), Group Discussion Questions, Application, Revision Cards (flip cards, keyboard accessible).

**Site-wide functionality, current state:** sticky audio panel with browser text-to-speech, a speed **dropdown** (replaced the original row of speed buttons), read-along text highlighting during playback, sentence-level resume for Play Lesson, oauto-inserted per-section minimise buttons, Expand All/Minimise All, floating "Jump to section" TOC, responsive tables, autosaving fillable answers (part-namespaced localStorage keys), answer download-as-text, clear-all-answers with confirmation.

## Part 3 of 3, "Serving in Christ" — build complete

**Source:** Level 3 of the Discipleship Evangelism Programme — 16 lessons, all source summaries fetched from delessons.org: The Divine Flow; Using the Gifts to Minister; Miracles Glorify God; The Power of Godly Relationships; Persecution; The King and His Kingdom; The Object of Saving Faith; The Proper Use of God's Law; Not Under Law but Under Grace; No More Consciousness of Sin; I Am Loved, I Am Pretty; The Fruit of Salvation (Part 1); The Fruit of Salvation (Part 2); A Call to Discipleship; How to Use Your Testimony; Using Everyone's Gifts to Disciple.

**Arc (approved 18 September 2026):** four sections, 3/3/5/5 shape —
- **Section A, Living in the Spirit's Power** (L01-L03): The Divine Flow, Using the Gifts to Minister, Miracles Glorify God
- **Section B, Living Among Others** (L04-L06): The Power of Godly Relationships, Persecution, The King and His Kingdom
- **Section C, Living Free from Law and Sin** (L07-L11): The Object of Saving Faith, The Proper Use of God's Law, Not Under Law but Under Grace, No More Consciousness of Sin, I Am Loved I Am Pretty
- **Section D, Living as a Disciple** (L12-L16): The Fruit of Salvation (Part 1), The Fruit of Salvation (Part 2), A Call to Discipleship, How to Use Your Testimony, Using Everyone's Gifts to Disciple

Numbering: local per-part, restarting at 01 (`btf-p3-l01` through `btf-p3-l16`).

**Content:** all 16 lessons drafted in the project's Phase 2A/2B format, saved to `build-tools/part3/btf-p3-content-draft.md`, sent to Dave for review, and confirmed via "proceed" to move to full build. Scripture quotations matched standard NKJV renderings from training knowledge; not independently cross-checked verse-by-verse against an external NKJV source. If that extra layer of certainty is wanted, flag it for a follow-up verification pass, particularly for the ~96 Revision Card quotations.

**Build (19 September 2026):** content translated into `builder.py`'s schema (`build-tools/p3_lessons.py`), all 16 HTML files built, `index.html` updated with Part 3's four sections and TOC links, `btf-Pt3 Complete Course.md` and a standalone `Bible Truth Foundation Pt3 - Teachers Guide.html` generated. Integrity sweep passed: no `.callout-tip` in student files, no external dependencies, no stray "(NKJV)" labels in body content (declared once at series level only), correct localStorage key patterns, no duplicate Opening Questions or Core Truths across lessons, 6 Revision Cards per lesson. One pre-existing template convention (a literal en-dash in each lesson's `<title>` tag, inherited from `builder.py`) was found and deliberately left unchanged, since it already exists identically in every live Part 1/2 file.

**Committed and pushed** in four chunks (CLAUDE.md doc update, build tooling, 16 lesson files, index/Complete Course/Teacher's Guide) — see Dated changelog for commit detail. **Push required a one-time credential setup on the device shell** (a GitHub PAT stored via `git config credential.helper store`); future sessions on this same device shell should already have it and can push without repeating that step.

## Known recurring issue: git lock files

`device_bash` (the tool used to run commands on Dave's machine) cannot delete files without an explicit granted permission, and that permission request has been denied every time it's been tried. Result: `.git/HEAD.lock`, `.git/index.lock`, and/or `.git/objects/maintenance.lock` reliably get left behind after git operations and block the next one. **As of 18 September 2026, `.git/index.lock` is currently stuck again** — Dave needs to delete it manually via File Explorer (View → show Hidden items → the `.git` folder) before any further git command will run. Full detail and the divergence-recovery procedure (
don't use `git merge`/`git pull`) are in `CLAUDE.md`.

## Dated changelog

- **18 Sep 2026** — Recap and audit performed. Confirmed live site matches local Part 1 build. Confirmed hosting chain (GitHub → Cloudflare Pages, not delessons.org). Reverse-engineered full functional spec for Part 2 build instructions. Created this status file.
- **18 Sep 2026** — Part 2 of 3 ("Growing in Christ") built in full: 16 lessons, index.html updated, Complete Course markdown, Teacher's Guide. Git push initially rejected (
remote had 10 newer commits from another session's audio-engine overhaul: speed dropdown, `btf-lesson-page.js`, read-along highlighting, favicon.svg). Resolved by manually materialising remote file versions rather than merging, rebuilding all 16 lessons against the new template, and landing a clean commit (
`e194054` on `dffb1a4`) via fetch + reset --mixed + commit + push. Confirmed live after a ~90 second Cloudflare propagation wait.
- **18 Sep 2026** — Part 3 planning: fetched all 16 Level 3 source summaries from delessons.org. Proposed and got approval for a four-section arc (3/3/5/5) and the subtitle "Serving in Christ." Dave chose content-only scope for this stage. Generalised the HTML builder into `build-tools/builder.py` (part-aware, always builds from the current live template) so Part 3's eventual HTML build won't need a bespoke script. Began content-authoring for Section A (3 of 16 lessons drafted, not yet reviewed). CLAUDE.md rewritten to reflect the current audio engine, the generalised builder, and the git lock-file/divergence procedure, ahead of starting a fresh chat.
- **19 Sep 2026** — New session picked up Part 3 content-writing. Confirmed with Dave that the prior session's Section A draft was never saved to disk (session notes only) and needed to be redrafted. Re-fetched all 16 Level 3 source summaries fresh from delessons.org (one page, "Not Under Law but Under Grace", 521-errored on delessons.org itself; recovered via the equivalent AWMI CDN PDF). Wrote full Phase 2A+2B content for all 16 lessons across all four sections, saving to `build-tools/part3/btf-p3-content-draft.md` incrementally after each section (not held only in chat this time). Ran a structural red-flag check (distinct Opening Questions/Core Truths, no Teaching Tip callouts, NT Connections row counts, Revision Card counts) and a full house-style sweep removing all em/en dashes from prose. Sent to Dave for review. **Not yet approved; no HTML built; index.html untouched; nothing committed or pushed.**
- **19 Sep 2026** — Dave reviewed and approved the Part 3 content, then said "proceed" to authorise the full build. Translated all 16 lessons from the approved draft's table-based format into `builder.py`'s schema (`build-tools/p3_lessons.py`); fixed a stray "(NKJV)" label leak (157 occurrences stripped from body content) caught by the builder's own integrity assertion. Built all 16 Part 3 HTML files. Updated `index.html` with Part 3's four sections and floating TOC links (two false starts on the footer/TOC text match, caused by literal Unicode dash/middot characters versus the file's actual HTML entities; fixed by editing the patch script directly rather than trusting an unverified string-replace). Generated `btf-Pt3 Complete Course.md` and `Bible Truth Foundation Pt3 - Teachers Guide.html` (with original facilitator notes per lesson in `build-tools/p3_teacher_notes.py`). Ran the full Red Flags integrity sweep; only finding was a pre-existing en-dash in the `<title>` tag inherited from the template, confirmed identical to Part 1/2's shipped files and left as-is. Committed in four logical chunks (CLAUDE.md documentation update; build tooling; 16 lesson HTML files; index.html + Complete Course + Teacher's Guide). Git push initially failed: the device shell had no credential helper configured for GitHub (separate from Dave's native Windows git setup) — resolved by Dave generating a GitHub PAT and storing it via `git config credential.helper store` on the device shell, a one-time setup for this device. Pushed successfully (`e194054..6aeb3b1`, 4 commits). Cloudflare Pages live-site verification could not be completed from either the device shell or the cloud workspace (both environments' network egress blocks `biblefoundations.pages.dev`); **Dave should spot-check the live site directly** to confirm Part 3 is showing correctly.
