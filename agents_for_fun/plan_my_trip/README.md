# 🗺️ AI Travel Planner
### *Generate personalized, budget-aware travel itineraries for any destination in India — in seconds.*

> Part of [`sid_builds`](https://github.com/siddhant7trivedi/sid_builds) — AI agents built for real PM and developer workflows.

---

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Claude](https://img.shields.io/badge/Claude-Sonnet-D97706?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-22c55e?style=for-the-badge)

---

## ⚡ What This Does

**AI Travel Planner** is a single-agent tool that takes your destination, travel dates, budget, and preferences — and generates a complete, ready-to-use trip plan — so that travelers can skip hours of research and get a personalized itinerary instantly, without juggling 10 browser tabs.

**Built for:** `Travelers · Trip planners · Anyone exploring India on a budget`

---

## 💡 Why I Built This

As a PM, I noticed that travel planning is one of the most fragmented user experiences — you need Google Maps for routes, TripAdvisor for attractions, Zomato for food, MakeMyTrip for hotels, and a spreadsheet to track costs. No single tool personalizes across all these dimensions simultaneously.

This agent solves it by taking one structured input and returning a complete, opinionated plan that accounts for budget, travel style, geography, and accommodation — all in one shot. Building this taught me how to design prompts that enforce structured JSON output reliably, and how to separate agent logic from UI concerns cleanly.

---

## 🧠 How It Works

```
[User Input] ──► [TripInput dataclass] ──► [Prompt Builder] ──► [Claude Sonnet API] ──► [JSON Plan] ──► [Streamlit UI]
```

1. **Input collection** — Streamlit form captures destination, dates, travelers, budget, travel preference (Pleasure / Leisure / Spiritual / Adventure / Isolated / Balanced), and hotel status
2. **Prompt construction** — `agent.py` builds a structured prompt with explicit rules: real place names, INR pricing, geographic flow optimization, and strict JSON schema
3. **AI generation** — Claude Sonnet processes the prompt and returns a structured travel plan covering itinerary, hotel recommendation, cost breakdown, dining, hidden gems, and personalized tips
4. **Rendering** — `app.py` parses the JSON and renders it as a day-wise collapsible UI with budget alerts and metric cards

---

## 🖥️ Demo

> Add a screenshot after first run: `assets/demo.png`

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| **Frontend** | Streamlit |
| **LLM Backend** | Claude Sonnet (`claude-sonnet-4-6` via Anthropic API) |
| **Language** | Python 3.10+ |
| **Key Libraries** | `anthropic`, `streamlit` |

---

## 🚀 Getting Started

### Prerequisites

```bash
# Set your Anthropic API key
export ANTHROPIC_API_KEY=your_key_here
```

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/siddhant7trivedi/sid_builds.git
cd sid_builds/single_ai_agents/ai_travel_planner

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

---

## 📂 Folder Structure

```
ai_travel_planner/
├── app.py              # Streamlit UI — form, rendering, layout
├── agent.py            # Core agent logic — prompt builder + API call
├── requirements.txt
├── assets/
│   └── demo.png        # Add after first run
└── README.md
```

---

## 🔍 Sample Output

```
Trip: Manali, 4 days, ₹40,000, 2 travelers, Adventure

Day 1 — Arrival & Acclimatization
  10:00 AM  Check in at The Orchard Greens Resort (Old Manali)
  12:30 PM  Lunch at Drifter's Café — wood-fired pizza with mountain views
  03:00 PM  Walk the Old Manali trail up to Manu Temple
  06:00 PM  Sunset at Hadimba Devi Temple complex

Day 2 — Solang Valley & Snow
  08:00 AM  Drive to Solang Valley (30 min from hotel)
  09:30 AM  Zorbing or snow activities (seasonal) — ₹600/person
  ...

Cost Breakdown:
  Accommodation  ₹12,000  (₹3,000/night × 4)
  Food           ₹8,000
  Transport      ₹6,000
  Activities     ₹4,000
  ─────────────────────
  Total          ₹30,000  ✅ Under budget
```

---

## 🗺️ Roadmap

- [x] MVP — day-wise itinerary, cost breakdown, hotel recommendation, dining, hidden gems
- [ ] Interactive map with Folium — visualize route from hotel to each attraction
- [ ] Live weather via OpenWeatherMap API
- [ ] Hotel availability check via RapidAPI
- [ ] Export itinerary as PDF
- [ ] Multi-city trip planning

---

## 🔗 More from sid_builds

| Agent | What It Does |
|---|---|
| [PRD Generator](../prd_generator) | Generate structured PRDs from a problem statement |
| [Resume-Job Matcher](../resume_job_match_analyzer) | Score resume fit against a job description |
| [AI Travel Planner](../ai_travel_planner) | Personalized travel itineraries with budget tracking |

---

## 📄 License

MIT — free to use, adapt, and build on.

---

<div align="center">

**Built by [Sid](https://github.com/siddhant7trivedi) · [LinkedIn](https://www.linkedin.com/in/siddhant7trivedi/)**

*If this was useful, star the repo ⭐*

</div>
