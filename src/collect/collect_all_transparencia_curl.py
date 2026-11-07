import os
import subprocess
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TARGET_DIR = BASE_DIR / "dados_brutos" / "pe_de_meia_transparencia"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

def download_pe_de_meia_curl():
    print("Iniciando coleta automatizada do Pé-de-Meia via Portal da Transparência (curl.exe)...", flush=True)

    months = []
    curr_yr = datetime.now().year
    curr_mo = datetime.now().month
    for y in range(2024, curr_yr + 1):
        start_m = 3 if y == 2024 else 1 # Pé-de-Meia começou em 03/2024
        end_m = curr_mo if y == curr_yr else 12
        for m in range(start_m, end_m + 1):
            months.append(f"{y}{m:02d}")

    print(f"Total de meses a verificar: {len(months)} ({months[0]} a {months[-1]})", flush=True)

    downloaded = 0
    for yyyymm in months:
        filename = f"{yyyymm}_PeDeMeia.zip"
        rel_dest = os.path.normpath(f"dados_brutos/pe_de_meia_transparencia/{filename}")
        full_dest = TARGET_DIR / filename

        if full_dest.exists() and full_dest.stat().st_size > 100000:
            print(f"[JA EXISTE] {filename} ({full_dest.stat().st_size / (1024*1024):.2f} MB)", flush=True)
            downloaded += 1
            continue

        url = f"https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/pe-de-meia/{yyyymm}_PeDeMeia.zip"
        print(f"Baixando pacote do Pé-de-Meia: {filename}...", flush=True)

        cmd = [
            "curl.exe", "-k", "-L", "-s",
            "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "-o", rel_dest,
            url
        ]


        subprocess.run(cmd, cwd=str(BASE_DIR))

        if full_dest.exists() and full_dest.stat().st_size > 100000:
            print(f"[OK] Download concluído: {filename} ({full_dest.stat().st_size / (1024*1024):.2f} MB)", flush=True)
            downloaded += 1
        else:
            if full_dest.exists():
                full_dest.unlink() # remove se for página HTML de erro / vazia
            print(f"[NAO DISPONIVEL / INDISPONIVEL] {yyyymm}", flush=True)

    print(f"\nFinalizada a coleta do Pé-de-Meia! Pacotes obtidos com sucesso: {downloaded}", flush=True)

if __name__ == "__main__":
    download_pe_de_meia_curl()
