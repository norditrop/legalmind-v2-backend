
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def google_search(query, num_results=10):
    try:
        search_url = f"https://html.duckduckgo.com/html/?q={query}"
        response = requests.get(search_url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")
        links = []

        for result in soup.select("a.result__a")[:num_results]:
            url = result.get("href")
            if url:
                links.append(url)

        return links
    except Exception as e:
        return {"erro": str(e)}

def summarize_links(links):
    summarized = []
    for url in links:
        try:
            resp = requests.get(url, headers=HEADERS, timeout=5)
            soup = BeautifulSoup(resp.text, "html.parser")
            title = soup.title.string.strip() if soup.title else "Sem título"
            domain = urlparse(url).netloc
            summary = {
                "url": url,
                "titulo": title,
                "fonte": domain
            }
            summarized.append(summary)
        except:
            continue
    return summarized

def busca_ativa(query):
    raw_links = google_search(query)
    return summarize_links(raw_links)
