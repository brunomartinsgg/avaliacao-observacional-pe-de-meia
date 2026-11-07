import os
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROCESSED_DIR = BASE_DIR / "dados_tratados"
CHARTS_DIR = PROCESSED_DIR / "graficos"

SCRATCH_DIR = Path(r"C:\Users\Bruno\.gemini\antigravity\brain\df4e2c63-3667-4160-9f37-ee1b397d5125\scratch")
SCRATCH_DIR.mkdir(parents=True, exist_ok=True)

out_dir_str = os.path.normpath(str(CHARTS_DIR))
subprocess.run(
    ["powershell", "-Command", f"New-Item -ItemType Directory -Force -Path '{out_dir_str}'"],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
)

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

def save_fig_powershell(fig, filename):
    scratch_path = SCRATCH_DIR / filename
    fig.savefig(scratch_path, format='png', dpi=300, bbox_inches='tight')

    dest_path = os.path.normpath(str(CHARTS_DIR / filename))
    src_path = os.path.normpath(str(scratch_path))

    subprocess.run(
        ["powershell", "-Command", f"Copy-Item -Force -Path '{src_path}' -Destination '{dest_path}'"],
        check=True
    )
    print(f"[OK] Gráfico salvo com sucesso: {filename}", flush=True)

def generate_visualizations():
    print("=================================================================", flush=True)
    print("Gerando Gráficos e Visualizações Nacionais (27 UFs)...", flush=True)
    print("=================================================================", flush=True)

    master_file = PROCESSED_DIR / "matriz_mestre.csv"
    pm_file = PROCESSED_DIR / "pe_de_meia_uf_nacional.csv"
    if not master_file.exists():
        print(f"[ERRO] {master_file} não encontrado.")
        return

    df = pd.read_csv(master_file)

    # 1. Execução Financeira do Pé-de-Meia por UF (Mar–Abr/2024, sem beneficiários únicos)
    if pm_file.exists():
        df_pm = pd.read_csv(pm_file).sort_values('total_investido_pedemeia_bimestre', ascending=False)
        fig, ax1 = plt.subplots(figsize=(14, 6))
        bars = ax1.bar(df_pm['uf'], df_pm['total_investido_pedemeia_bimestre'] / 1e6, color='#1f77b4', alpha=0.88)
        ax1.set_title('Execução Financeira do Pé-de-Meia por UF — 1º Bimestre Operacional (Mar–Abr/2024)', fontsize=13, fontweight='bold', pad=12)
        ax1.set_xlabel('Unidade da Federação (UF)', fontsize=11, fontweight='bold')
        ax1.set_ylabel('Total Transferido (R$ Milhões)', fontsize=11, fontweight='bold', color='#1f77b4')
        for bar in bars[:10]:
            h = bar.get_height()
            ax1.annotate(f'{h:.1f}M', (bar.get_x() + bar.get_width()/2, h), xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', fontsize=8, fontweight='bold')
        plt.tight_layout()
        save_fig_powershell(fig, "grafico_repasses_pedemeia_uf_nacional.png")
        plt.close(fig)

    # 2. Evolução da Nota de Matemática SAEB e IDEB por Rede (2019–2025)
    df_ideb = df[df['ano'].isin([2019, 2021, 2023, 2025])].copy()
    if not df_ideb.empty:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))
        sns.lineplot(data=df_ideb, x='ano', y='ideb_nota_matematica', hue='rede', marker='o', linewidth=2.5, ax=ax1, palette={'Estadual': '#1f77b4', 'Privada': '#ff7f0e'})
        ax1.axvline(2023.5, color='red', linestyle='--', alpha=0.7, label='Início Pé-de-Meia (2024)')
        ax1.set_title('Média UF da Nota SAEB Matemática (2019–2025)', fontsize=12, fontweight='bold')
        ax1.set_xticks([2019, 2021, 2023, 2025])
        ax1.set_ylabel('Proficiência Média SAEB Matemática', fontsize=11)
        ax1.legend()

        sns.lineplot(data=df_ideb, x='ano', y='ideb_observado', hue='rede', marker='s', linewidth=2.5, ax=ax2, palette={'Estadual': '#1f77b4', 'Privada': '#ff7f0e'})
        ax2.axvline(2023.5, color='red', linestyle='--', alpha=0.7, label='Início Pé-de-Meia (2024)')
        ax2.set_title('Média UF do IDEB Observado no Ensino Médio (2019–2025)', fontsize=12, fontweight='bold')
        ax2.set_xticks([2019, 2021, 2023, 2025])
        ax2.set_ylabel('IDEB Observado (0 a 10)', fontsize=11)
        ax2.legend()
        plt.tight_layout()
        save_fig_powershell(fig, "grafico_ideb_matematica_evolucao.png")
        plt.close(fig)

    # 3. Taxas de Abandono e Aprovação por UF e Rede (2022–2025)
    df_rend = df[df['ano'].isin([2022, 2023, 2024, 2025])].copy()
    if not df_rend.empty:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))
        sns.lineplot(data=df_rend, x='ano', y='taxa_abandono_ensino_medio', hue='rede', marker='o', linewidth=2.5, ax=ax1, palette={'Estadual': '#d62728', 'Privada': '#2ca02c'})
        ax1.axvline(2023.5, color='black', linestyle='--', alpha=0.7, label='Início Pé-de-Meia (2024)')
        ax1.set_title('Taxa Média de Abandono no Ensino Médio por UF (2022–2025)', fontsize=12, fontweight='bold')
        ax1.set_xticks([2022, 2023, 2024, 2025])
        ax1.set_ylabel('Taxa de Abandono (%)', fontsize=11)
        ax1.legend()

        sns.lineplot(data=df_rend, x='ano', y='taxa_aprovacao_ensino_medio', hue='rede', marker='s', linewidth=2.5, ax=ax2, palette={'Estadual': '#1f77b4', 'Privada': '#2ca02c'})
        ax2.axvline(2023.5, color='black', linestyle='--', alpha=0.7, label='Início Pé-de-Meia (2024)')
        ax2.set_title('Taxa Média de Aprovação no Ensino Médio por UF (2022–2025)', fontsize=12, fontweight='bold')
        ax2.set_xticks([2022, 2023, 2024, 2025])
        ax2.set_ylabel('Taxa de Aprovação (%)', fontsize=11)
        ax2.legend()
        plt.tight_layout()
        save_fig_powershell(fig, "grafico_taxas_rendimento_2025.png")
        plt.close(fig)

    print("\n[SUCESSO] Todos os gráficos nacionais foram gerados e salvos em dados_tratados/graficos/")

if __name__ == "__main__":
    generate_visualizations()
