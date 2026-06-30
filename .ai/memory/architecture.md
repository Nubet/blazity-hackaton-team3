# Architecture

A Next.js (App Router) + TypeScript web app. No application code exists yet — the
repository is still a scaffold (README, LICENSE, and the Atlas workspace under
`.ai/`). The notes below are the intended shape, not implemented structure.

## Intended shape

- **Next.js App Router** with React Server Components by default; **Server
  Actions** for data mutations / triggering generation.
- **AI generation runs server-side only** (route handlers / Server Actions) via
  the Anthropic Claude SDK. The API key never reaches the client.
- **Per-platform tone adaptation** is the core domain logic: a data-driven
  mapping (prompt/profile per platform) shapes how materials become a post.
  Keep platform behavior data-driven rather than branched through call sites.
- **UI** with Tailwind CSS + shadcn/ui — primarily an input area for materials
  and an output card with a "copy to clipboard" action.
- **No CMS**; custom DB or no persistence (transient/in-session at MVP). A Sanity
  MCP server is present in some agent environments but is not used here.

## Current layout

- `.ai/` — Atlas AI workspace (config, memory, vocabulary, plans, research,
  decisions, results, skills). `.ai/config.json` is the source of truth for
  artifact locations.
- `AGENTS.md` / `CLAUDE.md` — agent instructions.
- `.agents/`, `.claude/`, `.cursor/` — agent surfaces. On Windows the per-surface
  `skills` entries are plain-file placeholders (symlink fallback), not symlinks.

## Unknowns (confirm as build progresses)

- Persistence choice (if any) and how materials/posts are stored
- Deployment target and runtime
- How uploaded materials are parsed/normalized before generation
