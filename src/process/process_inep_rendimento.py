import os
import zipfile
import subprocess
import numpy as np
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
RAW_DIR = BASE_DIR / "dados_brutos" / "censo_escolar"
PROCESSED_DIR = BASE_DIR / "dados_tratados"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

UF_MAP = [
    (11, "RO", "Rondônia"), (12, "AC", "Acre"), (13, "AM", "Amazonas"), (14, "RR", "Roraima"),
    (15, "PA", "Pará"), (16, "AP", "Amapá"), (17, "TO", "Tocantins"), (21, "MA", "Maranhão"),
    (22, "PI", "Piauí"), (23, "CE", "Ceará"), (24, "RN", "Rio Grande do Norte"), (25, "PB", "Paraíba"),
    (26, "PE", "Pernambuco"), (27, "AL", "Alagoas"), (28, "SE", "Sergipe"), (29, "BA", "Bahia"),
    (31, "MG", "Minas Gerais"), (32, "ES", "Espírito Santo"), (33, "RJ", "Rio de Janeiro"),
    (35, "SP", "São Paulo"), (41, "PR", "Paraná"), (42, "SC", "Santa Catarina"),
    (43, "RS", "Rio Grande do Sul"), (50, "MS", "Mato Grosso do Sul"), (51, "MT", "Mato Grosso"),
    (52, "GO", "Goiás"), (53, "DF", "Distrito Federal")
]
NAME_TO_UF = {nome.upper(): (cod, sg, nome) for cod, sg, nome in UF_MAP}

def to_float(val):
    if pd.isna(val):
        return np.nan
    s = str(val).strip().replace(",", ".")
    if s in ["", "-", "--", "ND", "nan", "None"]:
        return np.nan
    try:
        return float(s)
    except:
        return np.nan

def process_inep_rendimento_nacional():
    print("=================================================================", flush=True)
    print("Processando Taxas de Rendimento (INEP) - Escopo Nacional (Brasil/Regiões/UFs 2022-2025)...", flush=True)
    print("=================================================================", flush=True)

    zip_files = sorted(list(RAW_DIR.glob("tx_rend_brasil_regioes_ufs_*.zip")))
    if not zip_files:
        print("[AVISO] Nenhum arquivo tx_rend_brasil_regioes_ufs_*.zip encontrado.")
        return

    extracted_records = []
    for zpath in zip_files:
        print(f"Lendo {zpath.name}...", flush=True)
        with zipfile.ZipFile(zpath, 'r') as z:
            excel_files = [f for f in z.namelist() if f.endswith('.xlsx') or f.endswith('.xls')]
            if not excel_files:
                continue
            with z.open(excel_files[0]) as f:
                df = pd.read_excel(f, sheet_name=0, skiprows=8)
                for _, row in df.iterrows():
                    ano_val = str(row.get("NU_ANO_CENSO", "")).strip()
                    if not ano_val.isdigit():
                        continue
                    categoria = str(row.get("NO_CATEGORIA", "")).strip()
                    if categoria.upper() != "TOTAL":
                        continue
                    unid = str(row.get("UNIDGEO", "")).strip()
                    rede = str(row.get("NO_DEPENDENCIA", "")).strip()

                    if unid.upper() in NAME_TO_UF:
                        cod_uf, sg_uf, nome_uf = NAME_TO_UF[unid.upper()]
                        nivel = "UF"
                    elif unid == "Brasil":
                        cod_uf, sg_uf, nome_uf = (0, "BR", "Brasil")
                        nivel = "Brasil"
                    elif unid in ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"]:
                        cod_uf, sg_uf, nome_uf = (0, unid.upper()[:2], unid)
                        nivel = "Região"
                    else:
                        continue

                    extracted_records.append({
                        "nivel": nivel,
                        "codigo_uf": cod_uf,
                        "uf": sg_uf,
                        "unidade_geografica": nome_uf,
                        "ano": int(ano_val),
                        "rede": rede,
                        "taxa_aprovacao_ensino_medio": to_float(row.get("1_CAT_MED")),
                        "taxa_aprovacao_em_1serie": to_float(row.get("1_CAT_MED_01")),
                        "taxa_aprovacao_em_2serie": to_float(row.get("1_CAT_MED_02")),
                        "taxa_aprovacao_em_3serie": to_float(row.get("1_CAT_MED_03")),
                        "taxa_reprovacao_ensino_medio": to_float(row.get("2_CAT_MED")),
                        "taxa_reprovacao_em_1serie": to_float(row.get("2_CAT_MED_01")),
                        "taxa_reprovacao_em_2serie": to_float(row.get("2_CAT_MED_02")),
                        "taxa_reprovacao_em_3serie": to_float(row.get("2_CAT_MED_03")),
                        "taxa_abandono_ensino_medio": to_float(row.get("3_CAT_MED")),
                        "taxa_abandono_em_1serie": to_float(row.get("3_CAT_MED_01")),
                        "taxa_abandono_em_2serie": to_float(row.get("3_CAT_MED_02")),
                        "taxa_abandono_em_3serie": to_float(row.get("3_CAT_MED_03")),
                    })

    df_res = pd.DataFrame(extracted_records).drop_duplicates()
    out_csv = os.path.normpath(str(PROCESSED_DIR / "inep_taxas_rendimento_uf_brasil.csv"))
    csv_bytes = df_res.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
    subprocess.run(
        ["powershell", "-Command", f"$input | Set-Content -Path '{out_csv}' -Encoding UTF8"],
        input=csv_bytes, check=True
    )
    print(f"[OK] {len(df_res)} registros salvos em: {out_csv}")

if __name__ == "__main__":
    process_inep_rendimento_nacional()
