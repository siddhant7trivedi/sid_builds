"use client";

import { useState, useEffect } from "react";

type FeedbackTheme = {
  name: string;
  count: number;
  quotes: string[];
};

type AnalysisResult = {
  sentiment: "positive" | "mixed" | "negative";
  summary: string;
  themes: FeedbackTheme[];
  standout_quotes: string[];
};

const SENTIMENT = {
  positive: {
    label: "Positive",
    cls: "bg-emerald-100 text-emerald-800 dark:bg-emerald-900/40 dark:text-emerald-300",
    dot: "bg-emerald-500",
  },
  mixed: {
    label: "Mixed",
    cls: "bg-amber-100 text-amber-800 dark:bg-amber-900/40 dark:text-amber-300",
    dot: "bg-amber-500",
  },
  negative: {
    label: "Negative",
    cls: "bg-red-100 text-red-800 dark:bg-red-900/40 dark:text-red-300",
    dot: "bg-red-500",
  },
};

export default function Home() {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [error, setError] = useState("");
  const [expandedTheme, setExpandedTheme] = useState<number | null>(null);
  const [dark, setDark] = useState(false);

  useEffect(() => {
    setDark(document.documentElement.classList.contains("dark"));
  }, []);

  const toggleTheme = () => {
    const next = !dark;
    setDark(next);
    document.documentElement.classList.toggle("dark", next);
    localStorage.setItem("theme", next ? "dark" : "light");
  };

  const analyze = async () => {
    if (!text.trim()) return;
    setLoading(true);
    setError("");
    setResult(null);
    setExpandedTheme(null);

    try {
      const res = await fetch("/api/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.error || "Analysis failed");
      }

      setResult(data);
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if ((e.metaKey || e.ctrlKey) && e.key === "Enter") analyze();
  };

  return (
    <div className="min-h-screen text-zinc-900 dark:text-zinc-100">
      <div className="max-w-2xl mx-auto px-5 py-12">
        {/* Header */}
        <div className="flex items-start justify-between mb-10">
          <div>
            <h1 className="text-xl font-semibold tracking-tight text-zinc-900 dark:text-zinc-100">
              FeedbackLens
            </h1>
            <p className="text-sm text-zinc-400 dark:text-zinc-500 mt-0.5">
              Paste feedback. Get the signal.
            </p>
          </div>
          <button
            onClick={toggleTheme}
            className="mt-0.5 p-2 rounded-lg text-zinc-400 hover:text-zinc-600 dark:hover:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors"
            aria-label="Toggle theme"
          >
            {dark ? <SunIcon /> : <MoonIcon />}
          </button>
        </div>

        {/* Input */}
        <div className="space-y-3">
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Paste your feedback here — NPS responses, G2 reviews, Capterra comments, support tickets. Any format works."
            className="w-full h-48 px-4 py-3 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900 text-sm text-zinc-700 dark:text-zinc-300 placeholder-zinc-400 dark:placeholder-zinc-600 resize-none focus:outline-none focus:ring-2 focus:ring-zinc-300 dark:focus:ring-zinc-700 transition-colors"
          />
          <div className="flex items-center justify-between">
            <span className="text-xs text-zinc-400 dark:text-zinc-600">
              ⌘ + Enter to analyze
            </span>
            <button
              onClick={analyze}
              disabled={loading || !text.trim()}
              className="px-5 py-2.5 rounded-xl bg-zinc-900 dark:bg-zinc-100 text-zinc-50 dark:text-zinc-900 text-sm font-medium hover:bg-zinc-700 dark:hover:bg-zinc-300 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
            >
              {loading ? "Analyzing…" : "Analyze feedback"}
            </button>
          </div>
        </div>

        {/* Error */}
        {error && (
          <div className="mt-6 px-4 py-3 rounded-xl bg-red-50 dark:bg-red-950/50 border border-red-200 dark:border-red-900 text-red-700 dark:text-red-400 text-sm">
            {error}
          </div>
        )}

        {/* Loading skeleton */}
        {loading && (
          <div className="mt-10 space-y-4 animate-pulse">
            <div className="p-5 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900 space-y-3">
              <div className="h-5 w-24 bg-zinc-200 dark:bg-zinc-800 rounded-full" />
              <div className="space-y-2">
                <div className="h-3.5 bg-zinc-100 dark:bg-zinc-800 rounded w-full" />
                <div className="h-3.5 bg-zinc-100 dark:bg-zinc-800 rounded w-4/5" />
                <div className="h-3.5 bg-zinc-100 dark:bg-zinc-800 rounded w-3/5" />
              </div>
            </div>
            <div className="space-y-2">
              {[...Array(5)].map((_, i) => (
                <div
                  key={i}
                  className="h-12 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl"
                />
              ))}
            </div>
          </div>
        )}

        {/* Results */}
        {result && !loading && (
          <div className="mt-10 space-y-6">
            {/* Sentiment + Summary */}
            <div className="p-5 rounded-xl bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800">
              <div className="flex items-center gap-2.5 mb-3">
                <span
                  className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold ${SENTIMENT[result.sentiment].cls}`}
                >
                  <span
                    className={`w-1.5 h-1.5 rounded-full ${SENTIMENT[result.sentiment].dot}`}
                  />
                  {SENTIMENT[result.sentiment].label}
                </span>
                <span className="text-xs text-zinc-400 dark:text-zinc-500">
                  overall sentiment
                </span>
              </div>
              <p className="text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed">
                {result.summary}
              </p>
            </div>

            {/* Themes */}
            <div>
              <p className="text-xs font-semibold uppercase tracking-widest text-zinc-400 dark:text-zinc-500 mb-3">
                Top Themes
              </p>
              <div className="space-y-2">
                {result.themes.map((theme, i) => (
                  <div
                    key={i}
                    className="rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900 overflow-hidden"
                  >
                    <button
                      onClick={() =>
                        setExpandedTheme(expandedTheme === i ? null : i)
                      }
                      className="w-full flex items-center justify-between px-4 py-3 text-left hover:bg-zinc-50 dark:hover:bg-zinc-800/50 transition-colors"
                    >
                      <div className="flex items-center gap-3">
                        <span className="w-5 h-5 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-500 dark:text-zinc-400 text-xs font-medium flex items-center justify-center flex-shrink-0">
                          {i + 1}
                        </span>
                        <span className="text-sm font-medium text-zinc-800 dark:text-zinc-200">
                          {theme.name}
                        </span>
                      </div>
                      <div className="flex items-center gap-2 flex-shrink-0">
                        <span className="text-xs text-zinc-400 dark:text-zinc-500">
                          {theme.count} mention{theme.count !== 1 ? "s" : ""}
                        </span>
                        <ChevronIcon
                          className={`text-zinc-400 transition-transform duration-200 ${
                            expandedTheme === i ? "rotate-180" : ""
                          }`}
                        />
                      </div>
                    </button>
                    {expandedTheme === i && (
                      <div className="px-4 pb-4 space-y-2.5 border-t border-zinc-100 dark:border-zinc-800 pt-3">
                        {theme.quotes.map((quote, j) => (
                          <p
                            key={j}
                            className="text-sm text-zinc-500 dark:text-zinc-400 italic pl-3 border-l-2 border-zinc-200 dark:border-zinc-700 leading-relaxed"
                          >
                            &ldquo;{quote}&rdquo;
                          </p>
                        ))}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>

            {/* Standout Quotes */}
            <div>
              <p className="text-xs font-semibold uppercase tracking-widest text-zinc-400 dark:text-zinc-500 mb-3">
                Standout Quotes
              </p>
              <div className="space-y-2.5">
                {result.standout_quotes.map((quote, i) => (
                  <blockquote
                    key={i}
                    className="px-4 py-3 rounded-xl bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 text-sm text-zinc-500 dark:text-zinc-400 italic leading-relaxed"
                  >
                    &ldquo;{quote}&rdquo;
                  </blockquote>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

function SunIcon() {
  return (
    <svg
      width="18"
      height="18"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={1.5}
        d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364-6.364-.707.707M6.343 17.657l-.707.707M17.657 17.657l-.707-.707M6.343 6.343l-.707-.707M12 8a4 4 0 1 1 0 8 4 4 0 0 1 0-8z"
      />
    </svg>
  );
}

function MoonIcon() {
  return (
    <svg
      width="18"
      height="18"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={1.5}
        d="M20.354 15.354A9 9 0 0 1 8.646 3.646 9.003 9.003 0 0 0 12 21a9.003 9.003 0 0 0 8.354-5.646z"
      />
    </svg>
  );
}

function ChevronIcon({ className }: { className?: string }) {
  return (
    <svg
      className={`w-4 h-4 ${className}`}
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={2}
        d="M19 9l-7 7-7-7"
      />
    </svg>
  );
}
