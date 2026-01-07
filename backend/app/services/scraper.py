import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.select("p")
    text = " ".join(p.get_text() for p in paragraphs)

    return {
        "title": soup.title.string if soup.title else "",
        "text": text,
        "raw_html": response.text
    }
