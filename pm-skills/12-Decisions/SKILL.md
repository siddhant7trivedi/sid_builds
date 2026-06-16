---
name: product-decisions
description: "Use this skill when structuring, documenting, or communicating a significant product decision. Covers: decision frameworks (DACI, RAPID, reversibility), decision memos, trade-off analysis, assumption documentation, and stakeholder alignment. Trigger when the user needs to make a hard call, get alignment on a direction, or document a decision for future reference. Also useful for reversing or revisiting past decisions."
---

# Product Decisions Skill

## Purpose
Make decisions faster, with better alignment, and leave a clear record of why — so future teams can revisit with full context.

---

## Core Principles

1. **Disagree and commit** — Alignment doesn't mean unanimity; it means everyone knows the decision and their role
2. **Separate reversible from irreversible** — Reserve deliberation for irreversible decisions; default-do on reversible ones
3. **Document the "why" not just the "what"** — Future you will be grateful
4. **Decisions decay** — Revisit when assumptions change, not just on a schedule
5. **Recommended > Options** — Come with a recommendation, not just a list

---

## Decision Classification

### By Reversibility (Bezos Type 1 / Type 2)
| Type | Description | Approach |
|------|-------------|---------|
| Type 1 (Irreversible) | Hard or impossible to undo; high stakes | Full deliberation; structured process |
| Type 2 (Reversible) | Can be changed if wrong; low stakes | Default to action; lightweight documentation |

### By Scope
| Scope | Examples | Decision Owner |
|-------|---------|----------------|
| Feature/UX | Button placement, copy, flow | PM alone or with design |
| Product direction | Pivot, new segment, kill a feature | PM + Eng lead |
| Strategic | Platform strategy, pricing model | PM + Exec |
| Investment | Build vs. buy, major resourcing | PM + Finance + Exec |

---

## Decision Frameworks

### DACI (Roles in Decisions)
| Role | Meaning | Number of People |
|------|---------|-----------------|
| **D**river | Owns the process and drives to a decision | 1 |
| **A**pprover | Must sign off | 1–2 |
| **C**ontributors | Provide input; no vote | Many |
| **I**nformed | Notified after decision | Many |

### RAPID (Extended)
- **Recommend**: Who proposes the decision
- **Agree**: Who must agree (veto power)
- **Perform**: Who executes
- **Input**: Who provides information
- **Decide**: Who makes the final call

### Option-Based Framework
1. Define the decision question clearly
2. List options (usually 2–4; never just 1)
3. Score each against criteria that matter
4. State a recommendation
5. Document the key trade-off being made

---

## Decision Memo Format

A good decision memo is 1–2 pages max. It answers:
1. What decision needs to be made, and by when?
2. What are the options?
3. What criteria matter?
4. What's the recommendation and why?
5. What are we trading off?
6. What assumptions is this based on?
7. What's the review trigger?

---

## Trade-off Analysis

For every recommendation, make the trade-off explicit:
> "By choosing [X], we are trading [benefit of X] for [cost of X or opportunity cost of Y]."

Good trade-off statements:
- "By choosing PLG, we're trading faster sales velocity for lower CAC. We believe this is right because our ICP is technical and self-serves naturally."
- "By deprioritizing mobile, we're trading potential reach for engineering focus. We'll revisit when web PMF is established."

---

## Assumption Logging

For every significant decision, document the assumptions it rests on:

| Assumption | Confidence | How to Validate | Review By |
|------------|-----------|-----------------|-----------|
| [e.g., Customers will pay $X/seat] | Low | Pricing interviews | [Date] |
| [e.g., LLM accuracy is good enough] | Medium | Design partner pilot | [Date] |

If a key assumption is invalidated, the decision should be revisited.

---

## Reversing a Decision

When revisiting or reversing a previous decision:
1. Name the original decision and its date
2. State which assumption changed or was invalidated
3. Describe the new information
4. Make the updated recommendation
5. Document the reversal with context (don't just overwrite)

---

## Common Decision Anti-Patterns

| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| Decision by committee | No clear owner; slow | Assign a single Driver |
| Analysis paralysis | Velocity loss on reversible decisions | Default to action on Type 2 |
| Undocumented decisions | Future teams re-litigate same debates | Write the memo, even if short |
| Options without recommendation | Forces stakeholders to decide without context | Always include a recommendation |
| No review trigger | Decisions never updated | Set explicit "revisit when" criteria |

---

## Quality Checks

- [ ] Decision type classified (reversible vs. irreversible)
- [ ] Decision question is specific (not "what should we do about X")
- [ ] 2–4 options presented (not just one)
- [ ] Recommendation is explicit with rationale
- [ ] Trade-off is stated (what we're giving up)
- [ ] Key assumptions are documented
- [ ] DACI or RAPID roles assigned
- [ ] Review trigger is set
