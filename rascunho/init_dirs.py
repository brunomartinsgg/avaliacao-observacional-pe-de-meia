from pathlib import Path

DIRS = [
    "dados_brutos/censo_escolar",
    "dados_brutos/ideb_saeb",
    "dados_brutos/pe_de_meia_transparencia",
    "dados_brutos/cadunico",
    "dados_brutos/pnad_continua",
    "dados_brutos/alagoas_educacao",
    "dados_brutos/kaggle",
    "dados_brutos/outros"
]

def init_directories():
    base_dir = Path(__file__).resolve().parent.parent
    print(f"Base Directory: {base_dir}")
    for folder in DIRS:
        full_path = base_dir / folder
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"[OK] Diretório pronto: {full_path}")

if __name__ == "__main__":
    init_directories()

