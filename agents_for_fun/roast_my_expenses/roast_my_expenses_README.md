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

**Pipeline — do not skip steps or push categorization into the LLM prompt:**

1. **Ingest**
   - CSV: parse directly with `pandas`. This is the reliable path — treat it as the primary supported format.
   - PDF: extract tables with `pdfplumber` (or `camelot` as fallback). This is **best-effort** — bank statement PDF layouts vary widely and extraction quality will degrade on non-standard formats. Surface a confidence/warning message in the UI if extraction looks incomplete (e.g., very few rows found, or columns don't match expected transaction shape). Do not attempt to build bank-specific parsers for v1.

2. **Mask sensitive data**
   - Before any transaction data is sent to the LLM, strip/mask account numbers, IFSC codes, card numbers, and any other identifying account info. This applies to both CSV and PDF paths, no exceptions.

3. **Categorize — programmatically, not via LLM**
   - Map transaction descriptions to categories using a rules/keyword lookup table (e.g., "SWIGGY", "ZOMATO" → Food Delivery; "AMZN", "FLIPKART" → Shopping). This keeps categorization accurate and cheap — do not send raw transaction-by-transaction data to the LLM for classification.
   - Aggregate totals per category using `pandas groupby`.

4. **Roast — LLM call on the aggregated summary only**
   - Send the category totals (not raw transactions) to Claude with a prompt to generate a specific, witty roast per top category plus one closing scolding line for next month.
   - Roast tone: specific and savage, never generic. Must reference actual category names and amounts.

5. **Output UI**
   - Category breakdown (simple bar chart or table).
   - Roast text below/beside it.
   - If PDF extraction confidence was low, show a visible disclaimer.

---

## Tech Stack

- **Language:** Python
- **UI:** Streamlit
- **LLM:** Claude API (Anthropic)
- **Parsing:** `pandas` (CSV), `pdfplumber` (PDF, best-effort)
- **Architecture:** `agent.py` (categorization + Claude API logic) separated from `parser.py` (CSV/PDF ingestion) and `app.py` (UI) — parsing logic kept separate from agent logic so either can be improved independently.

---

## Getting Started

### Prerequisites

- Python 3.10+
- Anthropic API key

### Installation

```bash
git clone <repo-url>
cd roast_my_expenses
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
├── .env.example        # ANTHROPIC_API_KEY placeholder
└── README.md
```

---

Part of `sid_builds`
This project is part of my AI agent portfolio at `siddhant7trivedi/sid_builds` — a collection of production-grade AI tools built for real PM and engineering workflows.
