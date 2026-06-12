# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
npm install       # install dependencies
npm run dev       # start dev server at http://localhost:5173
npm run build     # production build
npm run preview   # preview production build locally
```

No test suite or linter is configured.

## Environment

Copy `.env.example` to `.env` and set `VITE_GITHUB_TOKEN` to a GitHub personal access token with **Models: Read-only** permission. The token is used client-side via `dangerouslyAllowBrowser: true` — fine for local dev, not for production.

## Architecture

The entire app is a single-page React + Vite app with no backend. All AI calls are made directly from the browser.

**Data flow:** `App.jsx` owns all state (`input`, `output`, `isLoading`). On generate, it calls the GitHub Models API (OpenAI-compatible endpoint at `https://models.inference.ai.azure.com`) using the `openai` SDK, streaming the response chunk-by-chunk into `output`. The model is `gpt-4o`.

**Key constraint:** The system prompt in `src/constants/systemPrompt.js` is the core product logic — it enforces the PRD structure, word limit (~600 words), and output format. Changes here directly affect output quality.

**Output rendering:** `OutputPanel.jsx` renders the streamed markdown via `react-markdown` with `@tailwindcss/typography` prose styles. PDF export uses `html2pdf.js` loaded lazily on demand.

## Switching AI provider

To switch from GitHub Models to Anthropic directly, replace the `OpenAI` client in `App.jsx` with `@anthropic-ai/sdk`, change the env var to `VITE_ANTHROPIC_API_KEY`, and update the streaming loop to use `client.messages.stream()` with `content_block_delta` events. The system prompt needs no changes.
