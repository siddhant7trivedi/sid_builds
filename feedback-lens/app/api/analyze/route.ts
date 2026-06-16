import Anthropic from "@anthropic-ai/sdk";
import { NextRequest, NextResponse } from "next/server";

const SYSTEM_PROMPT = `You are a product feedback analyst. Analyze the provided customer feedback and return structured JSON.

Rules:
- Identify the top 5 recurring themes, ranked by frequency
- For each theme: count how many reviews mention it and pull 2-3 short, exact quotes from the actual text
- Assess overall sentiment across all feedback as "positive", "mixed", or "negative"
- Write a 2-3 sentence summary a product manager could paste directly into a stakeholder update — direct, no jargon
- Pick 3-4 standout quotes that are the most impactful and quotable

Return ONLY valid JSON, no other text:
{
  "sentiment": "positive" | "mixed" | "negative",
  "summary": "2-3 sentence stakeholder-ready summary",
  "themes": [
    {
      "name": "Theme name in 2-5 words",
      "count": 8,
      "quotes": ["exact short quote", "another exact quote"]
    }
  ],
  "standout_quotes": ["quote 1", "quote 2", "quote 3"]
}`;

export async function POST(request: NextRequest) {
  const apiKey = process.env.ANTHROPIC_API_KEY;

  if (!apiKey) {
    return NextResponse.json(
      {
        error:
          "ANTHROPIC_API_KEY not set. Copy .env.local.example to .env.local and add your key.",
      },
      { status: 500 }
    );
  }

  try {
    const { text } = await request.json();

    if (!text?.trim()) {
      return NextResponse.json(
        { error: "No feedback text provided." },
        { status: 400 }
      );
    }

    const client = new Anthropic({ apiKey });

    const message = await client.messages.create({
      model: "claude-sonnet-4-6",
      max_tokens: 1500,
      system: SYSTEM_PROMPT,
      messages: [
        {
          role: "user",
          content: `Analyze this customer feedback:\n\n${text}`,
        },
      ],
    });

    const content = message.content[0];
    if (content.type !== "text") {
      throw new Error("Unexpected response type from model");
    }

    const jsonMatch = content.text.match(/\{[\s\S]*\}/);
    if (!jsonMatch) {
      throw new Error("Could not parse analysis response");
    }

    const result = JSON.parse(jsonMatch[0]);
    return NextResponse.json(result);
  } catch (err) {
    console.error("Analysis error:", err);
    return NextResponse.json(
      {
        error:
          err instanceof Error ? err.message : "Analysis failed. Try again.",
      },
      { status: 500 }
    );
  }
}
