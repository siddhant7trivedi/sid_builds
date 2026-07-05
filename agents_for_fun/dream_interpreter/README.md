# Dream Interpreter Agent 🌙

**An AI agent that interprets your dreams through a Jungian + modern psychology lens — running fully local.**

---

## What It Does

1. User types in a dream description.
2. Agent analyzes it through two lenses in one response:
   - **Jungian lens** — archetypes present, shadow elements, individuation themes.
   - **Modern psychology lens** — emotional processing, cognitive framing (what the dream content might reflect about waking-life stress, unresolved thoughts, etc.).
3. Output uses reflective, non-diagnostic language throughout — this is interpretive, not clinical.

No pattern tracking, no history, no persistence in v1 — single dream in, single analysis out, session ends.

---

## Why I Built This

Most people, including me, have wondered at some point what their dreams actually mean — and that's exactly where this idea came from: not *in* a dream, but while I was wide awake, thinking about what to build next.

It's also the first agent in my collection running on a local model (`llama3.1:8b` via Ollama) instead of the Claude API. Every other agent in Agents for Fun and `sid_builds` runs on Claude — I wanted a deliberate, low-stakes build to prove out local-model integration: no API key, no per-call cost, fully offline once Ollama is running.

The dream-interpretation framing is the hook — the real build goal underneath it is the local-model pattern.

---

## Tech Stack

- **Language:** Python
- **UI:** Streamlit
- **LLM:** `llama3.1:8b` via Ollama (local, no API key required)
- **Architecture:** `agent.py` (prompt construction, Ollama call, response parsing) separated from `app.py` (UI) — same separation pattern as other agents in the collection, model backend swapped out.

---

## Getting Started

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com) installed locally
- `llama3.1:8b` pulled via Ollama:
  ```bash
  ollama pull llama3.1:8b
  ```
- Ollama running locally (`ollama serve`, or it runs automatically after install on most setups)

### Installation

```bash
cd dream_interpreter
pip install -r requirements.txt
streamlit run app.py
```

No `.env` or API key needed — this agent runs fully local via Ollama.

### Folder Structure

```
dream_interpreter/
├── agent.py           # Prompt construction, Ollama API call, response parsing
├── app.py             # Streamlit UI: dream input, two-section output
├── requirements.txt   # Dependencies
└── README.md
```

---

Part of `sid_builds`
This project is part of my AI agent portfolio at `siddhant7trivedi/sid_builds` — a collection of production-grade AI tools built for real PM and engineering workflows.
