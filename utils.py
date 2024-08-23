import hashlib
import base64
from typing import Dict

# In-memory URL mapping
url_mapping: Dict[str, str] = {}

def shorten_url(long_url: str) -> str:
    """Shorten the given URL and return the short URL."""
    short_hash = hashlib.md5(long_url.encode()).digest()
    short_url = base64.urlsafe_b64encode(short_hash).decode().rstrip('=')
    url_mapping[short_url] = long_url
    return short_url

def expand_url(short_url: str) -> str:
    """Expand the given short URL back to the original URL."""
    return url_mapping.get(short_url)
