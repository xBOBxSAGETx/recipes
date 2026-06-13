# LESSONS

Hard-won rules from building these recipes. Each one is a failure we actually hit.
Read this before changing `build.py`, `template.html`, or adding a recipe — every
rule here exists because ignoring it broke something.

## Validation

- **`len(pages) == N` is NOT an overflow test.** A page can be the correct *count*
  while its content spills past the boundary — `overflow:hidden` clips the overrun
  so it's invisible in the PDF and even easy to miss in a low-dpi render. This gave
  false confidence repeatedly. The fix is `overflow_check.footer_collisions()`,
  which finds the footer by its y-position cluster and flags any body text that
  dips into the footer band. It is a **hard gate** in `build.py`. Trust it, and
  still eyeball a rasterized render — both, every time.

- **The rasterized eyeball stays mandatory.** A one-line collision slipped past a
  110-dpi visual check. Render and look, in addition to the detector.

- **Near-full pages need 2–3 spacing passes, not one.** The footer gate's safe
  limit is tight — on a packed page the last wrapped word can clear by a fraction
  of a point (a fix once landed at 750.4 vs a 750.2 limit, ~0.16pt). Don't expect
  to nail it in one edit; nudge a spacing token, re-run `build.py`, repeat. Fix it
  by tightening vertical rhythm on **page-2-only elements** (step padding, callout
  / diag / lead margins) so page 1 is untouched and no content is cut.

## Editing HTML

- **Never `sed` a line containing HTML entities (`&mdash;`, `&deg;`, `&amp;`, …).**
  `sed` mangles the `&`, nests old text inside new, and produces literal `mdash;`
  or doubled spans. Use Python string-replace or an editor's str-replace instead.

- **Balanced spans / one source of truth for CSS.** The design system lives in
  `template.html`. Change a token there; don't let recipes drift apart.

## Filenames

- **One dot only before `.pdf`.** iOS mislabels PDFs with internal dots (e.g.
  `Cubano.v1.3.pdf`) as type "data" and refuses to render them. Versions use
  hyphens: `v1-3`, `v2-1`. Build output is kebab-case `recipe-name.pdf`.

## Layout

- **Lean 2-page default. Never strand troubleshooting on its own page.** The house
  format is a tight 2-page guide: page 1 = identity + spec + ingredients + key
  targets; page 2 = method + the troubleshooting / quality / storage table folded in
  **at the bottom**, under the steps. A page that carries only a troubleshooting table
  above a screen of white space reads as bloat — fold it under the method on page 2.
  This was a real fix: chicken-curry, nixtamal, and sushi each shipped with a near-empty
  third page that was just troubleshooting/quality; all three got pulled back to 2 pages.

- **If a recipe overflows two pages, cut redundancy before adding a page.** A timeline
  that just restates the step list, a callout that repeats a key-targets row, notes that
  paraphrase the method — that's the fat. Meatloaf went 4pp&rarr;2pp by replacing an
  11-row timeline with one compact "run of show" callout and folding each side-sauce's
  one-line method into its `h2 .note`. Only add a page when the *content* genuinely
  needs it (a true multi-stage cook), never to relieve cramming you could trim away.

- **Small recipes are ONE page.** A short formula (e.g. hummus: ~8 ingredients, ~7
  steps) fits one page cleanly &mdash; don't pad it to two. One page is the leanest
  expression and still passes every gate.

- **Page titles are descriptors, not slogans.** Page 2 is `Execution`, not
  `Execution & Read`; `Build the Curry`, not `Read & Adjust`. Cut the cute "& X" tails.

## Recipe content

- **Per-page temp targets beat a front-page dashboard** for any multi-stage cook.
  A dashboard on page 1 is useless when you're standing at the griddle on page 4.
  Put each stage's targets on that stage's page.

- **Resolve vague heat to an IR number.** "Medium-low" / "warm" is not a target.
  Blooming spices in fat = 250–300°F; a press = 275–300°F surface; etc. If the
  cook is judged by a visual state instead (the bhuna's oil separation, a bagel's
  float test), say *that* explicitly — it's the real target.

- **Weigh in grams; keep counts for whole items.** Eggs, cardamom pods, bay leaves,
  cinnamon sticks stay as counts (you don't gram-weigh 3 bay leaves). Liquids may
  stay in ml. No bare tsp/tbsp — they're the imprecise unit we convert away.

- **Salt by weight is brand-independent.** "2 tsp Diamond Crystal" depends on the
  brand's bulk density; 6 g is 6 g. Convert and note "by weight."

- **Specify what the gram applies to.** "1.5 g cardamom" must say *seeds, not pods*
  (pods are ~20–25% seed by weight). Ambiguous units are silent errors.

## Method / equipment

- **Bagels: pan-on-steel dries the heel.** Direct conduction from a baking steel
  into the pan cooks the heel all bake → tough, dried bottom. Fix: air gap (steel
  one rack *below*, not touching the pan) + flip at halfway for heel relief. The
  pros use bagel boards then flip onto the hearth — the air-gap-then-flip is the
  home equivalent.

- **Match the method to the protein.** A mutton curry's long pressure cook destroys
  boneless chicken thigh — drop pressure, simmer on the stovetop. Don't port a
  recipe's timing across a protein swap without re-deriving it.

- **Fix contradictions when finalizing.** "Add all the salt at the sear" AND "adjust
  salt after reduction" can't both be the plan — salt light early, finish to taste.

## Repo discipline

- **One source per recipe. Don't fork and maintain both.** The Cuban bread formula
  lived in two files and a fix missed one. The bagel poolish/bulk fork meant every
  edit had to land twice (and drift crept in: a 22-vs-24 count, stale timings). If
  a variant is dead, delete it — git history is the archive.

## The meta-lesson

- **Failures live in the *connections* between components, not the components.**
  The bagel toughness and the salt failure were the same root error: treating parts
  in isolation instead of as one system. When something's wrong, check the seams —
  hydration vs. heel, marinade vs. reduction, dashboard vs. the page you're on.
