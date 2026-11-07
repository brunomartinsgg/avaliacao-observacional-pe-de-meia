import os
import time
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright


BASE_DIR = Path(__file__).resolve().parent.parent.parent
TARGET_DIR = BASE_DIR / "dados_brutos" / "censo_escolar"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

URL = "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-rendimento-escolar"

def run_playwright_inep():
    print(f"Navegando via Playwright em {URL}...", flush=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, wait_until="domcontentloaded", timeout=30000)

        time.sleep(3)

        # Clicar em todas as abas / expansíveis de anos se existirem
        collapsibles = page.query_selector_all(".collapsibleHeader, .accordion-toggle, details, summary, tab")
        for c in collapsibles:
            try:
                c.click()
                time.sleep(0.5)
            except:
                pass

        # Extrair todos os links href da página inteira
        links = page.evaluate("""() => {
            const arr = [];
            document.querySelectorAll('a[href]').forEach(a => {
                arr.push(a.href);
            });
            return arr;
        }""")

        inep_download_links = [l for l in links if "inep.gov.br" in l and any(ext in l.lower() for ext in [".zip", ".xlsx", ".xls", ".csv"])]
        inep_download_links = sorted(list(set(inep_download_links)))

        print(f"\nLinks de download INEP descobertos ({len(inep_download_links)}):", flush=True)
        for l in inep_download_links:
            print(f" -> {l}", flush=True)

        browser.close()

        # Baixar cada um dos links descobertos com curl.exe
        for l in inep_download_links:
            filename = l.split("/")[-1]
            rel_dest = os.path.normpath(f"dados_brutos/censo_escolar/{filename}")
            full_dest = TARGET_DIR / filename

            if full_dest.exists() and full_dest.stat().st_size > 1000:
                print(f"[JA EXISTE] {filename} ({full_dest.stat().st_size / 1024:.1f} KB)", flush=True)
                continue

            print(f"Baixando {filename} via curl.exe...", flush=True)
            cmd = ["curl.exe", "-k", "-L", "-s", "-o", rel_dest, l]
            subprocess.run(cmd, cwd=str(BASE_DIR))
            if full_dest.exists() and full_dest.stat().st_size > 1000:
                print(f"[OK] {filename} salvo com sucesso! ({full_dest.stat().st_size / (1024*1024):.2f} MB)", flush=True)
            else:
                print(f"[ERRO] {filename} falhou no download.", flush=True)


if __name__ == "__main__":
    run_playwright_inep()
