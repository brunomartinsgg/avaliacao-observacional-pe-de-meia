import os
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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

REGIAO_MAP = {
    'RO': 'Norte', 'AC': 'Norte', 'AM': 'Norte', 'RR': 'Norte', 'PA': 'Norte', 'AP': 'Norte', 'TO': 'Norte',
    'MA': 'Nordeste', 'PI': 'Nordeste', 'CE': 'Nordeste', 'RN': 'Nordeste', 'PB': 'Nordeste',
    'PE': 'Nordeste', 'AL': 'Nordeste', 'SE': 'Nordeste', 'BA': 'Nordeste',
    'MG': 'Sudeste', 'ES': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'SC': 'Sul', 'RS': 'Sul',
    'MS': 'Centro-Oeste', 'MT': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'DF': 'Centro-Oeste'
}

REGIAO_COLORS = {
    'Nordeste': '#d95f02',
    'Norte': '#1b9e77',
    'Centro-Oeste': '#7570b3',
    'Sudeste': '#386cb0',
    'Sul': '#e7298a'
}

FOOTER_TEXT = "média simples das 27 UFs; faixa = IC 95%"

def save_fig_powershell(fig, filename):
    scratch_path = SCRATCH_DIR / filename
    fig.savefig(scratch_path, format='png', dpi=300, bbox_inches='tight')

    dest_path = os.path.normpath(str(CHARTS_DIR / filename))
    src_path = os.path.normpath(str(scratch_path))

    try:
        subprocess.run(
            ["powershell", "-Command", f"Copy-Item -Force -Path '{src_path}' -Destination '{dest_path}'"],
            check=True
        )
        print(f"[OK] Gráfico salvo com sucesso em dados_tratados/graficos/: {filename}", flush=True)
    except Exception as e:
        print(f"[AVISO] Salvo em scratch ({scratch_path}); cópia para destino requer permissão fora do sandbox: {e}", flush=True)

