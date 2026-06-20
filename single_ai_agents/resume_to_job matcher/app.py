import os

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from backend.matcher import compute_keyword_match
from backend.ollama_client import OLLAMA_MODEL, analyze_match, check_ollama_connection
from backend.parser import parse_resume
from backend.scraper import scrape_job_description

# ── Page config ──────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Resume-to-Job Match Analyzer",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────────

st.markdown(
    """
<style>
    .block-container { padding-top: 2rem; }

    .score-ring {
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        width: 160px; height: 160px; border-radius: 50%;
        margin: 0 auto 1.5rem auto; font-weight: 800;
    }
    .score-high  { background: radial-gradient(circle, #d1fae5, #6ee7b7); color: #065f46; }
    .score-mid   { background: radial-gradient(circle, #fef9c3, #fde68a); color: #78350f; }
    .score-low   { background: radial-gradient(circle, #fee2e2, #fca5a5); color: #7f1d1d; }
    .score-num   { font-size: 3rem; line-height: 1; }
    .score-label { font-size: 0.8rem; letter-spacing: 0.05em; margin-top: 2px; }

    .tag {
        display: inline-block; padding: 3px 10px; border-radius: 999px;
        font-size: 0.78rem; font-weight: 600; margin: 2px;
    }
    .tag-green { background: #d1fae5; color: #065f46; }
    .tag-red   { background: #fee2e2; color: #7f1d1d; }
    .tag-gray  { background: #f3f4f6; color: #374151; }

    .section-header {
        font-size: 1.1rem; font-weight: 700; margin: 1rem 0 0.5rem 0;
        border-left: 4px solid #6366f1; padding-left: 0.6rem; color: #1e1b4b;
    }
    .card {
        background: #f8fafc; border: 1px solid #e2e8f0;
        border-radius: 10px; padding: 1rem 1.2rem; margin-bottom: 0.75rem;
    }
</style>
""",
    unsafe_allow_html=True,
)

# ── Sidebar ───────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("## ⚙️ Settings")

    is_running, available_models = check_ollama_connection()

    if is_running:
        st.success("Ollama is running", icon="✅")
        model_options = available_models if available_models else [OLLAMA_MODEL]
        chosen_model = st.selectbox("Model", model_options, index=0)
    else:
        st.error("Ollama not detected", icon="❌")
        st.markdown(
            """
**Start Ollama:**
```bash
ollama serve
```
**Pull a model:**
```bash
ollama pull llama3
ollama pull mistral
ollama pull phi3
```
""",
        )
        chosen_model = st.text_input("Model name", value=OLLAMA_MODEL)

    st.divider()
    st.markdown("### About")
    st.markdown(
        "100% local · No API keys · "
        "Your resume never leaves your machine."
    )
    st.markdown(
        "[GitHub](https://github.com/your-username/resume-job-match) · "
        "[Report issue](https://github.com/your-username/resume-job-match/issues)"
    )

# ── Header ────────────────────────────────────────────────────────────────────

st.markdown("# 🎯 Resume-to-Job Match Analyzer")
st.markdown(
    "Upload your resume, add a job description, and get an instant ATS-style fit score "
    "with actionable improvement suggestions — all running locally via Ollama."
)
st.divider()

# ── Inputs ────────────────────────────────────────────────────────────────────

col_resume, col_jd = st.columns(2, gap="large")

with col_resume:
    st.markdown("### 📄 Your Resume")
    uploaded_file = st.file_uploader(
        "Upload PDF or DOCX",
        type=["pdf", "docx"],
        help="Your resume is parsed locally — nothing is sent to any server.",
    )

with col_jd:
    st.markdown("### 💼 Job Description")
    jd_source = st.radio(
        "Input method",
        ["Paste text", "Enter URL"],
        horizontal=True,
        label_visibility="collapsed",
    )

    if jd_source == "Paste text":
        jd_input = st.text_area(
            "Paste the job description here",
            height=280,
            placeholder="Paste the full job description...",
        )
        jd_url = None
    else:
        jd_url = st.text_input(
            "Job posting URL",
            placeholder="https://www.linkedin.com/jobs/view/...",
        )
        jd_input = None

st.divider()

# ── Analyze button ────────────────────────────────────────────────────────────

analyze_clicked = st.button(
    "⚡ Analyze Match",
    type="primary",
    use_container_width=True,
    disabled=not is_running,
)

if not is_running:
    st.info("Start Ollama and pull a model to enable analysis (see sidebar).", icon="ℹ️")

# ── Analysis pipeline ─────────────────────────────────────────────────────────

