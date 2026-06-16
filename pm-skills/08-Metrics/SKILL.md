---
name: product-metrics
description: "Use this skill when defining, designing, or reviewing product metrics — including KPIs, OKRs, North Star metrics, guardrail metrics, and AI-specific quality metrics. Trigger when the user needs to instrument success, build a metrics framework, set OKRs, or debug a metric that isn't giving useful signal. Covers AARRR funnel, retention curves, and GenAI evaluation metrics."
---

# Product Metrics Skill

## Purpose
Build a metrics system that drives good product decisions — not just tracks activity.

---

## Core Principles

1. **One North Star** — Align the team on a single metric that best captures value delivered to users
2. **Input + output metrics** — Track leading indicators (inputs you control) + lagging outcomes
3. **Guardrail metrics** — Define what you must NOT hurt, not just what you want to improve
4. **Don't measure what you can't act on** — Every metric should trigger a decision
5. **AI quality metrics are first-class** — For GenAI products, model quality must be on the dashboard

---

## Metrics Hierarchy

```
North Star Metric (1)
    └── Level 1: Business Outcomes (revenue, retention, growth)
        └── Level 2: Product KPIs (activation, engagement, conversion)
            └── Level 3: Feature Metrics (adoption, task success, NPS)
                └── Level 4: Operational/Health Metrics (latency, error rate, uptime)
```

---

## AARRR Funnel Framework

| Stage | What It Measures | Example Metrics |
|-------|-----------------|-----------------|
| Acquisition | How users find you | CAC, channel attribution, sign-up rate |
| Activation | First value moment | Day 1/7 activation rate, time-to-first-value |
| Retention | Do they come back? | D7/D30/D90 retention, churn rate, NRR |
| Revenue | Monetization efficiency | ARR, MRR, ARPU, LTV:CAC |
| Referral | Do they bring others? | NPS, viral coefficient, referral rate |

---

## OKR Framework

### Objective (qualitative, inspirational)
> "What we want to achieve — directional, not measurable"

### Key Results (quantitative, time-bound)
> "How we'll know we achieved it — 2–5 per objective"

**Good KR format:**
> [Verb] [metric] from [baseline] to [target] by [date]

**Examples:**
- Increase D30 retention from 28% to 42% by Q3 end
- Reduce AI output error rate from 8% to <2% by June 30
- Achieve NPS ≥45 across SMB segment by Q4

---

## North Star Metric Selection

A good North Star:
- Captures value delivered to users (not just business value)
- Is a leading indicator of long-term retention / revenue
- Is actionable by the product team
- Can be broken into contributing sub-metrics

### Examples by product type
| Product Type | North Star Candidate |
|-------------|----------------------|
| B2B SaaS | Weekly Active Teams |
| AI assistant | AI-assisted tasks completed |
| Marketplace | Successful transactions per week |
| Media/content | Time spent on high-quality content |
| GenAI productivity | Hours saved per user per week |

---

## AI/GenAI-Specific Metrics

### Quality Metrics
| Metric | Description |
|--------|-------------|
| Precision | % of AI outputs that are correct |
| Recall | % of correct answers the AI surfaced |
| F1 Score | Harmonic mean of precision and recall |
| Hallucination rate | % of outputs containing factual errors |
| Task completion rate | % of AI-initiated tasks completed successfully |
| Human override rate | % of outputs users edited or rejected |

### Reliability Metrics
| Metric | Description |
|--------|-------------|
| Latency P50/P95/P99 | Response time distribution |
| Error rate | % of API calls returning errors |
| Timeout rate | % of calls exceeding time limit |
| Model fallback rate | % of calls rerouted to fallback model |

### Trust and Usage Metrics
| Metric | Description |
|--------|-------------|
| AI feature adoption | % of users using AI features |
| AI-assisted vs. manual ratio | How often users choose AI path |
| Regeneration rate | % of outputs user asked to regenerate |
| Confidence-to-accuracy correlation | Does your confidence score predict quality? |

---

## Guardrail Metrics

Define metrics that must NOT degrade when optimizing for the North Star:
- e.g., "Improving activation must not reduce D30 retention below 25%"
- e.g., "AI speed improvements must not increase hallucination rate above 3%"

---

## Common Metrics Mistakes

| Mistake | Fix |
|---------|-----|
| Vanity metrics (total signups, page views) | Replace with activation and retention |
| No guardrails | Add 2–3 must-not-harm metrics per experiment |
| Activity ≠ value (DAU without context) | Add quality signal (e.g., tasks completed) |
| AI metrics are all technical | Add user-facing quality signals (override rate, NPS) |
| Measuring too much | Cut to <10 KPIs that actually drive decisions |

---

## Quality Checks

- [ ] North Star metric defined and agreed upon
- [ ] AARRR funnel covered at minimum with 1 metric each
- [ ] OKRs are measurable with baseline and target
- [ ] Guardrail metrics defined
- [ ] AI quality metrics instrumented (if GenAI product)
- [ ] Every metric has an owner who can act on it
- [ ] Instrumentation plan exists for each metric
