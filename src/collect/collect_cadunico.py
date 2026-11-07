import os
import time
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TARGET_DIR = BASE_DIR / "dados_brutos" / "cadunico"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

SAGICAD_URL = "https://aplicacoes.mds.gov.br/sagi-paineis/analise_dados_abertos/"
PBF_CAD_URL = "https://aplicacoes.cidadania.gov.br/ri/pbfcad/painel.html"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def collect_cadunico():
    print("Iniciando verificação de bases do CadÚnico / Sagicad...", flush=True)

    # Tentar capturar via Playwright para renderizar seletores JS
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(user_agent=HEADERS["User-Agent"])
            page = context.new_page()

            print(f"Navegando para {SAGICAD_URL}...", flush=True)
            page.goto(SAGICAD_URL, wait_until="networkidle", timeout=30000)
            time.sleep(3)

            # Procurar por links de exportação CSV ou XLS na página renderizada
            export_links = page.query_selector_all("a[href*='export'], a[href*='csv'], a[href*='xlsx']")
            print(f"Links de exportação previstos no Sagicad: {len(export_links)}", flush=True)

            for i, link in enumerate(export_links):
                href = link.get_attribute("href") or ""
                if href.startswith("http") or href.endswith((".csv", ".xlsx", ".zip")):
                    dest = TARGET_DIR / f"sagicad_export_{i+1}.csv"
                    if not dest.exists():
                        resp = page.request.get(href)
                        if resp.status == 200:
                            with open(str(dest), "wb") as f:
                                f.write(resp.body())
                            print(f"[OK] Exportação Sagicad salva em {dest.name}", flush=True)

            browser.close()
    except Exception as e:
        print(f"[AVISO] Raspagem CadÚnico via Playwright: {e}", flush=True)

if __name__ == "__main__":
    collect_cadunico()
