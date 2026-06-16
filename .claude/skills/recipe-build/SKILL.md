---
name: recipe-build
description: Build a new recipe or substantially change an existing one the house way — and ALWAYS for bulk/freezer runs. Enforces the Recipe Build Protocol: interrogate inputs, define the target, function-map and STRIP (less = more), reason from mechanism + cultural grammar (NOT google summaries), settle unknowns with controlled tastings, never bulk an unvalidated recipe. Use whenever creating, converting, reworking, "fixing", or "auditing" a recipe.
---

# Recipe Build Protocol

Full rules in `CLAUDE.md`. This is the operational checklist. It exists because the half-assed
approach — spice-rack marinades, over-built salsas, and automated google-summary "audits" — cost
a **$120 bulk batch** and produced confident garbage (a blanket salt % stamped onto dishes the
cook had already nailed). The fix is **depth, not breadth.**

## The method (design, not a search)
0. **Interrogate first** — scale + stakes; the cook's existing method (start there, don't reinvent
   it); the **STATE of the variable ingredients** (old vs fresh chile, flour protein, salt brand —
   *counts are meaningless without state*); equipment + reference target.
1. **Define the target — sensory + cultural.** Its job, the eating experience, the family/cultural
   anchor. Before any ingredient.
2. **Function-map, then strip. LESS = MORE.** Each element = a *job + mechanism*. Find the 3–5 real
   levers; hold the rest; **strip until each ingredient earns its place.** Ratios/% of a base for
   scale (a proportion tool, not the spine).
3. **Reason from mechanism + cultural grammar.** Sources are evidence, **canonical only** (McGee,
   *Modernist Cuisine*, tested chefs, cuisine cookbooks, the cook's family) — **never SEO
   blogs/YouTube, never an automated search-and-summarize swarm.** The cook's tongue and family
   beat every source.
4. **Unknowns → a controlled A/B, one variable, taste-judged by the cook.** Not an opinion, not a
   summary.
5. **Never bulk an unvalidated recipe** — 1-lb test batch, taste, then scale. Mandatory.
6. **Version on the cook** — v1.0 until cooked.

## The 7 publish gates (every card passes all 7)
1. **Doneness** — probe only where it governs (thigh 175–185°F+; submerged = tenderness cue; dice/cookies = char/visual).
2. **Salt is TASTED, never calculated** — never chase a % or re-salt a dish the cook has made (their palate wins).
3. **Honesty** — no false "authentic/restaurant-style"; no claim as fact unless cooked.
4. **Lean** — no dashboards/version-callouts/pseudo-precision; each cue once; strip before adding a page.
5. **Numbers reconcile** — ratio == gram batch; divides/yields; named ingredients == shopping list; counts == prose.
6. **Cuisine identity** — fresh cuisines lead with the signature element; don't flatten genuinely layered ones.
7. **Balance & finish** — name the acid lever; guard the LIKELY failure.

## After it passes
`python build.py <name>` until `[PASS]`, eyeball the pages, commit + push.

> NOTE: the old `build-validate.js` swarm was **removed** — automated breadth-search "validation"
> is exactly what this protocol replaces. Validation is mechanism reasoning + the cook's fork.
