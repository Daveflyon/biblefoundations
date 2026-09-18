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

## Deployment chain

Local folder → GitHub (`Daveflyon/biblefoundations`, branch `main`) →
Cloudflare Pages (auto-deploy on push, no wrangler.toml, no manual step).
Live at https://biblefoundations.pages.dev/. Confirm the live site
reflects a change after pushing before calling a task done.

Do not confuse this with https://delessons.org/ — that is the source
ministry's own site, not where this project is hosted.

## File map

- `index.html` — homepage/hub, links to every lesson, holds the
  collapsible Part/Section navigation.
- `btf-pN-lNN-slug.html` — one file per lesson (N = part number, NN =
  lesson number within that part, zero-padded).
- `btf-site.css` — single shared stylesheet for every page. Never fork
  per lesson or per part.
- `btf-site.js` — single shared JS engine for every page (see Functional
  Spec below). Never fork per lesson or per part.
- `Bible Truth Foundation Pt1 - Teachers Guide.html` — teacher-facing
  content, kept separate from student pages.
- `btf-PtN Complete Course.md` — master markdown of a part's full lesson
  text, for read-through outside the HTML.
- `favicon.ico` — shared across all pages.
- `status-update-biblefoundations.md` — current status, what's live,
  what's open. Read this for "where are we right now."

## Non-negotiable build rules

- British English throughout. No em dashes or en dashes anywhere in
  prose — rephrase, use semicolons, or use periods.
- NKJV only, declared once at series level, never repeated on individual
  verses.
- Every HTML file fully self-contained and offline-capable: no external
  fonts, no CDN links, no external API calls. The browser's built-in
  `speechSynthesis` API is fine (it's local to the browser, not a network
  call).
- Never invent new CSS classes. If a lesson's content seems to need one
  that doesn't exist in `btf-site.css`, stop and ask before adding it.
- Never duplicate `btf-site.js` logic inline in a lesson file. The only
  inline `<script>` block a lesson file should have is the small
  per-lesson block for flashcard flip + fillable-answer save/restore/
  download/clear (see Functional Spec, items 6–7) — copy that block's
  structure from an existing lesson, changing only lesson-specific IDs
  and text.
- Teaching Tip callouts (`.callout-tip`) never appear in student-facing
  lesson files — Teacher's Guide content only.
- `<body data-btf-page="lesson">` on every lesson page, `<body
  data-btf-page="index">` on the index page — this attribute is what
  tells `btf-site.js` which behaviours to initialise. Missing or wrong
  and none of the interactivity works.

## Naming conventions

- Lesson files: `btf-p{part}-l{NN}-{slug}.html`, e.g.
  `btf-p1-l01-eternal-life.html`, `btf-p2-l01-self-centeredness.html`.
  Slugs lowercase, hyphenated, terse (match existing Part 1 slugs for
  style).
- Status file for this project: `status-update-biblefoundations.md`
  (the one file to open first in any session).
- Downloaded answer files (generated client-side): `btf-p{part}-l{NN}-
  my-answers.txt`.

## Functional spec — every interactive behaviour, reverse-engineered from
## the live Part 1 build (source of truth is the code, not any earlier
## project brief — some early spec language, e.g. an "arc bar," a
## scroll-triggered sticky bar, was never actually built this way)

1. **Sticky audio panel** — `.btf-audio-panel`, pinned to top of
   viewport on every page (`position: sticky; top: 0`), not a slide-in
   bar. Contains: main Play button (`#btf-btn-play-main`, "Play Lesson"
   on lesson pages / "Play Overview" on index), Stop button
   (`#btf-btn-stop`, disabled until something plays), five speed buttons
   (1x/1.25x/1.5x/1.75x/2x, `.btf-speed-btn[data-rate]`), and a live
   progress label (`#btf-audio-progress`).

