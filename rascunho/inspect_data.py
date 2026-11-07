import zipfile
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "dados_brutos"
PROCESSED_DIR = BASE_DIR / "dados_tratados"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def inspect_pe_de_meia():
    zip_path = RAW_DIR / "pe_de_meia_transparencia" / "202403_PeDeMeia.zip"
    if not zip_path.exists():
        print("Arquivo do Pé-de-Meia não encontrado.")
        return

    print(f"--- Lendo {zip_path.name} ---")
    with zipfile.ZipFile(zip_path, 'r') as z:
        print("Arquivos no ZIP Pé-de-Meia:", z.namelist())
        csv_name = [f for f in z.namelist() if f.endswith('.csv')][0]
        
        with z.open(csv_name) as f:
            df = pd.read_csv(f, sep=';', encoding='latin-1', dtype=str, nrows=1000)
            print(f"\nColunas encontradas no Pé-de-Meia ({len(df.columns)}):")
            print(df.columns.tolist())
            print("\nAuditoria de identificadores na amostra (1.000 linhas):")
            for col in ['NIS BENEFICIÁRIO', 'CPF BENEFICIÁRIO', 'NOME BENEFICIÁRIO', 'NIS RESPONSÁVEL', 'CPF RESPONSÁVEL']:
                if col in df.columns:
                    n_null = df[col].isna().sum()
                    print(f"  - {col}: {n_null}/1000 nulos | exemplos: {df[col].dropna().head(3).tolist()}")
            print("\nNota técnica: ~90% dos registros são menores de 18 anos com NIS/CPF do beneficiário ocultos (NaN)")
            print("e NOME BENEFICIÁRIO = '*** BENEFICIÁRIO MENOR DE 18 ANOS ***'. Não há identificador único confiável.")

def inspect_inep():
    zip_path = RAW_DIR / "censo_escolar" / "tx_rend_brasil_regioes_ufs_2025.zip"
    if not zip_path.exists():
        print("Arquivo do INEP Brasil/Regiões/UFs não encontrado.")
        return

    print(f"\n--- Lendo {zip_path.name} ---")
    with zipfile.ZipFile(zip_path, 'r') as z:
        print("Arquivos no ZIP INEP:", z.namelist())
        excel_or_csv = [f for f in z.namelist() if f.endswith(('.xlsx', '.xls', '.csv'))][0]
        print("Arquivo selecionado:", excel_or_csv)

if __name__ == "__main__":
    inspect_pe_de_meia()
    inspect_inep()

