# To-Do List App

A simple, clean to-do list app built as a Claude artifact. No backend, no frameworks — just a focused tool that lets users add, check off, and delete tasks.

## What It Does

- Add tasks via a text input + "Add" button
- Mark tasks complete with a checkbox (instant visual feedback — strikethrough + greyed out)
- Delete tasks with a single click
- Works entirely in-browser with no page reloads

## What It Doesn't Do (By Design)

No categories, no due dates, no priorities, no accounts. Intentionally minimal.

## Project Structure

```
todo-app/
├── README.md           ← You're here
├── CLAUDE.md           ← Instructions for Claude when working on this project
├── docs/
│   └── brief.md        ← Original client brief
└── src/
    └── TodoApp.jsx     ← The app (single-file React component)
```

## Running / Viewing

The app is a self-contained React artifact rendered inside Claude. Open `src/TodoApp.jsx` and ask Claude to render it, or ask Claude to "show the to-do app."

## Design Decisions

- **Font:** Inter for its clean, neutral legibility — nothing distracts from the task list itself
- **Palette:** Off-white background (`#F8F8F6`), near-black text (`#1A1A1A`), muted slate for completed tasks
- **Signature element:** A thin left-border accent on each task item that disappears on completion — a subtle visual metaphor for a task "losing its importance"
- **No animations on delete** — instant removal feels more decisive and satisfying than a fade
