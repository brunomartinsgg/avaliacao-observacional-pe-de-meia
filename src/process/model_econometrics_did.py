import os
import pandas as pd
import statsmodels.formula.api as smf
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROCESSED_DIR = BASE_DIR / "dados_tratados"
SCRATCH_OUT = Path(r"C:\Users\Bruno\.gemini\antigravity\brain\df4e2c63-3667-4160-9f37-ee1b397d5125\scratch\did_summaries_fe_t.txt")

def run_national_did_econometrics():
    print("=================================================================", flush=True)
    print("Modelagem Econométrica DiD Nacional: Efeito Fixo UF x Rede + Ano", flush=True)
    print("Erros-Padrão Agrupados por UF (27 Clusters) com Distribuição t (use_t=True)", flush=True)
    print("=================================================================", flush=True)

    master_path = PROCESSED_DIR / "matriz_mestre.csv"
    df_master = pd.read_csv(master_path)
    df_master['uf_rede'] = df_master['uf'] + "_" + df_master['rede']

    out_lines = []

    def log_model(title, model, param_keys):
        print(f"\n--- {title} ---")
        for pk in param_keys:
            if pk in model.params:
                b = model.params[pk]
                se = model.bse[pk]
                tval = model.tvalues[pk]
                pval = model.pvalues[pk]
                ci_l, ci_u = model.conf_int().loc[pk]
                print(f"  {pk}: coef={b:+.4f} | std_err={se:.4f} | t={tval:+.3f} | P>|t|={pval:.4f} | IC95%=[{ci_l:+.4f}, {ci_u:+.4f}]")
        out_lines.append(f"====================================================================\n{title}\n====================================================================\n")
        out_lines.append(model.summary().as_text())
        out_lines.append("\n\n")

    # 1. Modelos DiD para Taxas de Rendimento (2022, 2023 vs 2024, 2025)
    df_rend = df_master[df_master['ano'].isin([2022, 2023, 2024, 2025])].dropna(subset=['taxa_abandono_ensino_medio']).copy()
    df_pre_rend = df_rend[df_rend['ano'].isin([2022, 2023])].copy()
    df_pre_rend['ano_2023'] = (df_pre_rend['ano'] == 2023).astype(int)

    for col, label in [
        ("taxa_abandono_ensino_medio", "Taxa de Abandono EM"),
        ("taxa_aprovacao_ensino_medio", "Taxa de Aprovação EM"),
        ("taxa_reprovacao_ensino_medio", "Taxa de Reprovação EM"),
    ]:
        m_did = smf.ols(
            f"{col} ~ rede_publica:pos_pedemeia + C(uf_rede) + C(ano, Treatment(reference=2022))",
            data=df_rend
        ).fit(cov_type='cluster', cov_kwds={'groups': df_rend['uf']}, use_t=True)
        log_model(f"DiD FE (UFxRede + Ano) — {label} (2022-2025, N={int(m_did.nobs)})", m_did, ["rede_publica:pos_pedemeia"])

        m_pre = smf.ols(
            f"{col} ~ rede_publica:ano_2023 + C(uf_rede) + C(ano, Treatment(reference=2022))",
            data=df_pre_rend
        ).fit(cov_type='cluster', cov_kwds={'groups': df_pre_rend['uf']}, use_t=True)
        log_model(f"Pré-Tendência FE (UFxRede + Ano) — {label} (2022 vs 2023, N={int(m_pre.nobs)})", m_pre, ["rede_publica:ano_2023"])

    # 2. Modelos DiD para IDEB, Componentes (N e P) e Notas SAEB (2019-2025 e 2023 vs 2025)
    df_ideb = df_master[df_master['ano'].isin([2019, 2021, 2023, 2025])].dropna(subset=['ideb_nota_matematica']).copy()
    df_ideb_23_25 = df_master[df_master['ano'].isin([2023, 2025])].dropna(subset=['ideb_nota_matematica']).copy()
    df_pre_ideb = df_ideb[df_ideb['ano'].isin([2019, 2021, 2023])].copy()
    df_pre_ideb['ano_2021'] = (df_pre_ideb['ano'] == 2021).astype(int)
    df_pre_ideb['ano_2023'] = (df_pre_ideb['ano'] == 2023).astype(int)

    for col, label in [
        ("ideb_nota_matematica", "SAEB Matemática"),
        ("ideb_nota_portugues", "SAEB Língua Portuguesa"),
        ("ideb_nota_media", "Nota Média Padronizada SAEB (N)"),
        ("ideb_indicador_rendimento", "Indicador de Rendimento IDEB (P)"),
        ("ideb_observado", "IDEB Observado (N x P)"),
    ]:
        m_full = smf.ols(
            f"{col} ~ rede_publica:pos_pedemeia + C(uf_rede) + C(ano, Treatment(reference=2019))",
            data=df_ideb
        ).fit(cov_type='cluster', cov_kwds={'groups': df_ideb['uf']}, use_t=True)
        log_model(f"DiD FE (UFxRede + Ano) Painel Completo — {label} (2019-2025, N={int(m_full.nobs)})", m_full, ["rede_publica:pos_pedemeia"])

        m_win = smf.ols(
            f"{col} ~ rede_publica:pos_pedemeia + C(uf_rede) + C(ano, Treatment(reference=2023))",
            data=df_ideb_23_25
        ).fit(cov_type='cluster', cov_kwds={'groups': df_ideb_23_25['uf']}, use_t=True)
        log_model(f"DiD FE (UFxRede + Ano) Janela Imediata — {label} (2023 vs 2025, N={int(m_win.nobs)})", m_win, ["rede_publica:pos_pedemeia"])

        m_pre = smf.ols(
            f"{col} ~ rede_publica:ano_2021 + rede_publica:ano_2023 + C(uf_rede) + C(ano, Treatment(reference=2019))",
            data=df_pre_ideb
        ).fit(cov_type='cluster', cov_kwds={'groups': df_pre_ideb['uf']}, use_t=True)
        log_model(
            f"Pré-Tendência FE (UFxRede + Ano) — {label} (2019-2023, N={int(m_pre.nobs)})",
            m_pre,
            ["rede_publica:ano_2021", "rede_publica:ano_2023"]
        )

    SCRATCH_OUT.write_text("".join(out_lines), encoding="utf-8")
    print(f"\n[OK] Todos os summaries brutos salvos em {SCRATCH_OUT}", flush=True)

if __name__ == "__main__":
    run_national_did_econometrics()
