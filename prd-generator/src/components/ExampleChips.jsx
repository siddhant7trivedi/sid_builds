import { EXAMPLE_INPUTS } from '../constants/systemPrompt'

export default function ExampleChips({ onSelect }) {
  const labels = [
    'Email summarization',
    'Adaptive onboarding',
    'Auto-tagging tickets',
  ]

  return (
    <div className="mt-3">
      <p className="text-xs font-medium text-gray-400 uppercase tracking-wide mb-2">
        Try an example
      </p>
      <div className="flex flex-col gap-2">
        {EXAMPLE_INPUTS.map((example, i) => (
          <button
            key={i}
            onClick={() => onSelect(example)}
            className="text-left text-sm text-gray-600 bg-white border border-gray-200 rounded-lg px-3 py-2 hover:border-gray-400 hover:text-gray-900 transition-colors"
          >
            {labels[i]}
          </button>
        ))}
      </div>
    </div>
  )
}
