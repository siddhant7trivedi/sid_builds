# AI Agent Product Specification
**Agent Name:** [Name]
**Product:** [Product Name]
**Date:** [YYYY-MM-DD]
**PM Owner:** [Name]
**Status:** [Discovery / Spec / Build / Testing / Live]

---

## 1. Agent Overview

| Field | Detail |
|-------|--------|
| **One-line description** | [What does this agent do, in plain language?] |
| **Primary user** | [Persona / role] |
| **Core job it does** | [JTBD — "When I..., I need to..., so I can..."] |
| **Trigger** | [User-invoked / Event-triggered / Scheduled] |
| **Autonomy level** | [L0: Plan approval / L1: Step approval / L2: Notify / L3: Fully auto] |

---

## 2. Agent Scope

### What the agent CAN do (allowed actions):
- [e.g., Search internal documents]
- [e.g., Draft an email for review]
- [e.g., Look up CRM records]
- [e.g., Create calendar invites (with approval)]

### What the agent CANNOT do (hard constraints):
- ❌ [e.g., Send emails without explicit user approval]
- ❌ [e.g., Access financial data]
- ❌ [e.g., Modify or delete existing records]
- ❌ [e.g., Access data outside the user's own workspace]

---

## 3. Agent Architecture

### Pattern
- [ ] ReAct (reason + act loop)
- [ ] Plan and Execute
- [ ] Reflexion (self-correcting)
- [ ] Multi-agent
- [ ] Human-in-the-loop at specific checkpoints
- [ ] Other: ___

### Memory Design
| Memory Type | What's Stored | Persistence | Access Scope |
|-------------|-------------|-------------|-------------|
| Short-term (in-context) | [Current task context] | Session only | Agent only |
| Long-term | [User preferences, history] | Persistent | User-scoped |
| Business context | [Docs, CRM, calendar] | External retrieval | Permissioned |

---

## 4. Tool Specification

| Tool Name | Description | Inputs | Output | Reversible? | Risk Level |
|-----------|-------------|--------|--------|-------------|------------|
| `search_documents` | Searches user's document store | query (string) | Document list | ✅ Yes | Low |
| `draft_email` | Creates email draft | to, subject, body | Draft object | ✅ Yes | Low |
| `send_email` | Sends a draft email | draft_id | Confirmation | ❌ No | **High** |
| `create_event` | Creates calendar invite | title, time, attendees | Event ID | ⚠️ Partially | Medium |

**Reversibility Legend**: ✅ Read-only or undoable | ⚠️ Hard to undo | ❌ Irreversible

---

## 5. Trust Level Model

| Action / Tool | Trust Level | Approval Required? | How Surfaced to User |
|--------------|-------------|-------------------|---------------------|
| Search, read | L2 — Auto | No | Background log |
| Draft creation | L1 — Notify | No (shown for edit) | Inline preview |
| Send / post | L0 — Gate | YES — explicit | Confirmation dialog |
| Delete / modify | L0 — Gate | YES — explicit | Warning + confirm |

---

## 6. User Flows

### Happy Path: [Primary Use Case]

1. User triggers agent with: [e.g., "Find all emails from Acme Corp this week and summarize action items"]
2. Agent plans: [e.g., Search emails → Summarize → Present]
3. Step 1 — Agent searches emails [Tool: `search_emails`] → Shows "Searching..."
4. Step 2 — Agent summarizes [LLM processing] → Shows progress
5. Agent presents: [Summary with action items] → User reviews
6. [If action items found] → Agent offers: "Want me to draft replies or create tasks?" → User chooses

### Failure Flow: Tool Fails
1. `search_emails` returns error
2. Agent detects failure
3. Agent surfaces: "I couldn't access your email. [Check connection / Try again / Do this manually]"
4. User chooses resolution path

### Ambiguity Flow: Unclear Goal
1. User says: "Help me follow up with clients"
2. Agent detects ambiguity (which clients? what follow-up?)
3. Agent asks clarifying question: "Which clients would you like to follow up with — recent leads, all active accounts, or a specific list?"

---

## 7. Human-in-the-Loop Checkpoints

| Checkpoint | Trigger | User Prompt | Options |
|-----------|---------|-------------|---------|
| Pre-send email | Before any `send_email` call | "Ready to send this email to [name]. Proceed?" | Send / Edit / Cancel |
| Low confidence | Confidence score < [X]% | "I'm not fully confident about [X]. Want me to proceed or clarify?" | Proceed / Clarify / Stop |
| Unexpected scope | Agent encounters out-of-scope request | "This would require [action I'm not authorized for]. Would you like to [alternative]?" | Alternative / Cancel |
| Completion summary | After multi-step task | "Completed. Here's what I did: [log]" | Acknowledge / Undo |

---

## 8. Failure Mode Design

| Failure Type | Cause | Agent Behavior | User Message |
|-------------|-------|----------------|-------------|
| Tool call error | API failure | Retry 1×, then escalate | "Couldn't complete step X. [Action]" |
| Low confidence output | Model uncertainty | Flag + ask for review | "This may need your review — [reason]" |
| Ambiguous input | Underspecified goal | Ask clarifying question | "To do this well, I need to know [X]" |
| Out-of-scope request | User asks disallowed action | Decline + explain | "I'm not set up to [X]. Here's what I can do instead." |
| Context window exceeded | Input too long | Summarize/truncate with notice | "Working with a summary of [X] due to length." |
| Rate limit hit | Too many tool calls | Pause + notify | "Pausing briefly — resuming in [X]s" |

---

## 9. Data & Privacy

| Data Element | Source | Stored? | Retention | Scope |
|-------------|--------|---------|-----------|-------|
| Email content | Gmail | No — read only | Session | User-only |
| User preferences | Profile | Yes | Until user deletes | User-only |
| Agent action log | Internal | Yes | 90 days | User + Admin |

**Data the agent must NEVER access or transmit:**
- [e.g., Payment information]
- [e.g., Other users' private data]

---

## 10. Evaluation Plan

### Functional Metrics
| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Task success rate | ≥X% | Human eval on test set |
| Steps to completion | ≤X steps avg | Logged per task |
| Error recovery rate | ≥X% | % of failures that self-recovered |

### Safety Metrics
| Metric | Threshold | Alert |
|--------|-----------|-------|
| Out-of-scope action attempts | <X% | Immediate review |
| Irreversible actions without approval | 0% | Block + alert |
| User override rate | <X% | Weekly review |

### User Trust Metrics
| Metric | Target |
|--------|--------|
| Task abandonment rate | <X% |
| Post-task satisfaction score | ≥X/5 |
| "Would use again" | ≥X% |

---

## 11. Launch Criteria

- [ ] Task success rate ≥ target on test set
- [ ] All irreversible actions require explicit approval
- [ ] All failure modes tested with graceful degradation confirmed
- [ ] Out-of-scope guardrails tested
- [ ] Prompt injection resistance tested
- [ ] Data scope verified (no access beyond defined scope)
- [ ] Agent action log instrumented
- [ ] Human override always available at every step

---

## Appendix
*(Agent architecture diagram, tool schemas, eval dataset, safety red team results)*
