# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the app

Ollama must be running before launching the app:

```bash
ollama serve           # keep this running in a separate terminal
ollama pull llama3     # one-time; mistral and phi3 also work
streamlit run app.py
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Environment config (optional — all values have defaults):

```bash
cp .env.example .env
# OLLAMA_BASE_URL defaults to http://localhost:11434
# OLLAMA_MODEL defaults to llama3
```

## Architecture

The pipeline runs in four sequential steps on every "Analyze Match" click:

```
PDF/DOCX upload  ──▶  backend/parser.py   ──▶  resume_text (str)
URL or paste     ──▶  backend/scraper.py  ──▶  jd_text (str)
                                                      │
                                          backend/matcher.py
                                          (ATS keyword pre-scan — no LLM)
                                                      │
                                       backend/ollama_client.py
                                       (LLM deep analysis via Ollama REST)
                                                      │
                                              app.py renders results
```

**Two-phase scoring:** `matcher.py` runs first and is pure Python (no LLM). It checks both texts against `_KEYWORD_TAXONOMY` (70+ terms) plus uppercase acronyms extracted from the JD. This pre-scan result is injected directly into the Ollama prompt so the LLM doesn't have to re-derive keyword overlap — it focuses on semantic fit, experience alignment, and suggestions.

**Ollama integration** (`ollama_client.py`): uses `/api/generate` with `format: "json"` and `temperature: 0.1`. The model is told to return a specific JSON schema (fit_score, score_breakdown, strengths, gaps, improvement_suggestions, ats_tips, summary). If the response isn't valid JSON, a regex fallback extracts the first `{...}` block. Input is hard-truncated: resume to 4000 chars, JD to 2500 chars.

**PDF parsing** (`parser.py`): tries PyMuPDF (`fitz`) first; falls back to `pdfplumber` if PyMuPDF returns empty text. DOCX parsing also extracts table cell content (joined with ` | `), which catches skills tables common in resumes.

**JD scraping** (`scraper.py`): tries 9 platform-specific CSS selectors in order (LinkedIn, Indeed, generic) before falling back to `<main>` / `<article>` / `<body>`. Uses a browser-like User-Agent to avoid 403s.

**`app.py`** is a single-file Streamlit app with no page routing. All state is ephemeral — there is no session persistence between runs. The "Analyze" button is disabled at the UI level when `check_ollama_connection()` returns `False`.

## Extending the keyword taxonomy

Add terms to `_KEYWORD_TAXONOMY` in `backend/matcher.py`. Terms are matched via case-insensitive substring, so multi-word entries like `"machine learning"` work. Capitalized acronyms in the JD (2–6 uppercase letters) are extracted automatically via regex and don't need to be in the taxonomy.

## Modifying the LLM prompt

The full prompt template is `_PROMPT_TEMPLATE` in `backend/ollama_client.py`. The JSON schema is embedded in the prompt — if you add or rename fields in the schema, update the result-rendering code in `app.py` accordingly (the tabs read keys like `result.get("strengths")`, `result.get("gaps")`, etc.).

## Adding new JD scraping targets

Add a new dict to `_JD_SELECTORS` in `backend/scraper.py`. Entries are tried in order; first match wins. Supports any BeautifulSoup `find(attrs=...)` selector (class, id, itemprop, data attributes).
