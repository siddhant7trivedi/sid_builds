# Product Management Agents

A collection of specialized AI agents that guide a product idea through the full product discovery and requirements lifecycle — from market validation to implementation-ready design.

## Agents

| Agent | Role |
|---|---|
| Market Opportunity | Evaluates whether a product idea represents a viable market opportunity — assesses demand, competition, and strategic positioning |
| Customer Discovery | Validates genuine customer problems — identifies target users, pain points, and willingness to adopt |
| Product Strategy | Defines roadmap, MVP scope, success metrics, and sustainable competitive advantages |
| PRD Agent | Translates validated insights into a comprehensive, implementation-ready Product Requirements Document |
| Solution Design | Transforms the PRD into a scalable solution — covers UX, AI interaction model, architecture, and HITL workflows |
| Prototyping | Validates technical feasibility through lightweight prototypes — evaluates model performance and failure modes |

## Usage

Run each agent sequentially. Each agent's output feeds the next as structured input, building a traceable chain from idea to implementation plan.

```
Market Opportunity → Customer Discovery → Product Strategy → PRD → Solution Design → Prototyping
```

## Claude Code Sub-Agents

Each spec has a corresponding Claude Code sub-agent in `.claude/agents/`. These can be invoked directly inside Claude Code using the Agent tool with the matching `subagent_type`.

| Sub-agent file | Spec |
|---|---|
| `.claude/agents/market-opportunity-agent.md` | [market-opportunity-agent.md](market-opportunity-agent.md) |
| `.claude/agents/customer-discovery-agent.md` | [customer-discovery-agent.md](customer-discovery-agent.md) |
| `.claude/agents/prod-strategy-agent.md` | [prod-strategy-agent.md](prod-strategy-agent.md) |
| `.claude/agents/prd-agent.md` | [prd-agent.md](prd-agent.md) |
| `.claude/agents/solution-design-agent.md` | [solution-design-agent.md](solution-design-agent.md) |
| `.claude/agents/prototyping-agent.md` | [prototyping-agent.md](prototyping-agent.md) |

Each sub-agent's description is scoped to its position in the pipeline so Claude Code knows when to invoke it and which prior outputs it depends on.
