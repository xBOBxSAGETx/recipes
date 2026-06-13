# HANDOFF — read me first

Context bridge so a new Claude Code session (or future-you) can pick up without loss.
Last updated: 2026-06-13.

## 🎯 THE GOAL (north star)
A **seamless workflow: Claude app on the phone → laptop → GitHub as the landing zone.**
- **Phone (capture + drive):** snap/read a recipe in the Claude iOS app; issue
  instructions from anywhere.
- **Laptop (engine):** runs the real work — `build.py` + Chromium render and validate
  the PDF. Reached from the phone via Claude Code **Remote Control**.
- **GitHub (landing zone / source of truth):** every recipe (HTML) and its validated
  PDF live here. The phone reads PDFs back from `pdfs/` via the GitHub mobile app.

The point: capture a recipe on the phone, have the laptop convert/critique/upgrade it
into a normalized, validated PDF, and land everything in GitHub — with the phone able
to both kick off the work and retrieve the finished PDF. No copy-paste babysitting,
laptop-independent storage, one durable home.

Everything below is in service of that loop. As of 2026-06-13 the phone↔laptop link
(Remote Control) is **paired and working** — see the SOLVED section.

## What this repo is
Aguillon House Kitchen — single-source HTML recipes in `recipes/`, rendered to
validated print PDFs by `build.py`. Design system = `template.html`. Rulebook =
`LESSONS.md`. Conventions for agents = `CLAUDE.md`. GitHub:
`https://github.com/xBOBxSAGETx/recipes` (PRIVATE).

## ✅ SOLVED (2026-06-13) — Remote Control is paired

`/rc` works. The iPhone can now drive this repo. Here's the REAL root cause, because
the earlier diagnosis was incomplete and cost an hour.

**The actual bug:** the saved credential
(`~/.claude/.credentials.json`) was created by `claude setup-token`, NOT a browser
login. Tell-tale signs:
- `scopes: ["user:inference"]` — the only scope; Remote Control requires
  `user:sessions:claude_code`, which it lacked.
- `expiresAt` was exactly **1 year** out — the signature of a long-lived setup-token.

**Why every `claude auth login` silently failed:** because the file made
`claude auth status` report `loggedIn: true`, the login flow **short-circuited and
never overwrote the credential** (its mtime stayed pinned to the day it was created).
`auth status` reads `subscriptionType`/`authMethod` (which looked healthy: "max",
"claude.ai") — it does NOT surface `scopes`, so it masked the problem. The
`ANTHROPIC_API_KEY`-in-the-env theory was a red herring; the process env was already
clean.

**The fix that worked:**
1. Verified live state instead of trusting `auth status`: read
   `~/.claude/.credentials.json` directly and saw `scopes: ["user:inference"]` + the
   1-year expiry + a stale mtime.
2. Backed it up, then **moved the stale credential file aside** so the CLI could not
   short-circuit.
3. Ran `/login` (browser) — which, with no file to short-circuit on, did a genuine
   fresh login and minted a full-scope token.
4. Validated the NEW `~/.claude/.credentials.json`: scopes now include
   `user:sessions:claude_code` and the token is short-lived (~8 h) = real OAuth.
5. `/rc` → QR → paired. ✅

**If it ever regresses:** don't trust `claude auth status`. Read
`~/.claude/.credentials.json` and check the `scopes` array. If it's only
`user:inference` (or `expiresAt` is ~1 year out), it's a setup-token — move the file
aside and re-run `/login` to force a real browser login. Archival copy of the broken
token: `~/.claude/backups/.credentials.inference-only.may29.json`.

## ✅ DONE THIS SESSION (all committed + pushed to main)
- Repo created from `aguillon-kitchen.zip`, `git init`, pushed to GitHub.
- Toolchain installed/verified: playwright + pypdf + pymupdf + Chromium. NOTE the CLI
  isn't on PATH — use `python -m playwright install chromium`, not bare `playwright`.
- Fixed page-2 footer overflow on `molasses-cookies` and `nyc-bagels-bulk`. All 7
  recipes PASS `python build.py`.
- Added `CLAUDE.md` (agent conventions) and this handoff.
- **Phone PDF delivery:** `build.py` now auto-copies every PASSING PDF to a
  git-tracked `pdfs/` folder → view in the GitHub mobile app, Save to Files. All 7
  are pushed.
- Set the GitHub repo description.

## The intended end-to-end loop (once Remote Control is paired)
1. iPhone Claude app reads a recipe photo → text.
2. Phone drives the Remote Control session: *"convert this into a recipe HTML in the
   house style, build until it passes, commit and push."* (laptop must be awake +
   session running).
3. GitHub mobile app → `pdfs/` → tap the PDF → Save to Files.
Critiques/upgrades are the same shape: *"review the curry's method, tighten it,
rebuild, push."*

## Key facts / decisions
- Account uses **Claude Max ($100) only** — no API key, no pay-per-token.
- PDFs are build outputs: `dist/` is the gitignored working dir; `pdfs/` is the
  git-tracked phone-facing copy (only PASSING PDFs land there).
- Claude Code version 2.1.177 (native install at `~/.local/bin/claude`, NOT npm — do
  not `npm i -g`, it'd make a conflicting copy). Remote Control needs ≥2.1.52. ✅
- Cloud option (claude.ai/code) was considered but rejected: a fresh cloud sandbox
  lacks the local Playwright/Chromium toolchain, so the build gate wouldn't "just
  work." Remote Control keeps the build on the laptop where the toolchain lives.
- Claude Cowork / Dispatch was considered: desktop-only, no GitHub, not the build
  engine — wrong fit. Remote Control is the right tool.

## After Remote Control works — open follow-ups (optional)
- Add a `--prune` to `build.py` to drop orphaned PDFs in `pdfs/` when a recipe is
  deleted (currently it only adds/updates, never removes).
- Record the auth gotcha permanently in `CLAUDE.md` once confirmed working.
