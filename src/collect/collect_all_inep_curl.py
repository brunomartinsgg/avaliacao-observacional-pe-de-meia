import os
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TARGET_DIR = BASE_DIR / "dados_brutos" / "censo_escolar"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

YEARS = ["2022", "2023", "2024", "2025"]
TYPES = [
    "tx_rend_brasil_regioes_ufs",
    "tx_rend_municipios",
    "tx_rend_escolas"
]

def download_inep_curl():
    print("Iniciando download em lote via curl.exe para INEP Taxas de Rendimento (2022-2025)...", flush=True)
    
    downloaded = 0
    for yr in YEARS:
        for tp in TYPES:
            filename = f"{tp}_{yr}.zip"
            rel_dest = f"dados_brutos/censo_escolar/{filename}"
            full_dest = TARGET_DIR / filename

            if full_dest.exists() and full_dest.stat().st_size > 1000:
                print(f"[JA EXISTE] {filename} ({full_dest.stat().st_size / 1024:.1f} KB)", flush=True)
                downloaded += 1
                continue

            url = f"https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/{yr}/{tp}_{yr}.zip"
            print(f"Baixando {filename} de {url}...", flush=True)

            cmd = [
                "curl.exe", "-k", "-L", "-s",
                "-o", rel_dest,
                url
            ]

            res = subprocess.run(cmd, cwd=str(BASE_DIR))
            if full_dest.exists() and full_dest.stat().st_size > 1000:
                print(f"[OK] Download concluído: {filename} ({full_dest.stat().st_size / (1024*1024):.2f} MB)", flush=True)
                downloaded += 1
            else:
                print(f"[FALHA/404] {filename}", flush=True)

    print(f"\nFinalizado! Total de arquivos INEP obtidos: {downloaded}/{len(YEARS)*len(TYPES)}", flush=True)

if __name__ == "__main__":
    download_inep_curl()
