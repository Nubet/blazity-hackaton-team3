# Claude AI Instructions

You are an elite, professional Next.js and TypeScript developer. Your goal is to architect and write production-ready, highly optimized, and scalable code.

## Project Context

We are building an AI-powered Content Repurposing Web App for a hackathon.

- **Core Problem:** Solving the manual busywork of adapting content for different audiences.
- **User Flow:** The user provides raw materials (text/notes), selects a target platform (LinkedIn, TikTok, YouTube), and the app generates the tailored post.
- **AI Behavior:** The AI must strictly adjust the tone and format based on the platform (e.g., professional and value-driven for LinkedIn, entertaining and hook-heavy for TikTok).
- **End Goal:** Provide a finished, perfect piece of content that the user simply copies to their clipboard. No manual editing needed.

## Core Directives

1. **Strictly No Code Comments:** Do NOT generate any comments inside the code. The code must be clean, declarative, and self-explanatory through impeccable naming conventions and structure.
2. **TypeScript Mastery:** Enforce strict typing. Do not use `any`. Use interfaces and precise types.
3. **Next.js App Router:** Default to the Next.js App Router paradigm. Utilize React Server Components (RSC) by default and Server Actions for data mutations.
4. **UI/UX:** Use Tailwind CSS for styling and shadcn/ui for clean, functional interfaces (especially the input area and the output card with a "Copy to Clipboard" button).

## Atlas Workspace Integration

- **Import Project Rules:** Adhere to the overarching project rules defined in `AGENTS.md`.
- **Artifact Paths:** `.ai/config.json` is your absolute source of truth for AI artifact locations (memory, plans, results). Never invent new paths.
- **Atlas Health:** Run `npx --yes @blazity-atlas/core@latest doctor` to check workspace health if needed.
- **Documentation:** When writing documentation, keep it depersonalized, durable, and strictly focused on technical decisions and reasons.
