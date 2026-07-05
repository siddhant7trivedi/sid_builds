import streamlit as st

from agent import interpret_dream

st.set_page_config(page_title="Dream Interpreter", page_icon="🌙", layout="wide")

st.title("🌙 Dream Interpreter")
st.caption("Describe your dream. Get a Jungian + modern psychology reading — running fully local.")

dream_input = st.text_area(
    "Your dream",
    placeholder="I was standing in a house I didn't recognise, but somehow knew it was mine. The rooms kept shifting…",
    height=160,
)

interpret_clicked = st.button("Interpret Dream", type="primary", disabled=not dream_input.strip())

if interpret_clicked and dream_input.strip():
    with st.spinner("Interpreting your dream locally…"):
        try:
            result = interpret_dream(dream_input)
        except Exception as exc:
            error_msg = str(exc)
            if "connection" in error_msg.lower() or "refused" in error_msg.lower():
                st.error(
                    "Could not reach Ollama. Make sure Ollama is running (`ollama serve`) "
                    "and `llama3.1:8b` is pulled (`ollama pull llama3.1:8b`)."
                )
            else:
                st.error(f"Something went wrong: {exc}")
            st.stop()

    jungian = result.get("jungian", "").strip()
    modern = result.get("modern_psychology", "").strip()

    left, right = st.columns(2, gap="large")

    with left:
        st.subheader("🔮 Jungian Lens")
        st.markdown(
            f"""<div style="background:#1a1a2e;border-left:4px solid #7c5cbf;
            padding:1.3rem 1.5rem;border-radius:8px;color:#e8e0f0;
            font-size:1.0rem;line-height:1.8;white-space:pre-wrap;">{jungian}</div>""",
            unsafe_allow_html=True,
        )

    with right:
        st.subheader("🧠 Modern Psychology Lens")
        st.markdown(
            f"""<div style="background:#0f2027;border-left:4px solid #2cb8b8;
            padding:1.3rem 1.5rem;border-radius:8px;color:#dff2f2;
            font-size:1.0rem;line-height:1.8;white-space:pre-wrap;">{modern}</div>""",
            unsafe_allow_html=True,
        )

    st.caption(
        "This is an interpretive reading, not a clinical diagnosis. "
        "Language is intentionally hedged — treat it as a reflective prompt, not a verdict."
    )
