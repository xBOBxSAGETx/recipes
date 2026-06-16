# FIXPLAN — execution-ready repo fixes

Generated 2026-06-16 from the audit + prep swarm. Concrete `from -> to` edits.

> ## ⚠ SALT EDITS ARE NOT TRUSTED — DO NOT APPLY BLINDLY
> The cook has MADE several of these: **cubano is UNDER-salted**, and **al-pastor, pho, and molasses had no salt problem** (pho is naturally salty). The audit's agents fixated on a `~0.9-1.0%` salt target and stamped it everywhere — that recommendation is **void**. Salt is judged by the cook's tongue, never by a %. Every edit tagged `⚠ SALT` below must be **verified against the actual cooked result or skipped**. Honesty *relabels* (don't print "no-salt" when Maggi is in the marinade) are fine; **prescriptive salt-amount changes are not.**

---

## 1. cubano-complete

1. **Kill the false 'No salt' subhead on the Marinade section header (Page 2)** `⚠ SALT — VERIFY/skip`
   - _why:_ The 56 g Maggi carries ~4.7 g sodium (~12 g salt-equivalent); calling this a no-salt marinade is dishonest. Honesty gate + count-every-sodium-source.
   - FROM: `<h2 style="margin-top:14px;"><span class="pt">Part 2</span> &nbsp;Marinade <span class="note">No salt &mdash; salt the meat (see cook)</span></h2>`
   - TO: `<h2 style="margin-top:14px;"><span class="pt">Part 2</span> &nbsp;Marinade <span class="note">Maggi IS the sodium &mdash; salt budget set on the meat</span></h2>`
2. **Trim Tex-Mex cumin from 20 g to a whisper (4 g) to honor the authentic Cuban 2:1 oregano:cumin ratio**
   - _why:_ Authentic Cuban mojo runs ~2 parts oregano to 1 part cumin with cumin as a background note (A Sassy Spoon; TikTok lechon ratio 2 tsp oregano : 1 tsp cumin). 20 g cumin vs 10 g oregano was inverted and Tex-Mex-heavy. Cuisine-identity gate.
   - FROM: `<tr><td>Ground cumin <span class="mut">(fresh)</span></td><td class="amt">20 g</td></tr>`
   - TO: `<tr><td>Ground cumin <span class="mut">(a whisper &mdash; background, not the lead)</span></td><td class="amt">4 g</td></tr>`
3. **Switch Mexican oregano to Mediterranean oregano and make it the dominant herb (10 g -> 8 g, now 2x the cumin)**
   - _why:_ Locked direction: it is a Cuban sandwich; Mexican oregano (citrus/anise note) is wrong cuisine. Mediterranean dried oregano is the shelf-standard Cuban-mojo herb (Slofoodgroup; A Sassy Spoon). 8 g keeps oregano at 2x cumin (4 g) per the authentic ratio.
   - FROM: `<tr><td>Mexican oregano <span class="mut">dried</span></td><td class="amt">10 g</td></tr>`
   - TO: `<tr><td>Mediterranean oregano <span class="mut">dried &mdash; this is a Cuban sandwich, not Mexican</span></td><td class="amt">8 g</td></tr>`
4. **Re-label the Maggi row to flag it as the sodium source instead of just 'umami'** `⚠ SALT — VERIFY/skip`
   - _why:_ 56 g Maggi at ~100 mg sodium/ml (~500 mg per 5 ml, Maggi label) and ~47 ml = ~4.7 g sodium. Naming it stops the recipe from triple-salting blind. Count-every-sodium-source.
   - FROM: `<tr><td>Maggi seasoning <span class="mut">(umami, rec.)</span></td><td class="amt">56 g</td></tr>`
   - TO: `<tr><td>Maggi seasoning <span class="mut">(umami &mdash; ~4.7 g sodium = the marinade&rsquo;s salt)</span></td><td class="amt">56 g</td></tr>`
5. **Replace the dash-only 'Salt (NOT in marinade)' row with the explicit on-meat salt budget** `⚠ SALT — VERIFY/skip`
   - _why:_ 6 lb butt = 2,722 g; 0.9-1.0% finished = ~24.5-27 g. Maggi migration adds salt, so dose the meat to ~0.8% (22 g, ~3.7 g/lb Diamond Crystal) and let Maggi + reduction close the gap. Salt-budget gate; numbers reconcile.
   - FROM: `<tr><td>Salt <span class="mut">(NOT in marinade &mdash; salt the meat)</span></td><td class="amt">&mdash;</td></tr>`
   - TO: `<tr><td>Salt <span class="mut">(on the meat, see cook &mdash; ~0.8%, Maggi covers the rest)</span></td><td class="amt">22 g</td></tr>`
6. **Fix the Combine step parenthetical that re-asserts 'no salt'** `⚠ SALT — VERIFY/skip`
   - _why:_ Removes the false no-salt claim and prevents triple-salting (Maggi + direct + reduction). Honesty gate.
   - FROM: `Whisk hard; it separates into fat/water phases, normal. <span class="mut">(no salt &mdash; the marinade becomes the reduction; salt the meat directly instead)</span></li>`
   - TO: `Whisk hard; it separates into fat/water phases, normal. <span class="mut">(the Maggi is the marinade&rsquo;s salt; the rest goes on the meat &mdash; don&rsquo;t add more here)</span></li>`
7. **Fix the '48 hr is the floor' step that calls it a no-salt marinade** `⚠ SALT — VERIFY/skip`
   - _why:_ Honesty gate: the marinade carries ~4.7 g sodium via Maggi, so 'no-salt marinade' is false.
   - FROM: `<li><b>48 hr is the floor, not the ceiling</b> &mdash; it&rsquo;s a no-salt marinade, so it leans on time to drive the bloomed aromatics in. Under that and the flavor reads shallow.</li>`
   - TO: `<li><b>48 hr is the floor, not the ceiling</b> &mdash; the Maggi + acid drive seasoning in over time; under 48 hr the flavor reads shallow.</li>`
8. **Fix the Marinate temp-target row that repeats 'no-salt marinade'** `⚠ SALT — VERIFY/skip`
   - _why:_ Last remaining no-salt claim on Page 2. Honesty gate.
   - FROM: `<tr><td class="sym">Marinate</td><td>Fridge <b>38&ndash;40&deg;F</b>, <b>48 hr minimum</b> (up to 72) &mdash; no-salt marinade, so time is what drives the flavor in.</td></tr>`
   - TO: `<tr><td class="sym">Marinate</td><td>Fridge <b>38&ndash;40&deg;F</b>, <b>48 hr minimum</b> (up to 72) &mdash; Maggi + acid drive seasoning in; time deepens it.</td></tr>`
9. **Make the 'salt the butt directly' cook row carry the explicit gram dose and acknowledge Maggi** `⚠ SALT — VERIFY/skip`
   - _why:_ Sets the concrete on-meat dose (22 g Diamond Crystal, ~3.7 g/lb) and stops the third salting by telling the cook to taste the reduction first. Salt-budget + numbers-reconcile gates.
   - FROM: `<tr><td><b>Salt the butt directly</b> before roasting <span class="mut">(marinade has none)</span></td><td class="amt">&mdash;</td></tr>`
   - TO: `<tr><td><b>Salt the butt directly</b> before roasting <span class="mut">(~0.8% &mdash; Maggi + reduction close the budget; taste the sauce, don&rsquo;t re-salt blind)</span></td><td class="amt">22 g</td></tr>`
10. **Add filling weights to the Build list (Page 4) per sandwich**
   - _why:_ Locked direction: add filling weights in grams. Classic cubano per sandwich = 2 slices Swiss (~40 g split top/bottom), 3 slices ham (~85 g), 2 pickle planks (~20 g), 1 tbsp mustard (~15 g) (The Recipe Critic; Muy Bueno). Pork ~110 g balances the build. Numbers-reconcile gate.
   - FROM: `<ol class="build">
        <li>Cuban loaf, split</li>
        <li>Yellow mustard, <b>both</b> inside faces</li>
        <li>Swiss <span class="mut">(bottom &mdash; glue)</span></li>
        <li>Roast pork <span class="mut">(soaked in the warm reduction)</span> + spoon extra sauce</li>
        <li>Ham <span class="mut">(ruffled)</span></li>
        <li>Dill pickle planks</li>
        <li>Swiss <span class="mut">(top)</span></li>
        <li>Top bread; <b>butter both outside faces</b></li>
      </ol>`
   - TO: `<ol class="build">
        <li>Cuban loaf, split <span class="mut">(per 8&Prime; sandwich, &times;8)</span></li>
        <li>Yellow mustard, <b>both</b> inside faces <span class="mut">(~15 g)</span></li>
        <li>Swiss <span class="mut">(bottom, ~20 g &mdash; glue)</span></li>
        <li>Roast pork <span class="mut">(soaked in the warm reduction)</span> + spoon extra sauce <span class="mut">(~110 g)</span></li>
        <li>Ham <span class="mut">(ruffled, ~85 g)</span></li>
        <li>Dill pickle planks <span class="mut">(~20 g)</span></li>
        <li>Swiss <span class="mut">(top, ~20 g)</span></li>
        <li>Top bread; <b>butter both outside faces</b></li>
      </ol>`

**Research notes:**
- Maggi sodium: ~500 mg per 5 ml teaspoon (Maggi label / RecipAl / Dillons). 56 g Maggi at density ~1.2 g/ml = ~47 ml -> ~4.7 g sodium = ~12 g salt-equivalent. This is a MAJOR sodium source the recipe currently denies.
- Salt target: 6 lb butt = 2,722 g. 0.9-1.0% finished pork = ~24.5-27 g total salt. Because Maggi migrates salt into the meat over 48 hr, dose the meat at ~0.8% (22 g Diamond Crystal, ~3.7 g/lb) and close the budget with Maggi + reduction; taste the sauce before any further salt. Stops the triple-salt (Maggi + direct + reduced marinade). America's Test Kitchen / VeryMeaty: ~1 tsp Diamond Crystal/lb is a common dry-brine starting point; Diamond Crystal flakes lighter so weigh in grams.
- Authentic Cuban mojo cumin:oregano ratio is ~2:1 oregano:cumin with cumin as a BACKGROUND note (A Sassy Spoon mojo criollo; TikTok lechon asado: 2 tsp oregano : 1 tsp cumin). Current recipe inverted this (20 g cumin : 10 g oregano) = Tex-Mex. New: cumin 4 g (whisper), oregano 8 g (2x).
- Oregano type: it is a CUBAN sandwich. Mexican oregano (citrus/anise, Lippia) is wrong cuisine; Mediterranean oregano (Origanum) is the shelf-standard for Cuban mojo (Slofoodgroup; A Sassy Spoon). True fresh Cuban oregano (Plectranthus, a mint-family thyme) loses oils when dried and isn't shelf-practical, so Mediterranean dried is the correct executable swap per the locked direction.
- Filling weights, classic cubano per 8" sandwich: 2 slices Swiss ~40 g (split ~20 g bottom / ~20 g top), 3 slices ham ~85 g, 2 pickle planks ~20 g, 1 tbsp yellow mustard ~15 g (The Recipe Critic; Muy Bueno; Dinner at the Zoo). Pork ~110 g to balance.
- Version note: card is currently v1.6 stamped in 5 footers + kicker. A human/build step should bump to v1.7 after applying these edits; not listed as a surgical edit because the orchestrator/normal commit flow handles the stamp, but flag it.

**Decide first:**
- Version bump: should the footer/kicker stamp go v1.6 -> v1.7 with this change? (5 footer occurrences + the page-1 kicker.) Assumed yes per house convention but not included as a surgical edit since it's mechanical and may be handled at commit.
- Direct-salt dose is set to 22 g (~0.8%) on the assumption that a meaningful fraction of the 56 g Maggi's sodium migrates into the meat over 48 hr. If the cook prefers to treat Maggi sodium as staying mostly in the pan/reduction, bump direct salt to ~24-25 g (~0.9%). Either is executable; 22 g chosen as the safer no-double-salt floor with 'taste the reduction' as the lever.

**Sources:** https://www.recipal.com/ingredients/474957-nutrition-facts-calories-protein-carbs-fat-maggi-seasoning-sauce · https://www.dillons.com/p/maggi-seasoning-sauce/0002800083257 · https://asassyspoon.com/mojo-marinade/ · https://www.tiktok.com/@alexrioscooks/video/7584188607804525855 · https://www.slofoodgroup.com/blogs/recipes-stories/mexican-oregano-vs-mediterranean-oregano-what-s-the-difference · https://www.americastestkitchen.com/articles/162-how-to-salt-a-roast · https://www.verymeaty.com/fresh-meat/pork/how-much-salt-per-pound-of-pork/ · https://therecipecritic.com/easy-cuban-sandwich-recipe/ · https://muybuenoblog.com/cuban-ham-cheese-sandwich-cubano/

---

## 2. pho

1. **Page-1 spec strip: kill the Brix 'Finish' cell, replace with a real, taste-based finish descriptor** `⚠ SALT — VERIFY/skip`
   - _why:_ The 8.7 Brix figure appears nowhere in the Leighton source (his PDF has no Brix/refractometer at all) and refractometer QC of a seasoned soup is theater — Brix reads total dissolved solids (sugar+salt+gelatin), not 'doneness.' Replace with the honest lever the card actually uses.
   - FROM: `<div><div class="lab">Finish</div><div class="val">8.7 Brix</div></div>`
   - TO: `<div><div class="lab">Finish</div><div class="val">Salt + fish sauce, to taste</div></div>`
2. **Page-1 spec strip: the 'Bones 1:1 + 30% water' cell stays, but the broth concentration claim should not reference Brix anywhere (no other change needed here — confirm cell text). No edit required; listed for completeness only.**
   - _why:_ This matches Leighton exactly (5 kg bones / 6.5 L water = 1:1 to final volume + ~30% evap allowance). Keep as-is.
   - FROM: `<div><div class="lab">Bones</div><div class="val">1:1 + 30% water</div></div>`
   - TO: `<div><div class="lab">Bones</div><div class="val">1:1 + 30% water</div></div>`
3. **Page 1: delete the entire 'Brix Checkpoints' section (the h2 and the diag table beneath it)**
   - _why:_ Remove the refractometer/Brix QC table entirely — fabricated numbers not in the Leighton source and not how pho is actually checked. Deleting it also frees vertical space on page 1, which the new parboil step on page 2 needs to clear footer overflow.
   - FROM: `<h2>Brix Checkpoints <span class="note">refractometer QC &middot; read a cooled drop, not boiling broth &middot; low &rarr; reduce, high &rarr; dilute</span></h2>
  <table class="diag">
    <tr><th>Checkpoint</th><th>Target</th><th>Under &rarr; reduce</th><th>Over &rarr; add water</th></tr>
    <tr><td class="sym">Base broth <span class="mut" style="font-weight:600;">&mdash; unseasoned, post-strain</span></td><td>7.0%</td><td>Simmer down to concentrate up to 7.0 (confirms a full 24-hr extraction)</td><td>Top up with water to 3 L @ 7.0</td></tr>
    <tr><td class="sym">Finished ph&#7903; <span class="mut" style="font-weight:600;">&mdash; after the fish sauce</span></td><td>8.7%</td><td>Reduce the pot a little more, then re-check</td><td>Add boiling water to the pot &rarr; back to a near-boil &rarr; serve all</td></tr>
  </table>`
   - TO: ``
4. **Page-1 'blend method' callout: strip the Brix dilution language, keep the genuine make-ahead principle**
   - _why:_ Keep Leighton's real principle (concentrate hard, dilute at the end) but drop the made-up '8.7 target' — there is no numeric target to dilute to, you dilute to taste.
   - FROM: `<b>The blend method:</b> make the bone broth in advance (a weekend project), store it in the fridge or freezer, then transform it into finished ph&#7903; any weeknight in <b>30&ndash;45 min</b> &mdash; long extraction separated from quick assembly. <b>Dilution principle:</b> extract hard, season to ratio, dilute to your 8.7 target. A concentrated base diluted down keeps full flavor and body; an under-extracted broth is missing compounds you <i>can&rsquo;t</i> add back.`
   - TO: `<b>The blend method:</b> make the bone broth in advance (a weekend project), store it in the fridge or freezer, then transform it into finished ph&#7903; any weeknight in <b>30&ndash;45 min</b> &mdash; long extraction separated from quick assembly. <b>Extract hard, then dilute to taste:</b> a concentrated base thinned with water at service keeps full flavor and body; an under-extracted broth is missing compounds you <i>can&rsquo;t</i> add back.`
5. **Page-1 seasoning-curve caption: remove the '8.7 target' reference**
   - _why:_ Same Brix-theater removal; the curve concept (under, overshoot, balance) is fine, the numeric target is not real.
   - FROM: `<b>fish sauce</b> settles it back to the 8.7 target while adding umami.</p>`
   - TO: `<b>fish sauce</b> settles it back to balance while adding umami.</p>`
6. **Page 2: insert Leighton's blanch/parboil step into 'Bone Roasting' so the broth runs clear, and correct the false 'no parboil' claim**
   - _why:_ Leighton's source explicitly parboils for clarity: Option 1 = 'PARBOIL THE BONES TO REMOVE IMPURITIES / DUMP WATER / WASH THROUGH BONES / REPLACE WITH FRESH WATER / SIMMER'; Option 2 (advanced) = 'ROAST BONES UNTIL GOLDEN / PARBOIL QUICKLY... LESS SCUM RISES.' The current card's 'no parboil' is the opposite of the recipe it claims to follow and is the likely cause of a murky broth. This adopts Leighton's Option 2 (roast then quick blanch).
   - FROM: `<li><b>Straight from frozen:</b> bones go from freezer to oven &mdash; <b>no thaw, no parboil</b>.</li>
    <li><b>Roast hot:</b> <b>425&ndash;450&deg;F for ~1 hour</b>.</li>
    <li><b>Color target:</b> <b>golden-mahogany with dark spots</b> &mdash; dark spots are fine, black is not.</li>
    <li><b>Save the fat:</b> reserve the rendered tallow for blooming the spices at assembly.</li>`
   - TO: `<li><b>Roast hot:</b> bones from frozen, <b>roast at 425&ndash;450&deg;F for ~1 hour</b> to golden-mahogany (dark spots OK, black is not). Reserve the rendered tallow for the spice bloom.</li>
    <li><b>Then blanch:</b> drop the roasted bones into a pot of boiling water for <b>~5 min</b>, <b>dump the water, rinse the bones and pot</b>, refill with fresh water. This is what gives a clear broth &mdash; the quick parboil sheds the scum and blood proteins that roasting alone leaves behind.</li>`
7. **Page 2: retitle the 24-hour simmer 'Finish to number' step to drop the 7.0 Brix target**
   - _why:_ Removes the fabricated 7.0 Brix base target; replaces with the real, checkable signal Leighton and the card already cite elsewhere (a chilled broth that gels = full gelatin extraction).
   - FROM: `<li><b>Finish to number:</b> top up to the target volume at the end, strain. <b>Target: 7.0 Brix.</b></li>`
   - TO: `<li><b>Finish to volume:</b> at the end, top up to the target volume with water, then strain. The base should be deeply savory and, when chilled, set to a firm wobble.</li>`
8. **Page-3 Ingredients h2 note: drop the '@ 7.0 Brix' from the base description**
   - _why:_ Brix removal, consistency with page 2.
   - FROM: `<h2>Ingredients <span class="note">Base: 3 L bone broth @ 7.0 Brix (from page 2)</span></h2>`
   - TO: `<h2>Ingredients <span class="note">Base: 3 L concentrated bone broth (from page 2)</span></h2>`
9. **Page-3 Spices table: cinnamon 12 g -> 15 g (match Leighton for 3 L)**
   - _why:_ Leighton's PDF spec for the same 3 L finished pho lists 15G CINNAMON. The card's 12 g is an undocumented deviation.
   - FROM: `<tr><td>Cinnamon <span class="mut">cassia</span></td><td class="amt">12 g</td></tr>`
   - TO: `<tr><td>Cinnamon <span class="mut">cassia / Saigon</span></td><td class="amt">15 g</td></tr>`
10. **Page-3 Spices table: black cardamom 14 g -> 20 g (match Leighton)**
   - _why:_ Leighton lists 20G CARDAMOM for 3 L. (Note added because un-toasted black cardamom is a documented bitterness source.)
   - FROM: `<tr><td>Black cardamom</td><td class="amt">14 g</td></tr>`
   - TO: `<tr><td>Black cardamom <span class="mut">toast well</span></td><td class="amt">20 g</td></tr>`
11. **Page-3 Spices table: star anise 20 g -> 15 g (match Leighton; resolves the 'spice load 3-5x' overshoot on the dominant spice)**
   - _why:_ Leighton lists 15G STAR ANISE for 3 L (5 g/L). The card's 20 g (6.7 g/L) is both above Leighton and far above the ~2 g/L authentic ceiling that Viet World Kitchen / spice references cite as the bitterness threshold. 15 g matches the 'best online' target the user named.
   - FROM: `<tr><td>Star anise</td><td class="amt">20 g</td></tr>`
   - TO: `<tr><td>Star anise</td><td class="amt">15 g</td></tr>`
12. **Page-3 Spices table: clove 2 g -> 3 g (match Leighton)**
   - _why:_ Leighton lists 3G CLOVE for 3 L.
   - FROM: `<tr><td>Clove</td><td class="amt">2 g</td></tr>`
   - TO: `<tr><td>Clove</td><td class="amt">3 g</td></tr>`
13. **Page-3 Aromatics: keep garlic but flag it as Leighton-specific / non-canonical, halve to match his '1/2 garlic [head]'**
   - _why:_ User flagged garlic as not traditional in beef pho (correct — canonical Hanoi/Saigon pho bo is onion + ginger only). But Leighton, the recipe being matched, DOES use garlic ('1/2 GARLIC'). Resolution: keep it, mark it optional/non-traditional, and align the amount to Leighton's half-head rather than the card's invented 4-5 cloves. See open_questions if the house wants it removed entirely.
   - FROM: `<tr><td>Garlic cloves</td><td class="amt">4&ndash;5</td></tr>`
   - TO: `<tr><td>Garlic <span class="mut">optional, not traditional</span></td><td class="amt">&frac12; head</td></tr>`
14. **Page-3 Fish sauce row: drop the 'to 8.7 Brix' label, give Leighton's amount as the anchor**
   - _why:_ Brix removal. Leighton adds fish sauce only at the final adjustment; his writeup quantifies ~20 ml for 3 L. '8-15 ml' was tied to the fake Brix target.
   - FROM: `<tr><td>Fish sauce <span class="mut">to 8.7 Brix</span></td><td class="amt">8&ndash;15 ml</td></tr>`
   - TO: `<tr><td>Fish sauce <span class="mut">at the finish, to taste</span></td><td class="amt">~20 ml</td></tr>`
15. **Page-3 Method step 5: strip the Brix target and the dilute-to-number instruction**
   - _why:_ Removes the 8.7 Brix gate; keeps the real dilute-if-too-strong move. Fish sauce aligned to ~20 ml.
   - FROM: `<li><b>Final adjustment:</b> strain out the aromatics + spices. Add <b>fish sauce (8&ndash;15 ml)</b> until you catch a slight fishiness; optional 250 ml oxtail concentrate. <b>Target 8.7 Brix</b> &mdash; if over, add boiling water to the pot and bring back to a near-boil before serving.</li>`
   - TO: `<li><b>Final adjustment:</b> strain out the aromatics + spices. Add <b>fish sauce (~20 ml)</b> until you catch a slight fishiness; optional 250 ml oxtail concentrate. If the broth is too intense, add boiling water and bring back to a near-boil before serving &mdash; taste, don&rsquo;t measure.</li>`
16. **Page-3 Method step 3: align pre-season taste cue, keep amounts (salt/sugar/hat nem unchanged this pass)** `⚠ SALT — VERIFY/skip`
   - _why:_ Drops the hardcoded duplicate amounts from prose (they live in the ingredient table) so a future seasoning change touches one place. Amounts themselves left as-is — see open_questions on the salt budget.
   - FROM: `<li><b>Add broth + pre-season:</b> pour in the <b>3 L bone broth</b> (it quenches everything), bring to a gentle simmer. Add salt (35 g), rock sugar (55 g), h&#7841;t n&ecirc;m (20 g); stir to dissolve. Taste &mdash; 95% there, slightly salty.</li>`
   - TO: `<li><b>Add broth + pre-season:</b> pour in the <b>3 L bone broth</b> (it quenches everything), bring to a gentle simmer. Add the salt, rock sugar, and h&#7841;t n&ecirc;m; stir to dissolve. Taste &mdash; 95% there, deliberately a touch salty (fish sauce lands the rest).</li>`
17. **Page-3 Troubleshooting: replace the two Brix-dependent rows with taste-based fixes**
   - _why:_ Final Brix references; swaps the fake numeric targets for the real signal (a base that gels = strong enough).
   - FROM: `<tr><td class="sym">Too intense</td><td>Over-extraction / no brisket</td><td>Dilute to 8.7 Brix at service</td></tr>
    <tr><td class="sym">Too weak</td><td>Under-extraction (under 7 Brix base)</td><td>Simmer longer or reduce</td></tr>`
   - TO: `<tr><td class="sym">Too intense</td><td>Over-extraction / no brisket</td><td>Add boiling water at service, taste back to balance</td></tr>
    <tr><td class="sym">Too weak</td><td>Under-extracted base (didn&rsquo;t gel when chilled)</td><td>Simmer longer or reduce to concentrate</td></tr>`

**Research notes:**
- AUTHORITATIVE SOURCE FOUND: Leighton Pho's own 'Professional Guide to Cooking a Pho Using the Blend Method' PDF (pho-queue.squarespace.com). Its ingredient block for the finished 3 L pho (same yield as this card) is exactly: 15G CINNAMON, 20G CARDAMOM, 15G STAR ANISE, 3G CLOVE. NO coriander, NO fennel in the spice list. So nothing to ADD for coriander/fennel — the card and Leighton agree they're absent.
- Card's current spices (for 3 L): cinnamon 12g, black cardamom 14g, star anise 20g, clove 2g. Only star anise is HIGH vs Leighton (20 vs 15); the other three are LOW. After matching Leighton: 15/20/15/3.
- Star anise: card 20g over 3 L = 6.7 g/L. Leighton = 5 g/L. Spice references (Viet World Kitchen primer; Alibaba spice list) cite ~2 g/L as the authentic norm and the threshold above which star anise turns the broth bitter. So the card was ~3.3x the authentic norm; Leighton's 'best online' number is ~2.5x — the user explicitly wants Leighton matched, so 15g is the target, not 6g.
- PARBOIL/CLARITY: Leighton's source explicitly blanches. Verbatim: 'OPTION 1: PARBOIL THE BONES TO REMOVE IMPURITIES / DUMP WATER / WASH THROUGH BONES / REPLACE WITH FRESH WATER / SIMMER.' 'OPTION 2 (ADVANCED): ROAST BONES IN OVEN UNTIL GOLDEN / PARBOIL QUICKLY. YOU WILL FIND LESS SCUM RISES.' The current card's 'no thaw, no parboil' directly contradicts the recipe it claims to follow. Edit adopts Option 2 (roast then quick blanch).
- GARLIC: Leighton DOES use garlic ('1/2 GARLIC' = half a head) roasted with onion/ginger/brisket. Canonical Hanoi/Saigon pho bo uses only charred onion + ginger (garlic is non-traditional, more a Southern/home embellishment). User asked to 'reconsider' it. Decision taken: keep it (the card is explicitly 'after Leighton'), but label it optional/non-traditional and align quantity to Leighton's half-head instead of the card's invented 4-5 cloves.
- BRIX/REFRACTOMETER: The word Brix and any refractometer reference appear NOWHERE in Leighton's source PDF. The card invented the entire 7.0/8.7 Brix apparatus and falsely attributes a 'Science Edition' lineage. All Brix references are removed (spec cell, full Brix Checkpoints table on p1, callout, curve caption, p2 simmer target, p3 ingredients note, fish-sauce label, method step 5, two troubleshooting rows).
- SALT BUDGET TENSION (flagged, NOT silently changed): Card pre-seasons 35g salt + 20g hat nem over ~3000 g = ~1.17% from salt alone before fish sauce/hat nem sodium — already above the house ~0.9-1.0% target. Leighton runs even higher (50g salt + 19g hat nem + fish sauce + MSG). The locked direction scoped spices/garlic/parboil/Brix only and did NOT ask to change salt, so amounts are left as-is this pass and the conflict is raised in open_questions rather than resolved unilaterally.
- BONE:WATER ratio on the card (1:1 + 30% water) exactly matches Leighton ('5KG BONES WITH 6.5L WATER, ALLOW 30% MORE WATER'). No change.
- FOOTER OVERFLOW NOTE for the builder: page 1 loses an entire diag table (Brix Checkpoints), so it gains space. Page 2 gains one new step (blanch). After applying, run python build.py pho and eyeball page 2 — if the new blanch step pushes the simmer list into the footer, tighten ol.steps li padding on page-2-only elements per CLAUDE.md, do not cut content.

**Decide first:**
- SALT BUDGET: The card's pre-season (salt 35g = 1.17% + hat nem 20g + fish sauce) already exceeds the house 0.9-1.0% salt target, and Leighton's own numbers (salt 50g, hat nem 19g, fish sauce + MSG) are higher still. This pass leaves the seasoning amounts unchanged (out of the locked scope). Does the house want salt pulled down to ~27-30g (~0.9-1.0%) to meet the salt-budget gate, or kept at the current higher restaurant-style level for fidelity to Leighton? One decision needed before a build that must pass the salt gate.
- GARLIC, final call: kept as optional/non-traditional half-head (matches Leighton). If the house prefers strict canonical pho bo, remove the garlic row entirely instead — confirm which.
- SUBTITLE LINEAGE: page-1 sub reads 'after Leighton Pho, 2024 Science Edition.' With the Brix/'science' apparatus stripped, that 'Science Edition' tag is now inaccurate. Want it changed to plain 'after Leighton Pho's blend method' (honesty gate), or left as the user's preferred branding? Not edited above to avoid an unrequested wording change.

**Sources:** https://static1.squarespace.com/static/597e71c6e3df287cef6e7aff/t/62139152ddd92a1a98442642/1645449567071/PROFESSIONAL+GUIDE+TO+COOKING+A+PHO+USING+THE+BLEND+METHOD+LEIGHTON+PHO+rev+1a.pdf (Leighton Pho official PDF — spice grams 15g cinnamon / 20g cardamom / 15g star anise / 3g clove for 3 L; parboil Options 1 & 2; 1/2 garlic; no Brix) · https://jasonfarmer.com/world-class-beef-pho/ (independent writeup of Leighton's method — corroborates spice grams, fish sauce ~20 ml at finish, no blanch-skip, garlic used) · https://www.ytrecipe.com/recipes/restaurant-quality-pho-leighton-pho (Leighton recipe transcription — confirms no coriander/fennel, fish sauce only at final tasting, no Brix) · https://www.vietworldkitchen.com/blog/2017/04/primer-on-pho-spices.html (Andrea Nguyen pho spice primer — star anise as defining aroma; spice amounts vary by cook) · https://spice.alibaba.com/spice-basics/pho-spices-list (authentic per-liter norms: ~2 g/L star anise, bitterness above that; black cardamom must be toasted) · https://www.tiktok.com/@mydangfamily/video/7200806366389210411 (Leighton-credited home version showing parboil-then-roast and fish sauce at final phase)

---

## 3. colorado-green-chile

1. **Sub-line: drop chicharron framing, name pork shoulder + the tomato choice**
   - _why:_ Protein base is now browned pork butt, not chicharron. Pueblo/Colorado purist style skips tomato to let the green chile flavor lead; stating it sets the honest cuisine identity (Burrata & Bubbles, State of Dinner).
   - FROM: `<div class="sub">Chicharr&oacute;n-enriched &middot; fire-roasted &middot; breakfast-burrito-ready</div>`
   - TO: `<div class="sub">Browned pork shoulder &middot; fire-roasted chiles &middot; no tomato (Pueblo-style)</div>`
2. **Spec strip: replace the Chicharron cell with Pork weight**
   - _why:_ Pork shoulder (butt) is the protein base. 900 g (~2 lb) is scaled to this ~6-cup batch; standard Colorado recipes run 3-4 lb against 10 cups stock, so ~2 lb fits this 900-1000 ml batch (Burrata & Bubbles, The Fresh Cooky).
   - FROM: `<div><div class="lab">Chicharr&oacute;n</div><div class="val">115&ndash;170 g</div></div>`
   - TO: `<div><div class="lab">Pork butt</div><div class="val">900 g cubed</div></div>`
3. **Key Targets note: brown the pork hard (replaces onion-only fond cue)**
   - _why:_ The dominant fond source is now the seared pork, not the onion. Keeps the char-and-fleck cue.
   - FROM: `<h2>Key Targets <span class="note">char it hard, leave some fleck &mdash; brown the onion for fond</span></h2>`
   - TO: `<h2>Key Targets <span class="note">char chiles hard, leave fleck &mdash; brown the pork for fond</span></h2>`
4. **Key Targets table: replace the chicharron row with a pork-browning + doneness row**
   - _why:_ Replaces chicharron target with the two pork governing targets: a hard sear (flavor) and fork-tender doneness. 90 C / 195 F is the collagen-breakdown shred point for shoulder. The 'sits on a burrito' final-texture line is retained on the existing char-retention/sauce row above it.
   - FROM: `<tr><td class="sym">Chicharr&oacute;n</td><td>Bends, doesn&rsquo;t snap or dissolve</td><td class="sym">Final</td><td>Sits on a burrito without running</td></tr>`
   - TO: `<tr><td class="sym">Pork sear</td><td>Deep brown crust, sticky fond in pot</td><td class="sym">Pork done</td><td>Fork-tender, shreds at 90&deg;C / 195&deg;F</td></tr>`
5. **Aromatics: bump cumin to a real weight for the pork-forward batch**
   - _why:_ Authentic Colorado pork green chile runs ~1 Tbsp cumin (~6 g) against 3-4 lb pork; scaled to 900 g pork that is ~2 g. 0.5 g was a chicharron-era trace amount, too low once pork is the base (Burrata & Bubbles: 1 Tbsp cumin).
   - FROM: `<tr><td>Cumin</td><td class="amt">0.5 g</td></tr>`
   - TO: `<tr><td>Cumin</td><td class="amt">2 g</td></tr>`
6. **Base table: re-purpose flour line as the pork dredge (the anti-lump method)**
   - _why:_ Fixes the lumpy method: flour now coats the cubed pork and browns INTO the fond, so it disperses smoothly with no raw-flour lumps (standard Colorado technique: dredge/toss pork in flour, then sear). 30 g (~2 Tbsp) per 900 g pork is the documented ratio (Fresh Cooky / State of Dinner).
   - FROM: `<tr><td>AP flour <span class="mut">to consistency</span></td><td class="amt">16&ndash;32 g</td></tr>`
   - TO: `<tr><td>AP flour <span class="mut">dredge the pork</span></td><td class="amt">30 g</td></tr>`
7. **Pork + Finish block: replace chicharron line with cubed pork butt**
   - _why:_ Pork shoulder cubes are the protein base. 1.5" cubes (written &Prime; to match the existing 1&Prime; usage in the file) hold up over a 2-3 hr simmer and shred clean. Vinegar/lime finish retained as the acid lever.
   - FROM: `<span class="tag">Pork + Finish</span>
      <table class="ing">
        <tr><td>Chicharr&oacute;n <span class="mut">plain, thick-cut</span></td><td class="amt">115&ndash;170 g</td></tr>
        <tr><td>White vinegar or lime <span class="mut">finish</span></td><td class="amt">5&ndash;10 ml</td></tr>
      </table>`
   - TO: `<span class="tag">Pork + Finish</span>
      <table class="ing">
        <tr><td>Pork butt <span class="mut">1.5&Prime; cubes</span></td><td class="amt">900 g</td></tr>
        <tr><td>White vinegar or lime <span class="mut">finish</span></td><td class="amt">5&ndash;10 ml</td></tr>
      </table>`
8. **Mise callout: swap the chicharron-prep clause for pork dredge prep, drop the 'cooks fast' line (this is now a long braise)**
   - _why:_ Replaces chicharron-breaking with pork cubing + the dredge-just-before-sear cue (dredge early and the flour goes gummy). Removes the now-false 'cooks fast' line; this is a 2-3 hr braise.
   - FROM: `<b>Mise before the flame:</b> peppers at room temp (cold chars unevenly), stock measured and ready, onion diced + garlic minced, chicharr&oacute;n broken into rough <b>1&Prime; pieces</b>, a heavy pot (Dutch oven) hot, and a bowl + cover to steam the peppers. This one cooks fast once the onion hits the fat &mdash; have it all set.`
   - TO: `<b>Mise before the flame:</b> peppers at room temp (cold chars unevenly), stock measured and ready, onion diced + garlic minced, pork cut into <b>1.5&Prime; cubes</b> and patted dry, the <b>30 g flour</b> ready to dredge them just before searing, a heavy Dutch oven hot, and a bowl + cover to steam the peppers.`
9. **Method step 2: become BROWN THE PORK, then split aromatics into its own step**
   - _why:_ Core locked change: browned pork shoulder becomes the base. Dredge-then-sear is the proper anti-lump roux method — the flour toasts in the fat and dissolves smoothly later, no slurry, no lumps. Splitting into two steps keeps each step single-action and house-lean.
   - FROM: `<li><b>Build base:</b> heat the tallow over medium-high, add the onion and cook to <b>deep golden with fond, 8&ndash;10 min</b>. Add garlic + oregano + cumin, <b>30 sec</b> until fragrant.</li>`
   - TO: `<li><b>Brown the pork:</b> dredge the cubes in the <b>30 g flour</b>, shake off excess. Sear in the tallow over medium-high in batches to a <b>deep brown crust, ~4 min/side</b> &mdash; don&rsquo;t crowd. Remove pork; the flour-laced fond stays in the pot.</li>
    <li><b>Aromatics:</b> add the onion to the fond, cook to <b>deep golden, 8&ndash;10 min</b>. Add garlic + oregano + cumin, <b>30 sec</b> until fragrant.</li>`
10. **Method step 3 (add peppers + stock): fold the pork back in and deglaze**
   - _why:_ Pork rejoins here; deglazing dissolves the flour-fond into the liquid (the smooth-thickening mechanism). Explicitly retires the old sprinkle-flour-into-hot-liquid step that caused lumps.
   - FROM: `<li><b>Add peppers:</b> stir them in to coat, pour in the stock, bring to a simmer.</li>`
   - TO: `<li><b>Deglaze + simmer:</b> stir in the chopped peppers, return the pork and its juices, pour in the stock scraping up all fond, bring to a simmer. The dredge flour thickens as it heats &mdash; <b>no lumps, no slurry</b>.</li>`
11. **Method: delete the old lumpy 'Thicken: sprinkle flour' step entirely**
   - _why:_ This is the lumpy method being removed. Thickening is now handled by the dredge flour that browned on the pork and dissolved at deglaze. Removing a step also reclaims page-2 vertical space for the longer braise text.
   - FROM: `<li><b>Thicken:</b> sprinkle flour <b>~8 g at a time</b>, stirring constantly, until it coats a spoon and holds when drizzled (usually <b>16&ndash;32 g</b>).</li>`
   - TO: ``
12. **Method: replace the chicharron simmer step with the pork braise**
   - _why:_ Pork shoulder needs 2-3 hr to break down collagen (all sources). Replaces the 30-45 min chicharron melt step. 90 C / 195 F is the shred-tender internal target.
   - FROM: `<li><b>Chicharr&oacute;n:</b> add the rough 1&Prime; pieces, simmer <b>30&ndash;45 min</b>. Most melts in for richness; the bigger pieces stay. Done when they <b>bend, not snap</b>.</li>`
   - TO: `<li><b>Braise:</b> partly cover and simmer low <b>2&ndash;3 hr</b>, stirring now and then, until the pork is <b>fork-tender and shreds (90&deg;C / 195&deg;F)</b>. Add stock if it tightens past a spoon-coating sauce.</li>`
13. **Method step 6 Finish: tie the salt to a budget instead of 'aggressively'** `⚠ SALT — VERIFY/skip`
   - _why:_ 'Salt aggressively' is vague and risks over-salting; the spec already lists 14 g salt. Tying finish-salt to the 14 g / ~0.9% budget meets the salt-budget gate and removes guesswork. Vinegar/lime stays as the named acid lever.
   - FROM: `<li><b>Finish:</b> <b>salt aggressively</b> &mdash; it needs more than you think. Optional <b>5&ndash;10 ml vinegar or lime</b> at the end for brightness. Final texture: thick enough to <b>sit on a burrito without running</b>.</li>`
   - TO: `<li><b>Finish:</b> salt to taste toward the <b>14 g target</b> (~0.9% of the batch), then <b>5&ndash;10 ml vinegar or lime</b> for brightness. Final texture: thick enough to <b>sit on a burrito without running</b>.</li>`
14. **Troubleshooting: replace the 'thin / runny' slurry fix to match the new method**
   - _why:_ With dredge-thickening there is no slurry step; the honest fix is reduce, or add a touch more dredged-and-browned flour via meat. Removes a contradiction with the new method.
   - FROM: `<tr><td class="sym">Thin / runny</td><td>Under-thickened</td><td>Flour slurry: 8 g flour + 30 ml water</td></tr>`
   - TO: `<tr><td class="sym">Thin / runny</td><td>Too much stock</td><td>Simmer uncovered to reduce; or dredge 1-2 extra cubes</td></tr>`
15. **Troubleshooting: replace 'No pork depth / chicharron too thin' row**
   - _why:_ Depth now comes from the sear/fond, not chicharron thickness. The fix names the real lever: a hard, uncrowded sear.
   - FROM: `<tr><td class="sym">No pork depth</td><td>Chicharr&oacute;n too thin</td><td>Thicker cut; add extra lard</td></tr>`
   - TO: `<tr><td class="sym">No pork depth</td><td>Pork under-seared</td><td>Brown harder next batch; don&rsquo;t crowd the pot</td></tr>`
16. **Troubleshooting: replace 'Chicharron mushy' row with a pork-tough/under-braise row**
   - _why:_ The relevant pork failure is under-braise (chewy), not over-simmer. Names the doneness target again.
   - FROM: `<tr><td class="sym">Chicharr&oacute;n mushy</td><td>Simmered too long</td><td>Add half early, half in the last 10 min</td></tr>`
   - TO: `<tr><td class="sym">Pork tough</td><td>Under-braised</td><td>Keep at a low simmer to 90&deg;C / 195&deg;F &mdash; collagen needs time</td></tr>`
17. **Bottom callout: cut the chicharron-explained-again bloat; replace with the tomato choice + pork tips**
   - _why:_ Locked direction: cut the 4x-repeated chicharron explanation and explicitly flag the tomato decision (the recipe's biggest authenticity choice). Storage simplifies since pork reheats and freezes cleanly and improves next-day. The pork-neck-stock upgrade is dropped as redundant now that pork is the base.
   - FROM: `<b>The chicharr&oacute;n is seasoning, not bulk</b> &mdash; most dissolves into the sauce for richness; the few intact pieces you find are a bonus, so don&rsquo;t over-add. <b>Poblano sub:</b> no chilaca? Use poblano, char harder, and add 1&ndash;2 extra serranos. <b>Pork-forward upgrade:</b> roast 1 kg pork neck (220&deg;C / 425&deg;F, 45 min), simmer in 2 L water 3&ndash;4 hr, and use that as the stock. <b>Storage:</b> best same or next day; the chicharr&oacute;n version keeps ~48 hr &mdash; for longer, freeze the base <i>without</i> chicharr&oacute;n (3 months) and stir it in fresh on reheat.`
   - TO: `<b>Tomato &mdash; your call:</b> Pueblo/Colorado purists skip it to let the green chile lead (this build). For a redder, milder pot, stir in <b>200 g chopped tomato or 2 tomatillos</b> with the peppers &mdash; common in home and restaurant versions, but it mutes the chile. <b>Poblano sub:</b> no chilaca? Use poblano, char harder, add 1&ndash;2 extra serranos. <b>Storage:</b> flavor deepens overnight; keeps 4 days fridge, freezes 3 months.`
18. **Page-1 kicker version stamp bump**
   - _why:_ Protein base swap (chicharron to browned pork) + method rewrite is a major version; bump to v2.0 in the kicker stamp.
   - FROM: `<div class="kicker">Professional Guide &nbsp;/&nbsp; v1.0</div>`
   - TO: `<div class="kicker">Professional Guide &nbsp;/&nbsp; v2.0</div>`
19. **Page-1 footer version stamp bump**
   - _why:_ Every page footer must carry the current version stamp (gate 8); bump to v2.0.
   - FROM: `<div class="foot"><span>Aguillon House Kitchen</span><span>Colorado Green Chile v1.0 &middot; targets + ingredients</span><span>Page 1 / 2</span></div>`
   - TO: `<div class="foot"><span>Aguillon House Kitchen</span><span>Colorado Green Chile v2.0 &middot; targets + ingredients</span><span>Page 1 / 2</span></div>`
20. **Page-2 footer version stamp bump**
   - _why:_ Match the v2.0 bump on the page-2 footer (gate 8).
   - FROM: `<div class="foot"><span>Aguillon House Kitchen</span><span>Colorado Green Chile v1.0 &middot; method + troubleshoot</span><span>Page 2 / 2</span></div>`
   - TO: `<div class="foot"><span>Aguillon House Kitchen</span><span>Colorado Green Chile v2.0 &middot; method + troubleshoot</span><span>Page 2 / 2</span></div>`

**Research notes:**
- Authentic Colorado/Pueblo green chile uses cubed pork shoulder/butt (commonly 3-4 lb against ~10 cups stock), browned hard on all sides as the flavor base; this batch is ~6 cups, so pork scales to ~900 g (2 lb).
- The proper non-lumpy thickening is to DREDGE/TOSS the pork cubes in flour (~2 Tbsp / 30 g per ~2 lb) and sear them — the flour toasts into the fond and dissolves smoothly at deglaze. Sprinkling raw flour into hot liquid (the old step 4) is what caused lumps; removed.
- Tomato is a genuine regional debate: Pueblo/Colorado purists skip tomatoes/tomatillos to let the green chile lead; many home and restaurant versions add tomato/tomatillo for a redder, milder pot. Flagged as a choice (purist = no tomato in this build).
- Cumin in authentic recipes ~1 Tbsp (~6 g) per 3-4 lb pork; scaled to 900 g pork = ~2 g (was 0.5 g chicharron-era trace).
- Pork shoulder braises 2-3 hr to fork-tender/shreddable; collagen-breakdown shred point ~90 C / 195 F internal — used as the doneness governing target (doneness gate).
- Oregano is absent from the surveyed Colorado recipes but the existing 1 g Mexican oregano is kept (harmless, common in Mexican builds) — not a blocker.
- Salt: surveyed recipes only say 'liberally salt'; kept the recipe's existing 14 g (~0.9% of batch) and tied the finish step to that budget instead of 'aggressively' to satisfy the salt-budget gate.
- Step renumbering: removing the old 'Thicken' step and splitting brown/aromatics nets the same step count; the method reads 1 Char, 2 Brown pork, 3 Aromatics, 4 Deglaze+simmer, 5 Braise, 6 Finish. Verify it stays on page 2 after build; if it overflows, tighten page-2 step padding per LESSONS_LEARNED.

**Sources:** https://burrataandbubbles.com/colorado-style-pork-green-chile/ · https://stateofdinner.com/pork-green-chili/ · https://www.thefreshcooky.com/colorado-green-chile/ · https://muybuenoblog.com/pork-green-chile-multicooker-giveaway/ · https://www.palmerland.org/blog/recipe-pueblo-green-chili

---

## 4. naan

1. **Subhead — strip false 'restaurant-style' framing, reframe honestly as the soft/pliable quick style**
   - _why:_ 'Restaurant-style' is a false-authenticity claim — restaurant naan is yeast-raised and tandoor-baked. This is the no-yeast quick style; name it honestly (honesty + cuisine-identity gates). 'Yogurt-leavened' is also inaccurate (yogurt tenderizes/acidulates; baking powder is the leavener), so the line now names both correctly.
   - FROM: `<div class="sub">Yogurt-leavened &middot; thin &amp; pliable &middot; no yeast &middot; restaurant-style</div>`
   - TO: `<div class="sub">Yogurt + baking powder &middot; thin &amp; pliable &middot; no yeast &middot; quick weeknight style</div>`
2. **Ingredients h2 note — resolve cook-method contradiction (dry pan only vs covered + broiler) to match the page-2 method**
   - _why:_ Page 1 promised a plain 'dry pan' cook while page 2's method is covered-pan-then-broiler. Front-page note now states the same two-stage method so the card doesn't contradict itself (numbers-reconcile / honesty).
   - FROM: `<h2>Ingredients <span class="note">stretch to 2&ndash;3 mm &middot; cook on a dry pan at 450&ndash;500&deg;F</span></h2>`
   - TO: `<h2>Ingredients <span class="note">stretch to 2&ndash;3 mm &middot; covered dry pan 450&ndash;500&deg;F, then broiler char</span></h2>`
3. **Fix the 'why no yeast' callout — the 'yeast makes it bready' claim is backwards; reframe as an honest trade-off**
   - _why:_ The original claim is factually backwards: yeast gives a softer, fluffier, more complex crumb (FoodCrumbles / HomeDiningKitchen); baking powder is the faster shortcut, not a texture upgrade. Honest framing keeps the no-yeast style the user wants while telling the truth about the trade-off (honesty gate).
   - FROM: `<b>Why no yeast:</b> yeast makes thick, bready naan. <b>Yogurt + baking powder</b> gives the thin, pliable texture with just enough lift for bubbles.`
   - TO: `<b>Why no yeast:</b> yeast naan is softer and more complex but needs a proof. <b>Yogurt + baking powder</b> is the quick route &mdash; acid tang plus enough lift for bubbles, thin and pliable off a hot pan.`
4. **Fix divide-math error — dough total is 382 g, so 6-8 pieces are 48-64 g, not 35-40 g**
   - _why:_ Dough total = 220+106+30+15+6+3+2 = 382 g. 382/8 = 48 g, 382/6 = 64 g. The stated 35-40 g would only yield ~9-11 balls and contradicts 'Yield: 6-8 naan' (numbers-reconcile gate). New range matches the count and the front-page yield.
   - FROM: `divide into <b>6&ndash;8 balls (35&ndash;40 g)</b>.`
   - TO: `divide into <b>6&ndash;8 balls (~48&ndash;64 g each)</b>.`
5. **Salt — raise from 3 g to 4 g to hit the house salt budget** `⚠ SALT — VERIFY/skip`
   - _why:_ 3 g / 382 g dough = 0.79%, below the ~0.9-1.0% house target. 4 g = 1.05% of dough weight, landing in budget for a flatbread eaten with finishing butter (salt-budget gate). Diamond Crystal kosher per house standard.
   - FROM: `<tr><td>Salt</td><td class="amt">3 g</td></tr>`
   - TO: `<tr><td>Salt</td><td class="amt">4 g</td></tr>`
6. **Bump version stamp on page 1 footer and kicker to v1.1**
   - _why:_ Content changed; version stamp must advance (version-stamp gate). Update every footer/stamp occurrence below too.
   - FROM: `<div class="kicker">Professional Guide &nbsp;/&nbsp; v1.0</div>`
   - TO: `<div class="kicker">Professional Guide &nbsp;/&nbsp; v1.1</div>`
7. **Page 1 footer version stamp to v1.1**
   - _why:_ Consistent version stamp across both page footers (version-stamp gate).
   - FROM: `<span>Naan v1.0 &middot; dough + finish</span>`
   - TO: `<span>Naan v1.1 &middot; dough + finish</span>`
8. **Page 2 footer version stamp to v1.1**
   - _why:_ Consistent version stamp across both page footers (version-stamp gate).
   - FROM: `<span>Naan v1.0 &middot; method + troubleshoot</span>`
   - TO: `<span>Naan v1.1 &middot; method + troubleshoot</span>`

**Research notes:**
- Dough total weight = 220 g flour + 106 g yogurt + 30 g water + 15 g oil + 6 g sugar + 3 g salt + 2 g baking powder = 382 g. At 382 g, 6 balls = ~64 g and 8 balls = ~48 g; the recipe's stated 35-40 g/ball was the divide-math error (would imply ~9-11 balls, contradicting the 6-8 yield).
- Salt audit: 3 g / 382 g = 0.79% (below house 0.9-1.0%). Raised to 4 g = 1.05%. Only sodium source in the dough; finishing butter adds flavor salt separately if salted butter is used.
- Research confirms the 'yeast makes it bready' claim is backwards: yeast-leavened naan is softer/fluffier with more complex fermentation flavor; baking powder is the time-saving shortcut that trades flavor complexity for speed (FoodCrumbles, HomeDiningKitchen). Kept the no-yeast style per locked direction but corrected the framing.
- Authentic naan is tandoor-baked (up to ~480C / wall-pressed) and yeast-raised; 'restaurant-style' on a no-yeast pan recipe is a false-authenticity claim, so it was removed.
- Comparable no-yeast yogurt naan recipes run ~95-116 g balls (300 g flour + 280 g yogurt / 5-6 pieces), so this card's smaller ~48-64 g balls are on the thin/small side but internally consistent with its 382 g dough and 6-8 yield — no quantity change needed, only the printed gram range corrected.

**Sources:** https://foodcrumbles.com/naan-a-recipe-and-guide/ · https://homediningkitchen.com/is-yeast-or-baking-powder-better-for-naan/ · https://spicecravings.com/naan-recipe-no-yeast · https://casuallypeckish.com/no-yeast-naan-bread-with-yoghurt/ · https://en.wikipedia.org/wiki/Naan

---

## 5. nyc-bagels-bulk

1. **Fix the core mislabel: stop presenting 60% as a generic 'tenderness floor'. State it is tuned for high-gluten Sir Lancelot (14.2%). This is the diagnostics row at line 197.**
   - _why:_ Removes the false generic-rule framing. 60% is not a universal floor; it is the empirically-correct hydration for THIS flour (55% gave inedible tough bagels). Grounded in the rule that 14%+ flours absorb more water and need higher hydration to avoid dry/dense crumb (King Arthur / Tasting Table).
   - FROM: `<tr><td class="sym">Tough crumb, worse when toasted</td><td>Moisture-starved &mdash; <b>60% is the tenderness floor</b>.</td></tr>`
   - TO: `<tr><td class="sym">Tough crumb, worse when toasted</td><td>Moisture-starved. <b>60% is tuned to Sir Lancelot's 14.2% protein</b> &mdash; high-gluten flour drinks more water, so 55% baked tough/dense here. Don't drop below 60% with this flour.</td></tr>`
2. **Make the water row in the spec self-document WHY 60% (tuned to the flour), not just 'cold if warm kitchen'. Line 97.**
   - _why:_ Puts the tuning rationale at the point of use so the hydration number reads as deliberate-for-this-flour, not arbitrary. Reinforces the locked direction (keep 60%, fix framing).
   - FROM: `<tr><td>Water <span class="mut">(60% &mdash; cold if warm kitchen)</span></td><td class="amt">1,320 g</td></tr>`
   - TO: `<tr><td>Water <span class="mut">(60% &mdash; tuned to 14.2% flour; cold if warm kitchen)</span></td><td class="amt">1,320 g</td></tr>`
3. **Reconcile the boil-time self-flag. Line 180 currently sells a short 30s boil as 'more tender' while the diagnostics treat tenderness as the failure mode and 60% as the tenderness floor — self-contradicting. Reframe as an honest house choice for a thinner crust.**
   - _why:_ Resolves the contradiction by separating two things the card was conflating: boil time governs CRUST/skin thickness; hydration governs CRUMB tenderness. Research: 30s/side = softer, more bread-like crust; 60-90s = classic super-chewy NY crust (The Dough Academy / Taste of Artisan). Stated honestly as a house preference for a thinner crust, not the canonical NY thick chew.
   - FROM: `<li><b>Boil 30 sec / side.</b> Shorter boil = thinner, more tender crust. Seed wet, straight out of the water (everything blend).</li>`
   - TO: `<li><b>Boil 30 sec / side</b> &mdash; the house call: a thinner, lighter crust, not the thick chew a 60&ndash;90s boil builds. Crumb tenderness is set by hydration; this only governs the <b>skin</b>. Seed wet, straight out of the water (everything blend).</li>`
4. **Add a one-clause honesty note so the title 'NYC-Style' and the short-boil method agree: this is the house bagel (thinner crust), not a claim to the canonical thick-chew NY bagel. Sub line 81.**
   - _why:_ Keeps the honest 'house bagel' framing the locked direction asks for: '-Style' plus this clause stops the card overclaiming the canonical NY crust, and aligns the identity line with the deliberately short 30s boil.
   - FROM: `<div class="sub">Straight dough &middot; short ~3h bulk &rarr; shape &rarr; <b>emphasized pan proof</b> &rarr; cold hold &middot; boiled &amp; baked</div>`
   - TO: `<div class="sub">Straight dough &middot; short ~3h bulk &rarr; shape &rarr; <b>emphasized pan proof</b> &rarr; cold hold &middot; boiled &amp; baked &middot; <span class="mut">house bake: thinner-crust, not the classic thick chew</span></div>`

**Research notes:**
- High-gluten flour (14%+ protein, e.g. Sir Lancelot 14.2%) absorbs more water than bread/AP flour; sources recommend increasing liquid 5-10% to avoid dry, dense bagels. This grounds '60% is tuned to this flour' rather than a generic floor (King Arthur; Tasting Table).
- Boil time governs crust/skin, not crumb: 30s/side = softer, more bread-like, thinner crust; 60-90s/side = classic super-chewy thick NY crust (The Dough Academy; Taste of Artisan). The recipe's 30s boil therefore genuinely yields a thinner/lighter crust — an honest house choice, not a flaw.
- The two contradictions in the card both stem from conflating crust and crumb: line 180 praised a short boil as 'more tender' while line 197 framed tenderness as failure and 60% as the 'floor'. Splitting the levers (hydration -> crumb tenderness; boil -> crust thickness) resolves both without changing 60% or the 30s boil.
- Hydration was NOT changed (locked: 60% is empirically correct for the user's flour; 55% gave inedible tough bagels). Only framing edits.
- All edits use HTML entities (&mdash; &ndash; &amp;) and must be applied with Edit/Write, never sed (CLAUDE.md rule). After editing run `python build.py nyc-bagels-bulk` until [PASS]; page 2 is near-full so eyeball the rasterized page 2 for footer overflow.

**Sources:** https://www.kingarthurbaking.com/blog/2021/06/29/the-5-elements-of-great-bagels · https://www.tastingtable.com/1596286/flour-types-bagels-texture/ · https://thedoughacademy.com/how-long-to-boil-bagels/ · https://tasteofartisan.com/bagel-recipe/

---

## 6. endgame-hummus

1. **Spec strip: Tahini Ratio value**
   - _why:_ Raise tahini to tahini-forward. Zahav's principle is 'an obscene amount of tehina, as much as half the recipe by weight'; his cooked ratio is ~160 g tahini to ~400-420 g cooked chickpeas (~40%). 190 g = 40% of 480 g peas, up from the too-low 23%. The spec strip must mirror the new ingredient number.
   - FROM: `<div class="lab">Tahini Ratio</div><div class="val">110 g / 480 g peas</div>`
   - TO: `<div class="lab">Tahini Ratio</div><div class="val">190 g / 480 g peas</div>`
2. **Ingredients table: Tahini amount**
   - _why:_ Core edit: 110 g (23% of peas) -> 190 g (40% of peas) per the Zahav/Solomonov tahini-forward ratio (~160 g tahini to ~400-420 g cooked chickpeas). Tag the % inline so the ratio is legible at the bench.
   - FROM: `<tr><td>Tahini</td><td class="amt">110 g</td></tr>`
   - TO: `<tr><td>Tahini <span class="mut">~40% of pea weight</span></td><td class="amt">190 g</td></tr>`
3. **Ingredients table: Lemon juice amount (acid for body)**
   - _why:_ More tahini needs more acid to carry it through the seize-and-loosen that builds body. Holds the recipe's 0.29:1 lemon:tahini proportion (55/190) scaled from the old 35/110, with headroom for the 'season slightly over' step. Zahav runs leaner-tasting but tarter (~0.5:1); 55 g gives enough acid for body without sour. The lemon now also doubles as the garlic-steep medium.
   - FROM: `<tr><td>Lemon juice <span class="mut">~1 lemon</span></td><td class="amt">35 g</td></tr>`
   - TO: `<tr><td>Lemon juice <span class="mut">~1&frac12; lemons &mdash; garlic steeps here</span></td><td class="amt">55 g</td></tr>`
4. **Ingredients table: add fresh garlic mellowed in lemon**
   - _why:_ Locked direction: add fresh garlic mellowed in the lemon juice (the Zahav move — raw garlic stands in lemon ~10 min so the acid tames the raw harshness before it hits the base). Counts as a real garlic source distinct from the finishing garlic oil.
   - FROM: `<tr><td>Garlic oil</td><td class="amt">54 g</td></tr>`
   - TO: `<tr><td>Fresh garlic <span class="mut">grated, steeped in the lemon</span></td><td class="amt">2 cloves</td></tr>
    <tr><td>Garlic oil</td><td class="amt">54 g</td></tr>`
5. **Ingredients table: Fine sea salt (salt budget for the larger batch)** `⚠ SALT — VERIFY/skip`
   - _why:_ Batch mass rises with the extra tahini + lemon (~480+190+55+54+78 = ~857 g). 6 g is now ~0.7% and under-salts; 8 g lands ~0.93%, inside the 0.9-1.0% house budget.
   - FROM: `<tr><td>Fine sea salt</td><td class="amt">6 g</td></tr>`
   - TO: `<tr><td>Fine sea salt</td><td class="amt">8 g</td></tr>`
6. **Method step 2: steep garlic in lemon, then stream in** `⚠ SALT — VERIFY/skip`
   - _why:_ Implements the mellowed-garlic technique in the method (steep 10 min in lemon + a little salt, strain), placed before the lemon goes into the whipped tahini so the order stays correct.
   - FROM: `<li><b>Add lemon:</b> processor running, stream in the lemon juice, process <b>30 sec</b> to emulsify.</li>`
   - TO: `<li><b>Mellow garlic:</b> grate the garlic into the lemon juice with a pinch of the salt; let it stand <b>10 min</b>, then strain out the solids &mdash; the acid tames the raw bite.</li>
    <li><b>Add lemon:</b> processor running, stream in the strained lemon, process <b>30 sec</b> to emulsify.</li>`
7. **Callout: drop the false split-rescue claim, state the true mechanism**
   - _why:_ Honesty gate. Tahini-chickpea hummus doesn't 'split' like an oil emulsion that the ice would rescue; the ice/cold water loosens the seized tahini and whips it lighter. Reworded to the real mechanism, drops the false claim.
   - FROM: `<b>The ice finish</b> is the secret &mdash; it keeps the mass cold through 4&ndash;5 min of processing that would otherwise heat and split it, building a mousse-light texture you can&rsquo;t get any other way. Season a touch heavy; the chill rounds it off.`
   - TO: `<b>The ice finish</b> is the secret &mdash; the cold water thins the tahini and lets 4&ndash;5 min of processing whip air into it, building a mousse-light, pale texture you can&rsquo;t get any other way. Season a touch heavy; the chill rounds it off.`
8. **Footer version stamp -> v1.1**
   - _why:_ Version gate requires a vN.N stamp; bump v1.0 -> v1.1 for the tahini-forward rework and label it.
   - FROM: `<span>Endgame Hummus v1.0 &middot; whipped &middot; ice-finished</span>`
   - TO: `<span>Endgame Hummus v1.1 &middot; tahini-forward &middot; ice-finished</span>`
9. **Kicker version stamp -> v1.1**
   - _why:_ Keep the kicker version in sync with the footer bump.
   - FROM: `<div class="kicker">Professional Guide &nbsp;/&nbsp; v1.0</div>`
   - TO: `<div class="kicker">Professional Guide &nbsp;/&nbsp; v1.1</div>`

**Research notes:**
- Solomonov/Zahav principle: 'the secret to great Israeli-style hummus is an obscene amount of tehina, as much as half of the recipe by weight.' (food52, hostthetoast)
- Zahav full recipe: 1 cup (190 g) DRIED chickpeas, 4 garlic cloves unpeeled, 1/3 cup (~79 ml) fresh lemon, 2/3 cup tahini, ~1.5 tsp kosher salt, cumin. Dried chickpeas ~double cooked -> ~400-420 g cooked.
- 2/3 cup tahini = ~158-160 g (1 cup tahini = 240 g; gramsinacup.com). So Zahav tahini:cooked-chickpea ~= 160/410 = ~39%. Chose 190 g = 40% of this recipe's 480 g peas — the tahini-forward end of 'co-equal-ish' without overshooting Solomonov's own ratio.
- Garlic-mellow technique (verbatim from sources): break unpeeled garlic into blender with lemon juice + 0.5 tsp salt, stand 10 min to mellow, strain pressing solids. Adapted to grated fresh garlic steeped in the lemon then strained.
- Acid-for-body: chose 55 g lemon for 190 g tahini (0.29:1), holding the recipe's existing 35:110 proportion scaled up, with headroom for 'season slightly over.' Enough acid to take tahini through seize-then-loosen (body) without sour. Zahav itself is tarter at ~0.5:1.
- Salt budget: new batch ~857 g (480 peas + 190 tahini + 55 lemon + 54 garlic oil + 78 ice). 8 g salt = ~0.93%, inside 0.9-1.0% house target; old 6 g was ~0.7% against the larger batch.
- Honesty fix: ice/cold-water finish loosens seized tahini and whips air in (mousse/lighten), it does NOT rescue a broken emulsion 'split' — hummus is not an oil-in-water sauce that splits that way. Reworded.

**Sources:** https://food52.com/recipes/42695-zahav-s-hummus-tehina · https://hostthetoast.com/michael-solomonovs-perfect-hummus-tehina/ · https://www.deliciousisrael.com/blog/2019/9/22/zahavs-hummus-tehina · https://www.foodnetwork.com/fnk/recipes/hummus-7151796 · https://www.myjewishlearning.com/the-nosher/michael-solomonovs-hummus-recipe/ · https://www.gramsinacup.com/tahini/

---

## 7. chicken-curry

1. **Total salt grams (page 1 ingredient table, right column)** `⚠ SALT — VERIFY/skip`
   - _why:_ Card seasoned mass = chicken 1500 + onion 1500 + yogurt 225 + ghee 150 + g-g paste 60 + finish garlic 30 = ~3465 g. 18 g = 0.52%, well under the house 0.9-1.0% budget. 32 g = 0.92% of 3465 g, landing inside the band. Water (~350 ml) reduces out so it is excluded from the denominator.
   - FROM: `<tr><td>Salt <span class="mut">~12g at sear, rest to taste</span></td><td class="amt">18 g</td></tr>`
   - TO: `<tr><td>Salt <span class="mut">~22g with chicken, ~10g to finish</span></td><td class="amt">32 g</td></tr>`
2. **Salt amount at the chicken stage (page 2, step 7)** `⚠ SALT — VERIFY/skip`
   - _why:_ Two fixes in one: (1) raise the at-stage salt from ~12g to ~22g so the bulk of the new 32g total is in early and penetrates the meat; (2) kill the false 'building fond' / 'sear' mechanism — chicken is going into a wet, oil-separated yogurt masala, so there is no Maillard fond to build. Reframed as 'add/turn/coat,' which is what actually happens.
   - FROM: `<li><b>Sear:</b> high heat. Add chicken, season with <b>~12g salt</b> (hold the rest). Sear <b>4&ndash;5 min</b> until opaque &mdash; building fond.</li>`
   - TO: `<li><b>Add chicken:</b> medium-high. Add chicken, season with <b>~22g salt</b> (hold ~10g). Turn <b>4&ndash;5 min</b> until the outside is opaque and coated in masala.</li>`
3. **Fond reference in the simmer step (page 2, step 8)**
   - _why:_ Removes the second half of the false-fond mechanism. There is no fond to 'scrape up' in a wet gravy; the water is just loosening the clinging masala. Keeps the step honest and consistent with the step-7 fix.
   - FROM: `<li><b>Simmer:</b> add <b>~300 ml hot water</b>, scrape up the fond, cover and simmer until the chicken is cooked through &mdash; <b>~15&ndash;20 min</b> for thigh chunks. Stir once or twice.</li>`
   - TO: `<li><b>Simmer:</b> add <b>~300 ml hot water</b>, stir to loosen the masala, cover and simmer until the chicken is cooked through &mdash; <b>~15&ndash;20 min</b> for thigh chunks. Stir once or twice.</li>`
4. **Held-salt amount in the reduce/taste step (page 2, step 9)** `⚠ SALT — VERIFY/skip`
   - _why:_ Reconcile the held-salt number with the new split: 32g total minus ~22g in early = ~10g held for final correction after the sauce concentrates. Old text said ~6g, which matched the old 18g total and now would not add up.
   - FROM: `Now taste and bring to <b>final salt</b> (the held ~6g, to taste) &mdash; after reduction, not before.`
   - TO: `Now taste and bring to <b>final salt</b> (the held ~10g, to taste) &mdash; after reduction, not before.`
5. **Lemon juice amount (page 1 ingredient table, right column)**
   - _why:_ Acid lever against 1.5 kg caramelized-onion sweetness (a 1:1 onion-to-protein load — the dominant sweet note). Doubling lemon to 30g sits in the cited ~1 Tbsp acid per cup yogurt range and brightens against the jammy onion + tangy yogurt base without adding tomato (this recipe's identity is 'no tomato' — do not break it). Yogurt stays 225g (structural/tempered, not the acid knob here).
   - FROM: `<tr><td>Lemon juice</td><td class="amt">15 g</td></tr>`
   - TO: `<tr><td>Lemon juice</td><td class="amt">30 g</td></tr>`
6. **Lemon amount in the finish step (page 2, step 11)**
   - _why:_ Mirror the page-1 lemon bump (15g -> 30g) so the method matches the ingredient table — numbers must reconcile across pages.
   - FROM: `Add the <b>second 3.5g garam masala (finish half)</b>, kasuri methi, 15g lemon. The garlic should hit your nose immediately.`
   - TO: `Add the <b>second 3.5g garam masala (finish half)</b>, kasuri methi, 30g lemon. The garlic should hit your nose immediately.`
7. **Version stamp on page 1 (kicker)** `⚠ SALT — VERIFY/skip`
   - _why:_ Bump version for the salt/acid/mechanism revision so every footer + kicker carries the new stamp (gate 8 requires a version stamp; house convention bumps it per change).
   - FROM: `<div class="kicker">Professional Guide &nbsp;/&nbsp; v3.0</div>`
   - TO: `<div class="kicker">Professional Guide &nbsp;/&nbsp; v3.1</div>`
8. **Version stamp in page 1 footer**
   - _why:_ Keep the footer version in sync with the kicker bump to v3.1.
   - FROM: `<span>Chicken Curry v3.0 &middot; targets + ingredients</span>`
   - TO: `<span>Chicken Curry v3.1 &middot; targets + ingredients</span>`
9. **Version stamp in page 2 footer**
   - _why:_ Keep the page-2 footer version in sync with the v3.1 bump.
   - FROM: `<span>Chicken Curry v3.0 &middot; method + troubleshoot</span>`
   - TO: `<span>Chicken Curry v3.1 &middot; method + troubleshoot</span>`

**Research notes:**
- Salt math (the load-bearing computation): card seasoned mass = chicken 1500 + onion 1500 + yogurt 225 + ghee 150 + ginger-garlic 60 + finish garlic 30 = ~3465 g. Current 18 g = 0.52%. Target 32 g = 0.92%, inside the house 0.9-1.0% band. Added simmer water (~300-350 ml) is excluded because it reduces out.
- Salt split for 32 g total: ~22 g with the chicken (step 7) + ~10 g held for final correction after reduction (step 9). Old card was ~12 g + ~6 g = 18 g; both stage numbers had to move together to reconcile.
- False-mechanism kill: steps 7 and 8 claimed 'building fond' and 'scrape up the fond.' Chicken enters a wet, oil-separated yogurt masala — no dry Maillard fond forms. Reworded to add/turn/coat (step 7) and stir-to-loosen (step 8) so the card is honest.
- Acid lever: lemon doubled 15 g -> 30 g on both page 1 (ingredients) and page 2 (step 11) to push against the 1.5 kg (1:1) caramelized-onion sweetness + yogurt tang. Cited home/pro guidance puts fresh lemon at ~1 Tbsp per cup of yogurt as the brightness knob against sweet caramelized onion; 30 g (~2 Tbsp) is a measured nudge, not a flatten.
- Cuisine identity preserved: recipe sub-line is 'no tomato.' Did NOT add tomato as an acid source despite the locked direction listing it as an option — adding it would break the card's stated identity. Used lemon (and the existing yogurt) instead.
- Layered spice left intact: whole-bloom set (cumin 6g, green/black cardamom, cinnamon, bay, cloves), ground set (Kashmiri 30g, hot chili 7g, turmeric 4g), and two-stage garam masala (3.5g + 3.5g) are all untouched — direction said do not flatten.
- Edits are all unique exact-match strings verified against the read of recipes/chicken-curry.html; safe for Edit tool. After applying, run python build.py chicken-curry and confirm overflow_check passes — only numbers changed (no length growth on page 2), so overflow risk is near zero.

**Sources:** https://myannoyingopinions.com/2022/05/26/chicken-curry-with-yogurt-and-caramelized-onions/ · https://wholefoodsoulfoodkitchen.com/curry-yogurt-sauce/ · https://sweetishhill.com/how-do-you-balance-tomatoes-in-curry/

---

## 8. meatloaf-sandwich

1. **Fry Seasoning section note — replace the 55-60 g dose (the salt bug) with a sane per-batch dose and updated batch size** `⚠ SALT — VERIFY/skip`
   - _why:_ Real blend totals 111 g at 21.6% salt; a 55-60 g dose dumps ~12.4 g salt on one 1.65 lb batch (~7.5 g salt/lb), ~6x sane. McDonald's doses ~0.83 g/lb and a clean target is ~1.0-1.2 g salt/lb. A 10-12 g dose of the recut blend lands ~1.8-2.0 g salt/batch (~1.0-1.2 g/lb).
   - FROM: `<h2>Fry Seasoning <span class="note">~115 g batch, dry-mix &mdash; use 55&ndash;60 g, save the rest</span></h2>`
   - TO: `<h2>Fry Seasoning <span class="note">~105 g jar, dry-mix &mdash; dose 10&ndash;12 g per fry batch (~9 batches/jar)</span></h2>`
2. **Fry Seasoning salt — recut from 24 g to 18 g so the blend is ~17% salt (a dustable seasoning, not a salt-forward dredge)** `⚠ SALT — VERIFY/skip`
   - _why:_ New blend = paprika 30 + garlic 20 + onion 16 + pepper 10 + mustard 1 + salt 18 + sugar 6 + cayenne 2 + oregano 2 = 105 g; salt = 18/105 = 17.1%. At a 10-12 g dose that delivers 1.7-2.0 g salt/batch (~1.0-1.2 g/lb on 1.65 lb of fries), matching the per-pound target from the research.
   - FROM: `<tr><td>Salt <span class="mut">Diamond Crystal, by wt</span></td><td class="amt">24 g</td></tr>`
   - TO: `<tr><td>Salt <span class="mut">Diamond Crystal, by wt</span></td><td class="amt">18 g</td></tr>`
3. **Meatloaf de-stack (triple-glutamate) — remove Worcestershire from the meatloaf aromatics; soy is the single umami backbone** `⚠ SALT — VERIFY/skip`
   - _why:_ Soy + Worcestershire + fish sauce are three redundant glutamate sources stacked on the same beef. Keep soy sauce as the one clean lever; tomato paste + ketchup glaze already add glutamate. Dropping fish sauce (~1.3 g sodium/Tbsp) and Worcestershire also pulls ~1.5 g salt out, holding meatloaf at ~1.1% (907 g beef + binder).
   - FROM: `<tr><td>Worcestershire</td><td class="amt">10 g</td></tr>
        <tr><td>Fish sauce</td><td class="amt">5 g</td></tr>
        <tr><td>Tomato paste</td><td class="amt">10 g</td></tr>`
   - TO: `<tr><td>Tomato paste</td><td class="amt">10 g</td></tr>`
4. **Meatloaf method step 1 — drop the removed Worcestershire + fish sauce from the wet-mix instruction**
   - _why:_ Worcestershire and fish sauce are removed from the ingredient list; the step must match or it references missing ingredients.
   - FROM: `Whisk eggs, milk, soy, Worcestershire, fish sauce.</li>`
   - TO: `Whisk eggs, milk, soy.</li>`
5. **A1 Aioli de-stack (redundant A1) — remove Worcestershire from the aioli; A1 IS a Worcestershire-style sauce so it is the umami lever there**
   - _why:_ A1 steak sauce (100 g) is already a tamarind/Worcestershire-family sauce; adding 6 g Worcestershire doubles the same tangy-umami note. A1 stays as the single umami source in the aioli per the de-stack brief.
   - FROM: `<tr><td>Lemon juice</td><td class="amt">10 g</td></tr>
        <tr><td>Worcestershire</td><td class="amt">6 g</td></tr>
        <tr><td>Black pepper</td><td class="amt">2 g</td></tr>`
   - TO: `<tr><td>Lemon juice</td><td class="amt">10 g</td></tr>
        <tr><td>Black pepper</td><td class="amt">2 g</td></tr>`

**Research notes:**
- Fry batch = 4 russets at 700-800 g total = ~1.65 lb raw. Sane salt target ~1.0-1.2 g/lb -> ~1.8-2.0 g salt per batch. Current 55-60 g dose of a 21.6%-salt blend = ~12.4 g salt (~7.5 g/lb), ~6x too much.
- McDonald's doses ~5 g salt per 6 lb of fries (~0.83 g/lb); home guidance ~1 g salt/lb for 1/4-inch fries. (thehealthy/quora sources.)
- Recut blend math: paprika 30 + garlic 20 + onion 16 + pepper 10 + mustard 1 + salt 18 + sugar 6 + cayenne 2 + oregano 2 = 105 g; salt 18/105 = 17.1%. 10-12 g dose -> 1.7-2.0 g salt/batch. One jar ~9 batches.
- Glutamate sources stacked: soy, Worcestershire, fish sauce, tomato paste in the meatloaf, plus A1 + Worcestershire in the aioli. Soy ~1 g sodium/Tbsp, fish sauce ~1.3 g sodium/Tbsp, both ~25%/15% salt by weight.
- De-stack keeps ONE lever per component: soy in the meatloaf, A1 in the aioli. Removing fish sauce (5 g) + Worcestershire (10 g) from meatloaf pulls ~1.5 g salt, holding it near 1.1% on ~1150 g mix.
- Existing meatloaf salt count: salt 10 g + soy 15 g (~2.3 g salt) + Worcestershire 10 g (~0.15 g) + fish sauce 5 g (~1.25 g) ~= 13.9 g over ~1150 g = ~1.2%; after de-stack ~12.5 g = ~1.1%.

**Sources:** https://www.thehealthy.com/food/how-much-sodium-is-in-soy-sauce/ · https://www.quora.com/What-is-the-perfect-amount-of-salt-to-put-on-a-serving-of-fries · https://www.theanthonykitchen.com/fry-seasoning/ · https://www.sbs.com.au/food/article/fish-sauce-is-the-saltiest-offender-of-all-the-asian-sauces/os5i5pvtz · https://en.wikipedia.org/wiki/Umami · https://www.thetakeout.com/2129550/best-way-add-umami-meatloaf-fish-sauce/

---

## 9. sloppy-joes

1. **Fix food-science error #1: garlic bitterness is NOT oxidation. In step 3 (Sweat), correct the parenthetical cause.**
   - _why:_ Garlic going bitter is scorching/pyrolysis of its low-moisture, high-sugar/sulfur solids, not oxidation. Sources confirm sulfur compounds break down into bitter/acrid compounds above ~375F and it burns in under 30 sec. 'Oxidation' is the stated error and must be corrected wherever it appears.
   - FROM: `Add garlic the <b>last 1&ndash;2 min only</b> (prevents bitter oxidation).`
   - TO: `Add garlic the <b>last 1&ndash;2 min only</b> (it scorches fast &mdash; low moisture, high sugar/sulfur burns to acrid above ~375&deg;F).`
2. **Fix food-science error #2: same 'oxidized' claim in the Troubleshooting 'Bitter undertone' row.**
   - _why:_ Second instance of the same error. Keeps the fix column intact (late add is the correct remedy) while naming the real mechanism: scorching, not oxidation.
   - FROM: `<tr><td class="sym">Bitter undertone</td><td>Garlic oxidized; paste burnt</td><td>Add garlic only the last 1&ndash;2 min of sweat</td></tr>`
   - TO: `<tr><td class="sym">Bitter undertone</td><td>Garlic scorched (not oxidized); paste burnt</td><td>Add garlic only the last 1&ndash;2 min of sweat</td></tr>`
3. **Add anti-crowding / no-steam sear guidance to step 2 (Sear), which invokes the sear without explaining how to actually achieve the fond.**
   - _why:_ Sear is invoked 4x but never explains the crowding/steaming failure mode. Maillard needs dry surface contact above ~280F (optimal 330-390F); piling the pan traps released moisture, lowers temp, and halts browning. Single layer + 2 batches + a sit-to-crust is the technique the rest of the card depends on.
   - FROM: `<li><b>Sear:</b> hot skillet, add beef, break into chunks, <b>brown well to build fond</b> (375&ndash;400&deg;F). Retain <b>30&ndash;45 g fat</b>, drain the excess.</li>`
   - TO: `<li><b>Sear:</b> hot skillet (375&ndash;400&deg;F surface), add beef in a <b>single layer &mdash; don&rsquo;t crowd</b> (work in 2 batches if needed). Crowding traps moisture, drops the pan below ~300&deg;F, and steams instead of browning. Let it sit untouched 3&ndash;4 min to set a crust, then break into chunks and <b>brown well to build fond</b>. Retain <b>30&ndash;45 g fat</b>, drain the excess.</li>`
4. **Add a 'Too sweet' troubleshooting row (the ketchup + brown sugar base is the sweet load).**
   - _why:_ Locked direction requires a 'too sweet' row. Ketchup (300 g) plus brown sugar (20 g) is the sweet base; the standard fixes are an acid/mustard bump to balance and reducing the added sugar. Numbers tie to the card's existing ACV (15 g total), mustard (16 g), and brown sugar (20 g) so it reconciles.
   - FROM: `<tr><td class="sym">Too sharp / tangy</td><td>Acid concentrated in the reduction</td><td>Stage it: 10 g build, 5 g off-heat finish</td></tr>`
   - TO: `<tr><td class="sym">Too sharp / tangy</td><td>Acid concentrated in the reduction</td><td>Stage it: 10 g build, 5 g off-heat finish</td></tr>
    <tr><td class="sym">Too sweet / cloying</td><td>Ketchup + brown sugar base</td><td>Add 3&ndash;5 g ACV or 5 g mustard off-heat; next batch cut sugar to 10 g</td></tr>`
5. **Add a Bun + Assembly section on page 2 between the Method and Troubleshooting (folded under method, house style). ~150 g per bun reconciles with 907 g / 6 = ~151 g yield.** `⚠ SALT — VERIFY/skip`
   - _why:_ Locked direction requires bun + assembly. Buttered toasted cut sides create a barrier that prevents sogginess; resting the filling lets it stop steaming so it soaks less. Per-bun portion (~150 g) reconciles with the 907 g / 6 yield already on the card. Placed under method, above troubleshooting, per house layout rule.
   - FROM: `<h2>Troubleshooting <span class="note">salt window: ~8 g on beef, sauce adds ~4&ndash;5 g &mdash; taste-add only at the end</span></h2>`
   - TO: `<h2>Bun &amp; Assembly <span class="note">toast = a barrier against the sauce &mdash; no soggy bun</span></h2>
  <p class="lead">Split <b>6 potato or brioche buns</b>. Butter the cut sides (~5 g each) and toast cut-side down in the skillet to <b>golden</b>, ~60&ndash;90 sec &mdash; the toasted crust + butter seals the crumb so the glaze sits on top instead of soaking through. Let the filling rest 5 min so it stops steaming, then mound <b>~150 g per bun</b>; serve open or closed, eat now.</p>

  <h2>Troubleshooting <span class="note">salt window: ~8 g on beef, sauce adds ~4&ndash;5 g &mdash; taste-add only at the end</span></h2>`
6. **Bump version stamp from v1.0 to v1.1 everywhere it appears (kicker line 77, both foot strings lines 142 & 173).**
   - _why:_ House gate requires a version stamp; a content revision (sear technique, two error fixes, new section + troubleshooting row) should bump the version. Execute as replace-all of 'v1.0' -> 'v1.1'; verify all occurrences are updated.
   - FROM: `v1.0`
   - TO: `v1.1`

**Research notes:**
- Food-science error identified: garlic going bitter is scorching/pyrolysis (low moisture, high sugar + sulfur compounds burn fast, breaking to acrid compounds above ~375F in under 30 sec) — NOT 'oxidation.' The card states 'bitter oxidation' (step 3) and 'Garlic oxidized' (troubleshooting). Both fixed; the late-add remedy is correct and retained.
- Anti-crowding sear: Maillard needs dry surface contact above ~280F (optimal 330-390F). Crowding traps released moisture between chunks, drops pan temp, and steams instead of browning; remedy is single even layer, work in batches, let it sit to set a crust. The card's existing 375-400F pan target aligns with this.
- Too sweet: the ketchup (300 g) + brown sugar (20 g) base is the sweet load; standard balance is a splash of vinegar or extra mustard, and reducing the added sugar in the next batch. Fix numbers (3-5 g ACV, 5 g mustard, cut sugar to 10 g) tie to existing card quantities.
- Bun/assembly: butter + toast the cut sides to create a barrier so the glaze doesn't soak the crumb; rest the filling so it stops steaming (soaks less). Potato/brioche buns; ~150 g per bun reconciles with 907 g / 6 yield on the spec strip.
- All edits stay in grams/ml/counts, no bare tsp/tbsp, lean. Must run `python build.py sloppy-joes` until [PASS] and eyeball page 2 — the new Bun & Assembly h2 + p.lead plus the extra troubleshooting row add vertical content to page 2 and may trip overflow_check; if so, tighten page-2-only vertical rhythm (step padding / p.lead + callout margins) per CLAUDE.md, not page 1.

**Decide first:**
- Page 2 overflow risk: adding a Bun & Assembly h2 + paragraph AND a 7th troubleshooting row to an already two-section page may overflow the footer. This is a layout pass the executor handles by rebuilding and, if overflow_check fails, tightening page-2-only vertical rhythm (step padding, p.lead/callout/diag margins). Flagging so the executor expects 2-3 nudge-and-rebuild passes and eyeballs page 2 — not a content decision.

**Sources:** https://www.tastingtable.com/1911072/why-garlic-burns-faster/ · https://www.americastestkitchen.com/articles/7557-why-you-should-wait-to-add-garlic · https://www.mashed.com/1839174/ground-beef-browning-mistakes/ · https://www.tastingtable.com/2039950/avoid-ground-beef-mistakes/ · https://www.americastestkitchen.com/articles/1435-overhauling-sloppy-joes · https://www.aol.com/avoid-soggy-hamburger-buns-according-124000790.html · https://natashaskitchen.com/sloppy-joe-recipe/

---

## 10. pollo-asado

1. **Thigh doneness target in the Temperature Targets table (page 1)**
   - _why:_ Cubed thigh is dark meat; collagen-to-gelatin conversion runs 140-195F, and dark meat is meltingly tender/succulent at 185-195F vs tough-and-rubbery at 165-175F. 165F is the safety floor, not the eating target (America's Test Kitchen). Locked direction: replace 165-175F in all 3 places.
   - FROM: `<tr><td>Chicken internal</td><td class="amt">165&ndash;175&deg;F</td></tr>`
   - TO: `<tr><td>Chicken internal</td><td class="amt">185&ndash;195&deg;F</td></tr>`
2. **Thigh doneness target in the Method, step 7 (Finish)**
   - _why:_ Same dark-meat doneness correction; keep all three references consistent. The small cubes blow past 165F in seconds anyway, so 185-195F is the realistic and tastier pull point.
   - FROM: `<b>fresh cilantro on the green only</b>. Pull at <b>165&ndash;175&deg;F</b>, serve now.`
   - TO: `<b>fresh cilantro on the green only</b>. Pull at <b>185&ndash;195&deg;F</b>, serve now.`
3. **Thigh doneness target in the Troubleshooting table, Dry meat row Fix cell**
   - _why:_ Fixes the backwards logic: dryness comes from OVERcooking, and the fix is not overshooting the gelatin window (collagen breaks down 140-195F; past 205-210F fibers go stringy and dry). Pulling 'early' at 165-175F was the wrong lever for dark meat. Locked direction explicitly calls this out.
   - FROM: `<tr><td class="sym">Dry meat</td><td>Overcooked or low oil in marinade</td><td>Pull at 165&ndash;175&deg;F; keep the oil ratio</td></tr>`
   - TO: `<tr><td class="sym">Dry meat</td><td>Overcooked past the gelatin window, or low oil in marinade</td><td>Pull by 195&deg;F (don&rsquo;t overshoot to 205&deg;F+); keep the oil ratio</td></tr>`
4. **Cumin in the Green / Herb-Jalapeno marinade salt+spice line** `⚠ SALT — VERIFY/skip`
   - _why:_ Locked direction: cut cumin so herb/jalapeno/citrus lead. Cumin is earthy/heavy and muddies a bright fresh-green profile; the red achiote marinade carries the warm-spice load. Salt 4 g/450 g stays (~0.9% on meat, house budget); oregano 1 g kept as the herb note.
   - FROM: `<tr><td>Salt &middot; cumin &middot; oregano</td><td class="amt">4 &middot; 2 &middot; 1 g</td></tr>`
   - TO: `<tr><td>Salt &middot; oregano</td><td class="amt">4 &middot; 1 g</td></tr>`
5. **Add a pat-dry step before the sear (new Method step inserted after Temper / before Sear)**
   - _why:_ Locked direction: add a pat-dry step before the sear. Wet marinated surface flashes to steam on a 450-500F griddle and suppresses the Maillard char the recipe is built around. Inserting between Temper and Sear puts it in the correct sequence; step numbers auto-increment (CSS counter), so the later 'Chop/Finish' steps renumber automatically.
   - FROM: `<li><b>Temper:</b> pull the chicken <b>20 min</b> before cooking. Heat griddle / cast iron until screaming &mdash; <b>IR 450&ndash;500&deg;F</b>.</li>
    <li><b>Sear:</b>`
   - TO: `<li><b>Temper:</b> pull the chicken <b>20 min</b> before cooking. Heat griddle / cast iron until screaming &mdash; <b>IR 450&ndash;500&deg;F</b>.</li>
    <li><b>Pat dry:</b> lift cubes from the marinade and <b>blot every face</b> on paper towel &mdash; surface moisture steams and blocks char. A dry exterior sears on contact.</li>
    <li><b>Sear:</b>`

**Research notes:**
- Dark-meat (thigh) eating-doneness target is 185-195F, where collagen fully converts to gelatin for a silky/succulent texture; 165F is the USDA safety floor, not the flavor target (America's Test Kitchen).
- Collagen-breakdown 'sweet spot' is 140-195F internal; goal is to hold meat in that band. Past 205-210F the muscle fibers go stringy and lose chicken flavor -> this is the actual cause of 'dry meat', confirming the original troubleshooting fix (pull EARLY at 165-175) was backwards.
- Small ~1-1.5 inch cubes on a 450-500F griddle reach internal temp almost instantly, so 185-195F is easily and quickly achievable without drying when paired with the chop-and-sear method.
- Green marinade salt unchanged at 4 g per 450 g meat (~0.9%), within the house ~0.9-1.0% sodium budget; cumin removal only affects the spice/flavor line, no sodium impact.
- No footer/overflow concern flagged in advance, but page 2 gains one Method <li>; if overflow_check fails on rebuild, tighten page-2-only vertical rhythm (ol.steps li padding / callout margin) per CLAUDE.md, never touch page 1.

**Sources:** https://www.americastestkitchen.com/articles/3115-best-internal-temp-chicken-thighs-drumsticks

---

## 11. sushi-burrito

1. **Page-1 Key Targets: rice seasoning ratio label** `⚠ SALT — VERIFY/skip`
   - _why:_ The old 3:2:0.5 label contradicts the gram batch (vinegar 60 g, sugar 25 g, salt 6 g). 3:2:0.5 reduces to 6:4:1, but the real batch is ~10:4:1 — a different mix. Locked direction: make the page-1 label MATCH the gram batch exactly, so state the literal grams that already appear in the ingredient table and the page-2 troubleshooting subtitle (which already reads 60 : 25 : 6). This is a 12% sushi-zu by cooked-rice weight, inside the standard 8-10% sweet-leaning range for a richer roll.
   - FROM: `<td>3 : 2 : 0.5 vinegar:sugar:salt</td>`
   - TO: `<td>60 : 25 : 6 vinegar:sugar:salt (g)</td>`
2. **Page-1 Sauces table: add ponzu as the named plate acid**
   - _why:_ The stack is sweet and creamy (Kewpie crab mix + eel sauce + avocado) with no finishing acid on the plate — only lemon slices rolled inside. Ponzu (citrus + shoyu) is the house-appropriate plate acid that cuts fatty/creamy fish and brightens the whole stack. 30 g covers two burritos as a drizzle-and-dip lever.
   - FROM: `<tr><td>Eel sauce <span class="mut">unagi</span></td><td class="amt">40 g</td></tr>
        <tr><td>Good shoyu <span class="mut">to dip</span></td><td class="amt">&mdash;</td></tr>`
   - TO: `<tr><td>Eel sauce <span class="mut">unagi</span></td><td class="amt">40 g</td></tr>
        <tr><td>Ponzu <span class="mut">plate acid</span></td><td class="amt">30 g</td></tr>
        <tr><td>Good shoyu <span class="mut">to dip</span></td><td class="amt">&mdash;</td></tr>`
3. **Page-2 Method: name the plate acid in the plating/cut step**
   - _why:_ Adds the plate-acid step so the ponzu introduced in the sauces table is actually deployed, and names it explicitly as the balancing acid lever (house rule: name the acid). Folds into the existing 12-step method as step 13.
   - FROM: `<li><b>Cut:</b> wet a sharp knife, cut in half on the bias, wipe the blade between cuts for a clean face.</li>`
   - TO: `<li><b>Cut:</b> wet a sharp knife, cut in half on the bias, wipe the blade between cuts for a clean face.</li>
    <li><b>Finish:</b> spoon <b>ponzu</b> over the cut faces (or pool it on the plate to dip) &mdash; the acid lever that cuts the sweet-creamy stack. Eel sauce + spicy mayo bring richness; ponzu brings it back into balance.</li>`

**Research notes:**
- Sushi-zu standard ratio is 4:2:1 vinegar:sugar:salt by volume (kazsushibistro, cooksinfo). The recipe's gram batch (60:25:6 = ~10:4:1) is a sweeter, less-salty mix than 4:2:1 — but the LOCKED DIRECTION is to make the page-1 label match the GRAM BATCH, not to re-impose the textbook ratio. So the fix is to relabel, not re-formulate.
- The old page-1 label '3 : 2 : 0.5' reduces to 6:4:1, which matches neither 4:2:1 nor the gram batch (~10:4:1) — it was simply wrong. New label states the literal grams (60:25:6), which exactly matches both the ingredient table and the page-2 troubleshooting subtitle that already reads '300 : 300 : 60 : 25 : 6'.
- Sushi vinegar should be ~8-10% of cooked-rice weight (justonecookbook/suzumokikou range). 60 g sushi-zu on ~300 g raw (yielding more cooked) is on the generous/sweet side but internally consistent; no gram changes requested, only the label reconciliation.
- Rice:water 1:1 by weight (300 g : 300 g) is VERIFIED CORRECT for a pressure cooker / Instant Pot — near-zero evaporation means short-grain sushi rice wants 1:1, unlike stovetop (pressurecookrecipes, justonecookbook instant-pot). Page-1 spec 'Rice Ratio 1:1 rice:water' and step 2 both stand — no change needed.
- Plate acid: ponzu (yuzu/citrus + shoyu) both supports and cuts fatty fish and brightens creamy components (food52 yuzu-ponzu, tastingtable sushi-burrito, theendlessmeal). Chosen over plain lemon because lemon is already rolled inside; ponzu adds a savory-citrus finishing lever on the plate.

**Sources:** https://www.kazsushibistro.com/how-to-make-sushi-vinegar/ · https://www.cooksinfo.com/sushi-zu · https://www.justonecookbook.com/how-to-make-sushi-rice/ · https://www.suzumokikou.com/column/sushi-basics-how-to-make-sushi-vinegar-and-vinegared-rice-sushi-rice · https://www.pressurecookrecipes.com/instant-pot-sushi-rice/ · https://www.justonecookbook.com/instant-pot-rice/ · https://food52.com/recipes/60391-japanese-style-yuzu-ponzu-grilled-salmon · https://www.tastingtable.com/1852652/ingredients-add-sushi-burrito/ · https://www.theendlessmeal.com/ponzu-sauce/

---

## 12. al-pastor

1. **Cut achiote paste from 9% to 5% (175 g). 9% is muddy/bitter-high; authentic home recipes run 3-5% and even Bayless's achiote-forward version is ~7%.**
   - _why:_ 9% achiote dominates and turns the adobo muddy/medicinal. Muy Delish uses ~20 g achiote per ~3 lb pork (~1.5%); Bayless's achiote-forward version is ~7% (half a 50 g brick per 680 g pork). 5% is authentic-forward, color-rich, not bitter.
   - FROM: `<tr><td>Achiote paste <span class="mut">brick, El Yucateco</span></td><td class="pct">9%</td><td class="amt">315 g</td></tr>`
   - TO: `<tr><td>Achiote paste <span class="mut">brick, El Yucateco</span></td><td class="pct">5%</td><td class="amt">175 g</td></tr>`
2. **Trim white vinegar from 6.5% to 5% (175 ml) to rebalance acid without pineapple, letting grilled-onion sweetness carry.**
   - _why:_ Pineapple is OFF (team onion). Authentic marinades run vinegar ~4.4% (Muy Delish: 60 ml + OJ for ~3 lb). 6.5% with no pineapple sugar reads harsh/sour. 5% keeps the tang but lets the OJ (13%) and charred-onion sweetness balance it. Acid lever named: vinegar trim + griddle-onion sweetness, no pineapple.
   - FROM: `<tr><td>White vinegar <span class="mut">distilled / white wine</span></td><td class="pct">6.5%</td><td class="amt">228 ml</td></tr>`
   - TO: `<tr><td>White vinegar <span class="mut">distilled / white wine</span></td><td class="pct">5%</td><td class="amt">175 ml</td></tr>`
3. **Drop salt from 1.5% (52 g) to 1.0% (35 g) to hit the house 0.9-1.0% budget; flaky finishing salt at serve covers perceived seasoning.** `⚠ SALT — VERIFY/skip`
   - _why:_ House salt gate is ~0.9-1.0% of weight; 1.5% is over budget. The recipe already finishes with flaky salt on the taco (step + troubleshooting), so marinade salt can sit at 1.0% and still season correctly.
   - FROM: `<tr><td>Salt <span class="mut">Diamond Crystal, by wt</span></td><td class="pct">1.5%</td><td class="amt">52 g</td></tr>`
   - TO: `<tr><td>Salt <span class="mut">Diamond Crystal, by wt</span></td><td class="pct">1.0%</td><td class="amt">35 g</td></tr>`
4. **Update the salt-conversion callout to the new 35 g base and corrected Morton/table equivalents.** `⚠ SALT — VERIFY/skip`
   - _why:_ Callout must reconcile with the new 35 g salt. Also corrects the by-weight conversion factors: Diamond Crystal vs Morton kosher is ~1.25:1 by weight (Morton ≈ 75% of DC weight, not 60%), and fine table salt ≈ 60% of DC weight.
   - FROM: `<b>Salt is brand-dependent &mdash; convert by weight:</b> the 52 g is <b>Diamond Crystal</b> for 3.5 kg. Morton Kosher = <b>60%</b> of that (31 g); table salt = <b>50%</b> (26 g).`
   - TO: `<b>Salt is brand-dependent &mdash; convert by weight:</b> the 35 g is <b>Diamond Crystal</b> for 3.5 kg (1.0% &mdash; finish with flaky salt at serve). Morton Kosher = <b>~75%</b> of that (26 g); table salt = <b>~60%</b> (21 g).`
5. **Honest-label the unvalidated 'medium' heat claim in the Adobo Formula header note — mark it needs-tasting.**
   - _why:_ The 0.5/1/1.5% = mild/medium/hot scale is unvalidated guesswork. House honesty gate: don't assert a heat level we haven't confirmed. Hedged as estimated and flagged to taste-test before committing a freezer batch.
   - FROM: `<h2>Adobo Formula <span class="note">% of pork weight &mdash; &aacute;rbol 1% = medium; 0.5% mild, 1.5% hot</span></h2>`
   - TO: `<h2>Adobo Formula <span class="note">% of pork weight &mdash; &aacute;rbol is the heat dial (untasted: 1% = est. medium); taste a test batch before scaling</span></h2>`
6. **Honest-label the 'heat dial' note on the árbol ingredient row to match — mark it estimated/untasted.**
   - _why:_ Keeps the heat-level honesty consistent between the row and the header note: 1% árbol is an untasted estimate, not a confirmed 'medium'.
   - FROM: `<tr><td>&Aacute;rbol <span class="mut">dried &mdash; heat dial</span></td><td class="pct">1%</td><td class="amt">35 g</td></tr>`
   - TO: `<tr><td>&Aacute;rbol <span class="mut">dried &mdash; heat dial, est. medium</span></td><td class="pct">1%</td><td class="amt">35 g</td></tr>`
7. **Bump the version stamp from v1.0 to v1.1 in both page footers and the page-1 kicker (3 occurrences).**
   - _why:_ House gate requires a version bump on every substantive edit; footers/kicker carry the stamp. (Apply to all three: kicker 'v1.0', page-1 footer 'Al Pastor v1.0', page-2 footer 'Al Pastor v1.0'.)
   - FROM: `v1.0`
   - TO: `v1.1`

**Research notes:**
- Achiote: Rick Bayless al pastor uses half of a 3.5 oz (~50 g) achiote brick for 1.5 lb (680 g) pork ≈ 7.3% — and that is an achiote-forward version. Muy Delish authentic uses ~20 g achiote (¼ bar) per ~3 lb pork ≈ 1.5%. Most home recipes land 3-5%. Current 9% is high; spec'd 5% as authentic-forward middle.
- Vinegar: Muy Delish authentic uses ¼ cup (60 ml) white vinegar + ½ cup OJ for ~3 lb pork ≈ 4.4% of pork weight. Some recipes go ¾ cup for larger batches. Current 6.5% reads harsh with no pineapple sugar; spec'd 5%.
- Salt: house gate is ~0.9-1.0% of weight; current 1.5% is over. Recipe already finishes with flaky salt at serve, so 1.0% marinade salt seasons correctly. Spec'd 1.0% (35 g).
- Salt conversion factors corrected: Diamond Crystal kosher is the lightest; Morton kosher ≈ 1.25x denser (Morton weight ≈ 75% of DC for same volume/saltiness by weight), fine table salt ≈ 60% of DC weight. Original callout's 60%/50% figures were off.
- Heat: the 0.5/1/1.5% árbol = mild/medium/hot scale is unvalidated. Hedged to 'untasted: est. medium' and flagged 'taste a test batch before scaling' per honesty gate and the recipe-build test-batch-before-bulk rule (this is a freezer/bulk workflow).
- Pineapple intentionally NOT added (user is team onion). Acid/sweet rebalanced via vinegar trim (6.5→5%) leaning on the existing 13% OJ + charred white onion (already in cook steps 3-4 page 2) for sweetness. No new ingredient rows.
- OJ left at 13% (455 ml) — already in the authentic range (Muy Delish ~½ cup per 3 lb ≈ 8-9%; 13% is generous but supports the no-pineapple sweetness lever, so kept intentionally).

**Decide first:**
- Heat level at 1% árbol (35 g for 3.5 kg) is an untasted estimate — the spec now says so, but the actual mild/medium/hot calibration needs a test batch before a full freezer run.
- Salt at 1.0% assumes meaningful flaky-salt finishing at serve. If you skip the finishing salt, the meat may read slightly under-seasoned — bump marinade salt toward 1.2% only if testing confirms it.

**Sources:** https://www.rickbayless.com/recipe/pastor-style-tacos/ · https://www.muydelish.com/al-pastor-marinade/ · https://www.chilipeppermadness.com/recipes/al-pastor-marinade/ · https://pinaenlacocina.com/adobo-for-al-pastor/

---

## 13. pozole-rojo

1. **Spec/temperature header note: remove impossible pork internal-temp gate, replace with tenderness cue**
   - _why:_ Pork is submerged in a 190-200F broth; meat in liquid cannot exceed broth temp, so a 195-205F internal target is physically unreachable. Tenderness is the real doneness signal.
   - FROM: `<h2>Temperature Targets <span class="note">paste fries to brick/burgundy; pork done at 195&ndash;205&deg;F</span></h2>`
   - TO: `<h2>Temperature Targets <span class="note">paste fries to brick/burgundy; pork done when fork-tender</span></h2>`
2. **Temperature-targets diag table: replace the 'Pork internal 195-205F' cell with a tenderness/time cue**
   - _why:_ Submerged meat tops out at broth temp (190-200F); it never reaches 195-205F. Collagen-to-gelatin is a time-at-temperature reaction that yields fork-tender, easily shredded pork at this simmer in ~2.5-3 hr (matches the recipe's own simmer window).
   - FROM: `<tr><td class="sym">Broth simmer</td><td>190&ndash;200&deg;F</td><td class="sym">Pork internal</td><td>195&ndash;205&deg;F</td></tr>`
   - TO: `<tr><td class="sym">Broth simmer</td><td>190&ndash;200&deg;F</td><td class="sym">Pork done</td><td>fork-tender, ~2.5&ndash;3 hr</td></tr>`
3. **Step 5 (Toast): delete the phantom pasilla — it is not on the ingredient list**
   - _why:_ Pasilla is named in the method but has no entry or weight in the ingredient list (chiles are guajillo 140 g / ancho 50 g / arbol 10 g). Deleting it (vs inventing a weight) keeps the on-spec 70/25/5 ratio and 200 g paste total intact, no other numbers to reconcile.
   - FROM: `<li><b>Toast:</b> dry skillet &mdash; &aacute;rbol 15&ndash;20 sec/side, guajillo/ancho/pasilla 30&ndash;60 sec/side. Watch for the puff, then stem + seed.</li>`
   - TO: `<li><b>Toast:</b> dry skillet &mdash; &aacute;rbol 15&ndash;20 sec/side, guajillo/ancho 30&ndash;60 sec/side. Watch for the puff, then stem + seed.</li>`
4. **Step 10 (Finish): remove the impossible 195-205F pork gate, use the tenderness cue** `⚠ SALT — VERIFY/skip`
   - _why:_ Same physics: a 195-205F internal probe target on submerged meat can never trigger. Shreds-easily is the executable cue and is what governs when to pull the pork.
   - FROM: `<li><b>Finish:</b> pork at 195&ndash;205&deg;F &rarr; remove. Strain + skim the broth, add the chile-hominy, simmer <b>15 min</b>, return the pork 5 min. Salt; lime if flat.</li>`
   - TO: `<li><b>Finish:</b> pork fork-tender (shreds easily) &rarr; remove. Strain + skim the broth, add the chile-hominy, simmer <b>15 min</b>, return the pork 5 min. Salt; lime if flat.</li>`
5. **Troubleshooting 'Brown, not red' cause: drop pasilla so the card no longer references an ingredient it doesn't list**
   - _why:_ Pasilla is being deleted everywhere; this table is the third and last mention. Ancho is the dark chile that's actually in the build, so the cause stays accurate.
   - FROM: `<tr><td class="sym">Brown, not red</td><td>Too much dark chile (pasilla / ancho); old or over-toasted chiles</td><td>Go guajillo-forward (~70%); glossy chiles, toast lightly</td></tr>`
   - TO: `<tr><td class="sym">Brown, not red</td><td>Too much dark chile (ancho); old or over-toasted chiles</td><td>Go guajillo-forward (~70%); glossy chiles, toast lightly</td></tr>`
6. **Troubleshooting 'Tough pork' row: replace the 'Under 195F' cause/fix with an undercook-time cue**
   - _why:_ Final 195-205F reference. Tough pork is a time problem, not a probe-number problem, since the broth caps the meat at ~200F. Collagen breakdown peaks ~190-203F and is governed by time at that temperature.
   - FROM: `<tr><td class="sym">Tough pork</td><td>Under 195&deg;F</td><td>Keep simmering &mdash; collagen breaks at 195&ndash;205&deg;F</td></tr>`
   - TO: `<tr><td class="sym">Tough pork</td><td>Not simmered long enough</td><td>Keep simmering &mdash; collagen melts to gelatin over 2.5&ndash;3 hr at 190&ndash;200&deg;F</td></tr>`

**Research notes:**
- Collagen-to-gelatin is a time-at-temperature reaction; breakdown spans ~180-205F and peaks ~190-203F, yielding meat that pulls apart with a fork. Braised pork shoulder is typically fork-tender in ~2.5-3 hr (ScienceInsights, The MeatStick, ElevatingKitchen).
- Physics of the fix: pork submerged in a 190-200F simmer cannot exceed the broth temperature, so a 195-205F INTERNAL probe target is unreachable in this pot. The recipe's own broth-simmer target (190-200F) and simmer time (2.5-3 hr) already define doneness via tenderness, so the new cue is internally consistent with no number changes.
- Pasilla appears 3x in the source (step 5 Toast, the SVG-adjacent text? no, only method+troubleshooting) but NOT in the ingredient list. Exact mentions: step 5 'guajillo/ancho/pasilla', troubleshooting 'Brown, not red' cause 'pasilla / ancho', and the 'Too much dark chile (pasilla...)' phrasing. Chosen fix per locked direction: delete (no weight to invent), preserving the established guajillo 70% / ancho 25% / arbol 5% = 200 g paste.
- Authentic pozole chile ratios vary widely (1:1 guajillo:ancho up to guajillo-forward blends); the card's guajillo-forward 70/25/5 is legitimate and supported as the way to keep the broth RED rather than brown (guajillo carries red; dark chiles dull it). No ratio change needed (Mexican Food Journal, McCormick El Guapo, rachelrecipe).
- Authentic technique (paste-fry to brick/burgundy in shimmering lard, blanch the trotters/bones, lazy 190-200F simmer, no hard boil) is preserved untouched per the locked direction — these edits only fix the impossible doneness gate and the phantom chile.

**Sources:** https://scienceinsights.org/how-to-break-down-collagen-in-meat-for-tender-results/ · https://themeatstick.com/blogs/tips-recipes/the-science-of-collagen-how-to-turn-tough-cuts-into-tender-perfection · https://elevatingkitchen.com/what-temp-does-pork-shoulder-finish-at/ · https://www.verymeaty.com/fresh-meat/pork/what-temperature-does-pork-collagen-break-down/ · https://mexicanfoodjournal.com/red-pork-pozole/ · https://www.mccormick.com/blogs/el-guapo-recipes/guajillo-red-pozole · https://www.rachelrecipe.com/traditional-mexican-pozole-rojo-with-guajillo-and-ancho-chiles/

---

## 14. carne-asada-picada

1. **Cook Targets table — replace the unprobeable internal pull-temp row with a char/time cue**
   - _why:_ A thermometer can't read a 1-1.5 cm cube on a 450-500F surface — the probe spans the whole piece and equilibrates before you can pull. The row purported precision the tool can't deliver. Steak-bite/picada sources put ~1-inch cubes at 1-2 min/side on high heat, with 1 min/side landing the doneness you want for tender bites; on a smaller 1-1.5 cm cube ~1 min/side is the right anchor. Pairs with the existing 'crusty edge, tender' final-texture row, which now carries the actual doneness read.
   - FROM: `<tr><td>Internal <span class="mut">pull temp</span></td><td class="amt">130&ndash;140&deg;F</td></tr>`
   - TO: `<tr><td>Sear time <span class="mut">per face</span></td><td class="amt">~1 min/side</td></tr>`
2. **Cook step 4 (Finish & build) — replace the 130-140F internal pull with a char/feel cue** `⚠ SALT — VERIFY/skip`
   - _why:_ Locked direction: the 130-140F pull is unprobeable on a 1-1.5 cm cube and shouldn't govern the cook. Replaces it with the cue that actually governs small diced beef on a ripping-hot griddle — crust coverage + edges + firmed center, on a total-time window (3-5 min) the sources support. 'Pat dry going in' and 'hard sear' upstream already set up the crust this references.
   - FROM: `<li><b>Finish &amp; build:</b> pull at <b>medium, 130&ndash;140&deg;F</b>. Double-stacked tortillas, the seared beef, then <b>fresh lime, the Phase 2 salsa, raw onion + cilantro, flaky salt</b>. Brightness <i>and</i> heat both come on at the table.</li>`
   - TO: `<li><b>Finish &amp; build:</b> pull when the cubes are <b>browned on most faces with crusty edges and the centers have just firmed</b> (~3&ndash;5 min total on the hot surface) &mdash; chase color, not a probe; a 1.5 cm cube cooks through before any thermometer can read it. Double-stacked tortillas, the seared beef, then <b>fresh lime, the Phase 2 salsa, raw onion + cilantro, flaky salt</b>. Brightness <i>and</i> heat both come on at the table.</li>`
3. **Troubleshooting row 'Tough / chewy' — drop the internal-temp fix, keep the grain + overcook fix as a time/char cue**
   - _why:_ Third and last appearance of the 130-140F probe target. Same fix in cue form: overcooking a small cube is a time problem on a hot surface, not a temperature you can chase with a thermometer. Keeps the cross-grain instruction (the real toughness lever) intact.
   - FROM: `<tr><td class="sym">Tough / chewy</td><td>Cut with the grain, or overcooked</td><td>Dice across the grain; pull at 130&ndash;140&deg;F</td></tr>`
   - TO: `<tr><td class="sym">Tough / chewy</td><td>Cut with the grain, or overcooked</td><td>Dice across the grain; pull at first good crust (~3&ndash;5 min total), don&rsquo;t hold on the heat</td></tr>`

**Research notes:**
- All three occurrences of the 130-140F internal pull are now located: line 164 (Cook Targets table), line 175 (cook step 4 'Finish & build'), line 181 (Troubleshooting 'Tough/chewy' row). The three edits above cover all three — no stray instance remains.
- Doneness governance: on a 1-1.5 cm cube at 450-500F, internal temp does NOT govern and is not measurable — the cube is smaller than a useful probe insertion and equilibrates near-instantly. Char coverage + total time is the controlling read. This matches the recipe's existing 'Char coverage 15-20%' and 'crusty edge, tender' targets, which are kept.
- Timing anchor: multiple steak-bite/picada sources put ~1-inch cubes at 1-2 min/side / ~3-5 min total on high heat, with ~1 min/side = the tender (not well-done) result desired. On a smaller 1-1.5 cm cube the ~1 min/side and 3-5 min total windows hold; edits use ~1 min/side (table) and ~3-5 min total (steps), no contradiction.
- DECISION FLAG for the user (do not auto-change): the Phase 1 marinade leans on Maggi Jugo at 2% of beef weight (220 g per 11 kg clod) as the 'umami backbone', and the salt line is set LOW (0.6%, 66 g) explicitly because 'with Maggi, ~1% total sodium'. The user wants beef-FORWARD, but Maggi is doing the heavy umami lifting and is propping up the sodium budget. If he wants the beef to lead, the lever is to cut Maggi (e.g. 2% -> 1% / 110 g) and raise Diamond Crystal to carry sodium back to ~1% (roughly 0.6% -> ~0.9%, ~66 g -> ~100 g) — but that is a flavor-direction decision, not a mechanical fix, so it is flagged here and surfaced as an open question rather than edited. None of the three edits touch the marinade.
- No unit, span-balance, or footer-overflow risk introduced: edits swap text/values inline, add no new rows or blocks, and use existing entities (&ndash;, &deg;, &rsquo;). Cook step 4 grows by ~1 line of text on page 3 — page 3 is the lightest page (cook + troubleshooting), so overflow is very unlikely, but build.py's overflow_check is the gate; eyeball page 3 if it reads near-full.
- Version note (informational, not an edit): footers currently read v1.0 / v1-0. House practice bumps the version on a content change. If desired, the user/executor can bump to v1.1 / v1-1 across all three page footers and the kicker — left out of the edits because the locked direction was scoped to the pull-temp cue, and the version bump is a separate convention call.

**Decide first:**
- Maggi spine vs. beef-forward (DECISION, flagged not changed): the marinade carries 2% Maggi (220 g) and intentionally low salt (0.6%, 66 g) to land ~1% sodium. For a beef-forward result, do you want to cut Maggi toward ~1% (110 g) and raise Diamond Crystal toward ~0.9% (~100 g) to hold the sodium budget? This needs your call before any marinade edit — it changes the flavor identity, not just a number.
- Version bump: bump footers/kicker v1.0 -> v1.1 (and v1-0 -> v1-1) with this change, or leave the stamp as-is?

**Sources:** https://www.savingyoudinero.com/2022/07/08/easy-carne-picada-recipe/ — finely diced picada cooks to done in ~5 min on a hot surface; doneness read by brown crust · https://www.orwhateveryoudo.com/2023/09/easy-blackstone-carne-asada.html — sear then chop on the flat-top; visual brown-crust cue for griddle carne asada · https://www.sipandfeast.com/garlic-butter-steak-bites/ — 1-inch beef cubes seared on high heat, crust-and-release as the doneness read (resist flipping until it releases) · https://bestrecipebox.com/skillet-steak-bites/ — small beef cubes: ~1-2 min/side, ~3-5 min total on a hot skillet; sear all faces to a crust · https://iamhomesteader.com/steak-bites/ — 1-inch cubes: 1 min/side = medium-well (tender), 2 min/side = well done; time-based doneness, not probe

---

## 15. chicken-shawarma

1. **Spice blend — col 1 table: rebalance to allspice-led, sumac-forward, cumin restrained (lines 92-96). Replace the entire col-1 ingredient table body so allspice becomes the 28% lead, cumin drops from lead to a 12% base note, and sumac is introduced at 18%.**
   - _why:_ Locked direction: pivot the cumin-led blend to allspice + sumac forward (more Levantine). Allspice is the warm Levantine spine (reads as cinnamon/clove/nutmeg together) and sumac supplies the tart lemony note that defines authentic shawarma — sources put sumac at the top of the blend by volume. Cumin restrained from 28% to 12% so it's a base, not the lead. Percentages sum to 100%; grams to 50g batch unchanged.
   - FROM: `<tr><td>Cumin</td><td class="pct">28%</td><td class="amt">14 g</td></tr>
        <tr><td>Coriander</td><td class="pct">18%</td><td class="amt">9 g</td></tr>
        <tr><td>Paprika <span class="mut">sweet</span></td><td class="pct">15%</td><td class="amt">7.5 g</td></tr>
        <tr><td>Turmeric</td><td class="pct">10%</td><td class="amt">5 g</td></tr>
        <tr><td>Allspice <span class="mut">signature</span></td><td class="pct">9%</td><td class="amt">4.5 g</td></tr>`
   - TO: `<tr><td>Allspice <span class="mut">signature</span></td><td class="pct">28%</td><td class="amt">14 g</td></tr>
        <tr><td>Sumac <span class="mut">lemony tang</span></td><td class="pct">18%</td><td class="amt">9 g</td></tr>
        <tr><td>Cumin</td><td class="pct">12%</td><td class="amt">6 g</td></tr>
        <tr><td>Coriander</td><td class="pct">12%</td><td class="amt">6 g</td></tr>
        <tr><td>Paprika <span class="mut">sweet</span></td><td class="pct">8%</td><td class="amt">4 g</td></tr>`
2. **Spice blend — col 2 table: drop nutmeg (now redundant under a 28% allspice lead) and re-percent remaining warm spices (lines 101-105). Keeps the table at exactly 5 rows per column / 10 total.**
   - _why:_ Allspice at 28% already delivers the nutmeg-adjacent note (allspice literally tastes of cinnamon+clove+nutmeg), so a separate 3% nutmeg is redundant and over-spices — drop it per house 'count every spice / no over-spicing'. Turmeric moves here from col 1 and trims 10%->4% (it's a color/earth note, not a flavor lead). Whole blend now sums 28+18+12+12+8+7+6+4+3+2 = 100% and 50 g exactly.
   - FROM: `<tr><td>Black pepper</td><td class="pct">7%</td><td class="amt">3.5 g</td></tr>
        <tr><td>Cinnamon</td><td class="pct">5%</td><td class="amt">2.5 g</td></tr>
        <tr><td>Cardamom <span class="mut">green, seeds only</span></td><td class="pct">3%</td><td class="amt">1.5 g</td></tr>
        <tr><td>Nutmeg</td><td class="pct">3%</td><td class="amt">1.5 g</td></tr>
        <tr><td>Clove</td><td class="pct">2%</td><td class="amt">1 g</td></tr>`
   - TO: `<tr><td>Black pepper</td><td class="pct">7%</td><td class="amt">3.5 g</td></tr>
        <tr><td>Cinnamon</td><td class="pct">6%</td><td class="amt">3 g</td></tr>
        <tr><td>Turmeric <span class="mut">color</span></td><td class="pct">4%</td><td class="amt">2 g</td></tr>
        <tr><td>Cardamom <span class="mut">green, seeds only</span></td><td class="pct">3%</td><td class="amt">1.5 g</td></tr>
        <tr><td>Clove</td><td class="pct">2%</td><td class="amt">1 g</td></tr>`
3. **Spice-blend callout: rewrite the signature/clove guidance to match the new allspice-led, sumac-forward identity (line 110).**
   - _why:_ The old callout framed allspice as a conservative 9% afterthought and named only paprika/turmeric as pre-ground adds. New copy reflects the rebalance: allspice is now the lead, explains why nutmeg was dropped, names sumac as the forward tang and how to handle it. Sumac is sold pre-ground so it joins the homogenize pulse, not the whole-spice grind. House honesty: states the real role of each forward spice.
   - FROM: `<b>Grind everything together in a spice grinder</b> to a uniform powder &mdash; whole spices ground fresh are far more potent than pre-ground (the volatile oils oxidize fast). Grind the whole spices first, then pulse the pre-ground ones (paprika, turmeric) in to homogenize. <b>Cardamom: green pods, seeds only</b> &mdash; the papery husk is flavorless filler; the 1.5g is seed weight. <b>Allspice is the signature note</b> &mdash; 9% is conservative, bump to <b>12&ndash;15%</b> if timid; <b>go easy on clove</b>, it dominates fast. Blend keeps <b>6+ months</b> sealed.`
   - TO: `<b>Grind everything together in a spice grinder</b> to a uniform powder &mdash; whole spices ground fresh are far more potent than pre-ground (the volatile oils oxidize fast). Grind the whole spices first, then pulse the pre-ground ones (sumac, paprika, turmeric) in to homogenize. <b>Cardamom: green pods, seeds only</b> &mdash; the papery husk is flavorless filler; the 1.5g is seed weight. <b>Allspice leads (28%)</b> &mdash; the warm Levantine spine; it reads as cinnamon, clove, and nutmeg at once, so no separate nutmeg is needed. <b>Sumac (18%) is the tang</b> &mdash; tart, lemony, it defines authentic shawarma; add it after grinding (it's already a fine powder and scorches in a hot grinder). <b>Go easy on clove</b>, it dominates fast. Blend keeps <b>6+ months</b> sealed.`
4. **Temperature Targets, page 1 — chicken internal target 165-175F -> 175-185F (line 145). Place #1 of 3.**
   - _why:_ Locked direction: thigh doneness to 175-185F+ in all 3 places. Thighs are full of collagen; the breakdown sweet spot runs to ~195F, and America's Test Kitchen / ThermoWorks put 175F as the floor for tender (vs the USDA 165F safety minimum) and ~185F as best-tasting. At 165F a thigh is safe but chewy. Thin-sliced, hard-seared shawarma will sail past these temps anyway; spec'ing 175-185F sets the correct target.
   - FROM: `<tr><td>Chicken internal</td><td class="amt">165&ndash;175&deg;F</td></tr>`
   - TO: `<tr><td>Chicken internal</td><td class="amt">175&ndash;185&deg;F</td></tr>`
5. **Method step 7 (Serve) — pull temp 165-175F -> 175-185F (line 168). Place #2 of 3.**
   - _why:_ Same doneness change applied to the cook step that governs the pull. Keeps page 1 target and page 2 instruction in sync so the cook isn't given two different numbers.
   - FROM: `<li><b>Serve:</b> <b>immediately, no rest</b> &mdash; crispy edges degrade fast. Pull at <b>165&ndash;175&deg;F</b>. Taste before wrapping; it should eat great plain.</li>`
   - TO: `<li><b>Serve:</b> <b>immediately, no rest</b> &mdash; crispy edges degrade fast. Pull at <b>175&ndash;185&deg;F</b>. Taste before wrapping; it should eat great plain.</li>`
6. **Troubleshooting table, 'Dry meat' row — fix text 'Check 165-175F' -> 'Check 175-185F' (line 180). Place #3 of 3.**
   - _why:_ Third and final doneness reference. All three internal-temp mentions now read 175-185F so the card is internally consistent (numbers-reconcile gate).
   - FROM: `<tr><td class="sym">Dry meat</td><td>Overcooked or under-oiled marinade</td><td>Check 165&ndash;175&deg;F; use 15&ndash;20% oil</td></tr>`
   - TO: `<tr><td class="sym">Dry meat</td><td>Overcooked or under-oiled marinade</td><td>Check 175&ndash;185&deg;F; use 15&ndash;20% oil</td></tr>`
7. **Bump version stamp v1.0 -> v1.1 in the three footer/kicker spots and append a one-line change note to the body footers.**
   - _why:_ House rule: version-stamp every change. Material rebalance + doneness shift warrants a minor bump. (Page-1 kicker shown here; also update both .foot version strings on line 151 'Chicken Shawarma v1.0 · spice + marinade' -> 'v1.1' and line 209 'Chicken Shawarma v1.0 · 450-500°F · chop-and-sear' -> 'v1.1'. All three v1.0 instances -> v1.1.)
   - FROM: `<div class="kicker">Professional Guide &nbsp;/&nbsp; v1.0</div>`
   - TO: `<div class="kicker">Professional Guide &nbsp;/&nbsp; v1.1</div>`

**Research notes:**
- Doneness: USDA safety minimum for poultry is 165F, but that leaves thigh chewy. America's Test Kitchen and ThermoWorks both recommend 175F+ for thighs because thigh collagen converts to gelatin across ~140-195F; 175F = reliably tender floor, ~185F = best-tasting, 190-195F = falling-apart. 175-185F target is well supported and the hard-seared thin slices will reach it easily.
- Levantine shawarma flavor: sources agree the authentic profile is warm + tart, led by allspice (the Lebanese 7-spice / baharat spine that 'tastes like cinnamon, cloves, and nutmeg at once') with sumac providing the defining lemony tang. One source cites a Levantine ratio of 3 parts sumac to 1 part cumin and notes sumac is the dominant spice by volume in authentic blends. This justifies cumin restrained and sumac/allspice forward.
- Nutmeg dropped (was 3%): redundant once allspice is the 28% lead, since allspice already carries the nutmeg note. Removing it also avoids over-spicing (house 'count every spice') and keeps the table at a clean 10 rows by swapping nutmeg's slot for sumac.
- New blend sums verified: 28(allspice)+18(sumac)+12(cumin)+12(coriander)+8(paprika)+7(black pepper)+6(cinnamon)+4(turmeric)+3(cardamom)+2(clove) = 100%. Grams: 14+9+6+6+4+3.5+3+2+1.5+1 = 50.0 g, matching the existing 'makes ~50g, 22g into 900g batch' header — so no downstream marinade/scaling numbers change.
- Sumac handling: sumac is sold pre-ground and is acidic/can scorch, so it goes into the homogenize pulse after the whole-spice grind, not into the hot grinder with the seeds — reflected in the callout.
- No change needed to spice ratio (2.5% meat wt), 22g-into-900g loading, marinade percentages, or the scaling table — the blend was re-proportioned within the same total mass, so all dependent gram figures still reconcile.

**Sources:** https://www.americastestkitchen.com/articles/3115-best-internal-temp-chicken-thighs-drumsticks · https://blog.thermoworks.com/chicken-breasts-vs-thighs/ · https://www.acedarspoon.com/lebanese-seven-spice-blend-sabaa-baharat/ · https://apinchofadventure.com/shawarma-spice-blend/ · https://worldspice.com/products/shawarma-spice · https://silkroadrecipes.com/shawarma-spice-blend/ · https://www.themediterraneandish.com/sumac-grilled-chicken-thighs/

---

## 16. nixtamal-tortillas

1. **Lengthen the cook simmer and lead with the cue, demote the clock to a wide range**
   - _why:_ Locked direction: cue-led ~20-50 min. Web sources (Breadtopia, Mexican Please, Hank Shaw) put dent-corn pericarp slip at 30-45 min, up to an hour for landrace, vs the old 15-25 min which is too short for dent corn and risks an under-cooked, gummy nixtamal. Leads with the slip cue and the chalky-white center test, demotes the clock to a guide range.
   - FROM: `<li><b>Cook:</b> add corn, bring to a boil (~10 min), then gentle simmer <b>15&ndash;25 min</b>. Done when the pericarp (skin) <b>slips off easily</b> when rubbed and the kernel is soft.</li>`
   - TO: `<li><b>Cook:</b> add corn, bring to a boil (~10 min), then gentle simmer <b>until the pericarp slips</b> &mdash; rub a kernel and the skin should peel off easily, the kernel soft but the center still chalky-white. Roughly <b>20&ndash;50 min</b>; dent corn slips late, so judge by the cue, not the clock.</li>`
2. **Spec the optional salt in grams on the ingredient line** `⚠ SALT — VERIFY/skip`
   - _why:_ Locked direction + house rule: weigh in grams, no vague 'pinch'. 8 g over ~1,400 g masa is ~0.55% — a background seasoning that brings the corn forward without making the tortilla taste salty. Matches the common reference of ~5 g salt per pound of dried corn (680 g dried -> ~7.5 g) and the 4 g per small (~400 g) masa-harina batch.
   - FROM: `<tr><td>Salt <span class="mut">optional, in the final knead</span></td><td class="amt">pinch</td></tr>`
   - TO: `<tr><td>Salt <span class="mut">optional, in the final knead</span></td><td class="amt">8 g</td></tr>`
3. **Reconcile the salt mention in the combine step to grams** `⚠ SALT — VERIFY/skip`
   - _why:_ Same no-vague-pinch rule; keeps the body text consistent with the new 8 g ingredient line.
   - FROM: `<li><b>Combine:</b> scrape out, repeat with the second half, combine, knead <b>2&ndash;3 min</b>. Add a pinch of salt if using.</li>`
   - TO: `<li><b>Combine:</b> scrape out, repeat with the second half, combine, knead <b>2&ndash;3 min</b>. Knead in <b>8 g salt</b> if using.</li>`
4. **Fix the flip-count naming collision in the Stage 3 header note**
   - _why:_ Numbers-reconcile gate: the steps below have one initial contact (First side) plus two flips (Flip 1, Flip 2 puff) = three comal contacts but only TWO flips. 'Three flips' miscounts; the third event is a contact, not a flip. New note states the true mechanics and matches the step labels (Flip 1 / Flip 2).
   - FROM: `<h2><span class="pt">Stage 3</span> &nbsp;Press &amp; Cook <span class="note">Three flips &mdash; the third is the puff</span></h2>`
   - TO: `<h2><span class="pt">Stage 3</span> &nbsp;Press &amp; Cook <span class="note">Two flips, three contacts &mdash; the puff is on the second flip</span></h2>`
5. **Fix the matching collision in the Quality Targets Puff row**
   - _why:_ Same collision: 'third flip' contradicts the step labeled 'Flip 2 (puff)'. The puff happens on the second flip (third contact). Aligns the table with the corrected header and the Flip 2 step.
   - FROM: `<tr><td class="sym">Puff</td><td>Full inflation on the third flip</td><td>Comal temp, thickness, or hydration is off</td></tr>`
   - TO: `<tr><td class="sym">Puff</td><td>Full inflation on the second flip</td><td>Comal temp, thickness, or hydration is off</td></tr>`

**Research notes:**
- Simmer-to-slip time: Breadtopia and others report white/yellow DENT corn slips at 30-45 min, landrace blue/red up to ~1 hr; cue is pinch a kernel and the pericarp slips off easily, kernel softened, center still chalky-white. Old 15-25 min is too short for dent corn. New range 20-50 min, cue-led.
- Steep stays 8-12 hr overnight (sources agree) — unchanged.
- Salt: references cluster around ~4 g per small masa-harina batch (~400 g) and ~5 g per pound (454 g) of dried corn. 680 g dried corn -> ~7.5 g; ~1,400 g masa at 8 g = ~0.55%. 8 g is a clean number, keeps salt as a background note (tortillas should not taste salty), stays 'optional'. Did not push to house 0.9-1.0% because that band is for finished savory dishes, not a corn tortilla where salt is a flavor-lift only.
- Flip collision (the real bug): steps are First side (contact 1, no flip) -> Flip 1 (contact 2) -> Flip 2/puff (contact 3). So TWO flips / THREE contacts. Header note 'Three flips — the third is the puff' and Quality Targets 'Full inflation on the third flip' both miscount; the step itself is labeled 'Flip 2 (puff)'. Fixed both to 'two flips / second flip'. The step labels themselves (Flip 1, Flip 2) are already correct and need no change.
- No edits touch page-1 vertical rhythm beyond the cook step text length (one line of growth on page 1, well within margin); footer overflow risk is low but build.py must still confirm overflow_check passes on both pages.

**Sources:** https://breadtopia.com/how-to-nixtamalize-corn-for-tortillas-tamales-posole-and-more/ · https://www.mexicanplease.com/nixtamal/ · https://honest-food.net/how-to-make-nixtamal-nixtamalization/ · https://en.wikipedia.org/wiki/Nixtamalization · http://wildgreensandsardines.com/2019/03/recipe-homemade-masa-nixtamal-corn-tortillas.html · https://www.foodnetwork.com/fnk/recipes/fresh-masa-corn-tortillas-7426452

---

## 17. maseca-tortillas

1. **Drop the FLOAT TEST row from the Hydration Check table (page 1)**
   - _why:_ The float test measures whipped-lard AERATION in tamale masa, not hydration in tortilla masa. Sources confirm it is a tamale-only technique and 'not typically used for tortilla dough.' On unwhipped, lean tortilla masa it has no meaningful pass/fail and steers you toward over-hydration (sticky dough that tears at the press). The smush and earlobe rows already validate the 55-60% target correctly.
   - FROM: `<tr><td class="sym">Float test</td><td>A pea-sized ball floats in water</td><td>Sinks = under-hydrated; knead in more water</td></tr>`
   - TO: ``
2. **Retitle the section since only smush/earlobe remain (no longer a multi-test panel)**
   - _why:_ After removing the float row, 'all one question' reads oddly with only two tests; tighten to 'one question.' Lean copy fix.
   - FROM: `<h2>Hydration Check <span class="note">all one question &mdash; is the masa at 55&ndash;60%?</span></h2>`
   - TO: `<h2>Hydration Check <span class="note">one question &mdash; is the masa at 55&ndash;60%?</span></h2>`
3. **Make the 25% toast step explicit EXPERIMENTAL and optional in the formula line (it is unproven)**
   - _why:_ Locked direction: validate or mark-experimental the 25% toast step. Web research found NO source validating that toasting already-nixtamalized masa harina powder adds flavor (nuttiness is built in by nixtamalization). It is plausible but unproven, so it must not read as a mandatory formula step. Marking it optional/experimental keeps house honesty (no false 'this works').
   - FROM: `<tr><td>Maseca <span class="mut">masa harina, yellow &mdash; toast 100 g of it (step 1)</span></td><td class="pct">100%</td><td class="amt">400 g</td></tr>`
   - TO: `<tr><td>Maseca <span class="mut">masa harina, yellow &mdash; optional: toast 100 g (step 1, experimental)</span></td><td class="pct">100%</td><td class="amt">400 g</td></tr>`
4. **Mark the toast step itself experimental in the method and make it skippable**
   - _why:_ Same honesty fix in the method. Tells the cook it is an unverified add-on with a clear skip path (all 400 g straight), so the recipe is executable either way. Also trims the 'puts back toasty depth that drying strips out' claim, which the research did not support.
   - FROM: `<li><b>Toast a quarter.</b> Dry-toast <b>100 g of the Maseca</b> (no oil) in a comal/skillet over medium, stirring, until it smells <b>nutty and just barely colors</b> &mdash; <b>3&ndash;5 min</b>. Don&rsquo;t brown it (turns bitter). This puts back toasty depth that drying strips out. Stir it into the other <b>300 g</b>.</li>`
   - TO: `<li><b>Toast a quarter (optional, experimental).</b> Dry-toast <b>100 g of the Maseca</b> (no oil) over medium, stirring, until it smells <b>nutty and just barely colors</b> &mdash; <b>3&ndash;5 min</b>; don&rsquo;t brown it (turns bitter), then stir into the other <b>300 g</b>. Unproven flavor gain &mdash; skip it and use all 400 g straight if you want the baseline.</li>`
5. **Lower salt from 1.25% to 1.0% to meet the house 0.9-1.0% salt budget** `⚠ SALT — VERIFY/skip`
   - _why:_ House salt budget is ~0.9-1.0%; current 5 g / 400 g = 1.25% is over. 4 g / 400 g = 1.0%, which sits at the lower end of Masienda's 1/2-1 tsp per 120 g cup guidance and matches the house standard. Also names the house salt (Diamond Crystal kosher) per MEMORY, replacing the generic 'fine' which would salt differently by volume.
   - FROM: `<tr><td>Salt <span class="mut">fine</span></td><td class="pct">1.25%</td><td class="amt">5 g</td></tr>`
   - TO: `<tr><td>Salt <span class="mut">Diamond Crystal kosher</span></td><td class="pct">1.0%</td><td class="amt">4 g</td></tr>`
6. **Bump version stamp to v1.1 in the kicker** `⚠ SALT — VERIFY/skip`
   - _why:_ Material changes (float row removed, salt 5->4 g, toast marked experimental) warrant a version bump; gate 8 requires a version stamp in every footer and they must stay consistent.
   - FROM: `<div class="kicker">Professional Guide &nbsp;/&nbsp; v1.0</div>`
   - TO: `<div class="kicker">Professional Guide &nbsp;/&nbsp; v1.1</div>`
7. **Update page-1 footer version stamp to v1.1**
   - _why:_ Footer version stamp must match the bumped version (gate 8); both page footers must agree.
   - FROM: `<div class="foot"><span>Aguillon House Kitchen</span><span>Maseca Tortillas v1.0 &middot; formula &amp; masa</span><span>Page 1 / 2</span></div>`
   - TO: `<div class="foot"><span>Aguillon House Kitchen</span><span>Maseca Tortillas v1.1 &middot; formula &amp; masa</span><span>Page 1 / 2</span></div>`
8. **Update page-2 footer version stamp to v1.1**
   - _why:_ Footer version stamp must match the bumped version (gate 8); both page footers must agree.
   - FROM: `<div class="foot"><span>Aguillon House Kitchen</span><span>Maseca Tortillas v1.0 &middot; press &middot; cook &middot; keep</span><span>Page 2 / 2</span></div>`
   - TO: `<div class="foot"><span>Aguillon House Kitchen</span><span>Maseca Tortillas v1.1 &middot; press &middot; cook &middot; keep</span><span>Page 2 / 2</span></div>`

**Research notes:**
- FLOAT TEST: Multiple sources confirm the masa float test is a TAMALE technique that checks whipped-lard aeration (a grape/pea-sized ball floats because air is beaten into the fat). One source states it is 'specifically a tamale-making technique and is not typically used for tortilla dough, which has a completely different preparation method.' Tortilla masa here uses only 4% melted lard with no whipping, so a float result is meaningless and chasing it pushes over-hydration -> sticky dough -> tears at the press. Confirms the locked direction; the row is removed.
- TOAST STEP: No source validated toasting masa harina powder before making tortillas. Masienda/others attribute the nutty/toasted flavor to nixtamalization built into the product, not to a separate post-grind toast. The step is plausible but UNPROVEN, so it is marked optional/experimental rather than baked into the formula, with a clear skip path (use all 400 g straight).
- SALT: Masienda recommends 1/2 to 1 tsp salt per cup (120 g) masa harina; The Kitchn ~1/2 tsp kosher; another recipe 3/4 tsp fine sea salt per 240 g. House budget is 0.9-1.0%. Current 5 g/400 g = 1.25% (over). Set to 4 g = 1.0%, low-Masienda-range and on house standard. Switched generic 'fine' to Diamond Crystal kosher per house salt memory.
- HYDRATION: Sources show tortilla masa runs roughly 1:1 to ~1.4:1 water:masa by weight, dialed by feel; the recipe's ~115% start (460 g water / 400 g masa) sits inside that range and is adjusted by the smush/earlobe tests, so the hydration target (55-60% masa moisture) and the 115% start are left unchanged.
- LARD: Adding a small amount of lard to corn-tortilla masa is supported as a softness/pliability and keeping aid, and reduces reliance on the rest. The recipe's 4% melted-into-water lard is consistent with this; left unchanged.
- LEAN: Float removal is the main trim. Toast claim 'puts back toasty depth that drying strips out' was unsupported and is cut. Kept the 2-row hydration table and the page-2 troubleshooting/storage tables as-is (clean reference, not bloat); no extra trimming needed.

**Sources:** https://masienda.com/blogs/learn/recipe-tortillas-masa-harina · https://masienda.com/blogs/learn/how-to-make-tortillas-for-your-restaurant · https://mexicanmademeatless.com/the-masa-float-test-for-tamales/ · https://burpy.com/how-to-make-masa-for-tamales/ · https://www.rickbayless.com/recipe/corn-tortillas/ · https://www.thekitchn.com/how-to-make-corn-tortillas-from-scratch-cooking-lessons-from-the-kitchn-85904 · https://alittlespoon.com/corn-tortillas-with-lard/ · https://www.mexicanplease.com/corn-tortillas-using-homemade-masa-dough/

---

## 18. molasses-cookies

1. **Ingredient: switch salted butter to unsalted butter** `⚠ SALT — VERIFY/skip`
   - _why:_ Locked direction: salted butter hides ~5.5 g salt on top of the 6 g spec, making the real total impossible to read. Unsalted butter puts 100% of the salt in the spec where it can be counted (house rule: count every sodium source).
   - FROM: `<tr><td>Salted butter <span class="mut">cold, 1cm cubes</span></td><td class="amt">336 g</td></tr>`
   - TO: `<tr><td>Unsalted butter <span class="mut">cold, 1cm cubes</span></td><td class="amt">336 g</td></tr>`
2. **Ingredient: raise spec salt to absorb the salt previously hidden in salted butter** `⚠ SALT — VERIFY/skip`
   - _why:_ Salted butter at the National Dairy Council figure of ~1.65% salt by weight = 336 g x 0.0165 = ~5.5 g hidden salt. Adding that to the existing 6 g keeps the AS-BUILT total flavor identical (6 + 5.5 = 11.5 g) now that the butter contributes zero. This makes the number honest and reconcilable instead of hiding sodium in the fat.
   - FROM: `<tr><td>Salt <span class="mut">fine/kosher, by weight</span></td><td class="amt">6 g</td></tr>`
   - TO: `<tr><td>Salt <span class="mut">fine/kosher, by weight</span></td><td class="amt">11.5 g</td></tr>`
3. **Targets table: replace the 175F set-temp pull claim with a visual underbake lead**
   - _why:_ 175F internal (~79C) is fully-set dough with no jiggle, directly contradicting the chewy/jiggly promise. Leading with the visual underbake cue and dropping the optional probe target to ~165F keeps the center gooey, per locked direction.
   - FROM: `<tr><td class="sym">Pull temp</td><td><b>175&deg;F internal</b> &mdash; carryover finishes it to 180&ndash;185&deg;F.</td></tr>`
   - TO: `<tr><td class="sym">Pull cue</td><td><b>Visual first:</b> center still soft and puffed, edges set &amp; cracked. Probing only? <b>~165&deg;F internal</b> &mdash; carryover sets the center on the pan.</td></tr>`
4. **Method step 9 (Bake): replace the 175F pull line with the visual-first underbake cue**
   - _why:_ Same contradiction as the Targets row: a 175F pull cooks past the jiggly stage. The method must tell the baker to pull on the visual underbake cue, with the optional probe lowered to ~165F so the chewy center survives.
   - FROM: `Total <b>14&ndash;16 min</b>: edges golden &amp; cracked, center jiggles when shaken. <b>Pull at 175&deg;F internal</b> &mdash; carryover finishes it.`
   - TO: `Total <b>14&ndash;16 min</b>: edges golden &amp; cracked, center still soft and jiggles when shaken &mdash; <b>pull while the center looks underbaked.</b> Probing? <b>~165&deg;F internal.</b> Carryover sets it on the pan.`
5. **Troubleshooting 'Tough' row: drop the stale 'check internal temp' pointer that referenced the old 175F target**
   - _why:_ Keeps troubleshooting consistent with the new visual-first pull; 'check internal temp' implied the deleted 175F set-point and would push the baker to overbake into toughness.
   - FROM: `<tr><td class="sym">Tough</td><td>Overmixed at combine &rarr; pull at 14 min; check internal temp</td></tr>`
   - TO: `<tr><td class="sym">Tough</td><td>Overmixed at combine &rarr; pull at 14 min on the visual underbake cue</td></tr>`
6. **Troubleshooting 'Bland' row: update the salt-verify number to the new spec** `⚠ SALT — VERIFY/skip`
   - _why:_ Numbers must reconcile: the verify pointer has to match the new 11.5 g spec, otherwise a baker re-adding 6 g would under-salt by half the intended amount now that the butter is unsalted.
   - FROM: `<tr><td class="sym">Bland</td><td>Under-salted &rarr; verify <b>6g</b> salt + the flaky finish</td></tr>`
   - TO: `<tr><td class="sym">Bland</td><td>Under-salted &rarr; verify <b>11.5g</b> salt + the flaky finish</td></tr>`
7. **Version stamp: bump v1.0 to v1.1 in the kicker and both footers** `⚠ SALT — VERIFY/skip`
   - _why:_ House gate requires a version stamp in every footer; a material change (butter type + salt total + pull cue) warrants a bump so the printed card is traceable. Apply to the page-1 kicker ('Baking Guide / v1.0') and both footer strings ('Molasses Cookies v1.0 ...').
   - FROM: `v1.0`
   - TO: `v1.1`

**Research notes:**
- Salted butter carries ~1.6-1.7% salt by weight (National Dairy Council figure, ~643 mg sodium / 100 g per USDA). At the 1.65% midpoint, the recipe's 336 g salted butter hid 336 x 0.0165 = ~5.5 g salt on top of the 6 g spec, confirming the locked-direction estimate. Switching to unsalted and setting spec salt to 11.5 g preserves the as-built total (6 + 5.5).
- Salt budget check: 11.5 g salt / ~1,960 g dough = ~0.59% total salt. This is BELOW the house 0.9-1.0% target, but it equals the recipe's current as-built level (the card already ran at this concentration once the hidden butter salt is counted) and the cookie also gets a flaky-salt finish on top. The conservative call is to preserve the existing balance rather than re-season blind; flagged as an open question in case the user wants to push toward 0.9%.
- 175F internal (~79C) is fully-coagulated/set cookie dough with no jiggle, which is why it contradicted the 'center jiggles / chewy' promise. Gooey-center cookies are pulled visually underbaked; ~160-165F internal corresponds to a still-soft center that sets via carryover on the hot pan. Lowered the optional probe to ~165F and made the visual cue lead.
- All numbers reconcile after edits: butter 336 g (now unsalted), spec salt 11.5 g, Bland-row verify 11.5 g all agree; pull cue is consistent across Targets row, Bake step, and Tough troubleshooting row.

**Decide first:**
- Salt target intent: 11.5 g preserves the current as-built flavor (~0.59% of dough) but sits below the house 0.9-1.0% salt-budget guideline. Keep at 11.5 g (preserve known-good balance), or push up toward ~0.9% (~17-18 g) for a saltier cookie? Edit assumes preserve-as-built; change the 'to' on the salt and Bland-row edits if a higher target is wanted.
- Optional probe target is set to ~165F as the gooey-center pull. If you prefer a slightly firmer chewy (not gooey) center, ~170F is the alternative; confirm which doneness you want and I'll set the single number.

**Sources:** https://minervadairy.com/blog/how-much-salt-is-in-salted-butter/ · https://www.tastingtable.com/1798849/salted-butter-salt-quantity/ · https://greatist.com/eat/how-much-salt-is-in-salted-butter · https://android.fatsecret.com/calories-nutrition/usda/butter-(salted)/photos

---

## 19. toum

1. **Subhead texture claim (page 1 .sub line)**
   - _why:_ #1 of 3 'stiff peaks' fixes. Toum is the consistency of thick mayonnaise; sources describe it holding SOFT peaks, not the rigid stiff peaks of meringue. 'Mounds and holds a soft trail' is the honest house description.
   - FROM: `<div class="sub">Lebanese garlic sauce &middot; egg-free emulsion &middot; fluffy white paste that holds stiff peaks</div>`
   - TO: `<div class="sub">Lebanese garlic sauce &middot; egg-free emulsion &middot; fluffy white paste that mounds and holds a soft trail</div>`
2. **Quality Targets table — Final texture row (page 1 .diag)**
   - _why:_ #2 of 3 'stiff peaks' fixes. Same honesty correction in the target table — toum holds a soft peak/trail like thick mayo, it does not peak like whipped egg white.
   - FROM: `<tr><td class="sym">Final texture</td><td>Holds stiff peaks, bright white</td></tr>`
   - TO: `<tr><td class="sym">Final texture</td><td>Mounds and holds a soft trail, bright white</td></tr>`
3. **Method step 5 Check (page 2 ol.steps)**
   - _why:_ #3 of 3 'stiff peaks' fixes. The doneness cue in the method must match honest texture — a soft trail/mound off the spatula, not a stiff peak.
   - FROM: `<li><b>Check:</b> it should <b>hold stiff peaks, bright white</b>. Too thick &rarr; add ice water; processor warm &rarr; pause and let it cool.</li>`
   - TO: `<li><b>Check:</b> it should <b>mound and hold a soft trail, bright white</b>. Too thick &rarr; add ice water; processor warm &rarr; pause and let it cool.</li>`
4. **Ingredients callout — soften the absolute 'non-negotiable' claim to an honest mechanism statement**
   - _why:_ Minor honesty tweak in scope. 1:4 is a reliable working ratio but toum tolerates a range (sources run leaner and richer); 'non-negotiable' is stated as absolute fact when the real failure mode is oil ADDED too fast, not the ratio itself. 'Safe target' keeps the guidance without the false absolute, and the clause now correctly names the actual break cause (rate, not ratio).
   - FROM: `so the <b>1 : 4 garlic-to-oil ratio (by weight)</b> is non-negotiable: too much oil too fast and it breaks.`
   - TO: `so the <b>1 : 4 garlic-to-oil ratio (by weight)</b> is the safe target: add the oil too fast and it breaks.`

**Research notes:**
- Locked direction executed: 3 'stiff peaks' instances replaced with honest toum language ('mounds and holds a soft trail'). Located at line 77 (.sub), line 106 (Quality Targets table), line 124 (Method step 5).
- Texture research: toum has the consistency of thick mayonnaise and holds SOFT peaks, not stiff/rigid peaks. Multiple recipe authorities (Alphafoodie, Maureen Abood, The Mediterranean Dish) describe soft peaks / fluffy thick-mayo texture. Confirms 'stiff peaks' was an overclaim borrowed from meringue language.
- Minor honesty tweak (in-scope 'claims stated as fact'): changed the ingredients callout's '1:4 ratio is non-negotiable' to '1:4 ratio is the safe target' and re-pointed the break cause to oil added too fast (the actual mechanism) rather than the ratio. Toum tolerates a ratio range; the absolute claim was false-as-stated.
- No numbers changed — all gram weights, ratios, salt, scaling, and version stamp (v1.0) untouched. Edits are pure-text honesty corrections, so no rebuild math impact. Recipe should still PASS build.py (no new entities introduced via sed; all via Edit/Write per house rule).
- Sodium/balance not affected: salt 6 g into ~500 g batch is unchanged.
- No bare tsp/tbsp introduced; all new text is descriptive. Span balance unaffected (no <span> tags added or removed in any edit).

**Sources:** https://www.alphafoodie.com/lebanese-garlic-sauce/ · https://maureenabood.com/toum-lebanese-garlic-sauce/ · https://www.themediterraneandish.com/toum-garlic-sauce-recipe/ · https://feelgoodfoodie.net/recipe/lebanese-garlic-sauce/

---
