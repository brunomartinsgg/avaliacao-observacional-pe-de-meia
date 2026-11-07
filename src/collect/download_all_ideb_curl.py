import os
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TARGET_DIR = BASE_DIR / "dados_brutos" / "ideb_saeb"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

IDEB_FILES = [
    "divulgacao_ensino_medio_municipios_2025.zip",
    "divulgacao_regioes_ufs_ideb_2025.zip",
    "divulgacao_brasil_ideb_2025.zip",
    "divulgacao_regioes_ufs_ideb_2023.zip",
]

def download_ideb_batch():
    print("Iniciando download em lote dos arquivos do IDEB / SAEB (Brasil, Regiões/UFs e Municípios)...", flush=True)

    downloaded = 0
    for filename in IDEB_FILES:
        rel_dest = os.path.normpath(f"dados_brutos/ideb_saeb/{filename}")
        full_dest = TARGET_DIR / filename

        if full_dest.exists() and full_dest.stat().st_size > 10000:
            print(f"[JA EXISTE] {filename} ({full_dest.stat().st_size / (1024*1024):.2f} MB)", flush=True)
            downloaded += 1
            continue

        url = f"https://download.inep.gov.br/ideb/resultados/{filename}"
        print(f"Baixando {filename} de {url}...", flush=True)

        cmd = ["curl.exe", "-k", "-L", "-s", "-o", rel_dest, url]
        subprocess.run(cmd, cwd=str(BASE_DIR))

        if full_dest.exists() and full_dest.stat().st_size > 10000:
            print(f"[OK] {filename} baixado com sucesso! ({full_dest.stat().st_size / (1024*1024):.2f} MB)", flush=True)
            downloaded += 1
        else:
            print(f"[FALHA/AVISO] {filename}", flush=True)

    print(f"\nFinalizado! Total de arquivos do IDEB salvos em {TARGET_DIR}: {downloaded}", flush=True)

if __name__ == "__main__":
    download_ideb_batch()
