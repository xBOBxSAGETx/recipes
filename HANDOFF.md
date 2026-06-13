# HANDOFF — read me first

Context bridge so a new Claude Code session (or future-you) can pick up without loss.
Last updated: 2026-06-13.

## What this repo is
Aguillon House Kitchen — single-source HTML recipes in `recipes/`, rendered to
validated print PDFs by `build.py`. Design system = `template.html`. Rulebook =
`LESSONS.md`. Conventions for agents = `CLAUDE.md`. GitHub:
`https://github.com/xBOBxSAGETx/recipes` (PRIVATE).

## ⏳ WHERE WE LEFT OFF — the one open task: pair Remote Control

Goal: drive this repo from the iPhone via Claude Code **Remote Control** (laptop is
the engine that runs `build.py`; phone is the remote). `/rc` keeps failing with:

> "Remote Control requires a full-scope login token… run claude auth login"

**Root cause (diagnosed):** the saved login token is inference-only
(`scopes: ['user:inference']`, from `claude setup-token`). Remote Control needs the
full scopes a browser login grants. Re-login wasn't taking because
**`ANTHROPIC_API_KEY` was still set in already-open terminals**, and when that key is
in a process, `claude` uses the API key and ignores OAuth entirely — so
`claude auth login` ran but never updated the credential file.

**Already fixed:** `ANTHROPIC_API_KEY` removed from Windows **User** scope (user only
uses the Max plan, never the API key). `CLAUDE_CODE_OAUTH_TOKEN` confirmed not set
anywhere. So a BRAND-NEW terminal is now clean.

### ✅ DO THIS NEXT (in order)
1. Close ALL old PowerShell windows and Claude sessions (they still carry the API key
   in-process — that's what sabotaged every prior attempt).
2. Open ONE fresh PowerShell from the Start menu.
3. Prove it's clean — this MUST print a blank line:
   ```powershell
   echo $env:ANTHROPIC_API_KEY
   ```
   If it prints a key, that window is poisoned — close it, open another.
4. Re-auth and verify:
   ```powershell
   claude auth logout
   claude auth login          # finish browser sign-in with the MAX account
   claude auth status         # MUST now show MORE than just "user:inference"
   ```
5. Only if status looks right:
   ```powershell
   cd C:\Users\aagui\Recipes
   claude
   ```
   then type `/rc`, press SPACEBAR for the QR code.
6. iPhone: Claude app → Code tab → scan QR / tap the session. Paired = computer icon
   + green dot. (`/config` → "Enable Remote Control for all sessions" = automatic.)

The make-or-break check is **step 3**. Report what `claude auth status` prints after
login; if it's still only `user:inference`, the login issued a limited token again and
we dig further.

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
