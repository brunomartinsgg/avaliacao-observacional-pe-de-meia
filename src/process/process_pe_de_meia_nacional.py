import os
import zipfile
import subprocess
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
RAW_DIR = BASE_DIR / "dados_brutos" / "pe_de_meia_transparencia"
PROCESSED_DIR = BASE_DIR / "dados_tratados"
SCRATCH_DIR = Path(r"C:\Users\Bruno\.gemini\antigravity\brain\df4e2c63-3667-4160-9f37-ee1b397d5125\scratch")

UF_MAP = {
    "RO": (11, "Rondônia"), "AC": (12, "Acre"), "AM": (13, "Amazonas"), "RR": (14, "Roraima"),
    "PA": (15, "Pará"), "AP": (16, "Amapá"), "TO": (17, "Tocantins"), "MA": (21, "Maranhão"),
    "PI": (22, "Piauí"), "CE": (23, "Ceará"), "RN": (24, "Rio Grande do Norte"), "PB": (25, "Paraíba"),
    "PE": (26, "Pernambuco"), "AL": (27, "Alagoas"), "SE": (28, "Sergipe"), "BA": (29, "Bahia"),
    "MG": (31, "Minas Gerais"), "ES": (32, "Espírito Santo"), "RJ": (33, "Rio de Janeiro"),
    "SP": (35, "São Paulo"), "PR": (41, "Paraná"), "SC": (42, "Santa Catarina"),
    "RS": (43, "Rio Grande do Sul"), "MS": (50, "Mato Grosso do Sul"), "MT": (51, "Mato Grosso"),
    "GO": (52, "Goiás"), "DF": (53, "Distrito Federal")
}

