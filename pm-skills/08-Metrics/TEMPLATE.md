# Product Metrics Framework
**Product:** [Name]
**Date:** [YYYY-MM-DD]
**Owner:** [PM Name]
**Review Cadence:** [Weekly / Monthly]

---

## 1. North Star Metric

| Field | Detail |
|-------|--------|
| **Metric Name** | [e.g., AI-assisted tasks completed per week] |
| **Why this metric** | [Why does it best capture value delivered to users?] |
| **Current Baseline** | [X] |
| **12-Month Target** | [Y] |
| **Owner** | |
| **Instrumented?** | [Yes / No / In Progress] |

---

## 2. OKRs

### Objective 1: [Inspirational goal]

| Key Result | Baseline | Target | Due Date | Owner |
|-----------|---------|--------|----------|-------|
| KR1: [Verb metric from X to Y] | | | | |
| KR2: | | | | |
| KR3: | | | | |

### Objective 2: [Inspirational goal]

| Key Result | Baseline | Target | Due Date | Owner |
|-----------|---------|--------|----------|-------|
| KR1: | | | | |
| KR2: | | | | |

---

## 3. AARRR Funnel Metrics

| Funnel Stage | Metric | Current | Target | Owner |
|-------------|--------|---------|--------|-------|
| **Acquisition** | [e.g., Organic sign-up rate] | | | |
| **Activation** | [e.g., % users completing onboarding in D1] | | | |
| **Retention** | [e.g., D30 retention rate] | | | |
| **Revenue** | [e.g., MRR / ARR] | | | |
| **Referral** | [e.g., NPS score] | | | |

---

## 4. Core Product KPIs

| Metric | Description | Current | Target | Frequency | Owner |
|--------|-------------|---------|--------|-----------|-------|
| [e.g., Weekly Active Users] | | | | Weekly | |
| [e.g., Time-to-first-value] | | | | | |
| [e.g., Feature adoption rate] | | | | | |
| [e.g., Task completion rate] | | | | | |
| [e.g., Session length] | | | | | |

---

## 5. AI / GenAI Quality Metrics *(if applicable)*

### Output Quality
| Metric | Description | Current | Threshold | Owner |
|--------|-------------|---------|-----------|-------|
| Precision | % AI outputs correct | | ≥X% | |
| Hallucination rate | % outputs with factual errors | | <X% | |
| Human override rate | % outputs user edited/rejected | | <X% | |
| Task completion rate | % AI tasks finished successfully | | ≥X% | |

### Reliability
| Metric | Current | Target | Owner |
|--------|---------|--------|-------|
| Latency P50 | | <Xs | |
| Latency P95 | | <Xs | |
| Error rate | | <X% | |
| Model fallback rate | | <X% | |

### Usage & Trust
| Metric | Current | Target | Owner |
|--------|---------|--------|-------|
| AI feature adoption | | X% MAU | |
| Regeneration rate | | <X% | |
| AI-assisted task ratio | | X% | |

---

## 6. Guardrail Metrics

> These must NOT degrade when optimizing for North Star or OKRs.

| Guardrail Metric | Current | Floor / Ceiling | Alert If |
|-----------------|---------|-----------------|---------|
| [e.g., D30 retention] | | Must stay ≥25% | Drops below 25% |
| [e.g., AI error rate] | | Must stay <3% | Exceeds 3% |
| [e.g., P95 latency] | | Must stay <5s | Exceeds 5s |
| [e.g., Support ticket volume] | | Must not 2× | Week-over-week 2× |

---

## 7. Feature / Initiative Metrics

*(For specific features or experiments)*

### Feature: [Name]

| Metric | Baseline | Target | Timeline | Owner |
|--------|---------|--------|----------|-------|
| Adoption (% MAU using it) | | X% in 30 days | | |
| Retention impact | | Improve D30 by Y% | | |
| Task success rate | | ≥X% | | |

---

## 8. Instrumentation Status

| Metric | Instrumented? | Tool / Platform | Notes |
|--------|--------------|-----------------|-------|
| | ✅ / ❌ / 🟡 In Progress | [e.g., Mixpanel, Amplitude, DataDog] | |

---

## 9. Dashboard Links

| Dashboard | Tool | Link | Owner |
|-----------|------|------|-------|
| Product KPI Dashboard | | | |
| AI Quality Dashboard | | | |
| Funnel / Conversion | | | |
| Experiment Results | | | |

---

## 10. Metrics Review Cadence

| Review | Frequency | Participants | Output |
|--------|-----------|-------------|--------|
| Weekly metrics sync | Weekly | PM, Eng, Data | Anomaly flags + action items |
| OKR check-in | Monthly | PM, Exec | Progress update |
| AI quality review | Weekly | PM, Eng, Data | Model health + regression check |
| Full metrics audit | Quarterly | PM, Data | Instrument gaps, retire stale metrics |
