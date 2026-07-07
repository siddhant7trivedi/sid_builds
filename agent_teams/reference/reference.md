# Agent Teams Reference Guide

Source: https://code.claude.com/docs/en/agent-teams  
Last reviewed: 2026-07-07 | Claude Code v2.1.199+

---

## Overview

Agent teams let multiple Claude Code instances work together. One session is the **team lead** — it spawns teammates, assigns tasks, and synthesizes results. Teammates are fully independent sessions with their own context windows and can message each other directly.

This is different from subagents: subagents only report back to the caller; teammates communicate peer-to-peer through a shared task list and mailbox.

---

## Enable Agent Teams

Add to `.claude/settings.local.json` (project-level) or `~/.claude/settings.json` (user-level):

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

Without this env var: no team is set up at session start, no team directories are written, Claude will not spawn or propose teammates.

---

## Architecture

| Component     | Role |
|:--------------|:-----|
| **Team lead** | Main Claude Code session; spawns teammates, coordinates work |
| **Teammates** | Separate Claude Code instances; work on assigned tasks |
| **Task list** | Shared work queue; teammates claim and complete items |
| **Mailbox**   | Messaging system for direct agent-to-agent communication |

**Storage paths** (session-derived name = `session-` + first 8 chars of session ID):
- Team config: `~/.claude/teams/{team-name}/config.json` — removed on session exit
- Task list: `~/.claude/tasks/{team-name}/` — persists across sessions (same `cleanupPeriodDays` as transcripts)

The `config.json` holds runtime state (session IDs, tmux pane IDs). Do not edit it by hand — it is overwritten on every state update.

---

## Agent Teams vs. Subagents

| | Subagents | Agent Teams |
|:--|:--|:--|
| **Context** | Own window; results return to caller | Own window; fully independent |
| **Communication** | Report results to main agent only | Teammates message each other directly |
| **Coordination** | Main agent manages all work | Shared task list with self-coordination |
| **Best for** | Focused tasks where only the result matters | Complex work needing discussion and collaboration |
| **Token cost** | Lower — results summarized back to main | Higher — each teammate is a separate Claude instance |

**Rule of thumb:** use subagents when you need quick, focused workers. Use agent teams when teammates need to share findings, challenge each other, and self-coordinate.

---

## When to Use Agent Teams

**Strong use cases:**
- Parallel code review (security + performance + test coverage simultaneously)
- New modules or features where teammates each own separate files
- Debugging with competing hypotheses (adversarial investigation)
- Cross-layer changes spanning frontend, backend, and tests

**When NOT to use:**
- Sequential tasks with many dependencies
- Same-file edits (risk of overwrites)
- Routine tasks — a single session is more cost-effective
- Simple delegation — use subagents instead

---

## Spawning Teammates

Claude decides the number of teammates based on the task, or you specify:

```
Spawn three teammates to review PR #142:
- One focused on security implications
- One checking performance impact
- One validating test coverage
```

```
Spawn 4 teammates to refactor these modules in parallel. Use Sonnet for each teammate.
```

To get predictable names you can reference later, specify them in the spawn instruction.

