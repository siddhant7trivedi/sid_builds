---
name: product-launch
description: "Use this skill when planning or executing a product or feature launch. Covers: GTM strategy, launch tiers, launch checklists, messaging frameworks, rollout plans, internal readiness, and post-launch monitoring. Trigger when the user is preparing to ship something to users — from a small feature flag rollout to a full product launch. Includes GenAI-specific launch considerations."
---

# Product Launch Skill

## Purpose
Ship with confidence — aligned internally, ready externally, and able to respond fast when things go wrong.

---

## Core Principles

1. **Launch is a process, not a moment** — It starts at scoping and ends post-launch review
2. **Tier your launch** — Not every feature needs a press release; match effort to impact
3. **Internal readiness first** — Support, sales, and CS must know before users do
4. **Rollout ≠ launch** — Gradual rollout is how you ship safely; launch is how you drive awareness
5. **Measure before and after** — You can't know if launch worked without a baseline

---

## Launch Tiers

| Tier | Description | Who Notices | Activities |
|------|-------------|------------|------------|
| T1 — Major Launch | New product or flagship feature | Market, press, all customers | PR, blog, sales enablement, email, events |
| T2 — Significant Feature | High-impact feature, targeted segment | Segment users + buyers | In-app announcement, email, sales brief |
| T3 — Incremental Update | UX improvement, minor feature | Active users | In-app tooltip, changelog, support brief |
| T4 — Internal / Dark Launch | Dev, dogfooding, beta | Internal team only | Flag, internal comms |

---

## GTM Strategy Components

### 1. Messaging Framework
- **Headline**: What is the one thing we want the audience to walk away knowing?
- **Problem we solve**: Stated in user/buyer language
- **Our solution**: What we do and how
- **Why us**: Why we're the right choice
- **Proof points**: Customer quotes, data, case studies
- **CTA**: What we want them to do next

### 2. Audience Targeting
- Who is the primary launch audience? (Existing customers / prospects / press)
- What segment receives which message?
- Is there a different message for users vs. buyers?

### 3. Channel Strategy
| Channel | Audience | Message | Owner | Timing |
|---------|----------|---------|-------|--------|
| In-app announcement | Existing users | Feature value | PM/Design | Launch day |
| Email campaign | Existing customers | Adoption driver | Marketing | Launch day |
| Blog post | Prospects + community | Thought leadership | Marketing | T-3 days |
| Press / analyst | Market | Market narrative | Comms | Embargo |
| Sales enablement | Sales team | Deal acceleration | PM | T-7 days |
| Support article | All users | How to use it | CS | Launch day |

---

## Launch Readiness Checklist

### Product & Engineering
- [ ] Feature complete and QA'd
- [ ] Acceptance criteria verified
- [ ] Performance/load testing done
- [ ] Rollout plan defined (% flag or full)
- [ ] Feature flag in place for kill switch
- [ ] Monitoring and alerts configured
- [ ] Rollback plan documented and tested

### Analytics & Metrics
- [ ] Analytics events instrumented and verified
- [ ] Dashboards live with pre-launch baseline captured
- [ ] Success metrics agreed upon
- [ ] Guardrail metric alerts active

### Go-to-Market
- [ ] Messaging and positioning finalized
- [ ] Blog post / changelog written
- [ ] Email drafted and approved
- [ ] In-app messaging implemented
- [ ] Social copy prepared (if T1/T2)

### Internal Enablement
- [ ] Sales team briefed with battle card
- [ ] CS/Support team trained
- [ ] Support articles published
- [ ] FAQ documented
- [ ] Exec demo ready

### Legal & Compliance
- [ ] Privacy review done (if data involved)
- [ ] Security review done
- [ ] Terms of service / legal review (if new functionality)
- [ ] AI disclosure requirements met (if AI feature)

---

## Rollout Strategy

### Progressive Rollout
1. **1% canary**: Internal team + select beta users → monitor 24hr
2. **10% rollout**: Broader beta → monitor 48hr
3. **25% → 50%**: Expand if metrics healthy → monitor 48hr each
4. **100%**: Full launch

**Kill switch criteria** (auto-pause rollout if):
- Error rate exceeds [X]%
- P95 latency exceeds [X]s
- Any guardrail metric breaks threshold

---

## GenAI Launch Specifics

- **AI output quality baseline**: Capture quality metrics before launch as baseline
- **Hallucination rate disclosure**: Is there a user-facing transparency element?
- **Human-in-the-loop comms**: Make it clear where humans review AI output
- **Feedback mechanism**: Launch a way for users to flag bad AI outputs
- **Model version pinning**: Document which model version shipped, for regression tracking
- **AI safety/abuse monitoring**: Confirm monitoring is live before launch

---

## Post-Launch Monitoring (First 72 Hours)

| Metric | Check Frequency | Owner | Escalation Threshold |
|--------|----------------|-------|---------------------|
| Error rate | Every 30 min | Eng | >X% |
| P95 latency | Every 30 min | Eng | >Xs |
| Feature adoption | Daily | PM | |
| Support ticket volume | Daily | CS | 2× normal |
| NPS / satisfaction | Daily (if surveying) | PM | |
| AI quality metrics | Daily | Data | |

---

## Quality Checks

- [ ] Launch tier is assigned and activities match
- [ ] Messaging is audience-specific (user vs. buyer)
- [ ] All internal teams briefed before user-facing launch
- [ ] Rollout plan with kill switch defined
- [ ] Post-launch monitoring active with escalation owners
- [ ] GenAI-specific disclosures and feedback loop in place
