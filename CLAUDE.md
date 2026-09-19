# CLAUDE.md — Bible Truth Foundations (biblefoundations repo)

This file is read automatically at the start of every Claude Code session
in this folder. It is the operating manual for this specific repo: what
exists, how it deploys, and the rules that keep every new lesson
consistent with what is already live. Read `status-update-biblefoundations.md`
first for current project status and open decisions; this file is the
technical/build reference that doesn't change session to session.

## What this is

A 3-part Bible discipleship course, "Bible Truth Foundations," for The
Well Shrewsbury. Adapted with permission from the Discipleship Evangelism
Programme by Andrew Wommack and Don W. Krow (delessons.org) — their Level
1/2/3 map to this series' Part 1/2/3. Static HTML site, no framework, no
build step.

- Part 1, "New Life in Christ" — 16 lessons. Live.
- Part 2, "Growing in Christ" — 16 lessons. Live.
- Part 3, "Serving in Christ" — 16 lessons. In progress; content-authoring
  stage only as of 18 September 2026 (see status file for the arc and what's
  written so far). No HTML built yet, index.html not yet touched for Part 3.

## Deployment chain

Local folder → GitHub (`Daveflyon/biblefoundations`, branch `main`) →
Cloudflare Pages (auto-deploy on push, no wrangler.toml, no manual step).
Live at https://biblefoundations.pages.dev/. Confirm the live site
reflects a change after pushing before calling a task done — Cloudflare's
edge cache can serve a stale page for a minute or two after deploy, so
wait ~90 seconds and re-fetch with a cache-busting query string
(e.g. `?v=2`) before concluding a push didn't take effect.

Do not confuse this with https://delessons.org/ — that is the source
ministry's own site (used with permission for content only), not where
this project is hosted.

## File map

- `index.html` — homepage/hub, links to every lesson, holds the
  collapsible Part/Section navigation.
