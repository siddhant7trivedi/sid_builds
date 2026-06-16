export type FeedbackTheme = {
  name: string;
  count: number;
  quotes: string[];
};

export type AnalysisResult = {
  sentiment: "positive" | "mixed" | "negative";
  summary: string;
  themes: FeedbackTheme[];
  standout_quotes: string[];
};

export const SENTIMENT = {
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
