import os
import requests
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TARGET_DIR = BASE_DIR / "dados_brutos" / "pe_de_meia_transparencia"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def get_available_months():
    current_year = datetime.now().year
    current_month = datetime.now().month
    months = []
    for year in range(2024, current_year + 1):
        end_m = current_month if year == current_year else 12
        for month in range(1, end_m + 1):
            months.append(f"{year}{month:02d}")
    return months

def download_pe_de_meia():
    months = get_available_months()
    print(f"Verificando {len(months)} meses potenciais de dados do Pé-de-Meia...", flush=True)
    
    downloaded = 0
    for yyyymm in months:
        url = f"https://portaldatransparencia.gov.br/download-de-dados/pe-de-meia/{yyyymm}"
        dest_file = TARGET_DIR / f"{yyyymm}_PeDeMeia.zip"
        
        if dest_file.exists() and dest_file.stat().st_size > 0:
            print(f"[JA EXISTE] {dest_file.name} ({dest_file.stat().st_size / (1024*1024):.2f} MB)", flush=True)
            downloaded += 1
            continue
            
        try:
            with requests.get(url, headers=HEADERS, stream=True, allow_redirects=True, timeout=60) as r:
                if r.status_code == 200 and "zip" in r.headers.get("Content-Type", "").lower() or r.headers.get("Content-Length"):
                    content_len = int(r.headers.get("Content-Length", 0))
                    print(f"Baixando {yyyymm}_PeDeMeia.zip ({content_len / (1024*1024):.2f} MB) de {r.url}...", flush=True)
                    dest_file.parent.mkdir(parents=True, exist_ok=True)
                    with open(str(dest_file), "wb") as f:
                        for chunk in r.iter_content(chunk_size=1024*1024):
                            if chunk:
                                f.write(chunk)
                    print(f"[OK] Download concluído: {dest_file.name}", flush=True)
                    downloaded += 1
                else:
                    print(f"[NAO DISPONIVEL] {yyyymm}: HTTP {r.status_code}", flush=True)
        except Exception as e:
            print(f"[ERRO] {yyyymm}: {e}", flush=True)



    # Baixar também relatório Inesc se disponível
    inesc_url = "https://inesc.org.br/governo-destina-r-1-bilhao-ao-pe-de-meia-em-2025-mas-valor-e-apenas-8-do-gasto-anual-previsto-pelo-programa/"
    inesc_file = TARGET_DIR / "relatorio_inesc_pe_de_meia_2025.html"
    if not inesc_file.exists():
        try:
            r = requests.get(inesc_url, headers=HEADERS, timeout=15)
            if r.status_code == 200:
                with open(inesc_file, "w", encoding="utf-8") as f:
                    f.write(r.text)
                print(f"[OK] Artigo/Relatório Inesc salvo em {inesc_file.name}", flush=True)
        except Exception as e:
            print(f"[AVISO] Não foi possível salvar o artigo Inesc: {e}", flush=True)

    print(f"\nFinalizado! Total de pacotes de dados do Pé-de-Meia obtidos: {downloaded}", flush=True)


if __name__ == "__main__":
    download_pe_de_meia()
