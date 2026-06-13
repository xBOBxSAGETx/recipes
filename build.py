#!/usr/bin/env python3
"""
Aguillon House Kitchen — recipe build + validate pipeline.

Renders every recipe in /recipes to a print-ready PDF in /dist, running the full
validation suite on each. ANY failed gate aborts that recipe with a loud report —
we do not ship a PDF that hasn't passed every check.

Usage:
    python build.py                # build + validate all recipes
    python build.py nyc-bagels     # build + validate one (substring match)
    python build.py --check-only   # validate existing dist/ PDFs, don't re-render

Gates (all must pass):
    1. filename has exactly one dot (iOS mislabels multi-dot PDFs as type "data")
    2. valid PDF: %PDF header, parses with pypdf
    3. overflow_check: NO footer collisions on ANY page  <-- the hard one
    4. no bare tsp/tbsp in rendered text (weigh in grams; ml ok)
    5. balanced <span> tags in source
    6. no mangled HTML entities in RENDERED text (literal 'mdash;' etc.)
    7. every page is non-blank (rasterize check)
    8. version stamp present in the footer of every page

Requires: playwright (chromium), pypdf, pymupdf (fitz).
    pip install playwright pypdf pymupdf --break-system-packages
    playwright install chromium
"""
import sys, re, shutil, pathlib
from playwright.sync_api import sync_playwright
from pypdf import PdfReader
import fitz
from overflow_check import footer_collisions

ROOT = pathlib.Path(__file__).parent
RECIPES = ROOT / "recipes"
DIST = ROOT / "dist"          # working renders (gitignored)
PDFS = ROOT / "pdfs"          # phone-facing published copies (git-tracked)

def norm(s): return re.sub(r"[\s.,\-]+", "", (s or "").lower())

def render(src: pathlib.Path, out: pathlib.Path):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto(f"file://{src.resolve()}")
        pg.pdf(path=str(out), prefer_css_page_size=True, print_background=True)
        b.close()

def validate(src: pathlib.Path, out: pathlib.Path):
    """Return list of failure strings (empty = all gates passed)."""
    fails = []
    s = src.read_text()

    # 1. filename one dot
    if out.name.count(".") != 1:
        fails.append(f"filename has {out.name.count('.')} dots (must be exactly 1)")

    # 2. valid PDF
    try:
        head = out.read_bytes()[:5]
        if not head.startswith(b"%PDF"):
            fails.append("missing %PDF header")
        r = PdfReader(str(out))
        pages = [pg.extract_text() or "" for pg in r.pages]
    except Exception as e:
        fails.append(f"pypdf could not parse: {e}")
        return fails  # can't run text gates without pages

    full = " ".join(pages)

    # 3. overflow_check — HARD GATE
    ov = footer_collisions(str(out))
    if ov:
        fails.append(f"OVERFLOW / footer collision: {ov[:4]}")

    # 4. no bare tsp/tbsp
    if re.search(r"\btsp\b", full.lower()) or "tbsp" in full.lower():
        fails.append("contains tsp/tbsp (convert to grams)")

    # 5. balanced spans
    if s.count("<span") != s.count("</span>"):
        fails.append(f"unbalanced spans ({s.count('<span')} open / {s.count('</span>')} close)")

    # 6. mangled entities in RENDERED text (literal 'mdash;' etc. that should be glyphs)
    mangled = re.findall(r"\b(mdash|ndash|deg|frac\d+|plusmn|Prime|rarr|times);", full)
    if mangled:
        fails.append(f"mangled entities in output: {set(mangled)}")

    # 7. non-blank pages
    doc = fitz.open(str(out))
    for i, pg in enumerate(doc):
        sample = pg.get_pixmap(dpi=72).samples[::997]
        if len(set(sample)) < 5:
            fails.append(f"page {i+1} appears blank")

    # 8. version stamp in every page footer (looks for vN.N or vN-N token)
    has_ver = all(re.search(r"v\d", norm(p)) for p in pages)
    if not has_ver:
        fails.append("version stamp missing from one or more page footers")

    return fails

def build_one(src: pathlib.Path, check_only=False):
    out = DIST / (src.stem + ".pdf")   # kebab-case stem -> one-dot filename
    DIST.mkdir(exist_ok=True)
    if not check_only:
        render(src, out)
    fails = validate(src, out)
    status = "PASS" if not fails else "FAIL"
    print(f"[{status}] {src.name} -> dist/{out.name}")
    for f in fails:
        print(f"        - {f}")
    if not fails:
        # Publish the passing PDF to the git-tracked pdfs/ folder so it syncs to
        # the phone (browse in the GitHub mobile app). Only validated PDFs land here.
        PDFS.mkdir(exist_ok=True)
        shutil.copy2(out, PDFS / out.name)
        print(f"        published -> pdfs/{out.name}")
    return not fails

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check_only = "--check-only" in sys.argv
    srcs = sorted(RECIPES.glob("*.html"))
    if args:
        srcs = [s for s in srcs if any(a in s.stem for a in args)]
    if not srcs:
        print("No matching recipes in /recipes")
        sys.exit(1)
    ok = True
    for src in srcs:
        ok &= build_one(src, check_only)
    print("\n" + ("ALL RECIPES PASSED" if ok else "BUILD FAILED — see failures above"))
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
