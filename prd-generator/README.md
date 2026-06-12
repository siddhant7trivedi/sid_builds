# PRD Generator

A web app that transforms a rough feature idea into a structured PRD draft using Claude AI.

## Stack

- React + Vite
- Tailwind CSS
- Anthropic JS SDK (`claude-sonnet-4-6`)

## Getting started

### 1. Install dependencies

```bash
npm install
```

### 2. Set up your API key

```bash
cp .env.example .env
```

Open `.env` and add your Anthropic API key:

```
VITE_ANTHROPIC_API_KEY=your_key_here
```

Get your key at: https://console.anthropic.com

### 3. Run locally

```bash
npm run dev
```

App runs at `http://localhost:5173`

## Project structure

```
src/
├── App.jsx                     # Root component, API call logic
├── components/
│   ├── InputPanel.jsx          # Left panel — textarea + generate button
│   ├── OutputPanel.jsx         # Right panel — streamed PRD output
│   └── ExampleChips.jsx        # Prefill buttons for example inputs
├── constants/
│   └── systemPrompt.js         # Claude system prompt + example inputs
└── main.jsx                    # React entry point
```

## How it works

1. User inputs a rough feature idea
2. App sends it to Claude with a strict PM system prompt
3. Claude streams back a structured PRD with: Problem Statement, Goals & Metrics, User Stories, Functional Requirements, Out of Scope, and Open Questions
4. User copies the output

## Roadmap

- [ ] v1.1 — Save history to local storage
- [ ] v1.2 — Export to `.md` file
- [ ] v1.3 — Multi-turn refinement
- [ ] v2.0 — Export to `.docx`, deploy to Vercel
