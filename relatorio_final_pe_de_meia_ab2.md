# Relatório Técnico — Avaliação Observacional em Escopo Nacional do Programa Pé-de-Meia (Painel das 27 Unidades da Federação, 2019–2025)

**Data de Atualização**: `2026-11-06`  
**Escopo Geográfico**: Brasil Nacional — Painel Balanceado das 27 Unidades da Federação (UFs), 5 Grandes Regiões e Agregado Nacional  
**Método Econométrico**: Diferenças em Diferenças em Painel (TWFE) com Efeito Fixo $\text{UF} \times \text{Rede}$ (`C(uf_rede)`), Efeito Fixo de Ano (`C(ano)`), Termo de Interação ($\text{Rede Pública Estadual} \times \text{Pós-Programa}$) e Erros-Padrão Robustos Agrupados por UF (27 Clusters) com Distribuição $t$ de Student (`use_t=True`, $gl = 26$). Ao todo, foram estimados **21 modelos de regressão** compreendendo **26 testes de hipóteses** sobre coeficientes de interação na especificação principal (**13 testes DiD pós-programa** — sendo 3 de fluxo anual, 5 no painel bienal 2019–2025 e 5 na janela imediata 2023 vs. 2025 — e **13 testes de pré-tendência**; **52 testes** ao incluir a comparação com os 26 coeficientes da especificação preliminar sem efeitos fixos).  
**Natureza da Inferência**: Associação observacional descritiva em dados agregados em painel ecológico (sem atribuição de efeito causal; a violação empírica da hipótese de tendências paralelas no período pré-programa e a realização de múltiplos testes de hipóteses limitam a interpretação em todas as janelas avaliadas).  
**Documentação Complementar**: Os outputs integrais (`summary()`) de todos os 21 modelos estimados encontram-se no documento separado [`apendice_summaries_brutos_did.md`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/apendice_summaries_brutos_did.md), e a especificação técnica das 39 variáveis do painel consta em [`dicionario_de_dados.md`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/dicionario_de_dados.md).

---

## 1. Auditoria da Base do Pé-de-Meia, Conferência com o Portal da Transparência e Totais Anuais por UF

### 1.1. Cabeçalho Bruto dos Zips de 2024, Desidentificação de Menores e Uso de Parcelas de Matrícula e Conclusão como Proxy
Todos os 9 pacotes mensais oficiais de 2024 da Controladoria-Geral da União (`202403_PeDeMeia.zip` a `202412_PeDeMeia.zip`) apresentam exatamente o mesmo cabeçalho bruto (18 colunas separadas por ponto e vírgula em codificação `latin-1`):

```text
"MÊS FOLHA";"MÊS REFERÊNCIA";"UF";"CÓDIGO MUNICÍPIO SIAFI";"NOME MUNICÍPIO";"NIS BENEFICIÁRIO";"CPF BENEFICIÁRIO";"NOME BENEFICIÁRIO";"NIS RESPONSÁVEL";"CPF RESPONSÁVEL";"NOME RESPONSÁVEL";"CÓDIGO TIPO INCENTIVO";"TIPO INCENTIVO";"PERÍODO INCENTIVO";"CÓDIGO ETAPA ENSINO";"ETAPA ENSINO";"DATA DO PAGAMENTO";"VALOR PARCELA"
```

A auditoria direta das colunas de identificação nominal e documental no pacote retificado `202403_PeDeMeia.zip` (`2.416.252` linhas) mostra que:
- **`NOME BENEFICIÁRIO`**: **0,00%** nulo (`2.416.252` preenchidos), mas **88,86%** dos registros (`2.147.193` linhas; ~90,2% nas amostras estaduais preliminares) trazem a string padronizada `*** BENEFICIÁRIO MENOR DE 18 ANOS ***`.
- **`CPF BENEFICIÁRIO`**: **88,86%** nulo (`2.147.193` `NaN`), estando preenchido de forma mascarada (`***.XXX.XXX-**`) apenas para os **11,14%** (`269.059` linhas) correspondentes a estudantes maiores de 18 anos.
- **`NIS BENEFICIÁRIO`**: **88,87%** nulo (`2.147.264` `NaN`) e **11,13%** preenchido (`268.988` linhas).
- **`CPF RESPONSÁVEL`**, **`NIS RESPONSÁVEL`** e **`NOME RESPONSÁVEL`**: apresentam **6,55%** (`158.192` `NaN`), **6,57%** (`158.758` `NaN`) e **0,63%** (`15.308` `NaN`) de valores ausentes, respectivamente, identificando o responsável familiar (que pode responder por mais de um estudante matriculado).

Formulamos como **hipótese de desidentificação de menores** que a omissão sistemática de `CPF BENEFICIÁRIO` e `NIS BENEFICIÁRIO` para estudantes com menos de 18 anos decorre do cumprimento das normas de proteção de dados pessoais de crianças e adolescentes previstas na Lei Geral de Proteção de Dados Pessoais (LGPD — Lei nº 13.709/2018, art. 14) e no Estatuto da Criança e do Adolescente (ECA — Lei nº 8.069/1990). Como consequência técnica direta dessa desidentificação de menores nos dados abertos, não há chave individual única confiável para rastrear um mesmo estudante através das folhas mensais; por isso, constantes fixadas em código e contagens diretas de CPFs/NIS únicos foram excluídas. Em seu lugar, como o `Incentivo-Matrícula` e o `Incentivo-Conclusão` correspondem a eventos de cota única anual por estudante elegível no ano letivo, utilizamos estritamente a contagem agregada de parcelas de **`Incentivo-Matrícula`** (`4.008.269` em 2024) e de **`Conclusão`** (`3.037.316` na folha `202502`) por UF como **estimativa (proxy) de estudantes beneficiários** e de **estudantes que receberam o depósito de conclusão até fev/2025**, rotulada explicitamente como **proxy** em todo o relatório e na matriz mestre.

### 1.2. Conferência do Total de Março–Abril/2024 contra o Publicado no Portal da Transparência (Sinal Padronizado)
A conferência cruzada entre o arquivo originalmente armazenado em disco para março/2024 (extraído em `2026-08-05`) e a versão oficial retificada publicada pela CGU no Portal da Transparência / repositório S3 (`Last-Modified: 2026-10-07`) identificou uma redução contábil exata decorrente do expurgo de linhas duplicadas na versão antiga de `202403_PeDeMeia.zip`.

> **Declaração sobre a Coluna "Versão Antiga em Disco"**: Os totais da versão antiga de `202403_PeDeMeia.zip` (`67.134.997 bytes`, contendo `4.205.138` parcelas e **R\$ 841.027.600,00**) foram medidos diretamente sobre o arquivo bruto original antes de sua substituição em disco. Como o pipeline (`process_pe_de_meia_nacional.py`) sobrescreveu `dados_brutos/pe_de_meia_transparencia/202403_PeDeMeia.zip` com o pacote oficial retificado pela CGU (`57.779.785 bytes`, `2.416.252` parcelas e **R\$ 483.250.400,00**), o arquivo antigo duplicado não faz mais parte do diretório `dados_brutos/`; assim, no estado atual do repositório, a coluna "Versão Antiga em Disco" constitui registro histórico/derivado da auditoria pré-substituição ($\text{Disco Antigo} = \text{Portal Retificado} + 1.788.886\text{ parcelas duplicadas expurgadas}$).

Na tabela abaixo, todas as colunas de diferença adotam de forma **estritamente padronizada** a convenção $\Delta = \text{Portal Retificado} - \text{Versão Antiga em Disco}$ (isto é, valores negativos indicam que o valor oficial retificado pela CGU é inferior ao que constava no arquivo antigo em disco):

