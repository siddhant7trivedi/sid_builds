import anthropic
import json
import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class TripInput:
    destination: str
    start_date: str
    end_date: str
    travelers: int
    budget_inr: int
    preference: str
    hotel_booked: bool
    hotel_name: Optional[str] = None
    hotel_area: Optional[str] = None
    hotel_stars: Optional[str] = None  # "3", "4", or "5" — used only if not booked


def build_prompt(trip: TripInput) -> str:
    days = _count_days(trip.start_date, trip.end_date)

    hotel_context = (
        f"The traveler has already booked: {trip.hotel_name or 'a hotel'}, "
        f"located at {trip.hotel_area or 'unspecified area'}."
        if trip.hotel_booked
        else f"No hotel is booked yet. Recommend a suitable {trip.hotel_stars or '4'}-star hotel "
             f"that fits the destination and remaining budget."
    )

    return f"""You are an expert Indian travel planner. Return ONLY a valid JSON object — no markdown, no explanation, no preamble.

Trip details:
- Destination: {trip.destination}
- Dates: {trip.start_date} to {trip.end_date} ({days} days)
- Travelers: {trip.travelers}
- Total budget: ₹{trip.budget_inr:,}
- Travel preference: {trip.preference}
- Hotel: {hotel_context}

Return this exact JSON structure:
{{
  "tripTitle": "Short catchy title",
  "summary": "2-sentence overview of what makes this trip special",
  "weather": "Season and weather insight for {trip.destination} during these dates, with temperature range and packing tip",
  "hotel": {{
    "recommended": true or false,
    "name": "Hotel name",
    "area": "Area or locality",
    "stars": "{trip.hotel_stars or 'user_provided'}",
    "estimatedCostPerNight": <number in INR>,
    "whyPick": "One sentence on why this hotel fits the trip"
  }},
  "days": [
    {{
      "dayNumber": 1,
      "theme": "Short evocative theme for the day",
      "slots": [
        {{
          "time": "9:00 AM",
          "title": "Place or activity name",
          "description": "1–2 sentences with a practical tip or local insight",
          "highlight": true,
          "estimatedCostPerPerson": <number in INR>
        }}
      ]
    }}
  ],
  "dining": [
    "Restaurant or dish name — one-line reason why"
  ],
  "hiddenGems": [
    "Lesser-known spot or experience with a brief why"
  ],
  "costBreakdown": {{
    "accommodation": <total INR for all nights>,
    "food": <total INR for all travelers>,
    "transport": <total INR>,
    "activities": <total INR>,
    "total": <sum of above>
  }},
  "travelTips": [
    "Practical tip specific to this destination and preference"
  ],
  "personalizedRecs": [
    {{
      "title": "Recommendation title",
      "description": "Why it specifically fits this traveler's {trip.preference} preference"
    }}
  ]
}}

Rules:
- Use REAL place names in {trip.destination}
- All costs in INR, realistic for Indian travel
- Optimize the day flow geographically — minimize backtracking from the hotel
- Keep slot count to 4–6 per day (realistic pace)
- dining: exactly 3 items
- hiddenGems: 2–3 items
- travelTips: exactly 3 items
- personalizedRecs: exactly 3 items"""


def _count_days(start: str, end: str) -> int:
    from datetime import datetime
    fmt = "%Y-%m-%d"
    return (datetime.strptime(end, fmt) - datetime.strptime(start, fmt)).days + 1


def generate_travel_plan(trip: TripInput) -> dict:
    """
    Calls the Anthropic API and returns the parsed travel plan as a dict.
    Raises ValueError on JSON parse failure, re-raises API exceptions.
    """
    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[{"role": "user", "content": build_prompt(trip)}],
    )

    raw = message.content[0].text.strip()

    # Strip markdown fences if model adds them despite instructions
    raw = re.sub(r"^```json\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)

    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(f"Model returned invalid JSON: {e}\n\nRaw output:\n{raw}")
