# RoastMyExpenses 💸

**An AI agent that roasts your bank statement — and scolds you for next month.**

---

## Why I Built This

Everyone has that one spending category they lie to themselves about. I wanted an agent that skips the polite budgeting-app language ("consider reducing discretionary spend") and just says the quiet part loud — specific numbers, specific categories, no mercy.

---

## What It Does

1. User uploads a bank statement — CSV or PDF, single month or full year.
2. Agent extracts transactions, categorizes spend (food delivery, shopping, subscriptions, etc.), and aggregates totals per category.
3. Agent generates a **roast**: specific, savage callouts on the biggest spend categories ("₹14,000 on food delivery — your kitchen is decorative"), plus a closing "scolding" line telling the user what to fix next month.
4. Roast renders in the UI along with a simple category breakdown.

---

## How It Works

**Pipeline:**

1. **Ingest** — CSV via `pandas` (primary path). PDF via `pdfplumber` (best-effort — bank PDF layouts vary; a confidence warning is shown if extraction looks incomplete).

2. **Mask sensitive data** — Account numbers, IFSC codes, and card numbers are stripped/masked before any data leaves the parser. Applies to both CSV and PDF paths, no exceptions.

3. **Categorize programmatically** — Transaction descriptions are mapped to categories (Food Delivery, Groceries, Shopping, Subscriptions, Transport, etc.) using a keyword rules table. No LLM involved here — keeps it accurate and cheap.

4. **Aggregate** — `pandas groupby` sums spend per category.

5. **Roast** — Only the aggregated category totals (never raw transactions) go to Claude (`claude-opus-4-8`). The model streams back a savage, specific roast referencing real amounts and a single "Next Month's Challenge" line.

6. **UI** — Streamlit: horizontal bar chart, category table, and live-streaming roast output.

---

## Tech Stack

- **Language:** Python
- **UI:** Streamlit
- **LLM:** Claude API — `claude-opus-4-8` with streaming
- **Parsing:** `pandas` (CSV), `pdfplumber` (PDF, best-effort)
- **Architecture:** `parser.py` (ingestion + masking) → `agent.py` (categorization + Claude call) → `app.py` (UI)

---

## Getting Started

### Prerequisites

- Python 3.10+
- Anthropic API key

### Installation

```bash
git clone https://github.com/siddhant7trivedi/sid_builds.git
cd sid_builds/agents_for_fun/roast_my_expenses
pip install -r requirements.txt
cp .env.example .env   # add your ANTHROPIC_API_KEY
streamlit run app.py
```

### Folder Structure

```
roast_my_expenses/
├── parser.py          # CSV/PDF ingestion, transaction extraction, data masking
├── agent.py           # Categorization lookup, aggregation, Claude API call for the roast
├── app.py             # Streamlit UI: upload, category breakdown, roast output
├── requirements.txt   # Dependencies
├── .env.example       # ANTHROPIC_API_KEY placeholder
└── README.md
```

---

Part of `sid_builds` — a collection of production-grade AI tools built for real PM and engineering workflows.
