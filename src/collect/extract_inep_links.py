import re
import requests
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TARGET_DIR = BASE_DIR / "dados_brutos" / "censo_escolar"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

URL = "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-rendimento-escolar"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def extract_and_download():
    print(f"Acessando {URL}...", flush=True)
    r = requests.get(URL, headers=HEADERS, timeout=15)
    links = set(re.findall(r'href=[\'"]?(https?://download\.inep\.gov\.br/[^\'"\s>]+)[\'"]?', r.text, re.IGNORECASE))
    
    print(f"Links INEP encontrados: {len(links)}", flush=True)
    for l in sorted(list(links)):
        print(f"Found: {l}")
        filename = l.split("/")[-1]
        rel_dest = f"dados_brutos/censo_escolar/{filename}"
        full_dest = TARGET_DIR / filename
        
        if full_dest.exists() and full_dest.stat().st_size > 1000:
            print(f"[JA EXISTE] {filename}")
            continue
            
        print(f"Baixando {filename} via curl.exe...")
        cmd = ["curl.exe", "-k", "-L", "-s", "-o", rel_dest, l]
        subprocess.run(cmd, cwd=str(BASE_DIR))
        if full_dest.exists() and full_dest.stat().st_size > 1000:
            print(f"[OK] Download com sucesso: {filename} ({full_dest.stat().st_size / (1024*1024):.2f} MB)")
        else:
            print(f"[ERRO/FALHA] {filename}")

if __name__ == "__main__":
    extract_and_download()
