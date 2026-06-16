# FeedbackLens

Paste a batch of raw customer feedback — NPS responses, G2 reviews, Capterra comments — and get back:

- **Overall sentiment** (positive / mixed / negative)
- **Top 5 recurring themes** with supporting quotes (expandable)
- **A stakeholder-ready summary** you can drop straight into an update
- **Standout quotes** worth sharing with the team

Built for product managers who need signal from feedback fast. No charts, no dashboards, no accounts.

## Setup

**1. Clone the repo**

```bash
git clone <repo-url>
cd feedback-lens
npm install
```

**2. Add your Anthropic API key**

```bash
cp .env.local.example .env.local
```

Open `.env.local` and replace `sk-ant-...` with your key from [console.anthropic.com](https://console.anthropic.com).

**3. Run it**

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Usage

Paste any raw feedback text into the box — one review per paragraph, numbered lists, mixed formats, whatever you have. Hit **Analyze feedback** (or ⌘+Enter) and results appear in seconds.

Click any theme to expand it and see the quotes that back it up.

## Cost

Each analysis call uses the Claude API (Anthropic). A typical batch of 20–50 reviews costs around **$0.01–0.03**. You pay for your own usage via your API key — the tool itself is free.

## Stack

- [Next.js](https://nextjs.org) (App Router)
- [Tailwind CSS v4](https://tailwindcss.com)
- [Anthropic SDK](https://github.com/anthropics/anthropic-sdk-typescript) → Claude claude-sonnet-4-6
