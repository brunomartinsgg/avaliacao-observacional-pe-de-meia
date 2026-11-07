import os
import time
import subprocess
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TARGET_DIR = BASE_DIR / "dados_brutos" / "pe_de_meia_transparencia"
SCRATCH_DIR = Path(r"C:\Users\Bruno\.gemini\antigravity\brain\df4e2c63-3667-4160-9f37-ee1b397d5125\scratch\pm_dl")
SCRATCH_DIR.mkdir(parents=True, exist_ok=True)

MESES_2024 = ["202403", "202404", "202405", "202406", "202408", "202409", "202410", "202411", "202412"]
MESES_2025 = [
    "202501", "202502", "202503", "202504", "202505", "202506",
    "202507", "202508", "202509", "202510", "202511", "202512"
]
ALL_MESES = MESES_2024 + MESES_2025

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://portaldatransparencia.gov.br/download-de-dados/pe-de-meia"
}

def download_sequential():
    session = requests.Session()
    session.headers.update(HEADERS)

    # First, also fetch updated 202403 from S3 into scratch if not already valid in scratch
    s3_03_scratch = SCRATCH_DIR / "s3_202403_PeDeMeia.zip"
    if not s3_03_scratch.exists() or s3_03_scratch.stat().st_size < 100000:
        url03 = "https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/pe-de-meia/202403_PeDeMeia.zip"
        print("Baixando versão atualizada de 202403_PeDeMeia.zip do S3 para conferência...", flush=True)
        with session.get(url03, stream=True, timeout=180) as r:
            print(f"  202403 S3 status={r.status_code}, Content-Length={r.headers.get('Content-Length')}, Last-Modified={r.headers.get('Last-Modified')}", flush=True)
            if r.status_code == 200:
                with open(s3_03_scratch, "wb") as f:
                    for ch in r.iter_content(chunk_size=1024 * 1024):
                        if ch:
                            f.write(ch)
        time.sleep(3)

    ok_count = 0
    for ym in ALL_MESES:
        filename = f"{ym}_PeDeMeia.zip"
        full_dest = TARGET_DIR / filename
        scratch_file = SCRATCH_DIR / filename

        if full_dest.exists() and full_dest.stat().st_size > 100000:
            print(f"[JA EXISTE] {filename} ({full_dest.stat().st_size:,} bytes)", flush=True)
            ok_count += 1
            continue

        s3_url = f"https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/pe-de-meia/{filename}"
        print(f"Baixando {filename}...", flush=True)
        try:
            with session.get(s3_url, stream=True, timeout=180) as r:
                if r.status_code != 200:
                    print(f"  [AVISO] {filename} retornou HTTP {r.status_code} (waf={r.headers.get('x-amzn-waf-action')})", flush=True)
                    continue
                with open(scratch_file, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1024 * 1024):
                        if chunk:
                            f.write(chunk)

            if scratch_file.exists() and scratch_file.stat().st_size > 100000:
                src_str = os.path.normpath(str(scratch_file))
                dst_str = os.path.normpath(str(full_dest))
                subprocess.run(
                    ["powershell", "-Command", f"Copy-Item -Force -Path '{src_str}' -Destination '{dst_str}'"],
                    check=True
                )
                scratch_file.unlink(missing_ok=True)
                print(f"  [OK] {filename} salvo ({full_dest.stat().st_size:,} bytes)", flush=True)
                ok_count += 1
                time.sleep(3)
            else:
                print(f"  [FALHA] Arquivo {filename} pequeno demais.", flush=True)
        except Exception as e:
            print(f"  [ERRO] {filename}: {e}", flush=True)

    print(f"\nTotal de pacotes mensais em {TARGET_DIR}: {ok_count}/{len(ALL_MESES)}", flush=True)

if __name__ == "__main__":
    download_sequential()
