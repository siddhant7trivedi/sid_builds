# RoastIN 🔥

**An AI agent that roasts any LinkedIn post.**

---

## Why I Built This

LinkedIn is drowning in humble-brags, "I'm humbled to announce," and engagement-bait hooks that all sound the same. I wanted an agent that calls out exactly *why* a post is cringe — no softening, no fix, just the honest read.

This is part of my **Agents for Fun** collection — lower-stakes builds I use to practice patterns (tone-specific generation, prompt constraint) that don't fit the enterprise-PM framing of my main `sid_builds` portfolio.

---

## What It Does

1. User pastes any LinkedIn post (their own or someone else's) into the app.
2. Agent generates a **roast** — short, sharp, specific callouts on why the post is cringe: clichés used, humble-brag detected, hook that doesn't hook, buzzword count.
3. Roast renders in the UI. No rewrite, no fix, no corporate-safe version — just the takedown.

---

## Tech Stack

- **Language:** Python
- **UI:** Streamlit
- **LLM:** Claude API (Anthropic)
- **Architecture:** `agent.py` (prompt + API logic) separated from `app.py` (UI), consistent with the pattern used in FeedbackLens.

---

## Getting Started

### Prerequisites

- Python 3.10+
- Anthropic API key

### Installation

```bash
git clone <repo-url>
cd roastin
pip install -r requirements.txt
cp .env.example .env   # add your ANTHROPIC_API_KEY
streamlit run app.py
```

### Folder Structure

```
roastin/
├── agent.py          # Core agent logic: prompt construction, Claude API call, response parsing
├── app.py            # Streamlit UI: input box, single roast output panel
├── requirements.txt  # Dependencies
├── .env.example       # ANTHROPIC_API_KEY placeholder
└── README.md
```

---

Part of `sid_builds`
This project is part of my AI agent portfolio at `siddhant7trivedi/sid_builds` — a collection of production-grade AI tools built for real PM and engineering workflows.
