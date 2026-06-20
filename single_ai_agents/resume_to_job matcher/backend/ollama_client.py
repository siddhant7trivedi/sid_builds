import json
import os

import requests

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")

_PROMPT_TEMPLATE = """\
You are a senior ATS (Applicant Tracking System) analyst and career coach. \
Analyze the resume against the job description below and return a structured JSON assessment.

### RESUME
{resume_text}

### JOB DESCRIPTION
{jd_text}

### ATS PRE-SCAN (already computed)
- Keywords matched: {matched_keywords}
- Keywords missing from resume: {missing_keywords}
- Keyword match rate: {match_rate}%

Return ONLY a valid JSON object — no markdown fences, no extra text — using exactly this schema:
{{
  "fit_score": <integer 0-100>,
  "score_breakdown": {{
    "skills_match": <integer 0-100>,
    "experience_match": <integer 0-100>,
    "education_match": <integer 0-100>,
    "keyword_density": <integer 0-100>
  }},
  "strengths": [<3-5 specific strengths as strings>],
  "gaps": {{
    "missing_keywords": [<list of important missing keywords>],
    "missing_skills": [<skills or experience the JD requires but resume lacks>],
    "missing_certifications": [<certifications the role wants, or empty list>]
  }},
  "improvement_suggestions": [<4-6 concrete, role-specific resume edits as strings>],
  "ats_tips": [<3-5 ATS formatting and keyword optimization tips as strings>],
  "summary": "<2-3 sentence overall assessment of fit>"
}}"""


def check_ollama_connection() -> tuple[bool, list[str]]:
    """Return (is_running, list_of_model_names)."""
    try:
        resp = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        if resp.status_code == 200:
            models = [m["name"] for m in resp.json().get("models", [])]
            return True, models
    except Exception:
        pass
    return False, []


def analyze_match(
    resume_text: str,
    jd_text: str,
    keyword_data: dict,
    model: str | None = None,
) -> dict:
    """
    Send resume + JD to Ollama and return a structured analysis dict.
    Raises RuntimeError on connection failure or unparseable response.
    """
    model = model or OLLAMA_MODEL

    prompt = _PROMPT_TEMPLATE.format(
        resume_text=resume_text[:4000],
        jd_text=jd_text[:2500],
        matched_keywords=", ".join(keyword_data.get("matched_keywords", [])) or "none detected",
        missing_keywords=", ".join(keyword_data.get("missing_keywords", [])) or "none detected",
        match_rate=keyword_data.get("match_rate", 0),
    )

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.1,
            "num_predict": 2048,
        },
    }

    try:
        resp = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json=payload,
            timeout=180,
        )
        resp.raise_for_status()
    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            "Cannot connect to Ollama. Make sure it is running: `ollama serve`"
        )
    except requests.exceptions.Timeout:
        raise RuntimeError(
            "Ollama took too long to respond. Try a lighter model (mistral, phi3)."
        )
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"Ollama API error: {e}")

    raw = resp.json().get("response", "")
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Last-ditch: find the first { ... } block in the response
        import re

        match = re.search(r"\{.*\}", raw, re.DOTALL)
        if match:
            return json.loads(match.group())
        raise RuntimeError(
            "Ollama returned a response that could not be parsed as JSON. "
            "Try a different model or reduce input length."
        )
