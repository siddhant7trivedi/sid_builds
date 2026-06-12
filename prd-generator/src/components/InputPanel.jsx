import ExampleChips from './ExampleChips'

export default function InputPanel({ value, onChange, onGenerate, onClear, isLoading }) {
  return (
    <div className="flex flex-col h-full gap-4 p-6 bg-gray-50 border-r border-gray-200 overflow-y-auto">
      <div>
        <div className="flex items-center gap-2 mb-4">
          <div className="w-2 h-2 rounded-full bg-gray-800" />
          <h1 className="text-base font-medium text-gray-900">PRD Generator</h1>
        </div>
        <p className="text-xs font-medium text-gray-400 uppercase tracking-wide mb-2">
          Feature idea
        </p>
        <textarea
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder="Describe the feature you want to build. Include the target user and business goal if you have them."
          className="w-full min-h-[200px] resize-y text-sm leading-relaxed p-3 rounded-lg border border-gray-200 bg-white text-gray-900 placeholder-gray-400 focus:outline-none focus:border-gray-400 transition-colors"
        />
      </div>

      <div className="flex gap-2">
        <button
          onClick={onGenerate}
          disabled={isLoading || !value.trim()}
          className="flex-1 flex items-center justify-center gap-2 px-4 py-2.5 bg-gray-900 text-white text-sm font-medium rounded-lg hover:bg-gray-700 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
        >
          {isLoading ? (
            <>
              <span className="inline-block w-3.5 h-3.5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
              Generating...
            </>
          ) : (
            'Generate PRD'
          )}
        </button>

        {value && !isLoading && (
          <button
            onClick={onClear}
            className="px-3 py-2.5 text-sm text-gray-500 border border-gray-200 rounded-lg hover:border-gray-400 hover:text-gray-700 transition-colors"
          >
            Clear
          </button>
        )}
      </div>

      <ExampleChips onSelect={onChange} />
    </div>
  )
}
