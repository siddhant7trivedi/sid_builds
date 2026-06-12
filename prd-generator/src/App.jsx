import { useState } from 'react'
import OpenAI from 'openai'
import InputPanel from './components/InputPanel'
import OutputPanel from './components/OutputPanel'
import { SYSTEM_PROMPT } from './constants/systemPrompt'

const client = new OpenAI({
  baseURL: 'https://models.inference.ai.azure.com',
  apiKey: import.meta.env.VITE_GITHUB_TOKEN,
  dangerouslyAllowBrowser: true,
})

export default function App() {
  const [input, setInput] = useState('')
  const [output, setOutput] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const handleGenerate = async () => {
    if (!input.trim() || isLoading) return

    setIsLoading(true)
    setOutput('')

    try {
      const stream = await client.chat.completions.create({
        model: 'gpt-4o',
        max_tokens: 2048,
        stream: true,
        messages: [
          { role: 'system', content: SYSTEM_PROMPT },
          { role: 'user', content: input },
        ],
      })

      for await (const chunk of stream) {
        const text = chunk.choices[0]?.delta?.content ?? ''
        if (text) setOutput((prev) => prev + text)
      }
    } catch (err) {
      console.error('API error:', err)
      setOutput('Error generating PRD. Check your GitHub token and try again.')
    } finally {
      setIsLoading(false)
    }
  }

  const handleClear = () => {
    setInput('')
    setOutput('')
  }

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-6">
      <div className="w-full max-w-5xl bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
        <div className="grid grid-cols-2" style={{ height: '85vh' }}>
          <InputPanel
            value={input}
            onChange={setInput}
            onGenerate={handleGenerate}
            onClear={handleClear}
            isLoading={isLoading}
          />
          <OutputPanel
            output={output}
            isLoading={isLoading}
          />
        </div>
      </div>
    </div>
  )
}
