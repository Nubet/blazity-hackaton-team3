# Stack

Decided for the build; no application code or `package.json` exists yet, so the
commands below are conventional expectations to apply once the app is scaffolded.

## Decided

- **Language:** TypeScript, strict typing. Avoid `any`; prefer interfaces and
  precise types.
- **Framework:** Next.js (App Router) with React Server Components by default and
  Server Actions for mutations.
- **Styling/UI:** Tailwind CSS + shadcn/ui.
- **AI:** Anthropic Claude via `@anthropic-ai/sdk`, called server-side only.
  Default to the latest Claude models (e.g. `claude-opus-4-8`,
  `claude-sonnet-4-6`).
- **Content store:** no CMS; custom DB or no persistence at MVP.

## Conventions

- No code comments — code should be self-explanatory through naming and structure.

## Known tooling

- Git for version control. Workflow: GitHub flow — feature branches, Conventional
  Commits.
- Atlas (`@blazity-atlas/core`) manages the AI workspace; check health with
  `npx --yes @blazity-atlas/core@latest doctor`.

## Expected commands (once scaffolded)

- `npm run dev` — local dev server
- `npm run build` — production build
- `npm run lint` — lint
- Tests: framework not chosen yet. With Vitest a single test runs as
  `npx vitest run <path>` (or `-t "<name>"`).

## Unknowns (confirm once chosen)

- Package manager (npm / pnpm / yarn)
- Testing framework
- Deployment target
