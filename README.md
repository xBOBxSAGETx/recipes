# Aguillon House Kitchen

Print-ready recipe PDFs in a consistent house design system. Each recipe is a
single HTML source in `recipes/`; `build.py` renders it to a validated PDF.

## Recipes

| Recipe | Source | Notes |
|---|---|---|
| NYC Bagels (bulk) | `recipes/nyc-bagels-bulk.html` | Straight-dough bulk method, air-gap + flip bake |
| The Cubano (complete) | `recipes/cubano-complete.html` | Full system: bread → pork → reduction → press |
| Cuban Pork System | `recipes/cuban-pork-system.html` | Standalone pork, mirrors the Cubano |
| Cuban Bread | `recipes/cuban-bread.html` | AP-flour, lard-structural, pressable |
| Chicken Curry | `recipes/chicken-curry.html` | Mutton-style base, chicken + stovetop |
| Chicken Shawarma | `recipes/chicken-shawarma.html` | Oil-marinade, chop-and-sear |
| Molasses Cookies | `recipes/molasses-cookies.html` | Dark chocolate + pistachio, cold-butter method |

## Build

```bash
pip install playwright pypdf pymupdf --break-system-packages
playwright install chromium

python build.py                # build + validate all → dist/
python build.py nyc-bagels     # one recipe (substring match)
python build.py --check-only   # validate existing dist/ PDFs
```

Working renders land in `dist/` (gitignored). Any failed validation gate aborts that
recipe with a report; we don't ship un-validated PDFs. Every recipe that **passes** is
also copied to `pdfs/` (git-tracked) — the phone-facing output: push it and the PDF is
viewable in the GitHub mobile app (tap → Save to Files/Books).

## How it's organized

- **`template.html`** — the single source of truth for the design system (palette,
  grammar, CSS). Recipes share this exact `<style>` block.
- **`build.py`** — render + validate pipeline. Gates documented at the top of the file.
- **`overflow_check.py`** — footer-collision detector. The reason a page can't
  silently overflow. Run as a hard gate by `build.py`.
- **`LESSONS.md`** — every failure we hit, written as a rule. Read it before editing.

## Design system (quick reference)

Palette: `--char-black #1a1714` · `--broth-gold #c8941e` · `--smoke-gray #6b6560`
· `--paper #f7f4ee` · `--line #d8d0c4`. Grammar: kicker → h1/sub/rule → spec strip
→ h2 sections → ingredient tables / gold-circle steps / callouts / diag tables →
version-stamped footer. Full notes in `template.html`.

## Conventions

- Weigh in grams; counts for whole items (eggs, pods, bay); ml for liquids; no tsp/tbsp.
- Filenames: one dot before `.pdf`; versions use hyphens (`v2-1`).
- Multi-stage cooks: temp targets on each stage's page, not one dashboard.
- One source per recipe — no forks left in the tree.
