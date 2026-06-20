import React, { useState } from "react";

const ACCENT = "#2D6A4F";
const BG = "#F5F5F0";
const BORDER = "#E5E5E3";
const TEXT_PRIMARY = "#1A1A1A";
const TEXT_MUTED = "#9CA3AF";

function TaskItem({ task, onToggle, onDelete, onEdit }) {
  const [editing, setEditing] = useState(false);
  const [editText, setEditText] = useState(task.text);

  const commitEdit = () => {
    const trimmed = editText.trim();
    if (trimmed) onEdit(task.id, trimmed);
    else setEditText(task.text);
    setEditing(false);
  };

  const handleEditKeyDown = (e) => {
    if (e.key === "Enter") commitEdit();
    if (e.key === "Escape") { setEditText(task.text); setEditing(false); }
  };

  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        gap: "12px",
        padding: "13px 16px",
        borderBottom: `1px solid ${BORDER}`,
        background: "#fff",
      }}
    >
      {/* Circular checkbox */}
      <button
        onClick={() => onToggle(task.id)}
        style={{
          width: "22px",
          height: "22px",
          borderRadius: "50%",
          border: task.completed ? "none" : `2px solid ${BORDER}`,
          background: task.completed ? ACCENT : "transparent",
          cursor: "pointer",
          flexShrink: 0,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          padding: 0,
        }}
      >
        {task.completed && (
          <svg width="12" height="9" viewBox="0 0 12 9" fill="none">
            <path d="M1 4L4.5 7.5L11 1" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        )}
      </button>

      {/* Task text or edit input */}
      {editing ? (
        <input
          autoFocus
          value={editText}
          onChange={(e) => setEditText(e.target.value)}
          onBlur={commitEdit}
          onKeyDown={handleEditKeyDown}
          style={{
            flex: 1,
            fontSize: "15px",
            color: TEXT_PRIMARY,
            border: `1px solid ${ACCENT}`,
            borderRadius: "4px",
            padding: "2px 6px",
            outline: "none",
            fontFamily: "inherit",
          }}
        />
      ) : (
        <span
          onDoubleClick={() => !task.completed && setEditing(true)}
          style={{
            flex: 1,
            fontSize: "15px",
            color: task.completed ? TEXT_MUTED : TEXT_PRIMARY,
            textDecoration: task.completed ? "line-through" : "none",
            cursor: task.completed ? "default" : "text",
            wordBreak: "break-word",
          }}
        >
          {task.text}
        </span>
      )}

      {/* Delete button */}
      <button
        onClick={() => onDelete(task.id)}
        title="Delete task"
        style={{
          background: "none",
          border: "none",
          cursor: "pointer",
          padding: "2px 4px",
          color: TEXT_MUTED,
          fontSize: "16px",
          lineHeight: 1,
          flexShrink: 0,
          opacity: 0.6,
        }}
      >
        ×
      </button>
    </div>
  );
}

export default function TodoApp() {
  const [tasks, setTasks] = useState([]);
  const [input, setInput] = useState("");

  const addTask = () => {
    const text = input.trim();
    if (!text) return;
    setTasks((prev) => [...prev, { id: Date.now(), text, completed: false }]);
    setInput("");
  };

  const toggleTask = (id) =>
    setTasks((prev) =>
      prev.map((t) => (t.id === id ? { ...t, completed: !t.completed } : t))
    );

  const deleteTask = (id) =>
    setTasks((prev) => prev.filter((t) => t.id !== id));

  const editTask = (id, text) =>
    setTasks((prev) => prev.map((t) => (t.id === id ? { ...t, text } : t)));

  const sortedTasks = [
    ...tasks.filter((t) => !t.completed),
    ...tasks.filter((t) => t.completed),
  ];

  const remaining = tasks.filter((t) => !t.completed).length;
  const total = tasks.length;

  return (
    <div
      style={{
        minHeight: "100vh",
        background: BG,
        display: "flex",
        justifyContent: "center",
        alignItems: "flex-start",
        padding: "64px 16px",
        fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
      }}
    >
      <div style={{ width: "100%", maxWidth: "420px" }}>
        {/* Header */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", marginBottom: "20px" }}>
          <h1 style={{ fontSize: "24px", fontWeight: 700, color: TEXT_PRIMARY, margin: 0, letterSpacing: "-0.4px" }}>
            To-Do
          </h1>
          {total > 0 && (
            <span style={{ fontSize: "14px", fontWeight: 600, color: ACCENT, letterSpacing: "0.5px" }}>
              {String(remaining).padStart(2, "0")} / {String(total).padStart(2, "0")}
            </span>
          )}
        </div>

        {/* Card */}
        <div style={{ background: "#fff", borderRadius: "12px", border: `1px solid ${BORDER}`, overflow: "hidden" }}>
          {/* Input row */}
          <div style={{ display: "flex", gap: "0", borderBottom: total > 0 ? `1px solid ${BORDER}` : "none" }}>
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && addTask()}
              placeholder="New task"
              style={{
                flex: 1,
                padding: "14px 16px",
                fontSize: "15px",
                border: "none",
                outline: "none",
                color: TEXT_PRIMARY,
                background: "transparent",
                fontFamily: "inherit",
              }}
            />
            <button
              onClick={addTask}
              style={{
                width: "48px",
                height: "48px",
                margin: "6px",
                background: ACCENT,
                color: "#fff",
                border: "none",
                borderRadius: "8px",
                cursor: "pointer",
                fontSize: "22px",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                flexShrink: 0,
              }}
            >
              +
            </button>
          </div>

          {/* Task list */}
          {sortedTasks.map((task) => (
            <TaskItem
              key={task.id}
              task={task}
              onToggle={toggleTask}
              onDelete={deleteTask}
              onEdit={editTask}
            />
          ))}

          {/* Footer: remaining count or empty state */}
          {total === 0 ? (
            <p style={{ textAlign: "center", color: TEXT_MUTED, fontSize: "14px", padding: "24px 16px", margin: 0 }}>
              Nothing here yet. Add a task above.
            </p>
          ) : (
            <div style={{ padding: "10px 16px", textAlign: "right" }}>
              <span style={{ fontSize: "13px", color: TEXT_MUTED }}>
                {remaining} remaining
              </span>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
