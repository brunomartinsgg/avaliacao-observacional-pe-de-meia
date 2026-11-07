import os
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TARGET_DIR = BASE_DIR / "dados_brutos" / "pe_de_meia_transparencia"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

# Lista de meses disponíveis para o Pé-de-Meia no Portal da Transparência (de 03/2024 em diante)
MONTHS = [
    "202403", "202404", "202405", "202406", "202407", "202408", "202409", "202410", "202411", "202412",
    "202501", "202502", "202503", "202504", "202505", "202506", "202507", "202508", "202509", "202510"
]

def run_download():
    print(f"Iniciando download em lote para os pacotes do Pé-de-Meia ({len(MONTHS)} meses)...", flush=True)

    downloaded = 0
    for yyyymm in MONTHS:
        filename = f"{yyyymm}_PeDeMeia.zip"
        rel_dest = os.path.normpath(f"dados_brutos/pe_de_meia_transparencia/{filename}")
        full_dest = TARGET_DIR / filename

        if full_dest.exists() and full_dest.stat().st_size > 1000000:
            print(f"[JA EXISTE] {filename} ({full_dest.stat().st_size / (1024*1024):.2f} MB)", flush=True)
            downloaded += 1
            continue

        url = f"https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/pe-de-meia/{yyyymm}_PeDeMeia.zip"
        print(f"Baixando {filename} de {url}...", flush=True)

        cmd = [
            "curl.exe", "-k", "-L", "-s",
            "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "-o", rel_dest,
            url
        ]

        subprocess.run(cmd, cwd=str(BASE_DIR))

        if full_dest.exists() and full_dest.stat().st_size > 1000000:
            print(f"[OK] {filename} baixado com sucesso! ({full_dest.stat().st_size / (1024*1024):.2f} MB)", flush=True)
            downloaded += 1
        else:
            if full_dest.exists() and full_dest.stat().st_size < 1000000:
                full_dest.unlink()
            print(f"[INDISPONIVEL OU FIM DA SERIE] {yyyymm}", flush=True)

    print(f"\nFinalizada a rotina de download do Pé-de-Meia! Total de pacotes em disco: {downloaded}", flush=True)

if __name__ == "__main__":
    run_download()
