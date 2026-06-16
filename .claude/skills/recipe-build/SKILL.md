---
name: recipe-build
description: Build a new recipe or substantially change an existing one the house way — and ALWAYS for bulk/freezer runs. Enforces the Recipe Build Protocol (interrogate inputs, formula-not-vibes, adversarial pre-delivery validation, test-batch-before-bulk) and the 7 publish gates. Use whenever creating, converting, reworking, "fixing", or "auditing" a recipe card.
---

# Recipe Build Protocol

Full rules live in `CLAUDE.md`. This skill is the operational checklist + the pre-delivery
validation engine. Born from a real failure: a carne asada got buried under cumin, an
over-engineered salsa took ~6 unvalidated revisions, and 15 lb of beef + $120 got committed
to recipes that had never been cooked. Never again.

## Step 0 — Interrogate (before proposing anything)
Ask, scaled to stakes:
- **Scale + stakes** — lbs and $$. ≤~2 lb one-off = loose; **>~3 lb / >~$40 / frozen-in-portions = full protocol.**
- **Existing method that works?** Start there — don't reinvent the user's zero-issues move.
- **STATE of the variable ingredients** — dried-chile age/pliability, flour protein, salt brand. *Counts are meaningless without state* (old brittle árbol ≠ fresh; you'd need ~2× the count).
- **Equipment + reference target** — what they're cooking on, and what "good" tastes like.

## Step 1 — Formula, not vibes
Ratios / % that **scale**, anchored to the user's baseline or a cited recipe. Variable-potency
items → a TARGET (heat level, % salt by weight) + a state adjustment, never a raw count.

## Step 2 — Validate before delivery (the swarm)
Author and run a Workflow from `build-validate.js` in this folder: it puts the DRAFT through
adversarial critics — traditional cook, food scientist, practical cook, "over-engineered?",
"did we ask the right inputs?" — each scoring it against the 7 publish gates, then a synthesis
verdict (**go / fix-then-go / no-go**) with required changes. Only show the user a draft that
survives, with assumptions + open questions flagged. (For tiny edits, run the gates yourself;
for new recipes and bulk, run the swarm.)

## Step 3 — Never bulk an unvalidated recipe
Bulk = cook a **1-lb test batch, taste, adjust, THEN scale.** Mandatory, not advisory.

## Step 4 — Version on the cook
Stays **v1.0** until actually cooked. Pre-cook iteration does not bump the version.

## The 7 publish gates (every card passes all 7)
1. **Doneness** — probe only where it governs (thigh 175–185°F+; submerged = tenderness cue; dice/cookies = char/visual).
2. **Salt is tasted, not calculated** — count sodium sources only to kill false "no-salt" claims; never chase a % and NEVER re-salt a dish the cook has made (their palate wins).
3. **Honesty** — no false "authentic/restaurant-style"; no identity/balance/mechanism claim as fact unless cooked.
4. **Lean** — no dashboards/version-callouts/pseudo-precision; each cue once.
5. **Numbers reconcile** — ratio == batch; divides/yields; named ingredients == shopping list; flip/step counts == prose.
6. **Cuisine identity** — ingredient-forward cuisines lead with the signature; don't flatten genuinely layered ones.
7. **Balance & finish** — name the acid lever; troubleshooting guards the LIKELY failure.

## After it passes
`python build.py <name>` until `[PASS]`, eyeball page 2, commit + push.
