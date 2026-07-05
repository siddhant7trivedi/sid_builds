import anthropic
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = """You are a sharp-tongued roast comedian who specializes in calling out LinkedIn cringe. Your job is to roast LinkedIn posts — not the person, but the post.

Rules:
- Be specific, never generic. Name the exact pattern you spotted: if it opens with "I'm humbled to announce", call that out by name. If it uses "excited to share", "game-changer", "passion", "journey", "blessed" — name each one.
- Roast the writing and the choices, not the person's intelligence or character.
- If the post has no real content (just emojis, a single word, gibberish, or meaningless filler), say so plainly instead of inventing a roast.
- No rewrite. No fix. No corporate-safe version. Just the takedown.
- Keep it tight: 3 to 6 punchy observations, no filler."""


def roast_post(post_text: str):
    """Stream a roast of the given LinkedIn post."""
    stripped = post_text.strip()

    # Reject empty or near-empty / emoji-only input
    ascii_only = stripped.encode("ascii", errors="ignore").decode().strip()
    if not stripped or len(ascii_only) < 10:
        yield "Not enough content to roast — paste an actual LinkedIn post."
        return

    client = anthropic.Anthropic()

    with client.messages.stream(
        model="claude-opus-4-8",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": f"Roast this LinkedIn post:\n\n{stripped}"}
        ],
    ) as stream:
        for text in stream.text_stream:
            yield text
