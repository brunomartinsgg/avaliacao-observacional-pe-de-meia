import os
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TARGET_DIR = BASE_DIR / "dados_brutos" / "censo_escolar"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

YEARS = ["2022", "2023", "2024", "2025"]

def download_inep_municipios():
    print("Iniciando download dos indicadores municipais do INEP (2022-2025)...", flush=True)

    for yr in YEARS:
        filename = f"tx_rend_municipios_{yr}.zip"
        rel_dest = os.path.normpath(f"dados_brutos/censo_escolar/{filename}")
        full_dest = TARGET_DIR / filename

        if full_dest.exists() and full_dest.stat().st_size > 1000000:
            print(f"[JA EXISTE] {filename} ({full_dest.stat().st_size / (1024*1024):.2f} MB)", flush=True)
            continue

        url = f"https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/{yr}/tx_rend_municipios_{yr}.zip"
        print(f"Baixando {filename} de {url}...", flush=True)

        cmd = ["curl.exe", "-k", "-L", "-s", "-o", rel_dest, url]
        subprocess.run(cmd, cwd=str(BASE_DIR))

        if full_dest.exists() and full_dest.stat().st_size > 1000000:
            print(f"[OK] {filename} baixado com sucesso! ({full_dest.stat().st_size / (1024*1024):.2f} MB)", flush=True)
        else:
            print(f"[FALHA/AVISO] {filename}", flush=True)

if __name__ == "__main__":
    download_inep_municipios()
