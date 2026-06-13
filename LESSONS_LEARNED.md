# LESSONS LEARNED — gotchas log

Mistakes actually hit while working this repo, each with its **root-cause fix**, so they
don't repeat. `LESSONS.md` is the *recipe* rulebook; this file is the *process* one —
the "why did Claude do that again" list. **Read it before editing.** Add an entry every
time something bites, even if it feels obvious in the moment.

---

## Fonts & non-Latin glyphs

- **Vietnamese / accented glyphs (ở, ạ, ê, á…) fall back to an ugly mismatched serif.**
  Helvetica/Arial have no *bold* form of some precomposed glyphs (e.g. ở U+1EDF), so
  Chromium substitutes a serif for that one character — bold "Ph" + thin serif "ở" looks
  broken.
  **Root-cause fix:** lead the document's `body` font stack with a Unicode-complete sans
  that has the glyphs in every weight — **Segoe UI** on Windows:
  `font-family:"Segoe UI","Helvetica Neue",Helvetica,Arial,sans-serif;`. That covers the
  WHOLE doc and every future edit.
  **The mistake I actually made (twice):** patched only the `<h1>` title with a scoped
  span and shipped it, leaving every other "phở" (Brix table, callouts, footers) still
  serif. **Fix the font stack, not individual words — you will always miss one.** If a
  glyph defect appears in one place, assume it's everywhere and fix at the root.

## Charts & diagrams

- **When the source has a chart, reproduce the chart — and match the source exactly.**
  Don't substitute a table (I replaced the phở seasoning *curve* with a table; the user
  wanted the graph). Inline **SVG** in the house palette renders crisp in the PDF and
  passes the overflow gate (text sits mid-page).
- **Match the source's layout, not just the gist.** The phở curve mismatched because I
  put all x-labels on the bottom; the source **alternates** them (top: even positions,
  bottom: odd) and has faint SWEET/SALTY gridlines. Replicate label placement, gridlines,
  and the actual point heights.

## Visual QC

- **"Eyeball it" means diff against the SOURCE, not just check for overflow.** A `[PASS]`
  from `build.py` means the gates passed — NOT that it's visually faithful. Render the
  source page and the output side by side and compare before calling it done.
- **Rasterize PDFs with PyMuPDF, not `pdftoppm`** (not installed here, and `Read` on a PDF
  fails with "pdftoppm not found"). Works for both uploaded sources and `dist/` output:
  `python -c "import fitz; fitz.open('dist/x.pdf')[PAGE].get_pixmap(dpi=150).save('dist/_chk.png')"`
  then Read the PNG. Delete the temp PNG after (it's in gitignored `dist/`).

- **The overflow gate had a blind spot — a footer collision can report `[PASS]`.** The old
  `overflow_check.py` found the footer as "the lowest y-cluster" and skipped anything within
  6pt of it; when a body row sagged *into* the footer band it looked like the footer and got
  skipped (nyc-bagels page 2 shipped with the last diagnostics row overlapping the footer,
  gate green). Fixed by **anchoring the footer by content** ("Aguillon House Kitchen" /
  "Page N/M") and flagging any non-footer span below the safe limit. Lesson stands regardless:
  **a `[PASS]` is necessary, not sufficient — eyeball page bottoms.** After any detector change,
  re-run the full build as a sweep (it flags every recipe at once).

- **Footer text is letter-spaced, so PyMuPDF extracts it with spaces between characters**
  ("A GU IL L ON ..."). Any text-matching against rendered spans (footer anchors, the
  mangled-entity gate, etc.) must normalize whitespace first (`re.sub(r"\s+","",t).lower()`),
  or literal substring matches silently fail.

## Process

- **Fix the root cause / all instances, not the first one you see.** Before declaring a
  defect fixed, grep for every occurrence. Patching the first instance and moving on is
  what makes the same gotcha resurface.
- **Git on Windows prints `LF will be replaced by CRLF` warnings** on add/commit. Benign —
  not an error, don't chase it.
