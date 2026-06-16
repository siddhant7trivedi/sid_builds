import type { Metadata } from "next";
import { Geist } from "next/font/google";
import "./globals.css";

const geist = Geist({ subsets: ["latin"], variable: "--font-geist-sans" });

export const metadata: Metadata = {
  title: "FeedbackLens",
  description: "Paste feedback. Get the signal.",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" className={geist.variable} suppressHydrationWarning>
      <head>
        <script
          dangerouslySetInnerHTML={{
            __html: `(function(){var s=localStorage.getItem('theme'),d=window.matchMedia('(prefers-color-scheme: dark)').matches;if(s==='dark'||(s===null&&d))document.documentElement.classList.add('dark');})();`,
          }}
        />
      </head>
      <body className="min-h-screen bg-zinc-50 dark:bg-zinc-950 transition-colors">
        {children}
      </body>
    </html>
  );
}