| Competência / Escopo | Versão Antiga em Disco — Registro Pré-Substituição (Ago/2026) | Publicado no Portal da Transparência (Retificação Out/2026) | Diferença Absoluta ($\text{Portal} - \text{Disco Antigo}$) | Diferença Percentual sobre o Disco Antigo ($\frac{\text{Portal} - \text{Disco Antigo}}{\text{Disco Antigo}}$) | Diferença Percentual sobre o Portal ($\frac{\text{Portal} - \text{Disco Antigo}}{\text{Portal}}$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Folha `202403` (Março/2024) — Valor (R\$)** | R\$ 841.027.600,00 | **R\$ 483.250.400,00** | **-R\$ 357.777.200,00** | **-42,54%** | **-74,04%** |
| **Folha `202403` (Março/2024) — Parcelas** | 4.205.138 | **2.416.252** | **-1.788.886** | **-42,54%** | **-74,04%** |
| **Folha `202404` (Abril/2024) — Valor (R\$)** | R\$ 552.561.000,00 | **R\$ 552.561.000,00** | **R\$ 0,00** | **0,00%** | **0,00%** |
| **Folha `202404` (Abril/2024) — Parcelas** | 2.762.805 | **2.762.805** | **0** | **0,00%** | **0,00%** |
| **Bimestre Mar–Abr/2024 (`202403`+`202404`) — Valor (R\$)** | R\$ 1.393.588.600,00 | **R\$ 1.035.811.400,00** | **-R\$ 357.777.200,00** | **-25,67%** | **-34,54%** |
| **Bimestre Mar–Abr/2024 (`202403`+`202404`) — Parcelas** | 6.967.943 | **5.179.057** | **-1.788.886** | **-25,67%** | **-34,54%** |

- **Diagnóstico Técnico da Retificação**: O pacote `202403_PeDeMeia.zip` de agosto/2026 (`67.134.997 bytes`) continha `1.788.886` registros duplicados de pagamento de Incentivo-Matrícula (verificado empiricamente nos beneficiários maiores de 18 anos com `NIS BENEFICIÁRIO` preenchido, nos quais 68,55% dos NIS apresentavam duas linhas idênticas na mesma data de pagamento). Na versão retificada pela CGU em outubro/2026 (`57.779.785 bytes`), as duplicidades foram eliminadas, reduzindo o total de março/2024 em **-R\$ 357.777.200,00** (`-42,54%` sobre o arquivo antigo) e fixando o acumulado oficial do 1º bimestre (`202403`–`202404`) em **R\$ 1.035.811.400,00** (`5.179.057` parcelas, uma redução de `-25,67%` frente ao arquivo antigo).

### 1.3. Execução Mensal Nacional de 2024 (Exercício Completo) e Total Anual 2024 por UF
Foram processadas todas as **9 competências mensais de 2024** publicadas pela CGU (`202403` a `202412`; não existe folha `202407` devido ao recesso escolar de julho). Dados parciais de 2025 foram excluídos para preservar a consistência anual do exercício fechado de 2024:

| Ano | Mês Folha (`YYYYMM`) | Valor Total Transferido (R\$) | Total de Parcelas Pagas | Observação Operacional |
| :---: | :---: | :---: | :---: | :--- |
| 2024 | `202403` | 483.250.400,00 | 2.416.252 | 1º Lote Incentivo-Matrícula (versão retificada CGU) |
| 2024 | `202404` | 552.561.000,00 | 2.762.805 | 1ª Parcela Frequência + Matrícula complementar |
| 2024 | `202405` | 549.488.000,00 | 2.747.440 | 2ª Parcela Frequência + Matrícula complementar |
| 2024 | `202406` | 659.172.000,00 | 3.295.860 | 3ª Parcela Frequência + Matrícula complementar |
| 2024 | `202408` | 630.427.600,00 | 3.152.138 | Retomada pós-recesso + expansão CadÚnico |
| 2024 | `202409` | 656.487.400,00 | 3.282.437 | Parcela regular de Frequência/Matrícula |
| 2024 | `202410` | 686.305.175,00 | 3.418.224 | Parcela regular de Frequência/Matrícula |
| 2024 | `202411` | 683.902.550,00 | 3.404.749 | Parcela regular de Frequência/Matrícula |
| 2024 | `202412` | 685.846.100,00 | 3.412.623 | Última folha do exercício civil de 2024 |
| **2024** | **Total Anual 2024 (9 folhas)** | **5.587.440.225,00** | **27.892.528** | **Exercício 2024 completo (100% das folhas publicadas)** |

A tabela a seguir apresenta o **Total do 1º Bimestre Retificado (Mar–Abr/2024)** e o **Total Anual de 2024 (`202403`–`202412`) por UF** consolidados em [`pe_de_meia_uf_nacional.csv`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/dados_tratados/pe_de_meia_uf_nacional.csv) (Na [`matriz_mestre.csv`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/dados_tratados/matriz_mestre.csv), esses valores preenchem estritamente as **27 linhas** de `ano == 2024` e `rede == "Estadual"`, permanecendo as outras 297 linhas — **91,67%** do painel de 324 linhas, incluindo toda a rede `Privada` e os demais anos — como `NaN`):

| Código UF | UF | Unidade da Federação | Total Mar–Abr/2024 Retificado (R\$) | Parcelas Mar–Abr/2024 Retificado | Total Anual 2024 — 9 Folhas (R\$) | Total de Parcelas 2024 | Parcelas Matrícula (2024) | Parcelas Frequência (2024) |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| 35 | SP | São Paulo | 143.023.200,00 | 715.116 | 647.261.225,00 | 3.235.801 | 541.702 | 2.694.099 |
| 29 | BA | Bahia | 107.599.200,00 | 537.996 | 605.883.725,00 | 3.018.872 | 409.783 | 2.609.089 |
| 31 | MG | Minas Gerais | 87.662.200,00 | 438.311 | 463.432.775,00 | 2.315.818 | 351.959 | 1.963.859 |
| 15 | PA | Pará | 76.241.400,00 | 381.207 | 433.420.975,00 | 2.159.614 | 276.635 | 1.882.979 |
| 23 | CE | Ceará | 84.346.400,00 | 421.732 | 416.072.725,00 | 2.078.405 | 284.534 | 1.793.871 |
| 33 | RJ | Rio de Janeiro | 68.184.800,00 | 340.924 | 391.863.575,00 | 1.955.999 | 275.306 | 1.680.693 |
| 26 | PE | Pernambuco | 72.676.400,00 | 363.382 | 390.247.175,00 | 1.948.611 | 256.595 | 1.692.016 |
| 21 | MA | Maranhão | 59.669.000,00 | 298.345 | 364.782.025,00 | 1.821.065 | 234.410 | 1.586.655 |
| 41 | PR | Paraná | 29.707.000,00 | 148.535 | 177.223.725,00 | 885.675 | 137.217 | 748.458 |
| 25 | PB | Paraíba | 27.458.800,00 | 137.294 | 165.565.700,00 | 826.168 | 110.765 | 715.403 |
| 22 | PI | Piauí | 27.685.600,00 | 138.428 | 164.737.800,00 | 820.849 | 107.073 | 713.776 |
| 13 | AM | Amazonas | 34.517.200,00 | 172.586 | 155.529.925,00 | 776.280 | 137.162 | 639.118 |
| 43 | RS | Rio Grande do Sul | 27.323.000,00 | 136.615 | 148.066.700,00 | 739.900 | 118.249 | 621.651 |
| 27 | AL | Alagoas | 27.184.000,00 | 135.920 | 146.244.725,00 | 729.120 | 97.193 | 631.927 |
| 52 | GO | Goiás | 25.759.200,00 | 128.796 | 140.532.500,00 | 701.655 | 107.346 | 594.309 |
| 24 | RN | Rio Grande do Norte | 25.208.800,00 | 126.044 | 126.751.575,00 | 632.935 | 88.011 | 544.924 |
| 28 | SE | Sergipe | 17.046.000,00 | 85.230 | 93.416.475,00 | 466.481 | 62.268 | 404.213 |
| 42 | SC | Santa Catarina | 12.746.800,00 | 63.734 | 81.231.775,00 | 405.980 | 58.538 | 347.442 |
| 51 | MT | Mato Grosso | 15.571.600,00 | 77.858 | 78.986.600,00 | 394.673 | 64.830 | 329.843 |
| 32 | ES | Espírito Santo | 13.417.600,00 | 67.088 | 78.182.925,00 | 390.554 | 59.246 | 331.308 |
| 17 | TO | Tocantins | 8.729.200,00 | 43.646 | 62.008.900,00 | 309.525 | 43.979 | 265.546 |
| 50 | MS | Mato Grosso do Sul | 10.019.400,00 | 50.097 | 58.983.400,00 | 294.766 | 44.518 | 250.248 |
| 53 | DF | Distrito Federal | 11.336.600,00 | 56.683 | 54.566.925,00 | 272.775 | 41.014 | 231.761 |
| 11 | RO | Rondônia | 7.210.800,00 | 36.054 | 46.148.550,00 | 230.156 | 34.831 | 195.325 |
| 12 | AC | Acre | 6.258.000,00 | 31.290 | 38.448.025,00 | 191.904 | 26.027 | 165.877 |
| 16 | AP | Amapá | 6.456.800,00 | 32.284 | 36.293.675,00 | 181.301 | 24.198 | 157.103 |
| 14 | RR | Roraima | 2.772.400,00 | 13.862 | 21.556.125,00 | 107.646 | 14.880 | 92.766 |
| **—** | **BR** | **Total Nacional (27 UFs)** | **1.035.811.400,00** | **5.179.057** | **5.587.440.225,00** | **27.892.528** | **4.008.269** | **23.884.259** |

### 1.4. Pessoas e Famílias Cadastradas no CadÚnico (`esta_assistencia.csv`), Conferência das Folhas de 2025 (`202501`, `202502` e `202503`), Proxy de Estudantes e Comparações entre UFs

#### 1.4.1. Estrutura de `esta_assistencia.csv` e Rótulo "Cadastradas no CadÚnico"
O arquivo `esta_assistencia.csv` (baixado de `https://dados.al.gov.br/catalogo/dataset/50283830-5248-4eef-8f77-f2ac5dadcc51/resource/92df3981-afc4-43b0-8d82-07a6aa8aee46/download/esta_assistencia.csv`) possui `8.910` linhas e `7` colunas (`['co_uf', 'no_uf', 'ano', 'variavel', 'inf_categoria', 'inf_subcategoria', 'valor']`), cobrindo integralmente as **27 Unidades da Federação** (`co_uf` `11` a `53`) nos anos `2012` a `2026` (`2013` a `2024` completos nos 12 meses), com `variavel = "Cadastro Único"` e duas categorias em `inf_categoria`:
- `'Número total de famílias cadastradas no Cadastro Único'` (`4.455` linhas)
- `'Número total de pessoas cadastradas no Cadastro Único'` (`4.455` linhas)

Como o arquivo reporta o estoque total inscrito no Cadastro Único sem recorte por faixa de renda familiar ou individual, todas as colunas e rótulos da [`matriz_mestre.csv`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/dados_tratados/matriz_mestre.csv), do [`dicionario_de_dados.md`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/dicionario_de_dados.md) e deste relatório denominam essas variáveis estritamente como **famílias e pessoas cadastradas no CadÚnico** (`familias_cadastradas_cadunico`, `pessoas_cadastradas_cadunico` e `reais_por_pessoa_cadastrada_cadunico_2024`), adotando o estoque de **Dezembro de 2024** (`41.539.082` famílias e `95.324.907` pessoas no Brasil).

#### 1.4.2. Conferência de `202501`, `202502` e `202503` em Disco para `Conclusão` (`"Ano letivo 2024"`) e Piso do Custo do Ciclo 2024
Foram inspecionados todos os pacotes de 2025 existentes em disco (`202501_PeDeMeia.zip` e `202502_PeDeMeia.zip` completos em `dados_brutos/pe_de_meia_transparencia/`, além do download parcial `202503_PeDeMeia.zip` em `scratch/pm_dl/`) filtrando `PERÍODO INCENTIVO == "Ano letivo 2024"`:

| Folha Auditada em Disco | Status do Arquivo | `Conclusão` (`Ano letivo 2024`) — Parcelas / Valor (R\$) | `Enem` (`Ano letivo 2024`) — Parcelas / Valor (R\$) | `Frequência` (`Fev–Nov 2024`) — Parcelas / Valor (R\$) | `Matrícula` (`Ano letivo 2024`) — Parcelas / Valor (R\$) | Total da Folha Auditada — Parcelas / Valor (R\$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`202501_PeDeMeia.zip`** (`11.939.416 bytes`) | Completo (27 UFs) | **0** (`R\$ 0,00`) | **0** (`R\$ 0,00`) | 519.611 (`R\$ 106.959.575,00`) | 22.766 (`R\$ 4.553.200,00`) | 542.377 (`R\$ 111.512.775,00`) |
| **`202502_PeDeMeia.zip`** (`91.128.445 bytes`) | Completo (27 UFs) | **3.037.316** (`R\$ 3.037.316.000,00` — **96,16%**) | **450.679** (`R\$ 90.135.800,00` — **2,85%**) | 125.897 (`R\$ 25.958.450,00` — **0,82%**) | 26.183 (`R\$ 5.236.600,00` — **0,17%**) | 3.640.075 (`R\$ 3.158.646.850,00`) |
| **`202503_PeDeMeia.zip`** (`57.671.680 bytes`, parcial) | Parcial (16 UFs: `AC`–`PE`, `2.331.900` linhas) | **111.734** (`R\$ 111.734.000,00`) | **20.037** (`R\$ 4.007.400,00`) | 24.189 (`R\$ 5.019.950,00`) | 4.075 (`R\$ 815.000,00`) *(+ `2.171.865` do `Ano letivo 2025`)* | 2.331.900 (`R\$ 560.123.550,00` incl. 2025) |

- **Achados da Conferência das Folhas de 2025**:
  1. **`202501_PeDeMeia.zip`**: Não contém **nenhum pagamento** (`0` parcelas) de `Conclusão` nem de `Enem`; traz apenas parcelas remanescentes de `Frequência` (`519.611` parcelas referentes a fev–nov/2024) e `Matrícula` (`22.766` parcelas com `PERÍODO INCENTIVO == "Ano letivo 2024"`).
  2. **`202502_PeDeMeia.zip` e Piso do Ciclo 2024 (`R\$ 8,71 bi ou mais`; `R\$ 2.174 por estudante ou mais`)**: A folha de fevereiro/2025 contém **`3.037.316` parcelas (`R\$ 3.037.316.000,00`) de `Conclusão`** e **`450.679` parcelas (`R\$ 90.135.800,00`) de `Enem`**, ambas integralmente rotuladas como `PERÍODO INCENTIVO == "Ano letivo 2024"`, somando **R\$ 3.127.451.800,00** (`3.487.995` parcelas). Combinado ao **Exercício 2024** (`R\$ 5.587.440.225,00`), o custo do **Ciclo 2024 contabilizado até fev/2025 (`2024 + Conclusão/Enem de fev/2025`)** constitui um **piso** de **R\$ 8.714.892.025,00 ou mais** (**R\$ 8,71 bi ou mais**, com `31.380.523` parcelas ou mais; e **R\$ 2.174,23 por estudante [proxy] ou mais**, isto é, **R\$ 2.174 por estudante ou mais**), visto que folhas subsequentes continuaram pagando depósitos retroativos do `Ano letivo 2024`.
  3. **`202503_PeDeMeia.zip` (parcial em disco — `AC` a `PE`)**: A descompressão do stream bruto de `202503` comprova que a folha de março/2025 ainda pagou lotes retroativos do `Ano letivo 2024` (ao menos `111.734` parcelas / `R\$ 111,73 milhões` de `Conclusão` nas 16 primeiras UFs em ordem alfabética: `BA` [`27.406`], `PB` [`12.780`], `GO` [`12.549`], `PA` [`11.147`], `AP` [`10.797`], `MA` [`9.874`], `MT` [`5.932`], `MG` [`5.485`], `DF` [`5.102`], `CE` [`4.475`], `AC` [`3.270`], `PE` [`2.010`], `AL` [`663`], `ES` [`150`], `AM` [`51`] e `MS` [`43`]).
  4. **Comprovação Empírica para o Amapá (`AP`), Hipótese para Santa Catarina (`SC`) e Uso do Exercício 2024 nas Comparações entre UFs**: Na folha `202502`, a razão nacional `Conclusão (202502) / Pagamentos (2024)` é de **10,89%** (`3.037.316 / 27.892.528`). Enquanto na maioria das UFs essa razão situa-se entre `7,74%` e `14,50%`, duas UFs destacam-se por razões atipicamente baixas em `202502`:
     - **Amapá (`AP` — Comprovado em disco)**: Apresentou razão `Conclusão (202502) / Pagamentos (2024)` de apenas **`4,03%`** (`7.315` parcelas de `Conclusão` em `202502`), mas está **empiricamente comprovado** nos microdados de `202503` que o estado teve outras **`10.797` parcelas de `Conclusão` do `Ano letivo 2024` pagas na folha de março/2025** (mais do que o volume pago em fevereiro/2025).
     - **Santa Catarina (`SC` — Hipótese)**: Apresentou razão `Conclusão (202502) / Pagamentos (2024)` de apenas **`2,84%`** (`11.529` parcelas em `202502`). Como a fatia parcial de `202503_PeDeMeia.zip` disponível em disco encerra-se na letra `P` (`PE`) e não alcança `SC`, formulamos como **hipótese** que os depósitos de `Conclusão` do `Ano letivo 2024` de `SC` também tenham ocorrido majoritariamente em folhas posteriores a fevereiro de 2025 (`202503` ou seguintes).
     - Como os pagamentos de `Conclusão` em `202502` refletem apenas os lotes processados até fevereiro de 2025 (não devendo a relação entre parcelas de conclusão e de matrícula ser lida como taxa de aprovação escolar), **todas as comparações financeiras entre UFs (`R\$ por pessoa cadastrada no CadÚnico` e `Custo por estudante — proxy`) utilizam estritamente o Exercício 2024 fechado (`202403`–`202412`)**.

#### 1.4.3. Tabela Consolidada por UF (Exercício 2024): CadÚnico, Proxy de Estudantes Beneficiários e de Estudantes que Receberam o Depósito de Conclusão até Fev/2025, Razão Conclusão/Pagamentos e Custo por Estudante (Proxy)

| Código UF | UF | Unidade da Federação | Pessoas Cadastradas no CadÚnico (Dez/2024) | Famílias Cadastradas no CadÚnico (Dez/2024) | Exercício 2024 — 9 Folhas (R\$) | Total de Pagamentos (2024) | Estudantes Beneficiários — Proxy: Parcelas Matrícula (2024) | Estudantes que Receberam o Depósito de Conclusão até Fev/2025 — Proxy: Parcelas Conclusão (`202502`) | Razão Conclusão (`202502`) / Pagamentos (2024) | R\$ / Pessoa Cadastrada no CadÚnico (Exercício 2024) | Custo por Estudante — Proxy (Exercício 2024, R\$) |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 35 | SP | São Paulo | 14.061.964 | 6.096.305 | 647.261.225,00 | 3.235.801 | 541.702 | 442.349 | 13,67% | R\$ 46,03 | **R\$ 1.194,87** |
| 29 | BA | Bahia | 9.306.164 | 4.258.068 | 605.883.725,00 | 3.018.872 | 409.783 | 295.556 | 9,79% | R\$ 65,11 | **R\$ 1.478,55** |
| 31 | MG | Minas Gerais | 8.831.622 | 3.740.333 | 463.432.775,00 | 2.315.818 | 351.959 | 269.102 | 11,62% | R\$ 52,47 | **R\$ 1.316,72** |
| 15 | PA | Pará | 5.491.482 | 2.261.365 | 433.420.975,00 | 2.159.614 | 276.635 | 231.433 | 10,72% | R\$ 78,93 | **R\$ 1.566,76** |
| 23 | CE | Ceará | 5.728.811 | 2.463.847 | 416.072.725,00 | 2.078.405 | 284.534 | 256.708 | 12,35% | R\$ 72,63 | **R\$ 1.462,30** |
| 33 | RJ | Rio de Janeiro | 6.765.817 | 3.291.238 | 391.863.575,00 | 1.955.999 | 275.306 | 191.663 | 9,80% | R\$ 57,92 | **R\$ 1.423,37** |
| 26 | PE | Pernambuco | 5.733.337 | 2.673.885 | 390.247.175,00 | 1.948.611 | 256.595 | 221.305 | 11,36% | R\$ 68,07 | **R\$ 1.520,87** |
| 21 | MA | Maranhão | 4.586.053 | 1.876.434 | 364.782.025,00 | 1.821.065 | 234.410 | 181.359 | 9,96% | R\$ 79,54 | **R\$ 1.556,17** |
| 41 | PR | Paraná | 4.322.514 | 1.806.659 | 177.223.725,00 | 885.675 | 137.217 | 115.278 | 13,02% | R\$ 41,00 | **R\$ 1.291,56** |
| 25 | PB | Paraíba | 2.515.081 | 1.108.111 | 165.565.700,00 | 826.168 | 110.765 | 64.129 | 7,76% | R\$ 65,83 | **R\$ 1.494,75** |
| 22 | PI | Piauí | 2.196.379 | 949.892 | 164.737.800,00 | 820.849 | 107.073 | 63.536 | 7,74% | R\$ 75,00 | **R\$ 1.538,56** |
| 13 | AM | Amazonas | 2.640.329 | 1.045.026 | 155.529.925,00 | 776.280 | 137.162 | 112.544 | 14,50% | R\$ 58,91 | **R\$ 1.133,91** |
| 43 | RS | Rio Grande do Sul | 3.801.979 | 1.735.926 | 148.066.700,00 | 739.900 | 118.249 | 76.018 | 10,27% | R\$ 38,94 | **R\$ 1.252,16** |
| 27 | AL | Alagoas | 2.007.149 | 882.674 | 146.244.725,00 | 729.120 | 97.193 | 73.388 | 10,07% | R\$ 72,86 | **R\$ 1.504,68** |
| 52 | GO | Goiás | 3.158.023 | 1.359.906 | 140.532.500,00 | 701.655 | 107.346 | 78.039 | 11,12% | R\$ 44,50 | **R\$ 1.309,15** |
| 24 | RN | Rio Grande do Norte | 2.006.894 | 870.425 | 126.751.575,00 | 632.935 | 88.011 | 61.606 | 9,73% | R\$ 63,16 | **R\$ 1.440,18** |
| 28 | SE | Sergipe | 1.380.778 | 637.472 | 93.416.475,00 | 466.481 | 62.268 | 50.301 | 10,78% | R\$ 67,65 | **R\$ 1.500,23** |
| 42 | SC | Santa Catarina | 1.757.012 | 697.898 | 81.231.775,00 | 405.980 | 58.538 | 11.529 | 2,84% | R\$ 46,23 | **R\$ 1.387,68** |
| 51 | MT | Mato Grosso | 1.698.257 | 724.562 | 78.986.600,00 | 394.673 | 64.830 | 44.064 | 11,16% | R\$ 46,51 | **R\$ 1.218,36** |
| 32 | ES | Espírito Santo | 1.797.037 | 756.250 | 78.182.925,00 | 390.554 | 59.246 | 51.680 | 13,23% | R\$ 43,51 | **R\$ 1.319,63** |
| 17 | TO | Tocantins | 912.392 | 365.669 | 62.008.900,00 | 309.525 | 43.979 | 28.861 | 9,32% | R\$ 67,96 | **R\$ 1.409,97** |
| 50 | MS | Mato Grosso do Sul | 1.407.448 | 610.733 | 58.983.400,00 | 294.766 | 44.518 | 33.734 | 11,44% | R\$ 41,91 | **R\$ 1.324,93** |
| 53 | DF | Distrito Federal | 920.154 | 402.023 | 54.566.925,00 | 272.775 | 41.014 | 23.077 | 8,46% | R\$ 59,30 | **R\$ 1.330,45** |
| 11 | RO | Rondônia | 845.945 | 359.012 | 46.148.550,00 | 230.156 | 34.831 | 24.710 | 10,74% | R\$ 54,55 | **R\$ 1.324,93** |
| 12 | AC | Acre | 559.246 | 205.162 | 38.448.025,00 | 191.904 | 26.027 | 17.652 | 9,20% | R\$ 68,75 | **R\$ 1.477,24** |
| 16 | AP | Amapá | 507.107 | 213.198 | 36.293.675,00 | 181.301 | 24.198 | 7.315 | 4,03% | R\$ 71,57 | **R\$ 1.499,86** |
| 14 | RR | Roraima | 385.933 | 147.009 | 21.556.125,00 | 107.646 | 14.880 | 10.380 | 9,64% | R\$ 55,85 | **R\$ 1.448,66** |
| **—** | **BR** | **Total Nacional (27 UFs)** | **95.324.907** | **41.539.082** | **5.587.440.225,00** | **27.892.528** | **4.008.269** | **3.037.316** | **10,89%** | **R\$ 58,61** | **R\$ 1.393,98** |

- *(Nota sobre o Piso do Custo Nacional por Estudante — Proxy no Ciclo 2024: Considerando o **piso** do Ciclo 2024 no agregado nacional [**R\$ 8,71 bi ou mais** / `R\$ 8.714.892.025,00` ou mais], a razão sobre as `4.008.269` parcelas de `Incentivo-Matrícula` de 2024 corresponde a um piso de **R\$ 2.174,23 por estudante [proxy] ou mais** — isto é, **R\$ 2.174 por estudante ou mais**).*

### 1.5. Tabela Exploratória de Cenários de Custo por Ponto Percentual (Abandono $\times$ Ciclo 2024 — Piso)

> [!IMPORTANT]
> **Natureza Estritamente Exploratória da Simulação**: Como a hipótese de tendências paralelas no período pré-programa é rejeitada ($p = 0,0031$ para a taxa de abandono entre 2022 e 2023), a proporção da associação DiD pós-2024 ($|\hat{\beta}| = 2,07\text{ p.p.}$) efetivamente atribuível ao programa é desconhecida. A tabela abaixo tem caráter **estritamente exploratório**, cruzando a redução observada no **Abandono do Ensino Médio** com o **Piso do Custo do Ciclo 2024** (**R\$ 8,71 bi ou mais**; **R\$ 2.174 por estudante [proxy] ou mais**), onde o cenário de **100%** representa apenas um **teto teórico** de atribuição.

| Base de Custo Consolidada (Piso) | Desfecho Avaliado (Painel 2022–2025) | Cenário Exploratório de Atribuição sobre $|\hat{\beta}|$ | Variação de Abandono Atribuída ($\Delta\text{ p.p.}$) | Custo Nacional por Ponto Percentual — Piso ($\text{R\$ bilhões / p.p.}$) |
| :--- | :--- | :---: | :---: | :---: |
| **Ciclo 2024 — Piso (`R\$ 8,71 bi ou mais`; `R\$ 2.174 / estudante ou mais`)** | **Redução do Abandono EM** ($|\hat{\beta}| = 2,07\text{ p.p.}$) | **100% (Teto Teórico)** | `2,07 p.p.` | **R\$ 4,21 bilhões / p.p. ou mais** |
| **Ciclo 2024 — Piso (`R\$ 8,71 bi ou mais`; `R\$ 2.174 / estudante ou mais`)** | **Redução do Abandono EM** ($|\hat{\beta}| = 2,07\text{ p.p.}$) | **50%** | `1,03 p.p.` | **R\$ 8,43 bilhões / p.p. ou mais** |
| **Ciclo 2024 — Piso (`R\$ 8,71 bi ou mais`; `R\$ 2.174 / estudante ou mais`)** | **Redução do Abandono EM** ($|\hat{\beta}| = 2,07\text{ p.p.}$) | **25%** | `0,52 p.p.` | **R\$ 16,85 bilhões / p.p. ou mais** |
| **Ciclo 2024 — Piso (`R\$ 8,71 bi ou mais`; `R\$ 2.174 / estudante ou mais`)** | **Redução do Abandono EM** ($|\hat{\beta}| = 2,07\text{ p.p.}$) | **0%** | `0,00 p.p.` | **Indefinido / Não aplicável** (variação atribuída nula) |

---

## 2. Séries Históricas por Rede de Ensino e Decomposição do IDEB ($N \times P$)

Para sustentar empiricamente a análise das trajetórias da **Rede Pública Estadual** (`Estadual`) e da **Rede Privada** (`Privada`) nas 27 UFs, apresentamos a seguir as médias estaduais por ano e rede extraídas de [`matriz_mestre.csv`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/dados_tratados/matriz_mestre.csv).

### 2.1. Série Anual das Taxas de Rendimento Escolar por Rede (2022–2025, Média das 27 UFs)

| Ano | Aprovação Estadual (%) | Aprovação Privada (%) | Reprovação Estadual (%) | Reprovação Privada (%) | Abandono Estadual (%) | Abandono Privada (%) | Hiato de Abandono ($\text{Estadual} - \text{Privada}$, p.p.) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2022** | 84,12 | 96,62 | 8,79 | 2,50 | 7,09 | 0,88 | +6,21 |
| **2023** | 89,78 | 96,85 | 6,21 | 2,39 | 4,01 | 0,77 | +3,24 |
| **2024** | 90,07 | 97,26 | 6,20 | 2,19 | 3,73 | 0,55 | +3,18 |
| **2025** | 93,80 | 97,61 | 3,70 | 2,02 | 2,51 | 0,36 | +2,14 |
| **Variação Pré (2022 $\to$ 2023)** | **+5,66 p.p.** | **+0,23 p.p.** | **-2,58 p.p.** | **-0,12 p.p.** | **-3,08 p.p.** | **-0,11 p.p.** | **-2,97 p.p.** |
| **Variação Pós vs. Pré (Média 24–25 $-$ Média 22–23)** | **+4,99 p.p.** | **+0,70 p.p.** | **-2,55 p.p.** | **-0,34 p.p.** | **-2,43 p.p.** | **-0,37 p.p.** | **-2,07 p.p.** |

- **Hipótese de Compressão Assintótica (Efeito Teto/Piso na Rede Privada)**: Conforme documentado na Tabela 2.1, já no ano-base de 2022 a rede privada operava próxima dos limites extremos da escala percentual — com taxa média de aprovação de **96,62%** (próxima ao teto de $100\%$) e taxa média de abandono de **0,88%** (próxima ao piso de $0\%$), evoluindo gradualmente até **97,61%** de aprovação e **0,36%** de abandono em 2025. Formulamos a hipótese de que essa compressão assintótica na rede privada — combinada à forte recuperação pós-pandemia na rede pública estadual entre 2022 e 2023 (quando o abandono estadual caiu de **7,09%** para **4,01%**, ou `-3,08 p.p.`, contra `-0,11 p.p.` na rede privada) — explica mecanicamente a rejeição da hipótese de tendências paralelas no período pré-programa ($\hat{\beta}_{\text{pré } 2023} = -2,9704\text{ p.p.}$, $p = 0,0031$).

### 2.2. Série Bienal do SAEB e Decomposição Exata do IDEB ($\text{IDEB} = N \times P$, 2019–2025, Média das 27 UFs)
Pela definição metodológica do INEP, o Índice de Desenvolvimento da Educação Básica é o produto da **Nota Média Padronizada** ($N$, obtida pela padronização das proficiências do SAEB em Matemática e Língua Portuguesa na escala de 0 a 10) pelo **Indicador de Rendimento** ($P$, média harmônica das taxas de aprovação das séries da etapa na escala de 0 a 1):

$$\text{IDEB}_{u,r,t} = N_{u,r,t} \times P_{u,r,t}$$

A tabela abaixo apresenta a evolução bienal das notas brutas do SAEB, da Nota Padronizada ($N$), do Indicador de Rendimento ($P$) e do IDEB Observado por rede de ensino nas 27 UFs:

| Ano | SAEB Mat. Estadual | SAEB Mat. Privada | SAEB Port. Estadual | SAEB Port. Privada | Nota Padronizada ($N$) Estadual | Nota Padronizada ($N$) Privada | Indicador Rendimento ($P$) Estadual | Indicador Rendimento ($P$) Privada | IDEB ($N \times P$) Estadual | IDEB ($N \times P$) Privada |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2019** | 266,21 | 331,17 | 269,09 | 319,97 | 4,4567 | 6,1307 | 0,8503 | 0,9628 | 3,8037 | 5,9037 |
| **2021** | 261,11 | 316,58 | 267,53 | 310,75 | 4,3618 | 5,7879 | 0,8828 | 0,9721 | 3,8519 | 5,6296 |
| **2023** | 263,33 | 314,38 | 267,83 | 311,26 | 4,3974 | 5,7646 | 0,9037 | 0,9663 | 3,9778 | 5,5704 |
| **2025** | 266,63 | 315,61 | 270,71 | 310,68 | 4,4869 | 5,7731 | 0,9414 | 0,9778 | 4,2259 | 5,6370 |
| **$\Delta$ 2023 $\to$ 2025** | **+3,30** | **+1,23** | **+2,88** | **-0,58** | **+0,0895** | **+0,0085** | **+0,0377** | **+0,0116** | **+0,2481** | **+0,0667** |
| **DiD (2023 vs. 2025)** | \multicolumn{2}{c|}{**+2,0719 pts** ($p = 0,3814$)} | \multicolumn{2}{c|}{**+3,4641 pts** ($p = 0,0817$)} | \multicolumn{2}{c|}{**+0,0810 un.** ($p = 0,1830$)} | \multicolumn{2}{c|}{**+0,0261 un.** ($p = 0,0505$)} | \multicolumn{2}{c|}{**+0,1815 pts** ($p = 0,0115$)} |

- **Hipótese de Decomposição do IDEB (Evidência Sugestiva no IDEB [$p = 0,0115$] Junto aos Componentes $N$ [$p = 0,1830$] e $P$ [$p = 0,0505$] na Janela 2023 vs. 2025)**: Na transição imediata entre 2023 e 2025, o IDEB observado na rede pública estadual avançou `+0,2481` ponto contra `+0,0667` ponto na rede privada, gerando uma estimativa DiD de $\hat{\beta}_{\text{IDEB}} = +0,1815$ ($EP = 0,0668$, $t = 2,718$, **$p = 0,0115$**), a qual deve ser interpretada como **apenas sugestiva** quando avaliada em conjunto com seus dois componentes multiplicativos e com o número total de testes realizados (**26 testes** na especificação principal, sendo **13 testes DiD pós-programa** e **5 na janela imediata 2023 vs. 2025**):
  1. O componente cognitivo padronizado (**Nota Média Padronizada $N$**) apresenta estimativa DiD de **$\hat{\beta}_N = +0,0810$** ($EP = 0,0592$, $t = 1,368$, **$p = 0,1830$**), **não sendo estatisticamente significativo** (assim como suas notas brutas componentes em Matemática, $p = 0,3814$, e Língua Portuguesa, $p = 0,0817$).
  2. O componente de fluxo (**Indicador de Rendimento $P$**) avança de `0,9037` para `0,9414` na rede estadual (`+0,0377`) contra `0,9663` para `0,9778` na rede privada (`+0,0116`), gerando uma estimativa DiD de **$\hat{\beta}_P = +0,0261$** ($EP = 0,0127$, $t = 2,051$, **$p = 0,0505$**, limítrofe ao nível nominal de 5%).
  3. Pela aproximação de primeira ordem da variação do produto ($\Delta \text{IDEB} \approx \bar{P}\,\Delta N + \bar{N}\,\Delta P$), na rede estadual a expansão do fluxo escolar ($\bar{N}_{\text{Est}} \cdot \Delta P_{\text{Est}} \approx 4,44 \times 0,0377 = +0,167\text{ pt}$, ou **67,5%** do ganho bruto de `+0,2481` pt do IDEB estadual) responde por dois terços do crescimento do índice entre 2023 e 2025. Sustentamos, portanto, a hipótese respaldada pela Tabela 2.2 de que o resultado **sugestivo** do IDEB agregado na janela 2023 vs. 2025 ($p = 0,0115$) reflete primordialmente a variação no **fluxo de aprovação escolar ($P$, $p = 0,0505$)** combinada à interação multiplicativa $N \times P$, sem ganho estatisticamente significativo isolado na proficiência padronizada ($N$, $p = 0,1830$).

### 2.3. Comparação entre a Média Simples das 27 UFs (`nivel == "UF"`) e a Série Nacional Oficial do INEP (`nivel == "Brasil"`) e Gráficos Gerados
Como os modelos econométricos em painel UF $\times$ Rede atribuem peso igual a cada uma das 27 Unidades da Federação (**Média Simples das 27 UFs**, extraída de [`matriz_mestre.csv`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/dados_tratados/matriz_mestre.csv)), enquanto o agregado nacional publicado pelo INEP (**Série Nacional Oficial — `nivel == "Brasil"`**, extraída de [`inep_taxas_rendimento_uf_brasil.csv`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/dados_tratados/inep_taxas_rendimento_uf_brasil.csv) e [`ideb_uf_brasil_ensino_medio.csv`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/dados_tratados/ideb_uf_brasil_ensino_medio.csv)) pondera implicitamente pelo corpo discente de cada estado, apresentamos ambas lado a lado, rotuladas explicitamente:

| Ano | Rede | Abandono EM (%) — **Média Simples 27 UFs** | Abandono EM (%) — **Série Nacional (`Brasil`)** | Aprovação EM (%) — **Média Simples 27 UFs** | Aprovação EM (%) — **Série Nacional (`Brasil`)** | SAEB Mat. (pts) — **Média Simples 27 UFs** | SAEB Mat. (pts) — **Série Nacional (`Brasil`)** | SAEB Port. (pts) — **Média Simples 27 UFs** | SAEB Port. (pts) — **Série Nacional (`Brasil`)** | IDEB (0–10) — **Média Simples 27 UFs** | IDEB (0–10) — **Série Nacional (`Brasil`)** |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2019** | `Estadual` | — | — | — | — | 266,21 | 268,61 | 269,09 | 272,02 | 3,80 | 3,90 |
| **2019** | `Privada` | — | — | — | — | 331,17 | 334,72 | 319,97 | 322,11 | 5,90 | 6,00 |
| **2021** | `Estadual` | — | — | — | — | 261,11 | 262,37 | 267,53 | 269,54 | 3,85 | 3,90 |
| **2021** | `Privada` | — | — | — | — | 316,58 | 322,25 | 310,75 | 314,46 | 5,63 | 5,60 |
| **2022** | `Estadual` | 7,09 | 6,60 | 84,12 | 85,00 | — | — | — | — | — | — |
| **2022** | `Privada` | 0,88 | 0,70 | 96,62 | 96,90 | — | — | — | — | — | — |
| **2023** | `Estadual` | 4,01 | 3,80 | 89,78 | 90,50 | 263,33 | 264,31 | 267,83 | 269,93 | 3,98 | 4,10 |
| **2023** | `Privada` | 0,77 | 0,60 | 96,85 | 97,10 | 314,38 | 318,35 | 311,26 | 314,00 | 5,57 | 5,60 |
| **2024** | `Estadual` | 3,73 | 3,70 | 90,07 | 90,80 | — | — | — | — | — | — |
| **2024** | `Privada` | 0,55 | 0,50 | 97,26 | 97,40 | — | — | — | — | — | — |
| **2025** | `Estadual` | 2,51 | 2,60 | 93,80 | 94,40 | 266,63 | 268,52 | 270,71 | 273,32 | 4,23 | 4,30 |
| **2025** | `Privada` | 0,36 | 0,30 | 97,61 | 97,70 | 315,61 | 321,73 | 310,68 | 314,77 | 5,64 | 5,80 |

As visualizações correspondentes estão consolidadas em `dados_tratados/graficos/`:
- [`grafico_repasses_pedemeia_uf_nacional.png`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/dados_tratados/graficos/grafico_repasses_pedemeia_uf_nacional.png): Repasses do Pé-de-Meia em `R\$ por pessoa cadastrada no CadÚnico em 2024` por UF (`Exercício 2024`), ordenado de forma decrescente e colorido por Grande Região do IBGE.
- [`grafico_ideb_matematica_evolucao.png`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/dados_tratados/graficos/grafico_ideb_matematica_evolucao.png): Evolução da média simples das 27 UFs na nota SAEB Matemática e no IDEB Observado por rede (`2019–2025`), com rodapé `"média simples das 27 UFs; faixa = IC 95%"`.
- [`grafico_taxas_rendimento_2025.png`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/dados_tratados/graficos/grafico_taxas_rendimento_2025.png): Evolução da média simples das 27 UFs nas taxas de abandono e aprovação no Ensino Médio por rede (`2022–2025`), com rodapé `"média simples das 27 UFs; faixa = IC 95%"`.
- [`grafico_diferenca_estadual_privada.png`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/dados_tratados/graficos/grafico_diferenca_estadual_privada.png): Evolução anual da diferença $\text{Estadual} - \text{Privada}$ para a Taxa de Abandono EM (`2022–2025`) e para o SAEB Matemática (`2019–2025`), com rodapé `"média simples das 27 UFs; faixa = IC 95%"`.

---

## 3. Comparação Lado a Lado das Especificações DiD (Sem Efeitos Fixos vs. Efeito Fixo $\text{UF} \times \text{Rede}$ + Ano com Distribuição $t$)

A bateria econométrica compreende **8 desfechos** avaliados em **21 modelos de regressão** e **26 testes de hipóteses sobre coeficientes de interação** na especificação principal com **Efeito Fixo $\text{UF} \times \text{Rede}$ + Ano** (`C(uf_rede) + C(ano)`) e **erros-padrão agrupados por UF com distribuição $t$ de Student** (`use_t=True`, $gl = 26$): são **13 testes de associação DiD pós-programa** (3 nas taxas anuais de rendimento 2022–2025, 5 no painel bienal completo 2019–2025 e 5 na janela imediata 2023 vs. 2025) e **13 testes formais de pré-tendência** (3 para 2022 vs. 2023 e 10 para 2019 vs. 2021 e 2019 vs. 2023). Somados aos 26 testes correspondentes da especificação preliminar (sem efeitos fixos de unidade, com distribuição normal padrão $z$), a tabela abaixo reporta **52 testes** lado a lado, cujos outputs brutos integrais estão em [`apendice_summaries_brutos_did.md`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/apendice_summaries_brutos_did.md):

| Desfecho | Janela Analítica | $N$ | Coeficiente ($\hat{\beta}$) | EP Anterior (Sem FE, dist. $z$) | Valor-$p$ Anterior ($z$) | EP Atual (FE $\text{UF}\times\text{Rede}$ + Ano, dist. $t$) | Estatística $t$ ($gl=26$) | Valor-$p$ Atual ($t$) | Diagnóstico Inferencial |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Taxa de Abandono EM (p.p.) — DiD** | 2022–2025 | 216 | **-2,0685** | 0,3002 | $< 0,0001$ | **0,3477** | -5,949 | **$< 0,0001$** | Associação significativa ($p < 0,001$); pré-tendência violada |
| **Taxa de Abandono EM (p.p.) — Pré-Tendência** | 2022 vs 2023 | 108 | **-2,9704** | 0,6439 | $< 0,0001$ | **0,9106** | -3,262 | **0,0031** | **Tendência prévia não-paralela** ($p = 0,0031$) |
| **Taxa de Aprovação EM (p.p.) — DiD** | 2022–2025 | 216 | **+4,2833** | 0,6889 | $< 0,0001$ | **0,7980** | +5,368 | **$< 0,0001$** | Associação significativa ($p < 0,001$); pré-tendência violada |
| **Taxa de Aprovação EM (p.p.) — Pré-Tendência** | 2022 vs 2023 | 108 | **+5,4296** | 1,4634 | 0,0002 | **2,0696** | +2,623 | **0,0144** | **Tendência prévia não-paralela** ($p = 0,0144$) |
| **Taxa de Reprovação EM (p.p.) — DiD** | 2022–2025 | 216 | **-2,2148** | 0,5144 | $< 0,0001$ | **0,5958** | -3,718 | **0,0010** | Associação significativa ($p = 0,0010$); pré-tendência violada |
| **Taxa de Reprovação EM (p.p.) — Pré-Tendência** | 2022 vs 2023 | 108 | **-2,4593** | 0,8997 | 0,0063 | **1,2724** | -1,933 | **0,0642** | Pré-tendência marginalmente significativa a 10% ($p = 0,0642$) |
| **SAEB Matemática (pts) — DiD Painel Completo** | 2019–2025 | 216 | **+8,1802** | 1,7779 | $< 0,0001$ | **2,0593** | +3,972 | **0,0005** | Contaminado pela divergência pré-programa 2019–2023 |
| **SAEB Matemática (pts) — DiD Janela Imediata** | **2023 vs 2025** | 108 | **+2,0719** | 1,6454 | 0,2079 | **2,3270** | +0,890 | **0,3814** | **Não significativo** ($p = 0,3814$) |
| **SAEB Matemática (pts) — Pré-Tendência 2021** | 2019 vs 2021 | 162 | **+9,4881** | 1,6418 | $< 0,0001$ | **2,0109** | +4,718 | **0,0001** | **Tendência prévia não-paralela** ($p = 0,0001$) |
| **SAEB Matemática (pts) — Pré-Tendência 2023** | 2019 vs 2023 | 162 | **+13,9067** | 1,8514 | $< 0,0001$ | **2,2676** | +6,133 | **$< 0,0001$** | **Tendência prévia não-paralela** ($p < 0,0001$) |
| **SAEB Português (pts) — DiD Painel Completo** | 2019–2025 | 216 | **+5,8777** | 1,4883 | 0,0001 | **1,7242** | +3,409 | **0,0021** | Contaminado pela divergência pré-programa 2019–2023 |
| **SAEB Português (pts) — DiD Janela Imediata** | **2023 vs 2025** | 108 | **+3,4641** | 1,3524 | 0,0104 | **1,9126** | +1,811 | **0,0817** | **Perde significância a 5%** ($p = 0,0817$, marginal a 10%) |
| **SAEB Português (pts) — Pré-Tendência 2021** | 2019 vs 2021 | 162 | **+7,6607** | 1,3649 | $< 0,0001$ | **1,6716** | +4,583 | **0,0001** | **Tendência prévia não-paralela** ($p = 0,0001$) |
| **SAEB Português (pts) — Pré-Tendência 2023** | 2019 vs 2023 | 162 | **+7,4507** | 1,4963 | $< 0,0001$ | **1,8328** | +4,065 | **0,0004** | **Tendência prévia não-paralela** ($p = 0,0004$) |
| **Nota Padronizada SAEB ($N$) — DiD Painel Completo** | 2019–2025 | 216 | **+0,2029** | 0,0461 | $< 0,0001$ | **0,0530** | +3,825 | **0,0007** | Contaminado pela divergência pré-programa 2019–2023 |
| **Nota Padronizada SAEB ($N$) — DiD Janela Imediata** | **2023 vs 2025** | 108 | **+0,0810** | 0,0420 | 0,0542 | **0,0592** | +1,368 | **0,1830** | **Não significativo** ($p = 0,1830$) |
| **Nota Padronizada SAEB ($N$) — Pré-Tendência 2021** | 2019 vs 2021 | 162 | **+0,2479** | 0,0419 | $< 0,0001$ | **0,0513** | +4,833 | **0,0001** | **Tendência prévia não-paralela** ($p = 0,0001$) |
| **Nota Padronizada SAEB ($N$) — Pré-Tendência 2023** | 2019 vs 2023 | 162 | **+0,3069** | 0,0471 | $< 0,0001$ | **0,0577** | +5,322 | **$< 0,0001$** | **Tendência prévia não-paralela** ($p < 0,0001$) |
| **Indicador de Rendimento ($P$) — DiD Painel Completo** | 2019–2025 | 216 | **+0,0517** | 0,0097 | $< 0,0001$ | **0,0112** | +4,623 | **0,0001** | Associação positiva no fluxo escolar; pré-tendência violada |
| **Indicador de Rendimento ($P$) — DiD Janela Imediata** | **2023 vs 2025** | 108 | **+0,0261** | 0,0091 | 0,0039 | **0,0127** | +2,051 | **0,0505** | Significância limítrofe a 5% ($p = 0,0505$) |
| **Indicador de Rendimento ($P$) — Pré-Tendência 2021** | 2019 vs 2021 | 162 | **+0,0233** | 0,0154 | 0,1309 | **0,0189** | +1,233 | **0,2284** | Não significativo no biênio pandêmico 2019–2021 |
| **Indicador de Rendimento ($P$) — Pré-Tendência 2023** | 2019 vs 2023 | 162 | **+0,0500** | 0,0110 | $< 0,0001$ | **0,0134** | +3,719 | **0,0010** | **Tendência prévia não-paralela** ($p = 0,0010$) |
| **IDEB Observado ($N \times P$) — DiD Painel Completo** | 2019–2025 | 216 | **+0,4123** | 0,0631 | $< 0,0001$ | **0,0731** | +5,639 | **$< 0,0001$** | Impulsionado por $P$ e pela divergência pré-programa |
| **IDEB Observado ($N \times P$) — DiD Janela Imediata** | **2023 vs 2025** | 108 | **+0,1815** | 0,0472 | 0,0001 | **0,0668** | +2,718 | **0,0115** | **Sugestivo** ($p = 0,0115$, junto a $N$ [$p = 0,1830$] e $P$ [$p = 0,0505$]; pré-tendência violada) |
| **IDEB Observado ($N \times P$) — Pré-Tendência 2021** | 2019 vs 2021 | 162 | **+0,3222** | 0,0839 | 0,0001 | **0,1027** | +3,136 | **0,0042** | **Tendência prévia não-paralela** ($p = 0,0042$) |
| **IDEB Observado ($N \times P$) — Pré-Tendência 2023** | 2019 vs 2023 | 162 | **+0,5074** | 0,0735 | $< 0,0001$ | **0,0901** | +5,634 | **$< 0,0001$** | **Tendência prévia não-paralela** ($p < 0,0001$) |

---

## 4. Limitações Metodológicas e Escopo Estritamente Observacional das Estimativas

1. **Violação Empírica da Hipótese de Tendências Paralelas e Impossibilidade de Atribuição Causal em Todas as Janelas**:
   - O pressuposto de identificação do estimador de Diferenças em Diferenças exige que, na ausência da política pública, o diferencial entre a Rede Pública Estadual (`rede_publica = 1`) e a Rede Privada (`rede_publica = 0`) permanecesse estável ao longo do tempo.
   - Os testes formais de pré-tendência rejeitam a hipótese nula de paralelismo antes da vigência do Pé-de-Meia tanto nas taxas de rendimento entre 2022 e 2023 (`rede_publica:ano_2023 = -2,9704 p.p.`, $p = 0,0031$ no abandono; `+5,4296 p.p.`, $p = 0,0144$ na aprovação) quanto nas notas do SAEB e no IDEB entre 2019 e 2023 ($p \le 0,0010$).
   - Essa convergência pré-existente invalida a interpretação causal não apenas nas janelas longas (`2019–2025` e `2022–2025`), mas **também na janela imediata (`2023 vs. 2025`)**, pois não é possível separar empiricamente qual parcela da variação diferencial pós-2024 corresponde à continuidade inercial da convergência estrutural entre as redes e qual parcela estaria associada ao programa. Consequentemente, todos os resultados deste estudo devem ser lidos exclusivamente como **associações observacionais descritivas**.
2. **Multiplicidade de Testes de Hipóteses e Caráter Sugestivo do IDEB na Janela Imediata ($p = 0,0115$) Junto aos Componentes $N$ ($p = 0,1830$) e $P$ ($p = 0,0505$)**:
   - A análise principal realizou **26 testes de hipóteses** distribuídos em **21 modelos** (sendo **13 testes DiD pós-programa** — dos quais **5 na janela imediata 2023 vs. 2025** — e **13 testes de pré-tendência**, ou **52 testes** considerando a comparação com a especificação sem efeitos fixos).
   - Sob ajustes conservadores para múltiplos testes (como Bonferroni sobre os 13 testes DiD, $\alpha_{\text{Bonf}} = 0,05/13 \approx 0,0038$, ou sobre os 5 desfechos da janela imediata 2023 vs. 2025, $\alpha_{\text{Bonf}} = 0,05/5 = 0,0100$), o valor-$p$ não ajustado do **IDEB Observado na janela 2023 vs. 2025** ($\hat{\beta} = +0,1815$, **$p = 0,0115$**) situa-se acima do limiar corrigido. Além disso, a decomposição nos seus dois fatores multiplicativos mostra que a **Nota Média Padronizada ($N$)** não apresenta significância estatística ($\hat{\beta}_N = +0,0810$, **$p = 0,1830$**) e o **Indicador de Rendimento ($P$)** apresenta significância apenas limítrofe ($\hat{\beta}_P = +0,0261$, **$p = 0,0505$**), além da violação prévia das tendências paralelas ($p = 0,0042$ em 2021 e $p < 0,0001$ em 2023). Por essas razões, a estimativa do IDEB na janela imediata deve ser reportada apenas como **sugestiva**, e sempre acompanhada de $N$ e $P$.
3. **Agregação Ecológica por UF $\times$ Rede**:
   - Na rede pública estadual, nem todos os alunos matriculados pertencem a famílias inscritas no CadÚnico elegíveis ao Pé-de-Meia; portanto, as variações observadas nas médias estaduais refletem associações agregadas em nível de rede de ensino (*Intention-to-Treat* ecológico), sujeitas a políticas estaduais concomitantes de busca ativa e recuperação da aprendizagem.
