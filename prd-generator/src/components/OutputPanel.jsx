import { useState, useRef } from 'react'
import ReactMarkdown from 'react-markdown'

export default function OutputPanel({ output, isLoading }) {
  const [copied, setCopied] = useState(false)
  const [exporting, setExporting] = useState(false)
  const contentRef = useRef(null)

  const wordCount = output ? output.split(/\s+/).filter(Boolean).length : 0

  const handleCopy = () => {
    if (!output) return
    navigator.clipboard.writeText(output)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  const handleExportPDF = async () => {
    if (!output || !contentRef.current) return
    setExporting(true)
    try {
      const html2pdf = (await import('html2pdf.js')).default
      await html2pdf()
        .set({
          margin: [12, 14],
          filename: 'prd.pdf',
          image: { type: 'jpeg', quality: 0.98 },
          html2canvas: { scale: 2 },
          jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' },
        })
        .from(contentRef.current)
        .save()
    } catch (err) {
      console.error('PDF export error:', err)
    } finally {
      setExporting(false)
    }
  }

  return (
    <div className="flex flex-col p-6 bg-white overflow-hidden" style={{ height: '100%' }}>
      <p className="text-xs font-medium text-gray-400 uppercase tracking-wide mb-4 shrink-0">
        Output
      </p>

      <div className="flex-1 overflow-y-auto">
        {!output && !isLoading ? (
          <div className="flex flex-col items-center justify-center h-full gap-2 text-gray-400">
            <svg xmlns="http://www.w3.org/2000/svg" className="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            <p className="text-sm">Your PRD will appear here</p>
          </div>
        ) : (
          <div ref={contentRef} className="prose prose-sm prose-gray max-w-none text-gray-800">
            <ReactMarkdown>{output}</ReactMarkdown>
            {isLoading && (
              <span className="inline-block w-2 h-4 bg-gray-400 animate-pulse ml-0.5 align-text-bottom" />
            )}
          </div>
        )}
      </div>

      {output && !isLoading && (
        <div className="flex items-center gap-2 pt-4 border-t border-gray-100 mt-4 shrink-0">
          <span className="text-xs text-gray-400">{wordCount} words</span>

          <div className="ml-auto flex items-center gap-2">
            <button
              onClick={handleExportPDF}
              disabled={exporting}
              className="flex items-center gap-1.5 text-xs text-gray-500 border border-gray-200 rounded-md px-3 py-1.5 hover:border-gray-400 transition-colors disabled:opacity-40"
            >
              {exporting ? (
                <>
                  <span className="inline-block w-3 h-3 border-2 border-gray-400/30 border-t-gray-400 rounded-full animate-spin" />
                  Exporting...
                </>
              ) : (
                <>
                  <svg xmlns="http://www.w3.org/2000/svg" className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                  </svg>
                  Export PDF
                </>
              )}
            </button>

            <button
              onClick={handleCopy}
              className="flex items-center gap-1.5 text-xs text-gray-500 border border-gray-200 rounded-md px-3 py-1.5 hover:border-gray-400 transition-colors"
            >
              {copied ? (
                <>
                  <svg xmlns="http://www.w3.org/2000/svg" className="w-3.5 h-3.5 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                  </svg>
                  Copied
                </>
              ) : (
                <>
                  <svg xmlns="http://www.w3.org/2000/svg" className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                  </svg>
                  Copy
                </>
              )}
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
