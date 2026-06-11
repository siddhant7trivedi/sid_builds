# CLAUDE.md — Working Instructions for This Project

This file tells Claude how to work on the To-Do List App. Read this before making any changes.

---

## Project Identity

A minimal to-do app. The brief is intentionally tight. Do not add features unless the user explicitly asks. The product's quality is its restraint.

**In scope:** add tasks, check off tasks, delete tasks.  
**Out of scope (do not add):** categories, due dates, priorities, filters, sorting, drag-to-reorder, local storage persistence, accounts, animations beyond the checkbox state change.

---

## Tech Stack

- **Single file React component** — `src/TodoApp.jsx`
- Rendered as a Claude artifact (no build step, no bundler)
- Available libraries in the artifact environment: React (useState), Tailwind (core utility classes only — no JIT/custom config), lucide-react for icons if needed
- No external API calls, no localStorage (not supported in Claude artifacts)

---

## Design Tokens

| Token | Value | Usage |
|---|---|---|
| Background | `#F8F8F6` | Page background |
| Surface | `#FFFFFF` | Task card / input area |
| Text primary | `#1A1A1A` | Active task text |
| Text muted | `#9CA3AF` | Completed task text |
| Accent | `#4F46E5` | Checkbox checked state, Add button |
| Border | `#E5E5E3` | Dividers, input borders |
| Delete hover | `#EF4444` | Delete icon on hover only |

**Typography:** Inter (system stack fallback: `-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`)  
**Border radius:** `8px` for cards, `6px` for buttons/inputs  
**Signature element:** A `3px` left border on each task item in the accent color — removed when task is completed

---

## Component Structure

```
<TodoApp>
  <Header />           — App title only. No subtitle. No branding.
  <InputRow />         — Text input + "Add" button, side by side
  <TaskList>
    <TaskItem />       — Checkbox | Task text | Delete icon (hover-reveal)
  </TaskList>
  <EmptyState />       — Shown when task list is empty: "Nothing here yet. Add a task above."
</TodoApp>
```

---

## Behaviour Rules

1. **Add:** Pressing Enter in the input OR clicking "Add" appends a new task. Empty/whitespace input is ignored (no error shown — just do nothing).
2. **Complete:** Clicking the checkbox immediately applies strikethrough + muted text colour. No delay, no animation required.
3. **Delete:** Clicking the delete icon removes the task immediately. No confirmation dialog.
4. **Completed tasks** sink to the bottom of the list (optional enhancement — ask before implementing).
5. **Input clears** after a task is added.

---

## Code Style

- Functional components only
- `useState` for all state (task list)
- Each task object: `{ id: Date.now(), text: string, completed: boolean }`
- Inline styles preferred over Tailwind for design-token-sensitive properties (colours, border accents)
- Tailwind utilities fine for spacing, flex, cursor, transition
- No prop drilling deeper than one level; everything lives in `TodoApp`

---

## What to Check Before Shipping Any Change

- [ ] Empty state shows when list is empty
- [ ] Add does nothing on blank input
- [ ] Checkbox toggles instantly
- [ ] Delete removes immediately
- [ ] Left-border accent absent on completed tasks
- [ ] No horizontal scroll on narrow viewports
