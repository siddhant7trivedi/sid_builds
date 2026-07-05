import json
import re

import ollama

MODEL = "llama3.1:latest"

_SYSTEM = """\
You are a thoughtful dream interpretation assistant trained in Jungian psychology \
and modern psychological frameworks. You interpret dreams through two lenses and \
return your analysis as a JSON object with exactly two string keys:
  "jungian"           — archetypes present, shadow elements, individuation themes
  "modern_psychology" — emotional processing, cognitive framing, waking-life stress patterns

Language rules (strictly enforced):
- Use hedged, interpretive language throughout: "this may suggest", "one interpretation is",
  "this could reflect", "it's possible that".
- Never use definitive framing: avoid "this means", "you have", "this proves", "you are".
- If the dream is vague or very short, give a proportionally shorter analysis —
  do not invent elaboration to sound thorough.
- Return ONLY valid JSON. No markdown fences, no preamble, no trailing text.\
"""


def interpret_dream(dream_text: str) -> dict[str, str]:
    user_msg = (
        f'Interpret this dream:\n\n"""\n{dream_text.strip()}\n"""\n\n'
        'Return JSON with keys "jungian" and "modern_psychology".'
    )

    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": _SYSTEM},
            {"role": "user", "content": user_msg},
        ],
        format="json",
    )

    # Handle both object-style (ollama >= 0.2) and dict-style responses
    if hasattr(response, "message"):
        content = response.message.content
    else:
        content = response["message"]["content"]

    return _parse(content)


def _parse(raw: str) -> dict[str, str]:
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass
        return {
            "jungian": raw.strip(),
            "modern_psychology": "(Structured response could not be parsed — full response shown above.)",
        }
