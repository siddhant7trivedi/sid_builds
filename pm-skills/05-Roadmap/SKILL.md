---
name: product-roadmap
description: "Use this skill when building, refining, or communicating a product roadmap. Covers: roadmap types (now/next/later, theme-based, timeline), prioritization frameworks, stakeholder communication, dependency mapping, and roadmap health checks. Trigger when the user needs to sequence work, align stakeholders, or communicate product direction. Includes AI product roadmap considerations."
---

# Product Roadmap Skill

## Purpose
Translate strategy into a sequenced, prioritized, and communicable plan that guides execution and aligns stakeholders.

---

## Core Principles

1. **Roadmap ≠ feature list** — It's a prioritized bet on outcomes, not a delivery schedule
2. **Audience-specific** — Engineering roadmap ≠ exec roadmap ≠ customer-facing roadmap
3. **Living document** — Update when assumptions change, not just on a calendar
4. **Outcome-first sequencing** — Sequence by which bets to test, not which features to ship
5. **Say no explicitly** — What's NOT on the roadmap is as strategic as what is

---

## Roadmap Types

| Type | Best For | Horizon |
|------|----------|---------|
| Now / Next / Later | Early stage, high uncertainty | Rolling |
| Theme-based | Strategy alignment, external comms | Quarterly |
| Timeline / Gantt | Dependencies, engineering execution | Sprint-level |
| Opportunity roadmap | Discovery-heavy teams | Quarterly |
| OKR-linked | Outcome-driven teams | Quarterly |

---

## Prioritization Frameworks

### RICE Score
> **Reach × Impact × Confidence ÷ Effort**
- Reach: How many users affected per time period?
- Impact: How much does it move the needle? (3=massive, 2=high, 1=medium, 0.5=low)
- Confidence: How sure are we? (100%=high, 80%=medium, 50%=low)
- Effort: Person-months

### MoSCoW
- **Must have** — Product fails without it
- **Should have** — High value, not critical for launch
- **Could have** — Nice to have if bandwidth exists
- **Won't have (now)** — Explicitly deprioritized

### Opportunity Scoring (Teresa Torres)
Map against: Importance to user × Satisfaction gap

### ICE (quick triage)
- Impact (1–10) × Confidence (1–10) × Ease (1–10)

---

## Roadmap Construction Workflow

### Step 1 — Anchor to Strategy
- What are the strategic bets this roadmap serves?
- What OKRs does each theme ladder to?

### Step 2 — Collect Inputs
- Customer research insights
- Sales/support feedback
- Competitive signals
- Technical debt priorities
- Regulatory requirements

### Step 3 — Define Themes (not features)
Themes are outcome clusters: e.g., "Reduce time-to-first-value" not "Onboarding v2"

### Step 4 — Prioritize within Themes
Use RICE or MoSCoW; score consistently

### Step 5 — Sequence for Dependencies
- What must be built before X?
- What are shared infra dependencies?
- What enables the next strategic bet?

### Step 6 — Map Horizons
- **Now (0–3mo)**: Committed sprint work
- **Next (3–6mo)**: Directional, some flexibility
- **Later (6–12mo+)**: Strategic intent, high uncertainty

### Step 7 — Stakeholder Alignment
- Engineering: feasibility + effort estimates
- Exec: OKR linkage + strategic narrative
- Sales/CS: GTM readiness + customer commitments
- Design: UX research and design lead time

---

## AI Product Roadmap Considerations

- **Model evaluation cadence**: Budget for ongoing eval as a first-class roadmap item
- **Prompt versioning and iteration**: Treat prompt engineering as a build cycle
- **Human-in-the-loop milestones**: Define when automation increases (trust gates)
- **Safety and guardrails**: Roadmap AI safety features explicitly — not as afterthoughts
- **Feedback loops**: When does the product start learning from usage?
- **Capability dependencies**: Track underlying model releases (OpenAI, Anthropic, etc.) as external dependencies

---

## Common Roadmap Anti-Patterns

| Anti-Pattern | Why It's Harmful | Fix |
|-------------|-----------------|-----|
| Feature factory | Optimizes for shipping, not outcomes | Anchor to OKRs |
| Roadmap = commitment | Creates rigidity | Communicate confidence levels |
| No "won't do" column | Leads to scope creep | Explicit deprioritization |
| One roadmap for all audiences | Creates confusion | Audience-specific views |
| Roadmap never updated | Loses credibility | Monthly review cadence |

---

## Quality Checks

- [ ] Each item links to a strategic bet or OKR
- [ ] Horizons are labeled with confidence levels
- [ ] Dependencies are mapped (especially cross-team)
- [ ] A "won't do (now)" list exists
- [ ] Audience-appropriate version exists for each stakeholder group
- [ ] AI evaluation and safety items are on the roadmap (if AI product)