**Model selection:**
- Teammates do not inherit the lead's `/model` selection by default
- Set **Default teammate model** in `/config`, or pick **Default (leader's model)** to sync
- Teammates do inherit the lead's effort level (v2.1.186+)

---

## Display Modes

| Mode | Description | Requirement |
|:--|:--|:--|
| `"in-process"` | All teammates in your main terminal (default since v2.1.179) | None — works in any terminal |
| `"auto"` | Split panes if tmux/iTerm2 detected, else in-process | tmux or iTerm2 + `it2` CLI |
| `"tmux"` | Split panes, auto-detects tmux vs. iTerm2 | tmux or iTerm2 + `it2` CLI |
| `"iterm2"` | iTerm2 native split panes explicitly (v2.1.186+) | `it2` CLI + iTerm2 Python API enabled |

Set globally in `~/.claude/settings.json`:
```json
{ "teammateMode": "auto" }
```

Set per session:
```bash
claude --teammate-mode auto
```

**In-process mode controls:**
- `↑ / ↓` — select teammate in agent panel
- `Enter` — open teammate transcript and message it
- `Escape` — interrupt selected teammate's current turn
- `x` on selected teammate — stop it
- `Ctrl+T` — toggle task list

**Idle row behavior (v2.1.199+):** A row stays in the panel while any agent is still working. Once all agents are idle, rows hide after 30 seconds. When more than 3 teammates are idle, surplus rows collapse into `N idle agents` — press Enter to expand.

---

## Task System

Tasks have three states: **pending → in progress → completed**. Tasks can declare dependencies; a pending task with unresolved dependencies cannot be claimed until those complete. File locking prevents race conditions when multiple teammates try to claim the same task.

**Lead assigns vs. self-claim:**
- Lead can explicitly assign a task to a specific teammate
- After finishing, a teammate self-claims the next unassigned, unblocked task

**If a task appears stuck:** check whether work is actually done, then tell the lead to nudge the teammate or update the status manually.

---

## Context and Communication

Each teammate has its own context window. On spawn, a teammate loads:
- `CLAUDE.md` from the working directory
- MCP servers from project and user settings
- Skills from project and user settings
- The spawn prompt from the lead

**What it does NOT get:** the lead's conversation history.

**Communication mechanisms:**
- `SendMessage` — direct message to a teammate by name (one recipient per call)
- Automatic idle notifications — teammate notifies lead when it finishes
- Shared task list — all agents see task status
- Failed turn notifications (v2.1.198+) — API error turns notify the lead with the error text

---

## Permissions

- Teammates start with the lead's permission settings
- If lead runs `--dangerously-skip-permissions`, all teammates do too
- Permissions are set at spawn time; per-teammate modes can be changed afterward but not set at spawn
- Teammate permission prompts bubble up to the lead — approve them there
- A teammate cannot approve permissions or relay consent on your behalf
- In auto mode, an approval claim relayed from another agent is treated as untrusted input

---

## Plan Approval for Teammates

For risky or complex tasks, require plan approval before a teammate makes changes:

```
Spawn an architect teammate to refactor the authentication module.
Require plan approval before they make any changes.
```

Workflow:
1. Teammate works in read-only plan mode
2. Finishes planning → sends plan approval request to lead
3. Lead reviews → approves or rejects with feedback
4. If rejected → teammate revises and resubmits
5. On approval → teammate exits plan mode and implements

Influence the lead's judgment by giving it criteria in the spawn prompt:
- `"only approve plans that include test coverage"`
- `"reject plans that modify the database schema"`

---

## Using Subagent Definitions as Teammate Roles

Reference a subagent type by name in the spawn instruction to reuse a defined role:

```
Spawn a teammate using the security-reviewer agent type to audit the auth module.
```

- Teammate honors that definition's `tools` allowlist and `model`
- The definition's body appends to the teammate's system prompt (doesn't replace it)
- `SendMessage` and task management tools are always available even when `tools` restricts others
- `skills` and `mcpServers` frontmatter fields are **not** applied when running as a teammate — those load from project/user settings instead

---

## Quality Gates with Hooks

Use hooks to enforce rules automatically:

| Hook | Fires when | Exit 2 effect |
|:--|:--|:--|
| `TeammateIdle` | A teammate is about to go idle | Sends feedback, keeps teammate working |
| `TaskCreated` | A task is being created | Blocks task creation with feedback |
| `TaskCompleted` | A task is being marked complete | Blocks completion with feedback |

All three hooks receive common fields: `session_id`, `prompt_id`, `transcript_path`, `cwd`, `permission_mode`, `hook_event_name`, `agent_id`, `agent_type`.

`TeammateIdle` additional behaviors:
- Exit 2 → prevents idle, teammate continues working
- JSON `{"continue": false, "stopReason": "..."}` → stops teammate entirely

---

## Shutdown

Tell the lead to send a graceful shutdown to a teammate by name:

```
Ask the researcher teammate to shut down
```

The teammate can approve (exits gracefully) or reject with an explanation. The team's shared directories clean up automatically when the session ends.

---

## Token Cost Management

Agent teams use **~7x more tokens** than standard sessions in plan mode. Each teammate has its own context window.

Cost reduction strategies:
- **Use Sonnet for teammates** — balances capability and cost
- **Keep teams small** — 3–5 teammates for most workflows
- **5–6 tasks per teammate** — keeps everyone productive without excessive context switching
- **Keep spawn prompts focused** — every token in the spawn prompt is in the teammate's context from the start
- **Shut down teammates when done** — idle teammates keep consuming tokens until exited
- **Start with research/review tasks** — lower coordination overhead than parallel implementation

---

## Team Size Guidelines

| Scenario | Recommendation |
|:--|:--|
| Most workflows | 3–5 teammates |
| 15 independent tasks | 3 teammates (5 tasks each) |
| Research/investigation | 3–5, each with a distinct lens |
| Code review | 3 (security / performance / test coverage) |
| Competing hypotheses debug | 3–5, explicitly adversarial |

Scale up only when work genuinely benefits from simultaneity. Three focused teammates often outperform five scattered ones.

---

## Task Sizing

| Size | Problem |
|:--|:--|
| Too small | Coordination overhead exceeds the benefit |
| Too large | Teammates work too long without check-ins; risk of wasted effort |
| Just right | Self-contained unit producing a clear deliverable (a function, a test file, a review) |

---

## Best Practices

1. **Include task-specific context in the spawn prompt** — teammates don't inherit the lead's conversation history
2. **Give each teammate a distinct, non-overlapping domain** — prevents redundant work and file conflicts
3. **Avoid same-file edits across teammates** — two teammates editing the same file leads to overwrites
4. **Make investigation prompts adversarial** — explicitly tell teammates to challenge each other's theories
5. **Monitor and steer** — check in on progress, redirect approaches that aren't working
6. **Wait for teammates before implementing** — if the lead starts doing work instead of delegating, tell it to wait
7. **Use CLAUDE.md for project-wide guidance** — teammates read it from their working directory automatically
8. **Pre-approve common operations** — reduce permission prompt friction before spawning

---

## Limitations (Experimental)

| Limitation | Detail |
|:--|:--|
| No session resumption with in-process teammates | `/resume` and `/rewind` don't restore teammates; lead may message non-existent teammates — spawn new ones |
| Task status can lag | Teammates sometimes fail to mark tasks complete; check manually if stuck |
| Slow shutdown | Teammates finish their current request/tool call before shutting down |
| One team per session | Can't create additional named teams or share a team across sessions |
| No nested teams | Only the lead can spawn teammates; teammates cannot spawn their own |
| No background subagents from in-process teammates | `run_in_background` from an in-process teammate returns an error |
| Lead is fixed | Can't promote a teammate to lead or transfer leadership |
| Permissions set at spawn | Can be changed per-teammate afterward but not set at spawn time |
| Split panes require tmux or iTerm2 | Not supported in VS Code integrated terminal, Windows Terminal, or Ghostty |

---

## Troubleshooting

**Teammates not appearing:**
- In-process mode: look in the agent panel below the prompt input
- Hidden idle rows reappear on next turn — send the teammate a message by name to wake it
- Task may not have been complex enough to warrant teammates
- Check `which tmux` if you requested split panes

**Too many permission prompts:**
- Pre-approve common operations in permission settings before spawning

**Teammates stopping on errors:**
- Select teammate in panel → press Enter → review output
- Give additional instructions directly, or spawn a replacement
- v2.1.198+: a message from the lead wakes a teammate waiting on API retry

**Lead finishes before work is done:**
- Tell it to keep going
- Tell it to wait for teammates before proceeding

**Orphaned tmux sessions:**
```bash
tmux ls
tmux kill-session -t <session-name>
```

---

## Related Features

| Feature | When to use |
|:--|:--|
| [Subagents](/en/sub-agents) | Quick, focused workers that only report results back; no inter-agent coordination needed |
| [Git worktrees](/en/worktrees) | Manual parallel sessions without automated coordination |
| Plan mode (`Shift+Tab`) | Analyze before implementing; good for complex tasks within a single session |