def process_pe_de_meia_nacional():
    # Se a versão retificada de 202403 (57.7 MB) estiver no scratch, atualizar em dados_brutos
    s3_03 = SCRATCH_DIR / "pm_dl" / "s3_202403_PeDeMeia.zip"
    dest_03 = RAW_DIR / "202403_PeDeMeia.zip"
    if s3_03.exists() and s3_03.stat().st_size == 57779785 and dest_03.stat().st_size != 57779785:
        print("Atualizando 202403_PeDeMeia.zip com a versão oficial retificada da CGU (57.779.785 bytes)...", flush=True)
        subprocess.run(
            ["powershell", "-Command", f"Copy-Item -Force -Path '{os.path.normpath(str(s3_03))}' -Destination '{os.path.normpath(str(dest_03))}'"],
            check=True
        )

    zip_files_2024 = sorted([z for z in RAW_DIR.glob("2024*_PeDeMeia.zip") if z.stat().st_size > 100000])
    zip_202502 = RAW_DIR / "202502_PeDeMeia.zip"
    zip_files = list(zip_files_2024)
    if zip_202502.exists() and zip_202502.stat().st_size > 100000:
        zip_files.append(zip_202502)

    if not zip_files_2024:
        print("Nenhum arquivo válido de 2024 do Pé-de-Meia encontrado.")
        return

    print(f"Processando {len(zip_files_2024)} pacotes mensais de 2024 (+ folha 202502 para Ciclo 2024) em escopo nacional (27 UFs)...", flush=True)

    with zipfile.ZipFile(zip_files_2024[0], 'r') as z0:
        c0 = [f for f in z0.namelist() if f.endswith('.csv')][0]
        with z0.open(c0) as f0:
            cols = pd.read_csv(f0, sep=';', encoding='latin-1', nrows=1).columns.tolist()
            print(f"Colunas auditadas ({len(cols)}): {cols}", flush=True)

    pm_agg = {}
    for zpath in zip_files:
        ym = zpath.name.split("_")[0]
        print(f"Lendo {zpath.name} ({zpath.stat().st_size:,} bytes)...", flush=True)
        with zipfile.ZipFile(zpath, 'r') as z:
            csv_files = [f for f in z.namelist() if f.endswith('.csv')]
            if not csv_files:
                continue
            with z.open(csv_files[0]) as f:
                for chunk in pd.read_csv(f, sep=';', encoding='latin-1', usecols=['UF', 'MÊS FOLHA', 'TIPO INCENTIVO', 'VALOR PARCELA'], dtype=str, chunksize=500000):
                    chunk['VAL_NUM'] = chunk['VALOR PARCELA'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)
                    grp = chunk.groupby(['UF', 'MÊS FOLHA', 'TIPO INCENTIVO']).agg(
                        total_investido=('VAL_NUM', 'sum'),
                        qtd_pagamentos=('VAL_NUM', 'count')
                    ).reset_index()
                    for _, r in grp.iterrows():
                        key = (str(r['UF']).strip().upper(), ym, str(r['TIPO INCENTIVO']).strip())
                        if key not in pm_agg:
                            pm_agg[key] = [0.0, 0]
                        pm_agg[key][0] += float(r['total_investido'])
                        pm_agg[key][1] += int(r['qtd_pagamentos'])

    rows = []
    for (uf_sg, mes_folha, tipo_inc), (val_tot, qtd_pag) in sorted(pm_agg.items()):
        if uf_sg not in UF_MAP:
            continue
        cod_uf, nome_uf = UF_MAP[uf_sg]
        ano_folha = int(mes_folha[:4])
        rows.append({
            "codigo_uf": cod_uf,
            "uf": uf_sg,
            "unidade_geografica": nome_uf,
            "ano": ano_folha,
            "mes_folha": mes_folha,
            "tipo_incentivo": tipo_inc,
            "total_investido_pedemeia": val_tot,
            "qtd_pagamentos_pedemeia": qtd_pag
        })

    df_detail = pd.DataFrame(rows)

    # Totais de 2024 (Ano Completo: 9 folhas 202403..202412) e Bimestre Mar-Abr/2024 retificado
    df_2024 = df_detail[df_detail['ano'] == 2024]
    df_bim = df_detail[df_detail['mes_folha'].isin(['202403', '202404'])].groupby('uf').agg(
        total_investido_mar_abr_2024_retificado=('total_investido_pedemeia', 'sum'),
        qtd_pagamentos_mar_abr_2024_retificado=('qtd_pagamentos_pedemeia', 'sum')
    ).to_dict('index')

    df_uf_2024 = df_2024.groupby(['codigo_uf', 'uf', 'unidade_geografica', 'ano']).agg(
        total_investido_pedemeia_ano=('total_investido_pedemeia', 'sum'),
        qtd_pagamentos_pedemeia_ano=('qtd_pagamentos_pedemeia', 'sum'),
    ).reset_index()

    pm_mat = df_2024[df_2024['tipo_incentivo'].str.contains('Matr', case=False, na=False)].groupby('uf')['qtd_pagamentos_pedemeia'].sum().to_dict()
    pm_freq = df_2024[df_2024['tipo_incentivo'].str.contains('Freq', case=False, na=False)].groupby('uf')['qtd_pagamentos_pedemeia'].sum().to_dict()

    df_uf_2024['qtd_pagamentos_incentivo_matricula'] = df_uf_2024['uf'].map(pm_mat).fillna(0).astype(int)
    df_uf_2024['qtd_pagamentos_incentivo_frequencia'] = df_uf_2024['uf'].map(pm_freq).fillna(0).astype(int)
    df_uf_2024['total_investido_pedemeia_bimestre'] = df_uf_2024['uf'].map(lambda u: df_bim.get(u, {}).get('total_investido_mar_abr_2024_retificado', 0.0))
    df_uf_2024['qtd_pagamentos_pedemeia_bimestre'] = df_uf_2024['uf'].map(lambda u: df_bim.get(u, {}).get('qtd_pagamentos_mar_abr_2024_retificado', 0)).astype(int)

    # Separar folha 202502 por tipo de incentivo (Conclusão, Enem e demais = Frequência + Matrícula)
    df_2502 = df_detail[df_detail['mes_folha'] == '202502'].copy()
    if not df_2502.empty:
        val_conc = df_2502[df_2502['tipo_incentivo'].str.contains('Concl', case=False, na=False)].groupby('uf')['total_investido_pedemeia'].sum().to_dict()
        qtd_conc = df_2502[df_2502['tipo_incentivo'].str.contains('Concl', case=False, na=False)].groupby('uf')['qtd_pagamentos_pedemeia'].sum().to_dict()
        val_enem = df_2502[df_2502['tipo_incentivo'].str.contains('Enem', case=False, na=False)].groupby('uf')['total_investido_pedemeia'].sum().to_dict()
        qtd_enem = df_2502[df_2502['tipo_incentivo'].str.contains('Enem', case=False, na=False)].groupby('uf')['qtd_pagamentos_pedemeia'].sum().to_dict()
        df_demais = df_2502[~df_2502['tipo_incentivo'].str.contains('Concl|Enem', case=False, na=False)]
        val_dem = df_demais.groupby('uf')['total_investido_pedemeia'].sum().to_dict()
        qtd_dem = df_demais.groupby('uf')['qtd_pagamentos_pedemeia'].sum().to_dict()

        df_uf_2024['valor_conclusao_202502'] = df_uf_2024['uf'].map(val_conc).fillna(0.0)
        df_uf_2024['qtd_pagamentos_conclusao_202502'] = df_uf_2024['uf'].map(qtd_conc).fillna(0).astype(int)
        df_uf_2024['valor_enem_202502'] = df_uf_2024['uf'].map(val_enem).fillna(0.0)
        df_uf_2024['qtd_pagamentos_enem_202502'] = df_uf_2024['uf'].map(qtd_enem).fillna(0).astype(int)
        df_uf_2024['valor_demais_202502'] = df_uf_2024['uf'].map(val_dem).fillna(0.0)
        df_uf_2024['qtd_pagamentos_demais_202502'] = df_uf_2024['uf'].map(qtd_dem).fillna(0).astype(int)
        df_uf_2024['total_investido_pedemeia_ciclo2024'] = (
            df_uf_2024['total_investido_pedemeia_ano'] +
            df_uf_2024['valor_conclusao_202502'] +
            df_uf_2024['valor_enem_202502']
        )
        df_uf_2024['qtd_pagamentos_pedemeia_ciclo2024'] = (
            df_uf_2024['qtd_pagamentos_pedemeia_ano'] +
            df_uf_2024['qtd_pagamentos_conclusao_202502'] +
            df_uf_2024['qtd_pagamentos_enem_202502']
        )
        df_uf_2024['razao_conclusao_pagamentos_2024_pct'] = (
            100.0 * df_uf_2024['qtd_pagamentos_conclusao_202502'] / df_uf_2024['qtd_pagamentos_pedemeia_ano']
        )
        df_uf_2024['custo_por_estudante_proxy_2024'] = (
            df_uf_2024['total_investido_pedemeia_ano'] / df_uf_2024['qtd_pagamentos_incentivo_matricula']
        )

    df_uf_2024 = df_uf_2024.sort_values(by='total_investido_pedemeia_ano', ascending=False)

    print(f"TOTAL BRASIL 2024 (9 folhas): R$ {df_uf_2024['total_investido_pedemeia_ano'].sum():,.2f} | Parcelas: {df_uf_2024['qtd_pagamentos_pedemeia_ano'].sum():,}")
    if 'total_investido_pedemeia_ciclo2024' in df_uf_2024.columns:
        print(f"TOTAL BRASIL CICLO 2024 (2024 + Conclusão/Enem fev/2025): R$ {df_uf_2024['total_investido_pedemeia_ciclo2024'].sum():,.2f} | Parcelas: {df_uf_2024['qtd_pagamentos_pedemeia_ciclo2024'].sum():,}")

    scratch_csv = SCRATCH_DIR / "pe_de_meia_uf_nacional.csv"
    df_uf_2024.to_csv(scratch_csv, index=False, encoding='utf-8-sig')
    out_uf = os.path.normpath(str(PROCESSED_DIR / "pe_de_meia_uf_nacional.csv"))
    subprocess.run(
        ["powershell", "-Command", f"Copy-Item -Force -Path '{os.path.normpath(str(scratch_csv))}' -Destination '{out_uf}'"],
        check=True
    )
    print(f"[OK] Salvo em {out_uf}", flush=True)

if __name__ == "__main__":
    process_pe_de_meia_nacional()
