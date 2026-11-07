import os
import subprocess
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TARGET_DIR = BASE_DIR / "dados_brutos" / "ideb_saeb"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

IDEB_URLS = [
    "https://download.inep.gov.br/educacao_basica/portal_ideb/planilhas_divulgacao/divulgacao_ensino_medio_municipios_2023.zip",
    "https://download.inep.gov.br/educacao_basica/portal_ideb/planilhas_divulgacao/divulgacao_anos_finais_municipios_2023.zip",
    "https://download.inep.gov.br/educacao_basica/portal_ideb/planilhas_divulgacao/divulgacao_ensino_medio_ufs_2023.zip",
    "https://download.inep.gov.br/educacao_basica/portal_ideb/planilhas_divulgacao/divulgacao_ensino_medio_brasil_2023.zip"
]

def collect_ideb():
    print("Iniciando download dos dados do IDEB / SAEB...", flush=True)

    downloaded = 0
    for url in IDEB_URLS:
        filename = url.split("/")[-1]
        rel_dest = os.path.normpath(f"dados_brutos/ideb_saeb/{filename}")
        full_dest = TARGET_DIR / filename

        if full_dest.exists() and full_dest.stat().st_size > 1000:
            print(f"[JA EXISTE] {filename} ({full_dest.stat().st_size / 1024:.1f} KB)", flush=True)
            downloaded += 1
            continue

        print(f"Baixando {filename} via curl.exe...", flush=True)
        cmd = ["curl.exe", "-k", "-L", "-s", "-o", rel_dest, url]
        subprocess.run(cmd, cwd=str(BASE_DIR))

        if full_dest.exists() and full_dest.stat().st_size > 1000:
            print(f"[OK] IDEB baixado com sucesso: {filename} ({full_dest.stat().st_size / (1024*1024):.2f} MB)", flush=True)
            downloaded += 1
        else:
            print(f"[FALHA/AVISO] {filename}", flush=True)

    print(f"\nFinalizada coleta de dados do IDEB! Arquivos salvos em {TARGET_DIR}", flush=True)

if __name__ == "__main__":
    collect_ideb()
