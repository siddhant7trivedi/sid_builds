# Product Management Agents

A collection of specialized AI agents that guide a product idea through the full product discovery and requirements lifecycle — from market validation to implementation-ready design.

## Agents

| Agent | Role |
|---|---|
| [Market Opportunity](market-opportunity-agent.md) | Evaluates whether a product idea represents a viable market opportunity — assesses demand, competition, and strategic positioning |
| [Customer Discovery](customer-discovery-agent.md) | Validates genuine customer problems — identifies target users, pain points, and willingness to adopt |
| [Product Strategy](prod-strategy-agent.md) | Defines roadmap, MVP scope, success metrics, and sustainable competitive advantages |
| [PRD Agent](prd-agent.md) | Translates validated insights into a comprehensive, implementation-ready Product Requirements Document |
| [Solution Design](solution-design-agent.md) | Transforms the PRD into a scalable solution — covers UX, AI interaction model, architecture, and HITL workflows |
| [Prototyping](prototyping-agent.md) | Validates technical feasibility through lightweight prototypes — evaluates model performance and failure modes |

## Usage

Run each agent sequentially. Each agent's output feeds the next as structured input, building a traceable chain from idea to implementation plan.

```
Market Opportunity → Customer Discovery → Product Strategy → PRD → Solution Design → Prototyping
```
