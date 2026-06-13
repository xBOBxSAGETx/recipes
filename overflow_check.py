"""Footer-collision detector. The footer (.foot) is CSS-pinned at bottom:0.4in, so its
text line sits at the very bottom of the page (y~758-766 on a 792pt page) and is the ONLY
thing allowed below the safe body limit (~y=750). Body content must end above that limit.

We anchor the footer by its KNOWN CONTENT ("Aguillon House Kitchen" / "Page N / M", present
on every page's .foot) rather than by raw y-position. The old version identified the footer
as "the lowest y-cluster" and skipped anything within 6pt of it — so a BODY row that had
collided down INTO the footer band looked like the footer and got skipped. That's a real
miss (nyc-bagels page 2 shipped with the last diagnostics row overlapping the footer while
this gate reported PASS). Anchoring by content means a sagging body span is still flagged
even when it overlaps the footer line."""
import fitz, re

# Footer text is letter-spaced (.foot has letter-spacing:.15em), so PyMuPDF extracts it
# with spaces wedged between characters ("A GU IL L ON ..."). Match on whitespace-stripped
# text so the anchors actually hit.
def _norm(s): return re.sub(r"\s+", "", s).lower()
FOOTER_MARK = "aguillonhousekitchen"
PAGE_RE = re.compile(r"page\d+/\d+")

def footer_collisions(pdf_path, safe_limit_in=0.58):
    doc = fitz.open(pdf_path); problems = []
    for pi, pg in enumerate(doc):
        H = pg.rect.height
        safe_bottom = H - safe_limit_in * 72        # ~750pt; body text must end above this
        spans = []
        for bl in pg.get_text("dict")["blocks"]:
            for ln in bl.get("lines", []):
                for sp in ln.get("spans", []):
                    t = sp["text"].strip()
                    if t:
                        spans.append((sp["bbox"][1], sp["bbox"][3], t))   # top, bottom, text
        if not spans:
            continue
        # Anchor the footer line by content (not by lowest-y), so colliding body text near
        # the footer is NOT mistaken for the footer itself.
        footer_tops = [top for top, bot, t in spans
                       if FOOTER_MARK in _norm(t) or PAGE_RE.search(_norm(t))]
        footer_y = min(footer_tops) if footer_tops else None
        for top, bot, t in spans:
            # The footer's own cells (kitchen mark, version, page N/M) share the footer line's
            # top y — skip those. A body span that has sagged into the zone sits ABOVE that line
            # (its top is higher), so it still gets flagged below.
            on_footer_line = footer_y is not None and abs(top - footer_y) <= 3
            if on_footer_line:
                continue
            if bot > safe_bottom:                   # body text dipping into / past the footer zone
                problems.append((pi + 1, round(bot, 1), t[:55]))
    return problems

if __name__ == "__main__":
    import sys
    probs = footer_collisions(sys.argv[1])
    if probs:
        print("OVERFLOW DETECTED:")
        for x in probs:
            print(f"  page {x[0]}  y={x[1]}  :: {x[2]}")
    else:
        print("CLEAN — body clears the footer on every page")
