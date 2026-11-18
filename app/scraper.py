import ipaddress
import socket
from urllib.parse import urlparse
import httpx
from bs4 import BeautifulSoup

MAX_HTML_CHARS = 30000
TIMEOUT_SECONDS = 15

def _validate_public_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("Only valid http:// and https:// website URLs are accepted.")
    host = parsed.hostname.lower()
    if host in {"localhost"} or host.endswith(".local"):
        raise ValueError("Local network addresses are not allowed.")
    try:
        addresses = socket.getaddrinfo(host, None)
        for item in addresses:
            ip = ipaddress.ip_address(item[4][0])
            if not ip.is_global:
                raise ValueError("Private or non-public IP addresses are not allowed.")
    except socket.gaierror:
        raise ValueError("The website hostname could not be resolved.")

async def fetch_website(url: str) -> dict:
    _validate_public_url(url)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; WebsiteLinkAnalyzer/1.0)"}
    try:
        async with httpx.AsyncClient(
            timeout=TIMEOUT_SECONDS,
            follow_redirects=True,
            headers=headers,
        ) as client:
            response = await client.get(url)
            response.raise_for_status()
    except httpx.HTTPError as exc:
        raise RuntimeError(f"Could not fetch the website: {exc.__class__.__name__}") from exc

    content_type = response.headers.get("content-type", "")
    if "text/html" not in content_type.lower():
        raise ValueError("The supplied URL did not return an HTML page.")

    soup = BeautifulSoup(response.text, "html.parser")
    for element in soup(["script", "style", "noscript", "svg"]):
        element.decompose()

    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    description_tag = soup.find("meta", attrs={"name": "description"})
    meta_description = description_tag.get("content", "").strip() if description_tag else ""
    headings = [
        item.get_text(" ", strip=True)
        for item in soup.find_all(["h1", "h2", "h3"])[:30]
        if item.get_text(" ", strip=True)
    ]
    links = []
    for anchor in soup.find_all("a", href=True)[:100]:
        label = anchor.get_text(" ", strip=True)
        href = anchor["href"].strip()
        if label or href:
            links.append({"text": label[:160], "href": href[:500]})

    text_content = " ".join(soup.stripped_strings)
    return {
        "final_url": str(response.url),
        "title": title[:300],
        "meta_description": meta_description[:1000],
        "headings": headings,
        "page_text": text_content[:MAX_HTML_CHARS],
        "links": links,
    }
