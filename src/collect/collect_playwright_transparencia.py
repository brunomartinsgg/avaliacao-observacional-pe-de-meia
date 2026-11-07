import os
import sys
import time
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TARGET_DIR = BASE_DIR / "dados_brutos" / "pe_de_meia_transparencia"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

def get_target_months():
    months = []
    current_year = datetime.now().year
    current_month = datetime.now().month
    for yr in range(2024, current_year + 1):
        end_m = current_month if yr == current_year else 12
        for m in range(1, end_m + 1):
            months.append(f"{yr}{m:02d}")
    return months

def collect_with_playwright():
    from playwright.sync_api import sync_playwright

    months = get_target_months()
    print(f"Iniciando coleta via Playwright para {len(months)} meses...", flush=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            accept_downloads=True
        )
        page = context.new_page()

        # Primeiro navegar para a página principal para obter cookies/tokens WAF
        print("Navegando para o Portal da Transparência para resolver WAF/Session...", flush=True)
        try:
            page.goto("https://portaldatransparencia.gov.br/download-de-dados/pe-de-meia", wait_until="networkidle", timeout=30000)
            time.sleep(3)
        except Exception as e:
            print(f"[AVISO] Navegação inicial: {e}", flush=True)

        downloaded_count = 0
        for yyyymm in months:
            dest_file = TARGET_DIR / f"{yyyymm}_PeDeMeia.zip"
            if dest_file.exists() and dest_file.stat().st_size > 50000:
                print(f"[JA EXISTE] {dest_file.name} ({dest_file.stat().st_size / (1024*1024):.2f} MB)", flush=True)
                downloaded_count += 1
                continue

            dl_url = f"https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/pe-de-meia/{yyyymm}_PeDeMeia.zip"
            print(f"Buscando {yyyymm}_PeDeMeia.zip...", flush=True)

            try:
                # Usar a API interna da página do Playwright para reutilizar cookies/sessão
                resp = page.request.get(dl_url, timeout=60000)
                if resp.status == 200:
                    body = resp.body()
                    if len(body) > 100000: # Garantir que não é página de erro HTML
                        with open(str(dest_file), "wb") as f:
                            f.write(body)
                        print(f"[OK] Download com sucesso: {dest_file.name} ({len(body)/(1024*1024):.2f} MB)", flush=True)
                        downloaded_count += 1
                    else:
                        print(f"[NAO DISPONIVEL / PEQUENO] {yyyymm}: {len(body)} bytes", flush=True)
                else:
                    print(f"[HTTP {resp.status}] {yyyymm}", flush=True)
            except Exception as e:
                print(f"[ERRO] {yyyymm}: {e}", flush=True)

        browser.close()
        print(f"\nFinalizado! Total de pacotes coletados: {downloaded_count}", flush=True)

if __name__ == "__main__":
    collect_with_playwright()
