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
| Engineering | Transforms the approved PRD and Solution Design into an implementation-ready engineering blueprint across frontend, backend, AI, data, cloud, DevOps, security, and testing |
| Testing | Validates release readiness through functional, UAT, security, performance, and AI evaluations — produces a Go / No-Go recommendation |
| Launch | Ensures successful product release and customer adoption — validates GTM readiness, rollout strategy, and production health |
| Evals | Measures business impact, customer value, and AI performance post-launch — recommends whether to Scale, Optimize, Experiment, Pivot, or Retire |

## Usage

Run each agent sequentially. Each agent's output feeds the next as structured input, building a traceable chain from idea to production and beyond.

```
Market Opportunity → Customer Discovery → Product Strategy → PRD → Solution Design → Prototyping → Engineering → Testing → Launch → Evals
```

## Outputs

All agent outputs are saved to the `outputs/` directory. Each agent writes its results as a file in that folder, named after the agent (e.g. `market-opportunity.md`, `prd.md`). This makes every stage's output available as structured input for the next agent in the pipeline.

## Claude Code Sub-Agents

Each agent is implemented as a Claude Code sub-agent in `.claude/agents/`. These can be invoked directly inside Claude Code using the Agent tool with the matching `subagent_type`.

| Sub-agent |
|---|
| `.claude/agents/market-opportunity-agent.md` |
| `.claude/agents/customer-discovery-agent.md` |
| `.claude/agents/prod-strategy-agent.md` |
| `.claude/agents/prd-agent.md` |
| `.claude/agents/solution-design-agent.md` |
| `.claude/agents/prototyping-agent.md` |
| `.claude/agents/engineering-agent.md` |
| `.claude/agents/testing-agent.md` |
| `.claude/agents/launch-agent.md` |
| `.claude/agents/evals-agent.md` |

Each sub-agent's description is scoped to its position in the pipeline so Claude Code knows when to invoke it and which prior outputs it depends on.