def generate_visualizations():
    print("=================================================================", flush=True)
    print("Gerando Gráficos e Visualizações Nacionais (27 UFs)...", flush=True)
    print("=================================================================", flush=True)

    master_file = PROCESSED_DIR / "matriz_mestre.csv"
    if not master_file.exists():
        print(f"[ERRO] {master_file} não encontrado.")
        return

    df = pd.read_csv(master_file)

    # 1. Repasses do Pé-de-Meia como R$ por pessoa cadastrada no CadÚnico em 2024 por UF (ordenado e colorido por região)
    df_2024_est = df[(df['ano'] == 2024) & (df['rede'] == 'Estadual')].copy()
    if not df_2024_est.empty and 'reais_por_pessoa_cadastrada_cadunico_2024' in df_2024_est.columns:
        df_2024_est['regiao'] = df_2024_est['uf'].map(REGIAO_MAP)
        df_2024_est = df_2024_est.sort_values('reais_por_pessoa_cadastrada_cadunico_2024', ascending=False).reset_index(drop=True)

        fig, ax1 = plt.subplots(figsize=(15, 6.5))
        bar_colors = [REGIAO_COLORS[r] for r in df_2024_est['regiao']]
        bars = ax1.bar(
            df_2024_est['uf'],
            df_2024_est['reais_por_pessoa_cadastrada_cadunico_2024'],
            color=bar_colors,
            alpha=0.9,
            edgecolor='#333333',
            linewidth=0.6
        )

        media_uf = df_2024_est['reais_por_pessoa_cadastrada_cadunico_2024'].mean()
        total_br = df_2024_est['total_investido_pedemeia_ano'].sum() / df_2024_est['pessoas_cadastradas_cadunico'].sum()

        ax1.axhline(total_br, color='#222222', linestyle='--', linewidth=1.4, label=f'Razão Nacional Agregada (Brasil = R$ {total_br:.2f})')
        ax1.axhline(media_uf, color='#666666', linestyle=':', linewidth=1.4, label=f'Média Simples das 27 UFs (R$ {media_uf:.2f})')

        ax1.set_title(
            'Repasses do Pé-de-Meia por Pessoa Cadastrada no CadÚnico em 2024 por UF (Exercício 2024, Ordenado e Colorido por Região)',
            fontsize=12.5, fontweight='bold', pad=14
        )
        ax1.set_xlabel('Unidade da Federação (UF)', fontsize=11, fontweight='bold')
        ax1.set_ylabel('R$ por Pessoa Cadastrada no CadÚnico (2024)', fontsize=11, fontweight='bold')
        ax1.set_ylim(0, df_2024_est['reais_por_pessoa_cadastrada_cadunico_2024'].max() * 1.15)

        for bar in bars:
            h = bar.get_height()
            ax1.annotate(
                f'{h:.1f}',
                (bar.get_x() + bar.get_width() / 2, h),
                xytext=(0, 3),
                textcoords='offset points',
                ha='center', va='bottom',
                fontsize=8, fontweight='bold'
            )

        regiao_Order = ['Nordeste', 'Norte', 'Centro-Oeste', 'Sudeste', 'Sul']
        region_patches = [mpatches.Patch(color=REGIAO_COLORS[r], label=r) for r in regiao_Order]
        handles_lines, labels_lines = ax1.get_legend_handles_labels()
        ax1.legend(
            handles=region_patches + handles_lines,
            title='Grande Região (IBGE) e Referências',
            loc='upper right',
            frameon=True,
            fontsize=9,
            title_fontsize=9.5,
            ncol=2
        )

        fig.text(
            0.5, -0.02,
            "Fonte: CGU/Portal da Transparência (Exercício 2024 — 9 folhas) e Cadastro Único (Dez/2024). Elaboração própria.",
            ha='center', fontsize=9, fontstyle='italic', color='#333333'
        )
        plt.tight_layout()
        save_fig_powershell(fig, "grafico_repasses_pedemeia_uf_nacional.png")
        plt.close(fig)

    # 2. Evolução da Nota de Matemática SAEB e IDEB por Rede (2019–2025) com rodapé IC 95%
    df_ideb = df[df['ano'].isin([2019, 2021, 2023, 2025])].copy()
    if not df_ideb.empty:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.8))
        sns.lineplot(
            data=df_ideb, x='ano', y='ideb_nota_matematica', hue='rede',
            errorbar=('ci', 95), marker='o', linewidth=2.5, ax=ax1,
            palette={'Estadual': '#1f77b4', 'Privada': '#ff7f0e'}
        )
        ax1.axvline(2023.5, color='red', linestyle='--', alpha=0.7, label='Início Pé-de-Meia (2024)')
        ax1.set_title('Média UF da Nota SAEB Matemática (2019–2025)', fontsize=12, fontweight='bold')
        ax1.set_xticks([2019, 2021, 2023, 2025])
        ax1.set_xlabel('Ano', fontsize=10.5)
        ax1.set_ylabel('Proficiência Média SAEB Matemática (pontos)', fontsize=10.5)
        ax1.legend()

        sns.lineplot(
            data=df_ideb, x='ano', y='ideb_observado', hue='rede',
            errorbar=('ci', 95), marker='s', linewidth=2.5, ax=ax2,
            palette={'Estadual': '#1f77b4', 'Privada': '#ff7f0e'}
        )
        ax2.axvline(2023.5, color='red', linestyle='--', alpha=0.7, label='Início Pé-de-Meia (2024)')
        ax2.set_title('Média UF do IDEB Observado no Ensino Médio (2019–2025)', fontsize=12, fontweight='bold')
        ax2.set_xticks([2019, 2021, 2023, 2025])
        ax2.set_xlabel('Ano', fontsize=10.5)
        ax2.set_ylabel('IDEB Observado (0 a 10)', fontsize=10.5)
        ax2.legend()

        fig.text(0.5, -0.02, FOOTER_TEXT, ha='center', fontsize=10, fontstyle='italic', fontweight='bold', color='#222222')
        plt.tight_layout()
        save_fig_powershell(fig, "grafico_ideb_matematica_evolucao.png")
        plt.close(fig)

    # 3. Taxas de Abandono e Aprovação por UF e Rede (2022–2025) com rodapé IC 95%
    df_rend = df[df['ano'].isin([2022, 2023, 2024, 2025])].copy()
    if not df_rend.empty:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.8))
        sns.lineplot(
            data=df_rend, x='ano', y='taxa_abandono_ensino_medio', hue='rede',
            errorbar=('ci', 95), marker='o', linewidth=2.5, ax=ax1,
            palette={'Estadual': '#d62728', 'Privada': '#2ca02c'}
        )
        ax1.axvline(2023.5, color='black', linestyle='--', alpha=0.7, label='Início Pé-de-Meia (2024)')
        ax1.set_title('Taxa Média de Abandono no Ensino Médio por UF (2022–2025)', fontsize=12, fontweight='bold')
        ax1.set_xticks([2022, 2023, 2024, 2025])
        ax1.set_xlabel('Ano', fontsize=10.5)
        ax1.set_ylabel('Taxa de Abandono (%)', fontsize=10.5)
        ax1.legend()

        sns.lineplot(
            data=df_rend, x='ano', y='taxa_aprovacao_ensino_medio', hue='rede',
            errorbar=('ci', 95), marker='s', linewidth=2.5, ax=ax2,
            palette={'Estadual': '#1f77b4', 'Privada': '#2ca02c'}
        )
        ax2.axvline(2023.5, color='black', linestyle='--', alpha=0.7, label='Início Pé-de-Meia (2024)')
        ax2.set_title('Taxa Média de Aprovação no Ensino Médio por UF (2022–2025)', fontsize=12, fontweight='bold')
        ax2.set_xticks([2022, 2023, 2024, 2025])
        ax2.set_xlabel('Ano', fontsize=10.5)
        ax2.set_ylabel('Taxa de Aprovação (%)', fontsize=10.5)
        ax2.legend()

        fig.text(0.5, -0.02, FOOTER_TEXT, ha='center', fontsize=10, fontstyle='italic', fontweight='bold', color='#222222')
        plt.tight_layout()
        save_fig_powershell(fig, "grafico_taxas_rendimento_2025.png")
        plt.close(fig)

    # 4. Novo Gráfico: Diferença (Estadual − Privada) por Ano para Abandono (2022–2025) e SAEB Matemática (2019–2025)
    piv_ab = df_rend.pivot(index=['uf', 'ano'], columns='rede', values='taxa_abandono_ensino_medio').reset_index()
    piv_ab['diff_estadual_privada'] = piv_ab['Estadual'] - piv_ab['Privada']

    piv_mat = df_ideb.pivot(index=['uf', 'ano'], columns='rede', values='ideb_nota_matematica').reset_index()
    piv_mat['diff_estadual_privada'] = piv_mat['Estadual'] - piv_mat['Privada']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.8))

    sns.lineplot(
        data=piv_ab, x='ano', y='diff_estadual_privada',
        errorbar=('ci', 95), marker='o', linewidth=2.5, color='#d62728', ax=ax1,
        label='Diferença (Estadual − Privada)'
    )
    ax1.axhline(0, color='#666666', linestyle=':', linewidth=1.0)
    ax1.axvline(2023.5, color='black', linestyle='--', alpha=0.7, label='Início Pé-de-Meia (2024)')
    ax1.set_title('Diferença Estadual − Privada: Taxa de Abandono EM (2022–2025)', fontsize=12, fontweight='bold')
    ax1.set_xticks([2022, 2023, 2024, 2025])
    ax1.set_xlabel('Ano', fontsize=10.5)
    ax1.set_ylabel('Diferença Estadual − Privada (p.p.)', fontsize=10.5)
    for yr in [2022, 2023, 2024, 2025]:
        m_val = piv_ab[piv_ab['ano'] == yr]['diff_estadual_privada'].mean()
        ax1.annotate(f'{m_val:+.2f} p.p.', (yr, m_val), xytext=(0, 8), textcoords='offset points', ha='center', fontsize=8.5, fontweight='bold')
    ax1.legend(loc='upper right')

    sns.lineplot(
        data=piv_mat, x='ano', y='diff_estadual_privada',
        errorbar=('ci', 95), marker='s', linewidth=2.5, color='#1f77b4', ax=ax2,
        label='Diferença (Estadual − Privada)'
    )
    ax2.axvline(2023.5, color='red', linestyle='--', alpha=0.7, label='Início Pé-de-Meia (2024)')
    ax2.set_title('Diferença Estadual − Privada: SAEB Matemática (2019–2025)', fontsize=12, fontweight='bold')
    ax2.set_xticks([2019, 2021, 2023, 2025])
    ax2.set_xlabel('Ano', fontsize=10.5)
    ax2.set_ylabel('Diferença Estadual − Privada (pontos SAEB)', fontsize=10.5)
    for yr in [2019, 2021, 2023, 2025]:
        m_val = piv_mat[piv_mat['ano'] == yr]['diff_estadual_privada'].mean()
        ax2.annotate(f'{m_val:+.2f} pts', (yr, m_val), xytext=(0, 8), textcoords='offset points', ha='center', fontsize=8.5, fontweight='bold')
    ax2.legend(loc='lower right')

    fig.text(0.5, -0.02, FOOTER_TEXT, ha='center', fontsize=10, fontstyle='italic', fontweight='bold', color='#222222')
    plt.tight_layout()
    save_fig_powershell(fig, "grafico_diferenca_estadual_privada.png")
    plt.close(fig)

    print("\n[SUCESSO] Todos os 4 gráficos nacionais foram gerados!", flush=True)

if __name__ == "__main__":
    generate_visualizations()
