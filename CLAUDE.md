# Aguillon House Kitchen — Claude Code guide

Single-source HTML recipes rendered to print-ready, validated PDFs. One recipe =
one file in `recipes/`. `template.html` is the design system; `LESSONS.md` is the
rulebook. **Read `LESSONS.md` before editing any recipe, `template.html`, or
`build.py`** — every rule there exists because ignoring it broke something.

## Build & validate

```bash
python build.py                # build + validate ALL recipes -> dist/
python build.py nyc-bagels     # one recipe (substring match on filename)
python build.py --check-only   # validate existing dist/ PDFs, don't re-render
```

- A recipe is DONE only when `build.py` prints `[PASS]` for it. Never call a recipe
  finished while any gate fails — fix and re-run until green.
- Toolchain is already installed on this machine (playwright, pypdf, pymupdf +
  Chromium). If a browser reinstall is ever needed it's
  `python -m playwright install chromium` — the bare `playwright` command is NOT on
  PATH (user install).
- Working renders go to `dist/` (gitignored). Every recipe that PASSES is also
  auto-copied to `pdfs/` (git-tracked) — that's the **phone-facing** output: commit
  + push and the recipe shows up in the GitHub mobile app, tap to Save to Files.
  So a finished change is: build (passes → publishes to `pdfs/`) → commit → push.

## The gates (all enforced by build.py)

1. Filename has exactly ONE dot before `.pdf` (iOS mislabels multi-dot PDFs as "data").
2. Valid PDF (parses with pypdf).
3. **No footer overflow** on any page (`overflow_check`) — the hard one.
4. No bare `tsp`/`tbsp` in rendered text (weigh in grams; ml ok).
5. Balanced `<span>` tags.
6. No mangled HTML entities in output (literal `mdash;` etc.).
7. No blank pages.
8. Version stamp (`vN.N` / `vN-N`) in every page footer.

## Editing rules (the ones that bite)

- **Never `sed` a line with HTML entities** (`&mdash; &deg; &amp;`) — it mangles the
  `&`. Use Edit/Write (Python string-replace), never stream-edit those lines.
- **Fixing footer overflow:** tighten vertical rhythm on **page-2-only** elements
  (step padding, callout / `.diag` / `p.lead` margins) so page 1 is untouched and no
  recipe content is cut. The safe limit is tight — expect 2–3 nudge-and-rebuild
  passes; the last wrapped word can clear by a fraction of a point.
- **Eyeball it too.** After a near-full page passes, rasterize page 2 and look — a
  one-line collision once slipped past the detector. Quick render:
  `python -c "import fitz; fitz.open('dist/NAME.pdf')[1].get_pixmap(dpi=140).save('dist/_chk.png')"`
  then read the PNG (delete it after; it's in gitignored `dist/`).

## Adding / converting a recipe

**Lean format is the house standard** (see `LESSONS.md` → Layout): a tight **2-page**
guide — page 1 = identity + spec + ingredients + key targets, page 2 = method with the
troubleshooting / quality table folded in **at the bottom**. NEVER give troubleshooting
(or quality/storage) its own page floating above white space — fold it under the method
on page 2. Overflowing two pages? Cut redundancy (a timeline that restates the steps, a
callout that repeats a target) before adding a page. Small recipes are **one page** —
don't pad. Page titles are plain descriptors (`Execution`, not `Execution & Read`).

1. Create `recipes/<kebab-name>.html` using the design system from `template.html`
   (same `<style>` block + grammar: kicker → h1/sub/rule → spec strip → h2 sections
   → ingredient tables / gold-circle steps / callouts / diag tables → footer).
2. Units: grams for weight; counts for whole items (eggs, pods, bay); ml for liquids;
   no tsp/tbsp. Resolve vague heat ("medium-low") to an IR temp, or state the visual
   cue. Multi-stage cooks: per-page temp targets, not a front-page dashboard.
3. Version-stamp the footer of every page.
4. Run `python build.py <name>` until `[PASS]`, eyeball page 2 if it's near-full.

## Commit & push

- Commit only finished, passing work. Conventional one-line summary + short body.
- Push to `main` when the user asks. End commit messages with the Co-Authored-By
  trailer if configured.
- One source per recipe — don't fork a recipe into two files (drift creeps in; git
  history is the archive).

## Working from the phone (Remote Control)

This repo is built to be driven from the Claude mobile app against a Remote Control
session running on the laptop. The laptop is the engine (it runs `build.py` +
Chromium); the phone is the remote. **The laptop must stay awake with the session
running.**

**One-time setup (laptop) — Remote Control needs a full-scope Max login:**
An `ANTHROPIC_API_KEY` or `setup-token` is *inference-only* and `/rc` will refuse it
("requires a full-scope login token"). The account here runs on the **Claude Max
plan only**; `ANTHROPIC_API_KEY` was removed from the Windows User env (2026-06-13)
so sessions use Max, not pay-per-token API billing. To pair:

1. Fresh terminal → `claude auth login` (browser login with the Max account).
2. `cd C:\Users\aagui\Recipes` then `claude`; in the session type `/rc`, press
   **spacebar** for the QR code.
3. Phone: Claude app → **Code** tab → scan the QR / tap the session. Paired = computer
   icon + green dot. (`/config` → "Enable Remote Control for all sessions" makes it
   automatic.)

**Driving it:** front-load instructions so the session doesn't stop to ask —
a complete instruction looks like:

> "Set the curry's salt to 9 g, rebuild, confirm overflow_check passes, commit and push."
> "Convert this pasted recipe into `recipes/<name>.html` in the house style, build
>  until it passes, then commit and push."
