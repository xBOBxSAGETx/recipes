"""Robust footer-collision detector. The footer (.foot) is CSS-pinned at bottom:0.4in,
so its text sits at y~760-766 on a 792pt page. Body content must stay above the footer
rule (~y=750). Anything between ~750 and the footer, or past it, is an overflow.
We identify the footer by its y-cluster (the lowest tight cluster of spans), then flag
any span above it that still dips below the safe body limit."""
import fitz

def footer_collisions(pdf_path, safe_limit_in=0.58):
    doc=fitz.open(pdf_path); problems=[]
    for pi,pg in enumerate(doc):
        H=pg.rect.height
        safe_bottom = H - safe_limit_in*72     # body text must end above this (~750pt)
        spans=[(sp["bbox"][3], sp["text"].strip())
               for bl in pg.get_text("dict")["blocks"]
               for ln in bl.get("lines",[]) for sp in ln.get("spans",[]) if sp["text"].strip()]
        if not spans: continue
        # footer y-cluster = spans within 6pt of the maximum y (the pinned footer line)
        maxy=max(y for y,_ in spans)
        footer_ys=[y for y,_ in spans if y>=maxy-6]
        footer_top=min(footer_ys)
        for y,t in spans:
            if y>=footer_top-6: continue        # this IS the footer line, skip
            if y>safe_bottom:                    # body text below the safe limit but above footer
                problems.append((pi+1, round(y,1), t[:55]))
    return problems

if __name__=="__main__":
    import sys
    probs=footer_collisions(sys.argv[1])
    if probs:
        print("OVERFLOW DETECTED:")
        for x in probs: print(f"  page {x[0]}  y={x[1]}  :: {x[2]}")
    else:
        print("CLEAN — body clears the footer on every page")
