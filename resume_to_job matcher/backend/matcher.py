import re

# Broad keyword taxonomy covering tech, PM, data, and general professional roles
_KEYWORD_TAXONOMY: list[str] = [
    # Languages
    "python", "javascript", "typescript", "java", "c++", "c#", "go", "golang",
    "rust", "ruby", "swift", "kotlin", "scala", "r", "matlab", "php", "bash", "shell",
    # Web frameworks
    "react", "angular", "vue", "nextjs", "nuxt", "svelte", "django", "flask",
    "fastapi", "spring", "rails", "express", "laravel", "asp.net",
    # Cloud & infra
    "aws", "azure", "gcp", "google cloud", "heroku", "vercel", "netlify",
    "docker", "kubernetes", "k8s", "terraform", "ansible", "helm", "nginx",
    "lambda", "ec2", "s3", "rds", "cloudformation", "ci/cd", "github actions",
    "jenkins", "circleci", "gitlab",
    # Databases
    "sql", "postgresql", "mysql", "sqlite", "mongodb", "redis", "elasticsearch",
    "cassandra", "dynamodb", "bigquery", "snowflake", "dbt", "airflow",
    # Data & ML
    "pandas", "numpy", "scikit-learn", "sklearn", "tensorflow", "pytorch",
    "keras", "xgboost", "lightgbm", "spark", "hadoop", "kafka", "mlflow",
    "machine learning", "deep learning", "nlp", "computer vision", "llm",
    "data science", "data engineering", "analytics", "etl",
    # Product & design
    "product management", "product manager", "roadmap", "okr", "kpi",
    "a/b testing", "user research", "ux", "ui", "figma", "sketch", "wireframe",
    "customer discovery", "go-to-market", "gtm", "sprint", "backlog", "prd",
    # Analytics tools
    "amplitude", "mixpanel", "segment", "looker", "tableau", "power bi",
    "google analytics", "metabase", "grafana", "datadog",
    # Methodologies & soft skills
    "agile", "scrum", "kanban", "devops", "microservices", "rest", "graphql",
    "api", "sdk", "saas", "b2b", "b2c", "stakeholder", "cross-functional",
    "leadership", "mentoring", "communication",
    # Certifications / credentials (common)
    "aws certified", "pmp", "csm", "cpa", "mba", "phd", "six sigma",
]


def compute_keyword_match(resume_text: str, jd_text: str) -> dict:
    """
    ATS-style keyword match: find taxonomy keywords present in the JD,
    then check which of those are also in the resume.
    """
    jd_lower = jd_text.lower()
    resume_lower = resume_text.lower()

    # Extract capitalized acronyms from the JD (e.g. REST, SDK, API)
    acronyms = {a.lower() for a in re.findall(r"\b[A-Z]{2,6}\b", jd_text)}
    jd_keywords = {kw for kw in _KEYWORD_TAXONOMY if kw in jd_lower} | acronyms

    matched = {kw for kw in jd_keywords if kw in resume_lower}
    missing = jd_keywords - matched

    match_rate = round(len(matched) / len(jd_keywords) * 100, 1) if jd_keywords else 0.0

    return {
        "match_rate": match_rate,
        "matched_keywords": sorted(matched),
        "missing_keywords": sorted(missing),
        "total_jd_keywords": len(jd_keywords),
        "matched_count": len(matched),
    }
