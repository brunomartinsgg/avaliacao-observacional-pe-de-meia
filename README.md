# Avaliação Observacional em Escopo Nacional do Programa Pé-de-Meia (Painel das 27 UFs, 2019–2025)

Este repositório contém o pipeline de engenharia de dados e modelagem econométrica por **Diferenças em Diferenças (DiD)** em painel nacional (27 Unidades da Federação $\times$ 2 redes de ensino [`Estadual` e `Privada`] $\times$ anos `2019` a `2025`), combinando os dados oficiais do **INEP** (Censo Escolar — Taxas de Rendimento e IDEB/SAEB do Ensino Médio) e da **Controladoria-Geral da União (CGU — Portal da Transparência)** para o programa **Pé-de-Meia**.

---

## 1. Estrutura de Diretórios e Arquivos de Entrega

```text
├── dados_brutos/
│   ├── censo_escolar/              # Pacotes ZIP oficiais de Taxas de Rendimento do INEP (2022–2025)
│   ├── ideb_saeb/                  # Pacotes ZIP oficiais do IDEB e notas SAEB do INEP (2019–2025)
│   └── pe_de_meia_transparencia/   # Pacotes ZIP mensais do Pé-de-Meia (CGU / Portal da Transparência)
├── dados_tratados/
│   ├── graficos/                   # Visualizações geradas pelo pipeline nacional
│   ├── ideb_uf_brasil_ensino_medio.csv
│   ├── inep_taxas_rendimento_uf_brasil.csv
│   ├── pe_de_meia_uf_nacional.csv
│   └── matriz_mestre.csv           # Painel balanceado consolidado (324 linhas x 39 colunas)
├── src/
│   ├── collect/                    # Scripts de coleta automatizada (INEP e CGU)
│   └── process/                    # Scripts de tratamento nacional, matriz mestre, econometria DiD e gráficos
├── rascunho/                       # Scripts auxiliares de diagnóstico, inspeção e testes exploratórios
├── relatorio_final_pe_de_meia_ab2.md  # Relatório técnico principal (versão limpa para submissão)
├── apendice_summaries_brutos_did.md   # Apêndice separado com os 21 blocos summary() brutos do statsmodels
├── dicionario_de_dados.md             # Dicionário de dados completo da matriz_mestre.csv (39 colunas)
└── README.md
```

---

## 2. Ordem de Execução do Pipeline

Execute os scripts abaixo a partir da raiz do projeto, na ordem numérica indicada:

### Etapa 1 — Coleta de Dados Brutos (`src/collect/`)
1. **Download do IDEB e Notas SAEB (Brasil, Regiões, UFs e Municípios — 2019–2025)**:
   ```powershell
   python src/collect/download_all_ideb_curl.py
   ```
2. **Download das Taxas de Rendimento Escolar do INEP (2022–2025)**:
   ```powershell
   python src/collect/download_inep_baseline.py
   ```
3. **Download das Folhas Mensais do Pé-de-Meia (2024 — Portal da Transparência / CGU)**:
   ```powershell
   python src/collect/download_pe_de_meia_nacional.py
   ```
   > **Nota sobre o Exercício de 2024**: O exercício de **2024 está 100% completo em disco** (`202403` a `202412`, todas as 9 folhas publicadas pela CGU, incluindo a versão retificada de `202403_PeDeMeia.zip`). Dados parciais de 2025 foram excluídos do pipeline de agregação e da matriz mestre para manter a integridade anual do exercício fechado de 2024.

---

### Etapa 2 — Tratamento e Consolidação do Painel Nacional (`src/process/`)
4. **Agregação Físico-Financeira Nacional do Pé-de-Meia por UF**:
   ```powershell
   python src/process/process_pe_de_meia_nacional.py
   ```
   *Gera `dados_tratados/pe_de_meia_uf_nacional.csv` com os totais auditados e retificados do 1º bimestre (`202403`–`202404`) e o acumulado anual de 2024 (`202403`–`202412`) por UF.*

5. **Processamento Nacional do IDEB e Proficiência SAEB (2019–2025)**:
   ```powershell
   python src/process/process_ideb_nacional.py
   ```
   *Gera `dados_tratados/ideb_uf_brasil_ensino_medio.csv` para o período 2019–2025.*

6. **Processamento Nacional das Taxas de Rendimento Escolar (2022–2025)**:
   ```powershell
   python src/process/process_inep_rendimento.py
   ```
   *Gera `dados_tratados/inep_taxas_rendimento_uf_brasil.csv`.*

7. **Construção da Matriz Mestre do Painel Nacional (`matriz_mestre.csv`)**:
   ```powershell
   python src/process/build_master_matrix.py
   ```
   *Integra as bases tratadas em um painel balanceado de 324 observações e 39 colunas (27 UFs $\times$ 2 redes [`Estadual` e `Privada`] $\times$ 6 anos [`2019, 2021, 2022, 2023, 2024, 2025`]), documentado em `dicionario_de_dados.md`.*

---

### Etapa 3 — Modelagem Econométrica DiD e Visualizações (`src/process/`)
8. **Estimação dos Modelos de Diferenças em Diferenças (Efeito Fixo $\text{UF} \times \text{Rede}$ + Ano, Erros Agrupados por UF com Distribuição $t$)**:
   ```powershell
   python src/process/model_econometrics_did.py
   ```
   *Estima os modelos DiD (incluindo a decomposição do IDEB em $N$ e $P$) e os testes formais de tendências pré-período (`use_t=True`, 27 clusters de UF), cujos outputs brutos estão consolidados em `apendice_summaries_brutos_did.md`.*

9. **Geração dos Gráficos Nacionais**:
   ```powershell
   python src/process/generate_visualizations.py
   ```
   *Salva as figuras atualizadas em `dados_tratados/graficos/`.*

---

## 3. Scripts Auxiliares em `rascunho/`
Os scripts exploratórios de diagnóstico e inicialização foram organizados na pasta `rascunho/`:
- `rascunho/inspect_data.py`: Inspeção diagnóstica de cabeçalhos e abas dos arquivos ZIP/XLSX.
- `rascunho/test_sidra.py`: Teste exploratório de conectividade com a API SIDRA/IBGE.
- `rascunho/init_dirs.py`: Script auxiliar de criação inicial da árvore de diretórios.
