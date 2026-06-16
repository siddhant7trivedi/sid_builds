# Experiment Design Document
**Experiment Name:** [Short, descriptive name]
**Product / Feature:** [Name]
**Date Created:** [YYYY-MM-DD]
**Owner:** [PM Name]
**Data/Analytics Owner:** [Name]
**Status:** [Designing / Running / Analyzing / Complete]

---

## 1. Hypothesis

> "We believe that **[change/treatment]** will cause **[primary metric]** to **[increase/decrease]** because **[rationale based on user insight or data]**. We'll know we're right if **[specific measurable outcome]** within **[time period]**."

**Linked to:** [OKR / Strategic Bet / PRD]

---

## 2. Background & Motivation

[2–3 sentences on why we're running this experiment. What problem, insight, or customer signal prompted this?]

---

## 3. Experiment Design

| Field | Detail |
|-------|--------|
| Experiment Type | [A/B / Multivariate / Holdout / Prompt Experiment] |
| Control | [Description of control state] |
| Treatment(s) | [Description of treatment(s)] |
| Randomization Unit | [User / Session / Device / Account] |
| Traffic Split | [e.g., 50% Control / 50% Treatment] |
| Targeted Segment | [e.g., All new users / SMB segment / US only] |
| Feature Flag / System | [e.g., LaunchDarkly, internal flag system] |

---

## 4. Metrics

### Primary Metric
| Metric | Baseline | Minimum Detectable Effect (MDE) | Direction |
|--------|---------|--------------------------------|-----------|
| [e.g., Task completion rate] | [X%] | [+5 percentage points] | ↑ Increase |

### Secondary Metrics
| Metric | Baseline | Expected Direction | Rationale |
|--------|---------|-------------------|-----------|
| [e.g., Time on task] | | ↓ Decrease | [Faster if UX improves] |
| [e.g., D7 retention] | | ↑ Increase | [Better first experience = return] |

### Guardrail Metrics (must NOT degrade)
| Metric | Current | Floor / Ceiling | Alert Threshold |
|--------|---------|-----------------|-----------------|
| [e.g., Error rate] | | <1% | >1.5% triggers review |
| [e.g., P95 latency] | | <3s | >4s triggers review |

---

## 5. Sample Size & Duration

| Field | Value |
|-------|-------|
| Statistical Significance Level (α) | 0.05 |
| Statistical Power (1-β) | 0.80 |
| Baseline conversion / metric value | [X%] |
| Minimum Detectable Effect | [Y%] |
| Required sample per variant | [Calculated: N] |
| Current daily eligible users | [Z] |
| **Estimated test duration** | **[X days / weeks]** |
| **Planned start date** | |
| **Planned end date** | |

> ⚠️ Do not end the experiment early based on interim results.

---

## 6. Pre-Registered Success Criteria

> The experiment is a **win** if:
> - [Primary metric] increases by ≥[MDE] with p < 0.05
> - No guardrail metric drops below its floor

> The experiment is a **loss** if:
> - [Primary metric] does not improve at p < 0.05 after full duration

> The experiment is **inconclusive** if:
> - Sample size wasn't reached, or there's a sample ratio mismatch

---

## 7. Implementation Notes

| Item | Detail |
|------|--------|
| Exposure logging event | [Event name — must be fired at exposure, not conversion] |
| Engineering owner | |
| QA checklist completed? | |
| Analytics tracking verified? | |

---

## 8. Risks & Mitigations

| Risk | Probability | Mitigation |
|------|-------------|------------|
| [e.g., Novelty effect inflates treatment] | Medium | [Run for 2+ full weeks] |
| [e.g., SRM due to caching] | Low | [Monitor SRM metric daily] |
| [e.g., Interference between experiments] | Medium | [Check experiment collision log] |

---

## 9. Monitoring During Experiment

| Check | Frequency | Who |
|-------|-----------|-----|
| SRM (sample ratio mismatch) | Daily | Analytics |
| Guardrail metrics | Daily | PM |
| Exposure count on track | Daily | Analytics |
| Any anomalies / bugs | Daily | Eng |

---

## 10. Results & Readout *(filled post-experiment)*

**Experiment End Date:** [YYYY-MM-DD]
**Actual Runtime:** [X days]
**Total Sample (Control / Treatment):** [N / N]

### Primary Metric Results
| Metric | Control | Treatment | Lift | p-value | Significant? |
|--------|---------|-----------|------|---------|-------------|
| | | | | | |

### Secondary Metric Results
| Metric | Control | Treatment | Direction | Notes |
|--------|---------|-----------|-----------|-------|
| | | | | |

### Guardrail Metric Results
| Metric | Control | Treatment | Status |
|--------|---------|-----------|--------|
| | | | ✅ OK / ⚠️ Degraded |

### Segment Analysis
| Segment | Result | Insight |
|---------|--------|---------|
| [e.g., New users] | | |
| [e.g., Mobile] | | |

---

## 11. Decision & Learnings

**Decision:** [✅ Ship / ❌ Don't ship / 🔄 Iterate / 🔬 Retest]

**Rationale:** [2–3 sentences]

**Key Learning:** [What did we learn about users / product / market?]

**Follow-up experiments or actions:**
1. 
2. 

---

## Appendix
*(Statistical output, raw data, dashboards)*
