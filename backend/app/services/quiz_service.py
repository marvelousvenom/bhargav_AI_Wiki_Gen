from app.services.llm_service import generate_quiz_llm
from app.services.scraper import scrape_wikipedia


def reduce_text(text: str, max_chars: int = 6000) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars]


def process_quiz(url: str, db):
    scraped = scrape_wikipedia(url)

    reduced_text = reduce_text(scraped["text"])

    llm_output = generate_quiz_llm(reduced_text)

    return llm_output
