import os
import requests
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TARGET_DIR = BASE_DIR / "dados_brutos" / "censo_escolar"

SCRATCH_DIR = Path(r"C:\Users\Bruno\.gemini\antigravity-ide\brain\76283ae0-6076-45c1-87c0-fc8f45728f62\scratch")
SCRATCH_DIR.mkdir(parents=True, exist_ok=True)

URLS = [
    "https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2023/tx_rend_municipios_2023.zip",
    "https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2022/tx_rend_municipios_2022.zip"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def download_baseline():
    print("Iniciando download dos arquivos de linha de base (2022 e 2023) do INEP...", flush=True)

    for url in URLS:
        fname = url.split("/")[-1]
        scratch_file = SCRATCH_DIR / fname
        dest_file = TARGET_DIR / fname

        print(f"Baixando {fname} para scratch...", flush=True)
        r = requests.get(url, headers=HEADERS, verify=False, timeout=60)

        if r.status_code == 200:
            with open(scratch_file, "wb") as f:
                f.write(r.content)
            print(f"[OK] Gravado no scratch ({len(r.content)/(1024*1024):.2f} MB). Copiando para {dest_file.name}...", flush=True)

            src_str = os.path.normpath(str(scratch_file))
            dst_str = os.path.normpath(str(dest_file))

            subprocess.run(
                ["powershell", "-Command", f"Copy-Item -Force -Path '{src_str}' -Destination '{dst_str}'"],
                check=True
            )
            print(f"[SUCESSO] {fname} salvo em {dst_str}!", flush=True)
        else:
            print(f"[FALHA] Status {r.status_code} ao baixar {fname}", flush=True)

if __name__ == "__main__":
    download_baseline()
