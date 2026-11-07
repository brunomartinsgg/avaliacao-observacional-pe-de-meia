import requests
import re
from bs4 import BeautifulSoup

url = "https://portaldatransparencia.gov.br/download-de-dados/pe-de-meia"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, "html.parser")

print("--- Links encontrados na página ---")
links = []
for a in soup.find_all("a", href=True):
    href = a["href"]
    text = a.get_text(strip=True)
    if "download" in href.lower() or "pe-de-meia" in href.lower() or "zip" in href.lower() or "csv" in href.lower():
        print(f"TEXT: {text} | HREF: {href}")
        links.append(href)

# Procura padrões de URL de download direto (ex: /download-de-dados/pe-de-meia/202403)
matches = re.findall(r'https?://[^\s"\'>]+pe-de-meia[^\s"\'>]*', resp.text)
print("\n--- Regex matches ---")
for m in set(matches):
    print(m)
