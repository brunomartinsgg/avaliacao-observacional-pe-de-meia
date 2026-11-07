import os
import subprocess
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
RAW_DIR = BASE_DIR / "dados_brutos"
PROCESSED_DIR = BASE_DIR / "dados_tratados"
SCRATCH_DIR = Path(r"C:\Users\Bruno\.gemini\antigravity\brain\df4e2c63-3667-4160-9f37-ee1b397d5125\scratch")

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

def build_master_matrix():
    print("=================================================================", flush=True)
    print("Construindo a Matriz Mestre Nacional (Painel 27 UFs x Rede x Ano)...", flush=True)
    print("=================================================================", flush=True)

    years_master = [2019, 2021, 2022, 2023, 2024, 2025]
    redes_master = ["Estadual", "Privada"]

    spine = []
    for cod_uf, sg_uf, nome_uf in UF_MAP:
        for yr in years_master:
            for rd in redes_master:
                spine.append({
                    "nivel": "UF",
                    "codigo_uf": cod_uf,
                    "uf": sg_uf,
                    "unidade_geografica": nome_uf,
                    "ano": yr,
                    "rede": rd,
                    "rede_publica": 1 if rd == "Estadual" else 0,
                    "pos_pedemeia": 1 if yr >= 2024 else 0
                })

    df_master = pd.DataFrame(spine)

    # 1. Integrar IDEB UF (2019, 2021, 2023, 2025)
    file_ideb = PROCESSED_DIR / "ideb_uf_brasil_ensino_medio.csv"
    if file_ideb.exists():
        df_ideb = pd.read_csv(file_ideb)
        df_ideb_uf = df_ideb[(df_ideb['nivel'] == 'UF') & (df_ideb['rede'].isin(redes_master))].copy()
        ideb_cols = ['uf', 'ano', 'rede', 'ideb_nota_matematica', 'ideb_nota_portugues', 'ideb_nota_media', 'ideb_indicador_rendimento', 'ideb_observado', 'ideb_taxa_aprovacao_em']
        df_master = pd.merge(df_master, df_ideb_uf[ideb_cols], on=['uf', 'ano', 'rede'], how='left')

    # 2. Integrar Taxas de Rendimento UF (2022, 2023, 2024, 2025)
    file_rend = PROCESSED_DIR / "inep_taxas_rendimento_uf_brasil.csv"
    if file_rend.exists():
        df_rend = pd.read_csv(file_rend)
        df_rend_uf = df_rend[(df_rend['nivel'] == 'UF') & (df_rend['rede'].isin(redes_master))].copy()
        rend_cols = [
            'uf', 'ano', 'rede',
            'taxa_aprovacao_ensino_medio', 'taxa_reprovacao_ensino_medio', 'taxa_abandono_ensino_medio',
            'taxa_abandono_em_1serie', 'taxa_abandono_em_2serie', 'taxa_abandono_em_3serie'
        ]
        df_master = pd.merge(df_master, df_rend_uf[rend_cols], on=['uf', 'ano', 'rede'], how='left')

    # 3. Integrar Pé-de-Meia Nacional por UF (Exercício 2024, Ciclo 2024 e métricas proxy)
    file_pm = PROCESSED_DIR / "pe_de_meia_uf_nacional.csv"
    if file_pm.exists():
        df_pm = pd.read_csv(file_pm)
        pm_cols = [
            'uf', 'ano',
            'total_investido_pedemeia_bimestre', 'qtd_pagamentos_pedemeia_bimestre',
            'total_investido_pedemeia_ano', 'qtd_pagamentos_pedemeia_ano',
            'qtd_pagamentos_incentivo_matricula', 'qtd_pagamentos_incentivo_frequencia',
            'valor_conclusao_202502', 'qtd_pagamentos_conclusao_202502',
            'valor_enem_202502', 'qtd_pagamentos_enem_202502',
            'valor_demais_202502', 'qtd_pagamentos_demais_202502',
            'total_investido_pedemeia_ciclo2024', 'qtd_pagamentos_pedemeia_ciclo2024',
            'razao_conclusao_pagamentos_2024_pct', 'custo_por_estudante_proxy_2024'
        ]
        pm_cols = [c for c in pm_cols if c in df_pm.columns]
        df_pm_merge = df_pm[pm_cols].copy()
        df_pm_merge['rede'] = 'Estadual'
        df_master = pd.merge(df_master, df_pm_merge, on=['uf', 'ano', 'rede'], how='left')

    # 4. Integrar Famílias e Pessoas Cadastradas no CadÚnico (esta_assistencia.csv - ano 2024, Dezembro)
    file_cad = RAW_DIR / "alagoas_educacao" / "esta_assistencia.csv"
    if not file_cad.exists():
        file_cad = SCRATCH_DIR / "esta_assistencia.csv"
    if file_cad.exists():
        df_cad = pd.read_csv(file_cad)
        df_cad_2024 = df_cad[(df_cad['ano'] == 2024) & (df_cad['inf_subcategoria'] == 'Dezembro')].copy()
        cad_uf = df_cad_2024.pivot(index='co_uf', columns='inf_categoria', values='valor').reset_index()
        cad_uf.columns = ['codigo_uf', 'familias_cadastradas_cadunico', 'pessoas_cadastradas_cadunico']
        cad_uf['ano'] = 2024
        cad_uf['rede'] = 'Estadual'
        df_master = pd.merge(
            df_master,
            cad_uf[['codigo_uf', 'ano', 'rede', 'familias_cadastradas_cadunico', 'pessoas_cadastradas_cadunico']],
            on=['codigo_uf', 'ano', 'rede'],
            how='left'
        )
        df_master['reais_por_pessoa_cadastrada_cadunico_2024'] = (
            df_master['total_investido_pedemeia_ano'] / df_master['pessoas_cadastradas_cadunico']
        )

    scratch_master = SCRATCH_DIR / "matriz_mestre.csv"
    df_master.to_csv(scratch_master, index=False, encoding='utf-8-sig')
    out_master = os.path.normpath(str(PROCESSED_DIR / "matriz_mestre.csv"))
    subprocess.run(
        ["powershell", "-Command", f"Copy-Item -Force -Path '{os.path.normpath(str(scratch_master))}' -Destination '{out_master}'"],
        check=True
    )
    print(f"[SUCESSO] Matriz Mestre Nacional gerada em: {out_master} ({len(df_master)} linhas x {df_master.shape[1]} colunas)")

if __name__ == "__main__":
    build_master_matrix()
