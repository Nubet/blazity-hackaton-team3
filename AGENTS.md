# Project AI Instructions

## What this repo is

`blazity-hackaton` — a hackathon project building an AI-powered content
repurposing web app: the user provides raw materials, picks a target platform
(LinkedIn, TikTok, YouTube, …), and the app generates a finished, platform-
tailored post to copy and publish. Today it is still a scaffold — only README,
LICENSE, and the Atlas AI workspace under `.ai/` exist; there is no application
code yet. See `.ai/memory/` for stable context.

## Structure

- `.ai/` — Atlas AI workspace. `.ai/config.json` is the source of truth for
  artifact locations (memory, vocabulary, plans, research, decisions, results).
- `AGENTS.md` / `CLAUDE.md` — agent instructions; `CLAUDE.md` imports this file.
- `.agents/`, `.claude/`, `.cursor/` — generated agent surfaces.

## Working rules

- Stack: Next.js (App Router) + TypeScript, Tailwind + shadcn/ui, Anthropic
  Claude via `@anthropic-ai/sdk`, no CMS. See `.ai/memory/stack.md` for detail.
- No application code exists yet — there is no `package.json`. Scaffold the app
  before assuming build/test commands work; the expected ones live in
  `.ai/memory/stack.md`.
- Run Claude calls server-side only (route handlers / Server Actions); never
  expose the API key to the client. Default to the latest Claude models.
- Workflow: GitHub flow — feature branches with Conventional Commits.
- Code convention: no code comments (see `.ai/memory/stack.md`).
- Atlas health check: `npx --yes @blazity-atlas/core@latest doctor`.
- Do not edit the `<!-- BEGIN/END ATLAS -->` managed block below by hand.
- Keep durable docs depersonalized (see Atlas Documentation Rules below).

<!-- BEGIN ATLAS: artifact-paths -->
## Atlas Artifact Paths

`.ai/config.json` is the source of truth for AI artifact locations in this repository.
Before writing plans, research, decisions, ADRs, results, memory, vocabulary, or skill outputs, resolve the destination through `artifactRoot`, `paths`, and `pathAliases`.
If an imported skill, template, or instruction mentions a different path, map it through `.ai/config.json` before reading or writing files.
Do not create new documentation roots unless `.ai/config.json` explicitly allows them.

## Atlas Documentation Rules

Durable documentation records needs, decisions, and reasons — never individuals or internal process.
Write "memory was needed to persist context across runs", not "<name> wanted memory".
Keep personal names, private schedules, internal-only references, and absolute local paths out of workspace artifacts.
<!-- END ATLAS: artifact-paths -->
