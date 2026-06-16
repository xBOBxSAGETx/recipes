# TODO — Aguillon House Kitchen

## 🔝 Priority
- [ ] **Install iCloud for Windows** on the laptop, set up an **iCloud Drive synced folder**
  for the recipe PDFs. The GitHub app *views* files fine but **won't download PDFs** to the
  phone; iCloud Drive shows them natively in the iPhone **Files** app (tap to open, offline
  at the griddle).
- [ ] **Wire `build.py` to copy every passing PDF into that iCloud folder** (once iCloud is
  installed + the folder path is known) → finished recipes auto-appear on the phone. No
  GitHub, no asking. Just tell Claude the folder path and it gets wired.

## 🔧 Repo audit fix queue — decisions locked 2026-06-16
Run each through the **Recipe Build Protocol** (validate before delivery; bulk items get a test batch). High → low.
1. [ ] **cubano-complete** — kill the false "no-salt marinade" (count Maggi's ~6 g Na), stop triple-salting, set a real salt target; trim Tex-Mex cumin to a whisper + Mediterranean (not Mexican) oregano; add filling weights.
2. [ ] **pho** — cut the 3–5× spice load; **cross-reference the Leighton pho recipe** (the gold standard) and match it; reconsider garlic adulteration / blanch.
3. [ ] **colorado-green-chile** — add **browned pork butt** chunks (in place of chicharrón-only); reconsider tomato; fix lumpy flour method; cut chicharrón-taught-4× bloat.
4. [ ] **naan** — KEEP the **pliable (no-yeast) style** (user prefers it). Fix only the FALSE "yeast = bready / restaurant-style" framing → honest "pliable-style"; fix divide-math + self-contradicting cook method.
5. [ ] **nyc-bagels-bulk** — KEEP **60% hydration** — empirically 55% gave tough/inedible bagels on **14.2% Sir Lancelot**. Audit's "drop to 55–58%" is WRONG for this flour. Fix framing, not the number.
6. [ ] **endgame-hummus** — raise tahini to tahini-forward (~co-equal w/ chickpea, ~50–60% of chickpea wt vs current ~23%); add fresh garlic / acid for body.
7. [ ] **chicken-curry** — up salt ~0.55% → **~0.9–1.0% (~28–34 g)**; kill the false "sear builds fond" mechanism; rebalance acid vs caramelized-onion sweetness.
8. [ ] **meatloaf-sandwich** — fix the over-salted fry blend (recut to a real salt target); de-stack the triple-glutamate + redundant A1.
9. [ ] **sloppy-joes** — add anti-crowding/steaming sear guidance; add a "too sweet" troubleshooting row + bun/assembly; fix the stated food-science error.
10. [ ] **pollo-asado** — thigh doneness → **185–195°F** (user's call); fix the backwards "dry meat → pull early" fix; cut cumin from the fresh green; add a pat-dry step.
11. [ ] **sushi-burrito** — reconcile rice ratio (page-1 label vs gram batch); set the best seasoning ratio and make page-1 == batch.
12. [ ] **al-pastor** — **NO pineapple** (team onion); handle acid/sweet balance another way (trim vinegar / lean on onion); honest-label the "medium" heat; reconsider 9% achiote.

### Pending the user's call (audit-flagged, not yet decided)
13. [ ] **pozole-rojo** — impossible 195–205°F pork gate → tenderness cue; delete phantom pasilla.
14. [ ] **carne-asada-picada** — unprobeable 130–140°F griddle pull (×3) → char/time cue; reconsider heavy Maggi spine.
15. [ ] **chicken-shawarma** — thigh 165°F → 175–185°F+; rebalance cumin-led blend toward allspice/sumac.
16. [ ] **nixtamal-tortillas** — simmer 15–25 → ~20–50 min (cue-led); spec the "pinch" salt; fix flip-count naming.
17. [ ] **maseca-tortillas** — drop the tamale float-test (wrong test); validate/justify the toast step; trim bloat.
18. [ ] **molasses-cookies** — unsalted butter + real salt total; fix the 175°F pull vs chewy promise.
19. [ ] **toum** — "stiff peaks" → "mounds / holds a trail" (×3); minor honesty tweaks.

## 🍳 Dial on the next cook
- [ ] **Carne asada picada** — cook a thawed bag, taste, fine-tune garlic / cumin / salt.
  v1.0 is a confirmed "money baseline," but only tasted as raw marinade so far — validate it
  seared.
- [ ] **Cubano v1.6 bread** — first real bake with **Sir Lancelot high-gluten + 63% + 48 hr
  marinade**. Confirm sturdier-after-toast and deeper flavor penetration. Try **64–65%**
  hydration if you want a more open crumb.

## 🧪 Build / finish later
- [x] **Legg's chorizo card** — vinegar filled in (5% acidity, ~4% / **19 ml per lb**, 1 pint
  per 25 lb) + Legg's double-grind method (½″ → season → 3/16″). ✅ done 2026-06-14
- [ ] **Sausage clones (scratch)** — endgame **Jimmy Dean breakfast sausage** + **endgame
  chorizo**, after the Legg's premix trials set a baseline to beat.
- [ ] **Scratch mojo** — replace the doctored Badia for full god-tier Cubano (sour orange /
  naranja agria, garlic, Mexican oregano, cumin).

## 📱 Phone access — how it actually works
- **View** any file in the GitHub mobile app (markdown renders, PDFs preview) — just no download.
- **Get a PDF onto the phone:** (a) ask Claude → it sends to the Claude app → Save to Files;
  (b) Safari → github.com → the PDF → **"Download raw file"** (works on the private repo while
  logged in); (c) the **iCloud Drive folder**, once set up (the goal above).
