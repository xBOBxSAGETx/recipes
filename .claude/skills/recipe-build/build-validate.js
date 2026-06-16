// recipe-build :: pre-delivery validation workflow (TEMPLATE)
// Point DRAFT at the recipe file to validate, then run with the Workflow tool.
// Puts the draft through 5 adversarial critics scoring the 7 house publish gates,
// then a synthesis verdict (go / fix-then-go / no-go) BEFORE the draft reaches the user.

export const meta = {
  name: 'recipe-build-validate',
  description: 'Adversarially validate a recipe draft against the 7 house publish gates before it reaches the user',
  phases: [
    { title: 'Critique', detail: '5 critics score the draft against the 7 gates' },
    { title: 'Verdict', detail: 'go / fix-then-go / no-go + required changes' },
  ],
}

// <-- SET THIS to the draft you are validating:
const DRAFT = 'C:/Users/aagui/Recipes/recipes/REPLACE-ME.html'

const GATES = `
HOUSE STANDARD: a recipe is a recipe, not a manifesto. Mexican = simple/fresh/ingredient-forward (no over-spicing). Formula/ratios, not arbitrary counts. Ask ingredient STATE. Nothing is validated unless cooked.

THE 7 PUBLISH GATES:
1 Doneness — a probe target only where it governs (dark thigh 175-185F+; meat submerged in simmering liquid = tenderness/time cue, can't exceed broth temp; small dice & soft cookies = char/visual cue).
2 Salt budget — every sodium source counted (salted butter, Maggi, soy/fish/Worcestershire, achiote, blends, ketchup); ~0.9-1.0% of finished mass; unsalted butter; taste a test piece before committing.
3 Honesty — no shortcut branded authentic/restaurant-style; no identity/balance/mechanism claim stated as fact unless cooked.
4 Lean — no temp-dashboards restating inline numbers, no version/clever callouts (git is the archive), no pseudo-precision (Brix, yeast models, 2-decimal %); each cue stated once.
5 Numbers reconcile — ratio label == gram batch; divides/yields; named ingredients == shopping list; flip/step counts == prose.
6 Cuisine identity — ingredient-forward cuisines lead with the signature element; do NOT flatten genuinely spice-layered cuisines.
7 Balance & finish — names its acid lever; troubleshooting guards the LIKELY failure.
`

const SCORE_SCHEMA = {
  type:'object', additionalProperties:false,
  required:['lens','gate_scores','most_dangerous','must_change'],
  properties:{
    lens:{type:'string'},
    gate_scores:{type:'array', items:{type:'object', additionalProperties:false, required:['gate','pass','why'],
      properties:{gate:{type:'string'}, pass:{type:'boolean'}, why:{type:'string'}}}},
    most_dangerous:{type:'string'},
    must_change:{type:'array', items:{type:'string'}}
  }
}

const VERDICT_SCHEMA = {
  type:'object', additionalProperties:false,
  required:['verdict','required_changes','open_questions','keep_untouched'],
  properties:{
    verdict:{type:'string'},
    required_changes:{type:'array', items:{type:'string'}},
    open_questions:{type:'array', items:{type:'string'}},
    keep_untouched:{type:'array', items:{type:'string'}}
  }
}

phase('Critique')
const lenses = [
  {k:'tradition', p:"a traditional cook of this dish's cuisine"},
  {k:'food-science', p:'a food scientist judging mechanism, salt/acid/heat balance, and doneness physics'},
  {k:'practical', p:'a practical cook judging repeatability and bench bugs (broken math, contradictions, vague endpoints)'},
  {k:'over-engineered', p:'a skeptic hunting over-engineering, bloat, theater, and crutches — is this needlessly complex?'},
  {k:'inputs', p:"an auditor asking whether the right input questions were asked (ingredient STATE, scale, equipment, the user's proven method)"},
]
const scores = (await parallel(lenses.map(l => () => agent(
  `${GATES}\n\nYou are ${l.p}. READ the recipe draft at ${DRAFT} with the Read tool. Score it against each of the 7 gates (pass/fail + why), name the single most dangerous problem, and list what MUST change before it reaches the user. Use WebSearch only for high-value verification.`,
  {label:`critique:${l.k}`, phase:'Critique', schema:SCORE_SCHEMA}
)))).filter(Boolean)

phase('Verdict')
const verdict = await agent(
  `${GATES}\n\nCRITIC SCORES (JSON):\n${JSON.stringify(scores)}\n\nGive ONE verdict: "go", "fix-then-go", or "no-go". List the REQUIRED changes (only real, agreed issues — kill nitpicks), the open questions to flag to the user, and what to KEEP untouched. Be decisive.`,
  {label:'verdict', phase:'Verdict', schema:VERDICT_SCHEMA}
)

return verdict
