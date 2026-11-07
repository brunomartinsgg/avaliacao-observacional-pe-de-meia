import os
import zipfile
import subprocess
import numpy as np
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
RAW_DIR = BASE_DIR / "dados_brutos" / "ideb_saeb"
PROCESSED_DIR = BASE_DIR / "dados_tratados"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

UF_MAP = [
    (11, "RO", "Rondônia", ["Rondônia"]),
    (12, "AC", "Acre", ["Acre"]),
    (13, "AM", "Amazonas", ["Amazonas"]),
    (14, "RR", "Roraima", ["Roraima"]),
    (15, "PA", "Pará", ["Pará"]),
    (16, "AP", "Amapá", ["Amapá"]),
    (17, "TO", "Tocantins", ["Tocantins"]),
    (21, "MA", "Maranhão", ["Maranhão"]),
    (22, "PI", "Piauí", ["Piauí"]),
    (23, "CE", "Ceará", ["Ceará"]),
    (24, "RN", "Rio Grande do Norte", ["Rio Grande do Norte", "R. G. do Norte"]),
    (25, "PB", "Paraíba", ["Paraíba"]),
    (26, "PE", "Pernambuco", ["Pernambuco"]),
    (27, "AL", "Alagoas", ["Alagoas"]),
    (28, "SE", "Sergipe", ["Sergipe"]),
    (29, "BA", "Bahia", ["Bahia"]),
    (31, "MG", "Minas Gerais", ["Minas Gerais"]),
    (32, "ES", "Espírito Santo", ["Espírito Santo"]),
    (33, "RJ", "Rio de Janeiro", ["Rio de Janeiro"]),
    (35, "SP", "São Paulo", ["São Paulo"]),
    (41, "PR", "Paraná", ["Paraná"]),
    (42, "SC", "Santa Catarina", ["Santa Catarina"]),
    (43, "RS", "Rio Grande do Sul", ["Rio Grande do Sul", "R. G. do Sul"]),
    (50, "MS", "Mato Grosso do Sul", ["Mato Grosso do Sul", "M. G. do Sul"]),
    (51, "MT", "Mato Grosso", ["Mato Grosso"]),
    (52, "GO", "Goiás", ["Goiás"]),
    (53, "DF", "Distrito Federal", ["Distrito Federal"]),
]

NAME_TO_UF = {}
for cod, sg, nome_padrao, aliases in UF_MAP:
    for al in aliases:
        NAME_TO_UF[al.upper().strip()] = (cod, sg, nome_padrao)

def clean_rede(r_str: str) -> str:
    s = str(r_str).strip()
    for prefix in ["Total", "Privada", "Estadual", "Pública", "Federal", "Municipal"]:
        if s.startswith(prefix):
            return prefix
    return s

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

def process_ideb_nacional():
    zp_uf = RAW_DIR / "divulgacao_regioes_ufs_ideb_2025.zip"
    zp_br = RAW_DIR / "divulgacao_brasil_ideb_2025.zip"
    if not zp_uf.exists():
        print(f"Arquivo {zp_uf} não encontrado.")
        return

    ideb_rows = []
    with zipfile.ZipFile(zp_uf, 'r') as z:
        xls = [f for f in z.namelist() if f.endswith('.xlsx')][0]
        with z.open(xls) as f:
            df_uf = pd.read_excel(f, sheet_name="UF e Regiões (EM)", skiprows=9)

    c0, c1 = df_uf.columns[0], df_uf.columns[1]
    for _, row in df_uf.iterrows():
        unid = str(row[c0]).strip() if pd.notna(row[c0]) else ""
        rede_raw = str(row[c1]).strip() if pd.notna(row[c1]) else ""
        if not unid or not rede_raw or rede_raw == "nan":
            continue
        rede = clean_rede(rede_raw)
        if unid.upper() in NAME_TO_UF:
            cod_uf, sg_uf, nome_uf = NAME_TO_UF[unid.upper()]
            nivel = "UF"
        elif unid in ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"]:
            cod_uf, sg_uf, nome_uf = (0, unid.upper()[:2], unid)
            nivel = "Região"
        else:
            continue

        for yr in [2019, 2021, 2023, 2025]:
            ideb_rows.append({
                "nivel": nivel,
                "codigo_uf": cod_uf,
                "uf": sg_uf,
                "unidade_geografica": nome_uf,
                "ano": yr,
                "rede": rede,
                "ideb_taxa_aprovacao_em": to_float(row.get(f"VL_APROVACAO_{yr}_SI_4")),
                "ideb_indicador_rendimento": to_float(row.get(f"VL_INDICADOR_REND_{yr}")),
                "ideb_nota_matematica": to_float(row.get(f"VL_NOTA_MATEMATICA_{yr}")),
                "ideb_nota_portugues": to_float(row.get(f"VL_NOTA_PORTUGUES_{yr}")),
                "ideb_nota_media": to_float(row.get(f"VL_NOTA_MEDIA_{yr}")),
                "ideb_observado": to_float(row.get(f"VL_OBSERVADO_{yr}")),
            })

    if zp_br.exists():
        with zipfile.ZipFile(zp_br, 'r') as z:
            xls = [f for f in z.namelist() if f.endswith('.xlsx')][0]
            with z.open(xls) as f:
                df_br = pd.read_excel(f, sheet_name="Brasil (EM)", skiprows=9)
        c0_b, c1_b = df_br.columns[0], df_br.columns[1]
        for _, row in df_br.iterrows():
            unid = str(row[c0_b]).strip() if pd.notna(row[c0_b]) else ""
            rede_raw = str(row[c1_b]).strip() if pd.notna(row[c1_b]) else ""
            if unid != "Brasil" or not rede_raw or rede_raw == "nan":
                continue
            rede = clean_rede(rede_raw)
            for yr in [2019, 2021, 2023, 2025]:
                ideb_rows.append({
                    "nivel": "Brasil",
                    "codigo_uf": 0,
                    "uf": "BR",
                    "unidade_geografica": "Brasil",
                    "ano": yr,
                    "rede": rede,
                    "ideb_taxa_aprovacao_em": to_float(row.get(f"VL_APROVACAO_{yr}_SI_4")),
                    "ideb_indicador_rendimento": to_float(row.get(f"VL_INDICADOR_REND_{yr}")),
                    "ideb_nota_matematica": to_float(row.get(f"VL_NOTA_MATEMATICA_{yr}")),
                    "ideb_nota_portugues": to_float(row.get(f"VL_NOTA_PORTUGUES_{yr}")),
                    "ideb_nota_media": to_float(row.get(f"VL_NOTA_MEDIA_{yr}")),
                    "ideb_observado": to_float(row.get(f"VL_OBSERVADO_{yr}")),
                })

    df_final = pd.DataFrame(ideb_rows)
    out_csv = os.path.normpath(str(PROCESSED_DIR / "ideb_uf_brasil_ensino_medio.csv"))
    csv_bytes = df_final.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
    subprocess.run(
        ["powershell", "-Command", f"$input | Set-Content -Path '{out_csv}' -Encoding UTF8"],
        input=csv_bytes, check=True
    )
    print(f"[OK] IDEB Nacional (UF/Regiões/Brasil 2019-2025) salvo em: {out_csv} ({len(df_final)} registros)")

if __name__ == "__main__":
    process_ideb_nacional()

