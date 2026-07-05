import streamlit as st
from agent import roast_post

st.set_page_config(page_title="RoastIN", page_icon="🔥", layout="centered")

st.title("RoastIN 🔥")
st.caption("Paste any LinkedIn post. Get a roast.")

post_input = st.text_area(
    "LinkedIn post",
    placeholder="Paste the LinkedIn post here...",
    height=220,
    label_visibility="collapsed",
)

if st.button("Roast It", type="primary", use_container_width=True):
    if not post_input.strip():
        st.warning("Paste a LinkedIn post first.")
    else:
        st.divider()
        st.subheader("The Roast")
        st.write_stream(roast_post(post_input))
