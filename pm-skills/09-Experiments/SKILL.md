---
name: experiments
description: "Use this skill when designing, running, or analyzing product experiments — including A/B tests, feature flags, multivariate tests, holdout groups, and AI prompt experiments. Covers: hypothesis formation, sample size calculation, statistical significance, and experiment readout. Trigger when the user wants to test an assumption, validate a feature, or run a controlled experiment. Includes GenAI-specific experiment design."
---

# Experiments Skill

## Purpose
Design rigorous experiments that produce clear, actionable signals — not confirmation of what we already believe.

---

## Core Principles

1. **Hypothesis first** — Define what you expect to happen and why, before you start
2. **One variable at a time** — Isolate the variable being tested (in A/B; multivariate is different)
3. **Pre-register your success criteria** — Define "success" before seeing the data
4. **Statistical rigor** — Underpowered tests produce misleading results
5. **Novelty effects are real** — New features often see a temporary boost; run long enough

---

## Experiment Types

| Type | Best For | Complexity |
|------|----------|------------|
| A/B Test | Single variable, clear control | Low |
| Multivariate (MVT) | Multiple variables, need interaction data | High |
| Holdout Group | Measure long-term impact of a feature | Medium |
| Feature Flag Rollout | Gradual rollout + canary testing | Medium |
| Pre/Post Analysis | When A/B isn't possible | Medium (confounded) |
| AI Prompt Experiment | Test prompt variations for quality | Medium |
| Qualitative Experiment | Usability test, diary study | Low |

---

## Experiment Design Process

### Step 1 — Hypothesis
> "We believe that [change] will cause [metric] to [increase/decrease] because [rationale]. We'll know we're right if [specific measurable outcome] within [time period]."

### Step 2 — Identify Primary and Secondary Metrics
- **Primary metric**: The ONE metric the experiment is designed to move
- **Secondary metrics**: Supporting signals that give context
- **Guardrail metrics**: What we must not harm

### Step 3 — Sample Size Calculation
Before running: calculate required sample size.
- Baseline conversion rate (or metric value)
- Minimum detectable effect (MDE) — how big does the change need to be to be meaningful?
- Statistical significance level: typically α = 0.05 (95% confidence)
- Statistical power: typically β = 0.80 (80% power)

**Rule of thumb**: For most web experiments, run for at least 2 full business cycles (typically 2 weeks).

### Step 4 — Experiment Setup
- Randomization unit (user, session, device?)
- Control vs. treatment split (typically 50/50; or 90/10 for risk mitigation)
- Exposure logging in place before launch
- Guardrail monitoring alerts set up

### Step 5 — Run and Monitor
- Don't peek and stop early (p-hacking risk)
- Monitor for sample ratio mismatch (SRM)
- Check guardrail metrics daily

### Step 6 — Readout
- Was the result statistically significant?
- Was the effect practically significant (large enough to matter)?
- Are there segment-level insights?
- What are the implications for the roadmap?

---

## GenAI-Specific Experiment Types

### Prompt Experiments
- Test variations of system prompts for quality, safety, and tone
- Use eval datasets with human-labeled ground truth
- Metrics: accuracy, hallucination rate, relevance, latency

### Model Comparison
- A/B test different model versions (e.g., GPT-4o vs. Claude 3.5)
- Hold prompt constant; vary model
- Metrics: output quality, cost per call, latency

### UI Framing Experiments
- Does showing an AI confidence score change user behavior?
- Does "AI-suggested" vs. "Suggested" framing affect trust?

### Human-in-the-Loop Experiments
- What's the optimal intervention threshold for human review?
- Do mandatory reviews improve output quality metrics?

---

## Statistical Concepts (Quick Reference)

| Concept | Definition |
|---------|------------|
| p-value | Probability of seeing results as extreme as observed if null hypothesis is true |
| Statistical significance | p < α (typically 0.05); does NOT mean the effect is large |
| Practical significance | Is the effect size large enough to matter for the business? |
| Power | Probability of detecting a true effect (typically 80%) |
| Type I error | False positive — declaring a winner when there isn't one |
| Type II error | False negative — missing a real effect |
| Sample ratio mismatch | Your A/B split didn't actually split the way you intended |

---

## Common Experiment Mistakes

| Mistake | Risk | Fix |
|---------|------|-----|
| Peeking and stopping early | Inflated false positive rate | Pre-register end date; use sequential testing |
| Underpowered test | Missed real effects | Calculate sample size before starting |
| Testing on wrong segment | Diluted signal | Filter analysis to exposed users |
| No guardrail metrics | Missed regressions | Set up daily guardrail alerts |
| One-week test | Novelty effect distorts results | Run at least 2 business cycles |

---

## Quality Checks

- [ ] Hypothesis written with specific metric and direction
- [ ] Primary metric defined before test launch
- [ ] Sample size calculated and test duration set
- [ ] Guardrail metrics and alerts configured
- [ ] Success threshold pre-registered
- [ ] Randomization unit is correct (user-level for most)
- [ ] Readout includes practical significance, not just p-value
