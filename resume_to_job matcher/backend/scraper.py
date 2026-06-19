import requests
from bs4 import BeautifulSoup


_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

# CSS selectors tried in order — first match wins
_JD_SELECTORS = [
    {"class": "job-description"},
    {"class": "jobDescription"},
    {"class": "job_description"},
    {"class": "description__text"},          # LinkedIn
    {"class": "jobsearch-jobDescriptionText"},  # Indeed
    {"id": "job-description"},
    {"id": "jobDescription"},
    {"itemprop": "description"},
    {"class": "posting-description"},
    {"class": "content"},
]


def scrape_job_description(url: str) -> str:
    """Fetch and extract job description text from a URL."""
    try:
        resp = requests.get(url, headers=_HEADERS, timeout=20)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"Could not fetch URL ({e.response.status_code}): {url}") from e
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Network error fetching URL: {e}") from e

    soup = BeautifulSoup(resp.text, "lxml")

    for tag in soup(["script", "style", "nav", "header", "footer", "aside"]):
        tag.decompose()

    for selector in _JD_SELECTORS:
        el = soup.find(attrs=selector)
        if el:
            return _clean(el.get_text(separator="\n", strip=True))

    # Broad fallback: <main>, <article>, or <body>
    container = soup.find("main") or soup.find("article") or soup.body
    if container:
        return _clean(container.get_text(separator="\n", strip=True))

    return _clean(soup.get_text(separator="\n", strip=True))


def _clean(text: str) -> str:
    import re

    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()
