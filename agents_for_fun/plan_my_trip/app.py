import streamlit as st
from datetime import date, timedelta
from agent import TripInput, generate_travel_plan

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🗺️",
    layout="centered",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 760px; }
    h1 { font-size: 1.6rem !important; font-weight: 600 !important; }
    .stButton > button {
        width: 100%; border-radius: 10px; padding: 0.6rem 1rem;
        font-weight: 500; font-size: 0.95rem;
    }
    .metric-row { display: flex; gap: 10px; margin-bottom: 1rem; }
    .metric-box {
        flex: 1; background: #f7f7f5; border-radius: 10px;
        padding: 12px 14px; border: 0.5px solid rgba(0,0,0,0.08);
    }
    .metric-label { font-size: 11px; color: #888; text-transform: uppercase; letter-spacing: 0.04em; }
    .metric-val { font-size: 18px; font-weight: 600; margin-top: 2px; }
    .day-slot { border-left: 2px solid #e0e0e0; padding-left: 12px; margin-bottom: 10px; }
    .day-slot.highlight { border-left-color: #1D9E75; }
    .slot-time { font-size: 11px; color: #888; }
    .slot-title { font-size: 14px; font-weight: 600; margin: 2px 0; }
    .slot-desc { font-size: 13px; color: #555; }
    .chip {
        display: inline-block; padding: 4px 10px; border-radius: 20px;
        background: #f0f0ee; border: 0.5px solid rgba(0,0,0,0.1);
        font-size: 12px; color: #555; margin: 3px 3px 3px 0;
    }
    .weather-box {
        background: #e6f1fb; border-radius: 10px; padding: 12px 14px;
        border: 0.5px solid rgba(24,95,165,0.25); color: #0c447c;
        font-size: 13px; margin-bottom: 1rem;
    }
    .hotel-box {
        background: #f7f7f5; border-radius: 10px; padding: 14px;
        border: 0.5px solid rgba(0,0,0,0.1); margin-bottom: 1rem;
    }
    .over-budget {
        background: #fcebeb; border-radius: 10px; padding: 10px 14px;
        border: 0.5px solid rgba(163,45,45,0.3); color: #a32d2d;
        font-size: 13px; margin-bottom: 10px;
    }
    .rec-box {
        border: 0.5px solid rgba(0,0,0,0.1); border-radius: 10px;
        padding: 12px 14px; margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)


# ── Header ─────────────────────────────────────────────────────────────────────
st.title("🗺️ AI Travel Planner")
st.caption("Personalized, budget-aware itineraries powered by Claude AI")
st.divider()


# ── Input form ─────────────────────────────────────────────────────────────────
with st.form("trip_form"):
    st.subheader("Trip Details")

    col1, col2 = st.columns(2)
    with col1:
        destination = st.text_input("Destination", placeholder="e.g. Manali, Himachal Pradesh")
    with col2:
        travelers = st.number_input("Travelers", min_value=1, max_value=20, value=2, step=1)

    col3, col4 = st.columns(2)
    with col3:
        start_date = st.date_input("Start Date", value=date.today() + timedelta(days=7))
    with col4:
        end_date = st.date_input("End Date", value=date.today() + timedelta(days=10))

    budget = st.number_input(
        "Total Budget (₹ INR)", min_value=1000, max_value=10_000_000,
        value=50000, step=1000, format="%d"
    )

    st.subheader("Travel Preference")
    preference = st.radio(
        label="Choose one",
        options=["🏖️ Pleasure", "☕ Leisure", "🙏 Spiritual", "🏔️ Adventure", "🌲 Isolated", "⚖️ Balanced"],
        horizontal=True,
        label_visibility="collapsed",
    )
    # Strip emoji for the prompt
    pref_clean = preference.split(" ", 1)[1]

    st.subheader("Accommodation")
    hotel_booked = st.toggle("I already have a hotel booked")

    hotel_name, hotel_area, hotel_stars = None, None, None
    if hotel_booked:
        hc1, hc2 = st.columns(2)
        with hc1:
            hotel_name = st.text_input("Hotel name", placeholder="e.g. The Taj Lake Palace")
        with hc2:
            hotel_area = st.text_input("Hotel area / locality", placeholder="e.g. Pichola Lake, Udaipur")
    else:
        hotel_stars = st.select_slider(
            "Preferred hotel category",
            options=["3★", "4★", "5★"],
            value="4★"
        ).replace("★", "")

    submitted = st.form_submit_button("✨ Generate My Travel Plan", use_container_width=True)


# ── Validation & generation ────────────────────────────────────────────────────
if submitted:
    errors = []
    if not destination.strip():
        errors.append("Please enter a destination.")
    if end_date <= start_date:
        errors.append("End date must be after start date.")
    if not budget:
        errors.append("Please enter a budget.")

    if errors:
        for e in errors:
            st.error(e)
        st.stop()

    trip = TripInput(
        destination=destination.strip(),
        start_date=str(start_date),
        end_date=str(end_date),
        travelers=int(travelers),
        budget_inr=int(budget),
        preference=pref_clean,
        hotel_booked=hotel_booked,
        hotel_name=hotel_name,
        hotel_area=hotel_area,
        hotel_stars=hotel_stars,
    )

    with st.spinner("Planning your trip..."):
        try:
            plan = generate_travel_plan(trip)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
            st.stop()

    # ── Results ────────────────────────────────────────────────────────────────
    st.divider()
    st.subheader(plan.get("tripTitle", "Your Travel Plan"))
    st.caption(plan.get("summary", ""))

    # Weather
    if plan.get("weather"):
        st.markdown(f'<div class="weather-box">🌤️ {plan["weather"]}</div>', unsafe_allow_html=True)

    # Hotel
    hotel = plan.get("hotel", {})
    if hotel:
        badge = "🤖 AI pick" if hotel.get("recommended") else "✅ Booked"
        stars_display = f"{hotel.get('stars', '')}★" if hotel.get("stars") not in ("user_provided", None) else ""
        nightly = hotel.get("estimatedCostPerNight")
        cost_line = f"Est. ₹{nightly:,}/night · " if nightly and hotel.get("recommended") else ""
        st.markdown(f"""
        <div class="hotel-box">
            <strong>{hotel.get('name', '')} {stars_display}</strong> &nbsp; <span style="font-size:12px; color:#888;">{badge}</span><br>
            <span style="font-size:12px; color:#888;">{hotel.get('area', '')}</span><br>
            <span style="font-size:13px; color:#555;">{cost_line}{hotel.get('whyPick', '')}</span>
        </div>
        """, unsafe_allow_html=True)

    # Cost breakdown
    st.subheader("💰 Cost Estimate")
    cb = plan.get("costBreakdown", {})
    total = cb.get("total", 0)
    over_budget = total > budget

    if over_budget:
        st.markdown(
            f'<div class="over-budget">⚠️ Estimated cost (₹{total:,}) exceeds your budget (₹{budget:,}). '
            f'Consider fewer days or a lower hotel category.</div>',
            unsafe_allow_html=True
        )

    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
    for col, label, key in [
        (mcol1, "Accommodation", "accommodation"),
        (mcol2, "Food", "food"),
        (mcol3, "Transport", "transport"),
        (mcol4, "Activities", "activities"),
    ]:
        with col:
            val = cb.get(key, 0)
            st.metric(label, f"₹{val:,}")

    color = "#a32d2d" if over_budget else "#1D9E75"
    st.markdown(
        f"<div style='text-align:right; font-size:14px; color:#888;'>Total estimate: "
        f"<strong style='color:{color};'>₹{total:,}</strong></div>",
        unsafe_allow_html=True
    )

    # Day-wise itinerary
    st.subheader("📅 Day-wise Itinerary")
    for day in plan.get("days", []):
        with st.expander(f"Day {day['dayNumber']} — {day.get('theme', '')}", expanded=(day["dayNumber"] == 1)):
            for slot in day.get("slots", []):
                cost_tag = f" · ₹{slot['estimatedCostPerPerson']:,}/person" if slot.get("estimatedCostPerPerson") else ""
                hl_class = "highlight" if slot.get("highlight") else ""
                st.markdown(f"""
                <div class="day-slot {hl_class}">
                    <div class="slot-time">{slot.get('time', '')}{cost_tag}</div>
                    <div class="slot-title">{slot.get('title', '')}</div>
                    <div class="slot-desc">{slot.get('description', '')}</div>
                </div>
                """, unsafe_allow_html=True)

    # Dining
    if plan.get("dining"):
        st.subheader("🍽️ Where to Eat")
        chips_html = "".join(f'<span class="chip">🍴 {d}</span>' for d in plan["dining"])
        st.markdown(chips_html, unsafe_allow_html=True)

    # Hidden gems
    if plan.get("hiddenGems"):
        st.subheader("💎 Hidden Gems")
        chips_html = "".join(f'<span class="chip">✦ {g}</span>' for g in plan["hiddenGems"])
        st.markdown(chips_html, unsafe_allow_html=True)

    # Personalized recs
    if plan.get("personalizedRecs"):
        st.subheader("⭐ Personalized For You")
        for rec in plan["personalizedRecs"]:
            st.markdown(f"""
            <div class="rec-box">
                <strong style="font-size:13px;">{rec.get('title', '')}</strong><br>
                <span style="font-size:12px; color:#555;">{rec.get('description', '')}</span>
            </div>
            """, unsafe_allow_html=True)

    # Travel tips
    if plan.get("travelTips"):
        st.subheader("💡 Travel Tips")
        for tip in plan["travelTips"]:
            st.markdown(f"- {tip}")
