import os
import time
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TARGET_DIR = BASE_DIR / "dados_brutos" / "ideb_saeb"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

URL = "https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/ideb/resultados"

def collect_ideb():
    print(f"Navegando em {URL} via Playwright...", flush=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, wait_until="domcontentloaded", timeout=30000)
        time.sleep(3)

        # Clicar em expansíveis se existirem
        elems = page.query_selector_all("a[href], button")
        for el in elems:
            try:
                txt = el.text_content().strip()
                if "Ensino Médio" in txt or "Municípios" in txt or "2023" in txt or "2021" in txt:
                    el.click()
                    time.sleep(0.5)
            except:
                pass

        links = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('a[href]')).map(a => a.href);
        }""")

        ideb_links = [l for l in links if "inep.gov.br" in l and any(ext in l.lower() for ext in [".xlsx", ".xls", ".zip", ".csv"])]
        ideb_links = sorted(list(set(ideb_links)))

        print(f"Links do IDEB descobertos: {len(ideb_links)}", flush=True)
        for l in ideb_links:
            print(f" -> {l}", flush=True)

        browser.close()

        downloaded = 0
        for l in ideb_links:
            filename = l.split("/")[-1]
            rel_dest = os.path.normpath(f"dados_brutos/ideb_saeb/{filename}")
            full_dest = TARGET_DIR / filename

            if full_dest.exists() and full_dest.stat().st_size > 1000:
                print(f"[JA EXISTE] {filename} ({full_dest.stat().st_size / 1024:.1f} KB)", flush=True)
                downloaded += 1
                continue

            print(f"Baixando {filename} via curl.exe...", flush=True)
            cmd = ["curl.exe", "-k", "-L", "-s", "-o", rel_dest, l]
            subprocess.run(cmd, cwd=str(BASE_DIR))

            if full_dest.exists() and full_dest.stat().st_size > 1000:
                print(f"[OK] {filename} salvo com sucesso! ({full_dest.stat().st_size / (1024*1024):.2f} MB)", flush=True)
                downloaded += 1

        print(f"\nFinalizada a coleta do IDEB/SAEB. Arquivos salvos: {downloaded}", flush=True)

if __name__ == "__main__":
    collect_ideb()
