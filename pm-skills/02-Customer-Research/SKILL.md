---
name: customer-research
description: "Use this skill when conducting customer research — including user interviews, surveys, JTBD analysis, persona development, and insight synthesis. Trigger when the user wants to understand customer needs, pain points, behaviors, or motivations before building or prioritizing features. Also use when synthesizing qualitative research into product decisions. Bias toward AI product user research patterns."
---

# Customer Research Skill

## Purpose
Convert raw customer signals into crisp, decision-ready product insights — not just quotes and observations.

---

## Core Principles

1. **Behavior > Opinion** — What users DO matters more than what they SAY
2. **Problems before solutions** — Never lead with your feature hypothesis
3. **Look for the workaround** — The hacky solution they use today reveals the real need
4. **Segment your insights** — One persona does not fit all; identify who said what
5. **Close the loop** — Every research round should update a documented assumption

---

## Research Methods Matrix

| Method | Best For | Time Investment | Signal Type |
|--------|----------|-----------------|-------------|
| Discovery Interviews | Deep problem understanding | High | Qualitative |
| Usability Testing | UX/flow validation | Medium | Behavioral |
| Survey | Quantify qualitative signals | Medium | Quantitative |
| Contextual Inquiry | Observe real workflow | High | Behavioral |
| Diary Study | Longitudinal behavior | High | Behavioral |
| Jobs-to-be-Done Interview | Understand switching triggers | High | Qualitative |

---

## Interview Workflow

### Before the Interview
- [ ] Define the research question (1 clear question per session)
- [ ] Recruit participants from the right segment (min 5 per persona)
- [ ] Prepare a discussion guide (not a script)
- [ ] Brief note-taker separately from interviewer

### During the Interview
- Open with context-setting, not your hypothesis
- Use the **5 Whys** to go deeper on pain points
- Ask about **past behavior** not hypothetical future behavior
- Ask: "Walk me through the last time you did X"
- Silence is okay — let them fill it

### After the Interview
- Tag notes within 24 hours (don't rely on memory)
- Code against: Problem / Behavior / Outcome / Workaround / Quote
- Update assumption log

---

## JTBD Framework (Jobs-to-be-Done)

### The Hiring Statement
> "When I [situation], I want to [motivation], so I can [outcome]."

### Functional vs. Emotional vs. Social Jobs
- **Functional**: The practical task (e.g., "summarize this 50-page contract")
- **Emotional**: How they want to feel (e.g., "confident before the client meeting")
- **Social**: How they want to be perceived (e.g., "look like the expert in the room")

### Switching Triggers
- What caused them to look for a new solution?
- What was the "last straw" moment?
- What almost stopped them from switching?

---

## Insight Synthesis Process

### Step 1 — Affinity Mapping
Group raw notes into themes (use FigJam, Miro, or sticky notes)

### Step 2 — Pattern Extraction
- What problems appear across 3+ participants?
- What workarounds are most common?
- Where is frustration highest?

### Step 3 — Insight Statement Formulation
> "[User segment] struggles with [problem] when [context], which leads to [negative outcome]. They currently [workaround], but it fails because [limitation]."

### Step 4 — Opportunity Framing
Convert insight → opportunity statement:
> "How might we help [user] to [achieve outcome] without [current pain]?"

### Step 5 — Update Assumptions Log
Mark which assumptions were confirmed, invalidated, or newly surfaced.

---

## GenAI-Specific Research Considerations

- **AI Trust Gap**: Ask about skepticism toward AI outputs — it's a real adoption barrier
- **Explainability needs**: Do users need to understand WHY the AI said X?
- **Oversight behavior**: How much do users verify AI outputs? In what contexts?
- **Prompt literacy**: What's their current comfort with prompting?
- **Workflow integration**: Where does AI fit in their existing tool stack?

---

## Quality Checks

- [ ] Research question was defined before interviews started
- [ ] Minimum 5 interviews per target segment
- [ ] Insights are behavioral, not just attitudinal
- [ ] Each insight is tied to a product assumption or decision
- [ ] JTBD statements are documented for top 2–3 jobs
- [ ] Workarounds and switching triggers are captured
