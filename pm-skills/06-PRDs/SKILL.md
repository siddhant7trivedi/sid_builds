---
name: prd
description: "Use this skill when writing or reviewing a Product Requirements Document (PRD) or feature spec. Covers: problem framing, user stories, acceptance criteria, functional and non-functional requirements, AI-specific requirements, success metrics, and edge cases. Trigger when the user wants to define what to build and why clearly enough that engineering, design, and data teams can execute. Bias toward AI feature PRDs."
---

# PRD Skill

## Purpose
Write requirements that are specific enough to build from, flexible enough to allow good engineering decisions, and clearly tied to user outcomes and business goals.

---

## Core Principles

1. **Problem first, solution second** — State the problem before describing the solution
2. **Requirements ≠ designs** — Specify what and why; leave how to engineering where possible
3. **Acceptance criteria are non-negotiable** — If you can't test it, it's not a requirement
4. **AI features need extra precision** — Model behavior, fallbacks, and edge cases must be specified
5. **Short is better** — A tight 2-page PRD beats a bloated 10-page one

---

## PRD Components

### Must-Have Sections
1. **Problem Statement** — What user problem are we solving and why now?
2. **Goals / Success Metrics** — How will we know if we succeeded?
3. **Non-Goals** — What are we explicitly NOT building?
4. **User Stories** — Who needs what and why?
5. **Functional Requirements** — What must the system do?
6. **Acceptance Criteria** — Testable pass/fail conditions for each requirement
7. **Edge Cases & Error States** — What happens when things go wrong?

### Recommended Sections
8. **Non-Functional Requirements** — Performance, security, accessibility, scalability
9. **UX Notes / Wireframe Links** — Key UX decisions or constraints
10. **Dependencies** — What must exist before this can ship?
11. **Open Questions** — Unresolved decisions with owners and due dates

### AI Feature-Specific Sections
12. **AI Behavior Specification** — Model inputs, expected outputs, quality thresholds
13. **Fallback Behavior** — What happens when AI fails or is uncertain?
14. **Human-in-the-Loop Design** — Where does a human review or override AI output?
15. **Evaluation Criteria** — How do we measure AI output quality?

---

## User Story Format

### Standard
> **As a** [user type], **I want to** [action], **so that** [outcome/value].

### Job-Focused (stronger)
> **When** [situation], **I need to** [action], **so I can** [goal], **without** [current friction].

---

## Acceptance Criteria Format

Use **Given / When / Then** (Gherkin style):
> **Given** [precondition],
> **When** [action occurs],
> **Then** [expected outcome].

---

## AI Requirements Specifics

### Model Behavior
- Input format(s) and constraints
- Expected output format and structure
- Quality threshold (e.g., "Accuracy must be ≥95% on benchmark dataset X")
- Latency requirement (e.g., "Response must be generated in <3 seconds P95")
- Context window handling (for LLMs)

### Fallback States
- What happens if the model returns an error?
- What happens if confidence is below threshold?
- What happens if the model is unavailable (rate limit, outage)?
- Is there a graceful degradation path?

### Human-in-the-Loop
- Define exactly where human review is required
- Define what "approve", "edit", and "reject" actions look like
- Define how human corrections are handled (feedback loop)

### Evaluation
- What benchmark or test set will be used?
- Who owns evaluation before release?
- What's the regression prevention mechanism post-release?

---

## Non-Functional Requirements Checklist

- [ ] **Performance**: Load time, latency, throughput targets
- [ ] **Scalability**: Expected user volume, peak load handling
- [ ] **Security**: Data handling, access controls, PII exposure
- [ ] **Privacy**: What data is stored? For how long? Who can access?
- [ ] **Accessibility**: WCAG compliance level
- [ ] **Reliability**: Uptime target, error rate threshold
- [ ] **Observability**: What logs/metrics must be captured?

---

## Common PRD Mistakes

| Mistake | Fix |
|---------|-----|
| Solution disguised as requirement | Reframe: "The system shall allow X" → "User needs to achieve Y" |
| No acceptance criteria | Add Given/When/Then for every requirement |
| Missing edge cases | Run "what if it fails?" for every AI call |
| Vague success metrics | Attach specific numbers and timeframes |
| AI fallback not specified | Always define what happens when AI can't answer |

---

## Quality Checks

- [ ] Problem statement written before solution description
- [ ] Every user story has acceptance criteria
- [ ] Non-goals are explicit
- [ ] AI behavior, fallback, and eval criteria specified (if AI feature)
- [ ] Success metrics are measurable and time-bound
- [ ] Open questions have owners and due dates
- [ ] PRD has been reviewed by engineering, design, and data
