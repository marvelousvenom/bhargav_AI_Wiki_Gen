from urllib.parse import urlparse

def validate_wikipedia_url(url: str) -> bool:
    parsed = urlparse(url)
    return (
        parsed.scheme in ["http", "https"]
        and "wikipedia.org/wiki/" in parsed.netloc + parsed.path
    )