2. **Text-to-speech engine** — uses the browser's `speechSynthesis`, en-GB.
   Main button plays every section on the page in order: opens each
   collapsed section as it's reached, scrolls it into view, reads it,
   pauses ~700ms, moves on. Main button toggles Play → Pause → Resume in
   place. Each collapsible section also gets its own auto-inserted
   "▶ Play Section" button (JS-inserted, never hand-authored) that plays
   just that section and can be paused/resumed independently; starting a
   different section stops whichever was playing. Playing section gets a
   highlight class. Speed choice persists via `localStorage` key
   `btf-audio-rate`, shared site-wide across all parts. Spoken text has
   UI chrome (buttons, inputs, toolbars, minimise buttons, TOC,
   flashcard backs) stripped out first, capped at 6000 characters.

3. **Collapsible sections** — every content block on a lesson page
   (`.section-toggle` / `.section-body`) and every Part/Section block on
   the index page (`.part-btn` / `.part-body`) toggle open/closed
   independently. Each open section body gets an auto-inserted
   "▲ Minimise" button (JS-appended at the end of the body) that closes
   just that section and scrolls back to its header. "+ Expand All" /
   "− Minimise All" buttons (`#btf-expand-all` / `#btf-minimise-all`)
   act on every collapsible on the page at once; Minimise All also
   scrolls the whole page to top.

4. **Responsive tables** — any table wrapped in `.table-wrap` gets each
   `<td>` auto-tagged with `data-label` copied from its column header at
   page load, so CSS can render it as stacked mobile cards below 640px.
   No manual `data-label` authoring needed — just use the wrapper.

5. **Floating table of contents** — `.toc-container`, fixed
   bottom-right, on every page. Toggle button `#toc-btn` ("☰ Jump to
   section") opens/closes `#toc-menu`, a list of anchor links to every
   major section on the current page, ending with "↑ Back to top"
   (intercepted to smooth-scroll rather than jump). Closes on: clicking a
   link, clicking outside, or pressing Escape (which also returns focus
   to the toggle button).

6. **Flashcards / revision cards** — per-lesson inline script (not in
   `btf-site.js`). `.flashcard[role="button"][tabindex="0"]` toggles a
   `.flipped` class on click, or on Enter/Space (Space also prevents
   page scroll). 3D flip is CSS-driven, already built — don't touch that
   CSS. 5–6 cards per lesson.

7. **Fillable Key Discovery Questions** — per-lesson inline script.
   Answer cells are `contenteditable` divs: `class="fillable"
   data-key="l{NN}-q{M}-answer"`. Autosaves to `localStorage` on every
   input, restores on page load. "Download" button
   (`#download-btn`) builds a plain-text file of every question/answer/
   group-note and triggers a browser download named per the convention
   above. "Clear all answers" button (`#clear-btn`) shows a native
   `confirm()` dialog before wiping all fillables and their
   `localStorage` keys for that lesson.

8. **`localStorage` key discipline** — `btf-audio-rate` is shared
   site-wide, never namespace it per part. Answer keys use the
   `l{NN}-q{M}-answer` pattern; when adding a new part, confirm whether
   lesson numbering continues globally or restarts within that part
   before writing any `data-key` values, so answers from different parts
   never collide in the same visitor's browser.

## Standard lesson page structure, in order

`<body data-btf-page="lesson">` → back link to index → title block
(series name, "Part N of 3: [subtitle]") → lesson title block (H1,
"Lesson N of 16 | Section X: [name]") → sticky audio panel → Opening
Question → Key Scripture → Core Truth → Bible Teaching (collapsible,
Note/Depth/Tip/Caution callouts as needed) → Key Discovery Questions
(collapsible, fillable) → Group Discussion (collapsible) → Application
(collapsible) → Revision Cards (collapsible, flashcards) → Expand
All/Minimise All → back link → page footer → floating TOC →
`<script src="btf-site.js">` → inline script (flashcard flip + fillable
answers).

## Workflow for adding a new part or lesson

1. Read `status-update-biblefoundations.md` for current state and open
   decisions.
2. Propose the section arc for the new part's lessons; wait for
   approval before writing content.
3. Generate lesson content in the project's gated phases (theology, then
   application) before building any HTML.
4. Build HTML using an existing lesson file as the literal template —
   copy its structure, don't reconstruct it from this spec alone.
5. Add the new part's sections to the existing `index.html` (don't
   create a second index page unless explicitly asked).
6. Commit in logical chunks (e.g. per lesson), not one giant commit.
7. Push to `origin main`; confirm the live site updated.
