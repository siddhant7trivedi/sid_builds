# AI Job Hunter

An AI-powered multi-agent job discovery system. Three specialist agents search in parallel, then a Headhunter ranks and curates the top results into a single report.

---

## Team

| Agent | Type | Role |
|-------|------|------|
| Company Tracker | Research Agent | Discovers job openings from official career pages and the open market |
| Job Validator | Validation Agent | Verifies active listings, removes duplicates, filters relevant jobs |
| Insights Agent | Intelligence Agent | Extracts salary, skills, experience, work mode, and more |
| Headhunter | Ranking Agent | Scores and ranks the best opportunities, writes the final report |

---

## How to Run

1. Open `input.md` and fill in your search criteria
2. Launch the Job Hunter Director in this folder:
   ```bash
   claude
   ```
3. Paste your search parameters when prompted
4. The three reporter agents run in parallel, then the Headhunter ranks results
5. Final report is saved to `output/job_hunter.md`

---

## Search Inputs

| Field | Requirement |
|-------|-------------|
| Job Title | Required |
| Companies | Optional (max 3) — prioritizes official career pages when provided |
| Cities | Required (max 3) |
| Years of Experience | Optional |
| Posted Within | Required — `10 days` / `20 days` / `30 days` / `Above 30 days` |
| Top Results | Optional (default: 5) |

---

## Output

`output/job_hunter.md` contains the ranked top N jobs. For each job:

- Company & Job Title
- Location
- Years of Experience required
- Salary (if available)
- Required Skills
- Employment Type (Full-time / Part-time / Contract)
- Work Mode (Remote / Hybrid / On-site)
- Posted Date
- Direct Job URL
- Why this role was selected

---

## Structure

```
ai_job_hunter/
├── CLAUDE.md          # Job Hunter Director instructions
├── README.md          # This file
├── input.md           # Search criteria template
├── output/
│   └── job_hunter.md  # Generated report (overwritten each run)
└── agents/
    ├── company_tracker.md   # Research Agent definition
    ├── job_validator.md     # Validation Agent definition
    ├── insights_agent.md    # Intelligence Agent definition
    └── headhunter.md        # Ranking Agent definition
```

---

## Requirements

- Claude Code with agent teams enabled
- Add to `.claude/settings.local.json`:
  ```json
  {
    "env": {
      "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
    }
  }
  ```
