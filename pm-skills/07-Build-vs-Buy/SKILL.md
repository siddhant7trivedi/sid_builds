---
name: build-vs-buy
description: "Use this skill when evaluating whether to build a capability in-house, buy/license a solution, or use a third-party API. Covers: TCO analysis, strategic fit assessment, make-or-buy frameworks, vendor evaluation, and decision documentation. Trigger when the user faces a build/buy/partner decision — especially for AI/ML capabilities, infra, or platform components."
---

# Build vs. Buy Skill

## Purpose
Make the build/buy/partner decision rigorously — balancing strategic differentiation, time-to-market, cost, and long-term control.

---

## Core Principles

1. **Strategic differentiation drives the decision** — Build what makes you different; buy what doesn't
2. **Total cost of ownership, not just upfront cost** — Build's true cost is hidden in maintenance, hiring, and opportunity cost
3. **Time matters** — Speed-to-market sometimes overrides cost optimization
4. **Lock-in is a real risk** — Evaluate vendor dependency at the start, not after signing
5. **The GenAI layer changes the math** — Building your own LLM is almost never right; the question is which APIs and which integrations

---

## Decision Framework

### Step 1 — Classify the Capability
| Capability Type | Default Decision |
|----------------|-----------------|
| Core differentiator (your moat) | Build |
| Table stakes / commodity | Buy |
| Core but not differentiating | Buy or partner |
| Experimental / uncertain value | Buy first, build if proven |

### Step 2 — Score Across 6 Dimensions

| Dimension | Build | Buy |
|-----------|-------|-----|
| Strategic fit (is this your moat?) | High | Low |
| Time-to-market | Slow | Fast |
| Total cost (3-year TCO) | Often higher | Often lower (watch: scaling costs) |
| Control and customization | High | Low to medium |
| Vendor/dependency risk | Low | High |
| Internal capability | Requires hiring/upskilling | Leverages existing |

### Step 3 — Define the Non-Negotiables
List requirements that a vendor MUST meet. Any gap is a blocker.

### Step 4 — Vendor Evaluation (if Buy path)
Score shortlisted vendors against weighted criteria.

### Step 5 — Make the Decision + Document It
Capture the decision, rationale, assumptions, and review triggers.

---

## Total Cost of Ownership (TCO) — Build Path

### Upfront
- Engineering design and development time
- Testing and QA
- Infrastructure setup

### Ongoing
- Engineering maintenance (bugs, updates, scaling)
- Infrastructure costs (compute, storage)
- Security and compliance overhead
- Opportunity cost (what else could this team build?)

### Hidden
- Talent dependency (what if key engineers leave?)
- Documentation and knowledge transfer
- Ramp time for new engineers

---

## Vendor Evaluation Criteria

| Criteria | Weight | Vendor A | Vendor B |
|---------|--------|----------|---------|
| Feature fit to requirements | High | | |
| Pricing / TCO | High | | |
| API quality / reliability | High | | |
| Security & compliance | High | | |
| Vendor stability / longevity | Medium | | |
| Integration ease | Medium | | |
| Support quality | Medium | | |
| Data portability / exit | Medium | | |
| Roadmap alignment | Low | | |

---

## GenAI-Specific Build vs. Buy Considerations

### Almost Always Buy
- Foundation model (LLM, embedding model, image model)
- Vector database infrastructure
- Basic observability and logging

### Evaluate Carefully
- RAG pipeline — Buy components, potentially assemble yourself
- Evaluation framework — Buy scaffolding, build domain-specific evals
- Fine-tuning — Buy capability (via API), own your training data

### Build Where Possible
- Domain-specific prompts and prompt management
- Evaluation datasets (this IS a moat)
- Output review and feedback loop
- Business logic around AI outputs

### Lock-in Red Flags
- Proprietary data formats
- No data export / portability
- API only (no self-hosted option) for sensitive data
- Vendor controls your evaluation criteria

---

## Decision Anti-Patterns

| Anti-Pattern | Why It's Harmful |
|-------------|-----------------|
| "We'll build it because we want to own it" | Ownership ≠ differentiation; hiding from the real cost |
| "Vendor is cheaper to start" | Scaling costs can 10× the initial price |
| "We'll evaluate buy options later" | Leads to build decisions made by default |
| "Best-of-breed at every layer" | Integration cost and complexity compounds |

---

## Quality Checks

- [ ] Capability classified as core differentiator vs. commodity
- [ ] 3-year TCO estimated for both paths
- [ ] Vendor non-negotiables defined before evaluation starts
- [ ] Lock-in risk explicitly assessed
- [ ] Decision rationale documented with assumptions
- [ ] Review triggers defined (when to revisit the decision)
