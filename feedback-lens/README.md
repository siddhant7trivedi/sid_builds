# FeedbackLens

> Turn a wall of raw user feedback into a PM-ready briefing in seconds.

Built for product managers who don't have time to read 200 NPS responses manually. Paste in any raw feedback — reviews, survey responses, support tickets — and get back a structured analysis you can act on immediately.

![Next.js](https://img.shields.io/badge/Next.js-15-black) ![Claude](https://img.shields.io/badge/Claude-Sonnet%204.6-orange) ![License](https://img.shields.io/badge/license-MIT-blue)

---

## What it does

Paste raw feedback → hit Analyze → get back in under 10 seconds:

- **Sentiment** — positive, mixed, or negative with a one-line explanation
- **Top themes** — recurring patterns ranked by frequency, each expandable with supporting detail
- **Stakeholder summary** — 3–4 sentences you can drop straight into a Slack update or exec briefing
- **Standout quotes** — the 3 responses most worth sharing with your team

No charts. No dashboards. No accounts. Just signal.

---

## Why I built this

Qualitative feedback is the most underused asset in most PM workflows. It piles up in Notion docs and spreadsheets while teams make decisions without it — not because they don't care, but because synthesizing it manually takes hours.

FeedbackLens is a scratchpad tool that removes that friction. It's designed to be used before a planning meeting, not as a platform you maintain.

---

## Setup

**1. Clone and install**

```bash
git clone https://github.com/siddhant7trivedi/sid_builds
cd feedback-lens
npm install
```

**2. Add your Anthropic API key**

```bash
cp .env.local.example .env.local
```

Open `.env.local` and add your key from [console.anthropic.com](https://console.anthropic.com):

```
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

**3. Run**

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

---

## Usage

Paste any raw feedback into the box — one review per paragraph, numbered lists, mixed formats. Hit **Analyze feedback** or `⌘ + Enter`.

Click any theme row to expand it and see the reasoning behind it.

A batch of 20 responses typically returns results in 5–8 seconds.

---

## Cost

Each analysis uses the Claude API via your own key. A typical batch of 20–50 responses costs **$0.01–0.03**. The tool itself is free.

---

## Stack

- [Next.js 15](https://nextjs.org) — App Router
- [Tailwind CSS v4](https://tailwindcss.com)
- [Anthropic SDK](https://github.com/anthropics/anthropic-sdk-typescript) — Claude Sonnet 4.6

---

## Part of sid_builds

This is one project in a hands-on portfolio of AI product tools built to learn by doing — not just studying.

[View the full repo →](https://github.com/siddhant7trivedi/sid_builds)