- `btf-pN-lNN-slug.html` — one file per lesson (N = part number, NN =
  lesson number *within that part*, zero-padded, restarting at 01 for
  each new part — confirmed from Part 2's files, e.g. `btf-p2-l01-...`).
- `btf-site.css` — single shared stylesheet for every page. Never fork
  per lesson or per part.
- `btf-site.js` — single shared JS engine for sticky audio panel,
  collapsibles, Expand All/Minimise All, floating TOC, responsive
  tables. Never fork per lesson or per part.
- `btf-lesson-page.js` — shared JS engine (added by a later audio-engine
  overhaul) for the current speed-dropdown control, read-along text
  highlighting during playback, and sentence-level resume for
  "Play Lesson." Referenced by every lesson page alongside `btf-site.js`.
  Never fork per lesson.
- `favicon.svg` — shared across all pages (replaced `favicon.ico` in the
  same overhaul; some older references to `.ico` in earlier docs are
  stale — `.svg` is current).
- `Bible Truth Foundation PtN - Teachers Guide.html` — teacher-facing
  content per part, kept separate from student pages. One file per part
  so far (Pt1, Pt2); confirm with Dave whether Pt3 stays separate or
  these get merged into one series-wide guide once all three parts are
  built.
- `btf-PtN Complete Course.md` — master markdown of a part's full lesson
  text, for read-through outside the HTML. One file per part so far.
- `status-update-biblefoundations.md` — current status, what's live,
  what's open, dated changelog. Read this for "where are we right now."
- `build-tools/builder.py` — generalised, part-aware Python HTML builder
  (added 18 September 2026). Takes a lesson content dict with `part` and
  `subtitle` keys (plus all the usual content fields) and clones the
  *current* `btf-p1-l01-eternal-life.html` as its template, so any lesson
  built with it automatically inherits whatever the live template's audio
  engine and markup currently are. This replaced an earlier session-local,
  Part-1-to-Part-2-hardcoded version. Use this for all future part builds
  rather than writing a new builder from scratch.
- `build-tools/part3/` — empty scaffold folder, created for Part 3
  content-authoring scripts (mirrors the pattern of session-local content
  scripts used for Part 2, but kept in-repo this time so a future session
  can find and reuse it).
- `.git/` — this folder is a git repository, connected to GitHub. See the
  **Known git issue** section below before running any git command.

## Non-negotiable build rules

- British English throughout. No em dashes or en dashes anywhere in
  prose — rephrase, use semicolons, or use periods.
- NKJV only, declared once at series level, never repeated on individual
  verses.
- Every HTML file fully self-contained and offline-capable: no external
  fonts, no CDN links, no external API calls. The browser's built-in
  `speechSynthesis` API is fine ('is local to the browser, not a network
  call).
- Never invent new CSS classes. If a lesson's content seems to need one
  that doesn't exist in `btf-site.css`, stop and ask before adding it.
- Never duplicate `btf-site.js` or `btf-lesson-page.js` logic inline in a
  lesson file. The only inline `<script>` block a lesson file should have
  is the small per-lesson block for flashcard flip + fillable-answer
  save/restore/download/clear — copy that block's structure from an
  existing lesson, changing only lesson-specific IDs and text.
- Teaching Tip callouts (`.callout-tip`) never appear in student-facing
  lesson files — Teacher's Guide content only. Note and Depth callouts
  are permitted in student sections.
- `<body data-btf-page="lesson">` on every lesson page, `<body
  data-btf-page="index">` on the index page — this attribute is what
  tells `btf-site.js` which behaviours to initialise. Missing or wrong
  and none of the interactivity works.
- Always build a new part's HTML from the *current* on-disk
  `btf-p1-l01-eternal-life.html` (via `build-tools/builder.py`), never
  from an older cached copy or from this document's earlier functional
  descriptions — the live template is the source of truth and has been
  overhalued more than once already.

## Naming conventions

- Lesson files: `btf-p{part}-l{NN}-{slug}.html`, e.g.
  `btf-p1-l01-eternal-life.html`, `btf-p2-l01-self-centredness.html`,
  `btf-p3-l01-the-divine-flow.html`. Slugs lowercase, hyphenated, terse
  (match existing slug style).
- Status file for this project: `status-update-biblefoundations.md`
  (the one file to open first in any session).
- Downloaded answer files (generated client-side): `btf-p{part}-l{NN}-
  my-answers.txt`. `btf-lesson-page.js` derives this from the page's own
  filename via regex `/^(btf-p\d+-l\d+)/i` — this was patched from a
  Part-1-only hardcoded pattern, so it already supports Part 3 correctly.
- `localStorage` answer keys: `p{part}-l{NN}-{M}-answer` /
  `-notes` pattern (part-namespaced, to prevent cross-part collisions —
  confirmed this is the pattern actually used in Part 2's shipped files).
  `btf-audio-rate` (speed preference) is the one exception: always
  shared site-wide, never namespaced per part.

## Functional spec — current interactive behaviour (post audio-engine
## overhaul; source of truth is the code on disk, not this document —
## verify against `btf-p1-l01-eternal-life.html` if anything here seems
## to disagree with what you see)

1. **Sticky audio panel** — pinned to top of viewport on every page.
   Main Play button ("Play Lesson" on lesson pages / "Play Overview" on
   index), Stop button, a speed **dropdown** (`.btf-speed-dropdown` /
   `.btf-speed-toggle` / `.btf-speed-menu` / `.btf-speed-option[data-rate]`
   — this replaced the earlier row of five separate speed buttons), and a
   live progress label.

2. **Text-to-speech engine** — browser `speechSynthesis`, en-GB. Main
   button plays every section on the page in order, opening/scrolling/
   highlighting as it goes, with **read-along text highlighting** during
   plaback and **sentence-level resume** if paused and restarted
   (both added in the overhaul — this logic now lives in
   `btf-lesson-page.js`, not inline). Per-section "▶ Play Section"
   buttons still work independently. Speed choice persists via
   `localStorage` key `btf-audio-rate`, shared site-wide.

3. **Collapsible sections** — unchanged from original build: every
   content block toggles independently, auto-inserted "▲ Minimise"
   buttons scroll back to that section's header, Expand All/Minimise All
   act on the whole page (Minimise All also scrolls to top).

4. **Responsive tables** — unchanged: `.table-wrap` wrapper auto-tags
   `data-label` per cell for mobile card layout below 640px.

5. **Floating table of contents** — unchanged: fixed bottom-right,
   toggle opens/closes a jump-list, closes on link click/outside click/
   Escape.

6. **Flashcards / revision cards** — unchanged: per-lesson inline
   script, `.flashcard[role="button"][tabindex="0"]`, click or Enter/
   Space to flip, CSS-driven 3D flip.

7. **Fillable Key Discovery Questions** — unchanged mechanically:
   `contenteditable` divs, `data-key` per the part-namespaced pattern
   above, autosave/restore via `localStorage`, Download and Clear (with
   confirm dialog) buttons, per-lesson inline script.

8. **`localStorage` key discipline** — see Naming conventions above.
   When adding a new part, the part-namespaced pattern is already
   established; just continue it.

## Standard lesson page structure, in order

`<body data-btf-page="lesson">` → back link to index → title block
(series name, "Part N of 3: [subtitle]") → lesson title block (H1,
"Lesson N of 16 | Section X: [name]") → sticky audio panel → Opening
Question → Key Scripture → Core Truth → Bible Teaching (collapsible,
Note/Depth/Caution callouts as needed — no Tip in student files) → Key
Discovery Questions (collapsible, fillable) → Group Discussion
(collapsible) → Application (collapsible) → Revision Cards (collapsible,
flashcards) → Expand All/Minimise All → back link → page footer →
floating TOC → `<script src="btf-site.js">` → `<script
src="btf-lesson-page.js">` → inline script (flashcard flip + fillable
answers only).

## Known git issue — read before running any git command

`device_bash` runs the Windows machine's shell but cannot delete files
without an explicit granted permission, and that permission has been
**denied every time it's been requested** (auto-mode classifier flags it
as "Irreversible Local Destruction"). Consequence: `.git/HEAD.lock`,
`.git/index.lock` and/or `.git/objects/maintenance.lock` reliably get
left behind after almost every git operation run from `device_bash`, and
they block the next git command until removed.

**Fix, every time:** ask Dave to manually delete those lock files via
File Explorer (View → show Hidden items → the `.git` folder) before the
next git command. This is a recurring, expected step, not a bug to solve
differently — do not keep retrying `device_request_delete_permission`.

**If the remote has diverged** (another session/device pushed commits
you don't have locally): do **not** run `git merge` or `git pull` — a
conflict would need interactive resolution that can't reliably clean up
after itself given the lock-file problem. Instead:
1. `git fetch origin`, then diff which files changed on each side
   (`git log --oneline HEAD..origin/main`, compare changed-file lists).
2. For any remote-changed file you don't need to change yourself, take
   the remote version directly: `git show origin/main:<path> > <path>`.
3. Rebuild anything you were changing (e.g. lesson files) from the
   *now-current* template/shared files, not from a stale local copy.
4. To land the final commit cleanly, have Dave run (via a PowerShell
   block, since lock files may need clearing first): delete locks →
   `git fetch` → `git reset --mixed origin/main` → `git add -A` →
   commit → `git push`. This has worked cleanly once already (18 Sep
   2026, commit `e194054` on top of `dffb1a4`).

**Author identity:** `device_bash`'s default git identity isn't
configured. Always commit with explicit flags:
`-c user.name="David Agyei" -c user.email="david.agyei@gmail.com"`.

**Deploy verification lag:** after a successful push, Cloudflare Pages
can take up to ~90 seconds to redeploy and its edge cache can serve a
stale page briefly after that — wait, then re-fetch with a cache-busting
query string before concluding anything is wrong.

## Workflow for adding a new part or lesson

1. Read `status-update-biblefoundations.md` for current state and open
   decisions.
2. Propose the section arc for the new part's lessons; wait for
   approval before writing content.
3. Generate lesson content in the project's gated phases (theology, then
   application) before building any HTML. Confirm with Dave whether this
   session is content-only (write and present for review, no HTML/git)
   or a full build — he has asked for content-only stages before.
4. Build HTML using `build-tools/builder.py` (clones the *current*
   `btf-p1-l01-eternal-life.html`, so it inherits the live audio engine
   automatically) rather than reconstructing structure from this spec
   alone or from an older template copy.
5. Add the new part's sections to the existing `index.html` (don't
   create a second index page unless explicitly asked).
6. Generate the part's Complete Course markdown and Teacher's Guide HTML
   once all lessons are built.
7. Commit in logical chunks, not one giant commit — but check
   `git log --oneline -5` first in case the remote has moved since the
   session started (see Known git issue above).
8. Push to `origin main`; wait ~90 seconds, then confirm the live site
   updated using a cache-busting fetch.
9. Update `status-update-biblefoundations.md` with a dated changelog
   entry before ending the session.
