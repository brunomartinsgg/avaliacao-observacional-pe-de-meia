import os
import re
import time
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TARGET_DIR = BASE_DIR / "dados_brutos" / "censo_escolar"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

INEP_TAXAS_URL = "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-rendimento-escolar"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def collect_inep_taxas():
    print("Iniciando download das Taxas de Rendimento do INEP (2022-2025)...", flush=True)

    years = ["2022", "2023", "2024", "2025"]
    types = [
        "tx_rend_brasil_regioes_ufs",
        "tx_rend_municipios",
        "tx_rend_escolas"
    ]

    downloaded = 0
    for yr in years:
        for tp in types:
            filename = f"{tp}_{yr}.zip"
            dest_path = TARGET_DIR / filename
            if dest_path.exists() and dest_path.stat().st_size > 1000:
                print(f"[JA EXISTE] {filename} ({dest_path.stat().st_size / 1024:.1f} KB)", flush=True)
                downloaded += 1
                continue

            url = f"https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/{yr}/{tp}_{yr}.zip"
            print(f"Tentando baixar {filename} de {url}...", flush=True)

            try:
                # Tentar via requests com SSL e retentativas
                r = requests.get(url, headers=HEADERS, stream=True, timeout=30, verify=False)
                if r.status_code == 200:
                    with open(str(dest_path), "wb") as f:
                        for chunk in r.iter_content(chunk_size=1024*1024):
                            if chunk:
                                f.write(chunk)
                    print(f"[OK] Taxas salvas com sucesso: {filename} ({dest_path.stat().st_size / (1024*1024):.2f} MB)", flush=True)
                    downloaded += 1
                else:
                    print(f"[HTTP {r.status_code}] {filename}", flush=True)
            except Exception as e:
                print(f"[ERRO] {filename}: {e}", flush=True)

    print(f"\nFinalizada coleta de Taxas de Rendimento INEP. Arquivos válidos: {downloaded}", flush=True)


    # 2. Se via requests não veio tudo, tentar via Playwright
    print("Iniciando raspagem avançada via Playwright...", flush=True)
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(INEP_TAXAS_URL, wait_until="networkidle", timeout=30000)
            time.sleep(3)

            # Procurar por todos os elementos de link ou abas de anos
            elements = page.query_selector_all("a[href]")
            found_count = 0
            for el in elements:
                href = el.get_attribute("href") or ""
                if any(ext in href.lower() for ext in [".zip", ".xlsx", ".xls", ".csv"]) and "inep.gov.br" in href:
                    filename = href.split("/")[-1]
                    dest_path = TARGET_DIR / filename
                    if not dest_path.exists():
                        print(f"Baixando via Playwright request: {filename}...", flush=True)
                        resp = page.request.get(href)
                        if resp.status == 200:
                            with open(str(dest_path), "wb") as f:
                                f.write(resp.body())
                            print(f"[OK] Download via Playwright: {filename}", flush=True)
                            found_count += 1
            browser.close()
            print(f"Finalizada coleta INEP via Playwright: {found_count} novos arquivos.", flush=True)
    except Exception as e:
        print(f"[ERRO] Playwright INEP: {e}", flush=True)

if __name__ == "__main__":
    collect_inep_taxas()
