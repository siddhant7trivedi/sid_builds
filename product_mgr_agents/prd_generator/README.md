# 📋 PRD Generator

Transform a raw product idea into a structured, implementation-ready Product Requirements Document — in minutes. Runs fully locally using **Llama 3.1 via Ollama**. No API keys. No cloud calls. No cost.

Built for Product Managers, founders, and builders who need to move fast from idea → documentation.

---

## What It Generates

From a single idea input, the tool produces a complete PRD with:

| Section | Description |
|---|---|
| Problem Statement | What pain exists, for whom, and why now |
| Objectives | 3–5 measurable goals |
| Target Users | Primary and secondary users with context |
| User Personas | 2 detailed personas with goals and pain points |
| User Stories | 5–8 stories in standard format |
| Functional Requirements | Numbered, grouped system requirements |
| Non-Functional Requirements | Performance, security, scalability constraints |
| Acceptance Criteria | Pass/fail criteria engineers can test |
| Assumptions & Dependencies | Stated assumptions and external dependencies |
| Risks & Mitigations | Top risks with likelihood, impact, mitigation |
| Success Metrics | Quantifiable KPIs with baselines and targets |
| MVP Scope | What's in v1, out of scope, and what's v2 |

Output is downloadable as `.md` or `.txt`.

---

## Tech Stack

- **Python** — core language
- **Streamlit** — UI framework
- **Ollama** — local LLM inference runtime
- **Llama 3.1** — the model doing the heavy lifting

---

## Setup

### Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com) installed

### Installation

```bash
# Clone the repo
git clone https://github.com/siddhant7trivedi/sid_builds.git
cd sid_builds/product_mgr_agents/prd_generator

# Install dependencies
pip install -r requirements.txt

# Pull the model (one-time, ~4.7GB)
ollama pull llama3.1
```

### Run

```bash
# Terminal 1 — start Ollama
ollama serve

# Terminal 2 — launch the app
streamlit run prd_generator.py
```

Open `http://localhost:8501` in your browser.

---

## Usage

1. Describe your product or feature idea in the text box (rough is fine)
2. Click **Generate PRD**
3. Wait ~30–60 seconds for Llama 3.1 to generate the full document
4. Download as Markdown or plain text

**Tip:** More context in your idea = better output. Include target users, the core problem, and any constraints you already know.

---

## Project Structure

```
prd_generator/
├── prd_generator.py   # App — UI + Ollama integration + prompt
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

---

## Part of `sid_builds`

This project is part of my AI agent portfolio at [`siddhant7trivedi/sid_builds`](https://github.com/siddhant7trivedi/sid_builds) — a collection of production-grade AI tools built for real PM and engineering workflows.

Other tools in the portfolio:
- Requirements Gap Analyzer
- Acceptance Criteria Generator
- Meeting Intelligence Agent
- Resume-to-Job Match Analyzer

---

## License

MIT