if analyze_clicked:
    # Validate inputs
    errors = []
    if not uploaded_file:
        errors.append("Please upload your resume (PDF or DOCX).")
    if jd_source == "Paste text" and not (jd_input or "").strip():
        errors.append("Please paste a job description.")
    if jd_source == "Enter URL" and not (jd_url or "").strip():
        errors.append("Please enter a job posting URL.")

    for err in errors:
        st.error(err)

    if not errors:
        with st.status("Analyzing your resume...", expanded=True) as status:

            # Step 1 — Parse resume
            st.write("📄 Parsing resume...")
            try:
                resume_text = parse_resume(
                    uploaded_file.getvalue(), uploaded_file.name
                )
            except Exception as e:
                st.error(f"Resume parsing failed: {e}")
                st.stop()

            if not resume_text.strip():
                st.error(
                    "Could not extract text from your resume. "
                    "Make sure it is not image-only (scanned). "
                    "Try converting to DOCX or a text-based PDF."
                )
                st.stop()

            # Step 2 — Get JD text
            st.write("💼 Loading job description...")
            try:
                if jd_source == "Enter URL":
                    jd_text = scrape_job_description(jd_url.strip())
                else:
                    jd_text = jd_input.strip()
            except Exception as e:
                st.error(f"Could not load job description: {e}")
                st.stop()

            if not jd_text.strip():
                st.error("Job description appears to be empty after loading.")
                st.stop()

            # Step 3 — ATS keyword pre-scan
            st.write("🔍 Running ATS keyword scan...")
            keyword_data = compute_keyword_match(resume_text, jd_text)

            # Step 4 — LLM deep analysis
            st.write(f"🤖 Sending to {chosen_model} for deep analysis...")
            try:
                result = analyze_match(
                    resume_text, jd_text, keyword_data, model=chosen_model
                )
            except RuntimeError as e:
                st.error(str(e))
                st.stop()

            status.update(label="Analysis complete!", state="complete", expanded=False)

        # ── Results ──────────────────────────────────────────────────────────

        st.divider()
        st.markdown("## 📊 Your Results")

        fit_score = int(result.get("fit_score", keyword_data["match_rate"]))
        summary = result.get("summary", "")

        # Score ring + summary
        res_col, sum_col = st.columns([1, 2], gap="large")

        with res_col:
            if fit_score >= 75:
                ring_cls = "score-high"
                verdict = "Strong Match"
            elif fit_score >= 50:
                ring_cls = "score-mid"
                verdict = "Moderate Match"
            else:
                ring_cls = "score-low"
                verdict = "Weak Match"

            st.markdown(
                f"""
<div class="score-ring {ring_cls}">
    <span class="score-num">{fit_score}%</span>
    <span class="score-label">{verdict}</span>
</div>
""",
                unsafe_allow_html=True,
            )

        with sum_col:
            st.markdown("#### Overall Assessment")
            if summary:
                st.markdown(summary)

            breakdown = result.get("score_breakdown", {})
            if breakdown:
                st.markdown("**Score Breakdown**")
                labels = {
                    "skills_match": "Skills Match",
                    "experience_match": "Experience",
                    "education_match": "Education",
                    "keyword_density": "Keyword Density",
                }
                for key, label in labels.items():
                    val = int(breakdown.get(key, 0))
                    st.markdown(f"`{label}`")
                    st.progress(val / 100, text=f"{val}%")

        st.divider()

        # Detail tabs
        tab_strengths, tab_gaps, tab_improve, tab_ats = st.tabs(
            ["✅ Strengths", "🔴 Gaps", "💡 Improvements", "⚙️ ATS Tips"]
        )

        with tab_strengths:
            strengths = result.get("strengths", [])
            if strengths:
                for item in strengths:
                    st.markdown(f"- {item}")
            else:
                st.info("No strengths identified.")

            # Matched keywords
            if keyword_data["matched_keywords"]:
                st.markdown('<div class="section-header">Matched Keywords</div>', unsafe_allow_html=True)
                tags = "".join(
                    f'<span class="tag tag-green">{kw}</span>'
                    for kw in keyword_data["matched_keywords"]
                )
                st.markdown(tags, unsafe_allow_html=True)

        with tab_gaps:
            gaps = result.get("gaps", {})

            missing_skills = gaps.get("missing_skills", [])
            if missing_skills:
                st.markdown('<div class="section-header">Missing Skills / Experience</div>', unsafe_allow_html=True)
                for item in missing_skills:
                    st.markdown(f"- {item}")

            missing_certs = gaps.get("missing_certifications", [])
            if missing_certs:
                st.markdown('<div class="section-header">Recommended Certifications</div>', unsafe_allow_html=True)
                for item in missing_certs:
                    st.markdown(f"- {item}")

            missing_kw = keyword_data["missing_keywords"]
            if missing_kw:
                st.markdown('<div class="section-header">Missing Keywords (ATS scan)</div>', unsafe_allow_html=True)
                tags = "".join(
                    f'<span class="tag tag-red">{kw}</span>'
                    for kw in missing_kw
                )
                st.markdown(tags, unsafe_allow_html=True)

            if not missing_skills and not missing_certs and not missing_kw:
                st.success("No significant gaps detected — great match!")

        with tab_improve:
            suggestions = result.get("improvement_suggestions", [])
            if suggestions:
                for i, item in enumerate(suggestions, 1):
                    st.markdown(
                        f'<div class="card"><b>{i}.</b> {item}</div>',
                        unsafe_allow_html=True,
                    )
            else:
                st.info("No improvement suggestions generated.")

        with tab_ats:
            ats_tips = result.get("ats_tips", [])
            if ats_tips:
                for tip in ats_tips:
                    st.markdown(f"- {tip}")
            else:
                st.info("No ATS tips generated.")

        # Raw data expander for debugging
        with st.expander("🛠 Raw analysis data"):
            st.json(result)
            st.markdown("**Keyword scan**")
            st.json(keyword_data)
            st.markdown("**Resume text (first 1000 chars)**")
            st.code(resume_text[:1000])
