---
name: ai-agents
description: "Use this skill when designing, specifying, or evaluating AI agent products or features. Covers: agent architecture patterns, task decomposition, tool design, memory and state management, orchestration, evaluation, safety, and human-in-the-loop design. Trigger when the user is building autonomous or semi-autonomous AI workflows, multi-step AI tasks, or AI systems that take actions in the world. Specific to GenAI product management."
---

# AI Agents Skill

## Purpose
Help PMs design AI agent products that are useful, reliable, safe, and trustworthy — not just technically impressive.

---

## Core Principles

1. **Reliability > capability** — An agent that works 95% of the time is more valuable than one that works 70% of the time with more features
2. **Design for failure** — Every agent will fail; design the failure modes, not just the happy path
3. **Trust is earned incrementally** — Start with human-in-the-loop; earn the right to automate
4. **The UX of uncertainty matters** — How does the agent communicate low confidence? That IS product design.
5. **Safety is a product requirement, not an afterthought** — Define constraints before capabilities

---

## Agent Architecture Concepts (PM-Level)

### Agent Components
| Component | What It Is | PM Consideration |
|-----------|-----------|-----------------|
| **Planner** | Breaks goals into steps | Transparency of planning to user? |
| **Memory** | Short-term context + long-term storage | What should persist? What resets? |
| **Tools** | External actions the agent can take | Which tools carry irreversible risk? |
| **Executor** | Carries out individual steps | Where should humans review? |
| **Evaluator** | Checks if the step worked | How do you surface failures to users? |

### Agent Patterns
| Pattern | Description | Use Case |
|---------|-------------|----------|
| ReAct | Reason + Act loop | Research, multi-step tasks |
| Plan and Execute | Plan full task first, then execute | Longer horizon tasks |
| Reflexion | Self-reflection + iteration on failure | Quality-critical tasks |
| Multi-agent | Specialized agents coordinate | Complex workflows |
| Human-in-the-loop | Human checkpoints at defined steps | High-stakes actions |

---

## Product Design Decisions for Agents

### 1. What is the agent's scope?
- What is it allowed to do? (Tool list)
- What is it explicitly NOT allowed to do? (Guardrails)
- What's the action boundary? (Read-only vs. read-write vs. transactional)

### 2. What triggers the agent?
- Explicit user invocation
- Event-triggered (e.g., new email arrives)
- Scheduled / recurring
- Chained from another agent

### 3. What's the trust level model?
| Level | Description | Example |
|-------|-------------|---------|
| L0 | Shows plan, waits for approval | "Here's my plan. Proceed?" |
| L1 | Executes steps, shows results | Drafts + sends for approval |
| L2 | Executes autonomously, notifies | Fully automated with log |
| L3 | Fully autonomous, logs only | Reserved for truly safe actions |

### 4. What does the agent know and remember?
- Conversation history (short-term)
- User preferences and context (long-term memory)
- Business context (documents, CRM, calendar)
- What data the agent SHOULD NOT have access to

### 5. How does the agent fail gracefully?
- Tool call fails → retry, fallback, or escalate to human?
- Ambiguous input → clarify or proceed with assumption?
- Low confidence → proceed with flag or stop?
- Out-of-scope request → decline and explain or attempt?

---

## Tool Design Principles

Each tool the agent can use should have:
- **Name**: Clear, verb-noun (e.g., `search_documents`, `create_draft`)
- **Description**: What it does — written for the LLM to reason about
- **Inputs**: Schema with types, required vs. optional
- **Output**: What it returns, including errors
- **Reversibility**: Is this action reversible? (Read = safe; Delete = dangerous)
- **Cost/Rate limit**: Any constraints on usage?

**Reversibility Tiers:**
| Tier | Type | Requirement |
|------|------|-------------|
| Safe | Read-only | Can run freely |
| Reversible | Writes that can be undone | Confirm or log |
| Irreversible | Deletes, sends, transactions | Always require explicit confirmation |

---

## Agent Evaluation Framework

### Functional Metrics
- Task success rate (did it complete the goal?)
- Step accuracy (was each step correct?)
- Steps to completion (efficiency)
- Error recovery rate (did it recover from mistakes?)

### Safety Metrics
- Out-of-scope action attempt rate
- Irreversible action frequency
- User override / correction rate
- Hallucinated tool call rate

### User Experience Metrics
- Task abandonment rate
- User override rate (they took over)
- Trust score (survey)
- Time-to-value vs. manual

---

## Human-in-the-Loop Design Patterns

| Pattern | When to Use | Implementation |
|---------|-------------|---------------|
| Pre-approval gate | Before irreversible actions | "About to send email — approve?" |
| Post-step review | After each major milestone | Summary + "Continue?" |
| Exception escalation | When confidence is low | "Not sure how to proceed — your input?" |
| Audit log | Low-stakes automated flows | Timestamped action log user can review |
| Override always available | All agent flows | Stop button + edit mode |

---

## GenAI Agent Product Risks

| Risk | Description | Mitigation |
|------|-------------|------------|
| Action amplification | Agent takes many actions faster than user realizes | Step-by-step visibility; rate limits |
| Prompt injection | Malicious content in environment hijacks agent | Input sanitization; constrained tool scope |
| Cascading failures | One bad step cascades | Checkpoints; human review gates |
| Overconfidence | Agent proceeds when it should stop | Confidence calibration; uncertainty surfacing |
| Data leakage | Agent accesses or transmits sensitive data | Strict data scope; access controls |

---

## Quality Checks

- [ ] Agent scope (allowed actions) is explicitly defined
- [ ] Trust level model defined (L0–L3 per action type)
- [ ] All tools classified by reversibility
- [ ] Failure modes designed, not just happy path
- [ ] Human-in-the-loop checkpoints defined
- [ ] Evaluation framework covers functional + safety metrics
- [ ] Data access scope is least-privilege
