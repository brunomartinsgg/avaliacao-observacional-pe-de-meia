# Apêndice Técnico — Outputs Brutos Integrais (`summary()`) dos Modelos DiD com Efeito Fixo $\text{UF} \times \text{Rede}$ + Ano e Distribuição $t$

Este apêndice apresenta os `21` blocos de saída bruta (`model.summary()`) gerados pelo pacote `statsmodels` a partir do script [`src/process/model_econometrics_did.py`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/src/process/model_econometrics_did.py) sobre a matriz mestre nacional ([`dados_tratados/matriz_mestre.csv`](file:///c:/Users/Bruno/OneDrive/Documentos/UFAL/6º%20Período/Ciência%20de%20Dados/dados_tratados/matriz_mestre.csv)), incluindo:
- **6 modelos de Taxas de Rendimento do Ensino Médio (2022–2025 e Pré-Tendência 2022 vs. 2023)**: Abandono, Aprovação e Reprovação;
- **15 modelos de Proficiência SAEB e Decomposição do IDEB (Painel Completo 2019–2025, Janela Imediata 2023 vs. 2025 e Pré-Tendência 2019–2023)**: SAEB Matemática, SAEB Língua Portuguesa, Nota Média Padronizada SAEB ($N$), Indicador de Rendimento ($P$) e IDEB Observado ($N \times P$).

```text
====================================================================
DiD FE (UFxRede + Ano) — Taxa de Abandono EM (2022-2025, N=216)
====================================================================
                                OLS Regression Results                                
======================================================================================
Dep. Variable:     taxa_abandono_ensino_medio   R-squared:                       0.829
Model:                                    OLS   Adj. R-squared:                  0.768
Method:                         Least Squares   F-statistic:                     504.7
Date:                        Thu, 05 Nov 2026   Prob (F-statistic):           3.14e-24
Time:                                13:10:20   Log-Likelihood:                -341.03
No. Observations:                         216   AIC:                             798.1
Df Residuals:                             158   BIC:                             993.8
Df Model:                                  57                                         
Covariance Type:                      cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                     8.5157      0.294     28.984      0.000       7.912       9.120
C(uf_rede)[T.AC_Privada]                     -5.6843      0.174    -32.694      0.000      -6.042      -5.327
C(uf_rede)[T.AL_Estadual]                    -2.4500    1.6e-14  -1.54e+14      0.000      -2.450      -2.450
C(uf_rede)[T.AL_Privada]                     -7.1343      0.174    -41.034      0.000      -7.492      -6.777
C(uf_rede)[T.AM_Estadual]                    -1.1250   1.44e-14  -7.82e+13      0.000      -1.125      -1.125
C(uf_rede)[T.AM_Privada]                     -7.2093      0.174    -41.466      0.000      -7.567      -6.852
C(uf_rede)[T.AP_Estadual]                    -0.9750   1.44e-14  -6.77e+13      0.000      -0.975      -0.975
C(uf_rede)[T.AP_Privada]                     -6.7343      0.174    -38.734      0.000      -7.092      -6.377
C(uf_rede)[T.BA_Estadual]                     0.5250   1.49e-14   3.52e+13      0.000       0.525       0.525
C(uf_rede)[T.BA_Privada]                     -6.8593      0.174    -39.453      0.000      -7.217      -6.502
C(uf_rede)[T.CE_Estadual]                    -4.3250   1.62e-14  -2.67e+14      0.000      -4.325      -4.325
C(uf_rede)[T.CE_Privada]                     -6.6093      0.174    -38.015      0.000      -6.967      -6.252
C(uf_rede)[T.DF_Estadual]                    -2.4750    1.4e-14  -1.77e+14      0.000      -2.475      -2.475
C(uf_rede)[T.DF_Privada]                     -7.2343      0.174    -41.610      0.000      -7.592      -6.877
C(uf_rede)[T.ES_Estadual]                    -5.1250   1.48e-14  -3.47e+14      0.000      -5.125      -5.125
C(uf_rede)[T.ES_Privada]                     -7.2343      0.174    -41.610      0.000      -7.592      -6.877
C(uf_rede)[T.GO_Estadual]                    -5.3750   1.41e-14   -3.8e+14      0.000      -5.375      -5.375
C(uf_rede)[T.GO_Privada]                     -6.9343      0.174    -39.884      0.000      -7.292      -6.577
C(uf_rede)[T.MA_Estadual]                    -2.7250   1.64e-14  -1.66e+14      0.000      -2.725      -2.725
C(uf_rede)[T.MA_Privada]                     -5.9593      0.174    -34.276      0.000      -6.317      -5.602
C(uf_rede)[T.MG_Estadual]                    -0.9500   1.37e-14  -6.94e+13      0.000      -0.950      -0.950
C(uf_rede)[T.MG_Privada]                     -6.2593      0.174    -36.002      0.000      -6.617      -5.902
C(uf_rede)[T.MS_Estadual]                    -3.4750   1.49e-14  -2.34e+14      0.000      -3.475      -3.475
C(uf_rede)[T.MS_Privada]                     -7.2343      0.174    -41.610      0.000      -7.592      -6.877
C(uf_rede)[T.MT_Estadual]                    -2.3500   1.57e-14   -1.5e+14      0.000      -2.350      -2.350
C(uf_rede)[T.MT_Privada]                     -6.0093      0.174    -34.564      0.000      -6.367      -5.652
C(uf_rede)[T.PA_Estadual]                    -2.8000   1.56e-14  -1.79e+14      0.000      -2.800      -2.800
C(uf_rede)[T.PA_Privada]                     -6.9843      0.174    -40.172      0.000      -7.342      -6.627
C(uf_rede)[T.PB_Estadual]                     1.0500    1.5e-14      7e+13      0.000       1.050       1.050
C(uf_rede)[T.PB_Privada]                     -7.0843      0.174    -40.747      0.000      -7.442      -6.727
C(uf_rede)[T.PE_Estadual]                    -5.5750   1.41e-14  -3.95e+14      0.000      -5.575      -5.575
C(uf_rede)[T.PE_Privada]                     -7.1593      0.174    -41.178      0.000      -7.517      -6.802
C(uf_rede)[T.PI_Estadual]                    -2.9750    1.4e-14  -2.12e+14      0.000      -2.975      -2.975
C(uf_rede)[T.PI_Privada]                     -7.2343      0.174    -41.610      0.000      -7.592      -6.877
C(uf_rede)[T.PR_Estadual]                    -4.8250   1.46e-14  -3.31e+14      0.000      -4.825      -4.825
C(uf_rede)[T.PR_Privada]                     -7.4093      0.174    -42.616      0.000      -7.767      -7.052
C(uf_rede)[T.RJ_Estadual]                    -1.1250   1.39e-14  -8.09e+13      0.000      -1.125      -1.125
C(uf_rede)[T.RJ_Privada]                     -6.8593      0.174    -39.453      0.000      -7.217      -6.502
C(uf_rede)[T.RN_Estadual]                     2.2500   1.75e-14   1.29e+14      0.000       2.250       2.250
C(uf_rede)[T.RN_Privada]                     -6.3843      0.174    -36.721      0.000      -6.742      -6.027
C(uf_rede)[T.RO_Estadual]                    -1.1000   1.48e-14  -7.43e+13      0.000      -1.100      -1.100
C(uf_rede)[T.RO_Privada]                     -7.1343      0.174    -41.034      0.000      -7.492      -6.777
C(uf_rede)[T.RR_Estadual]                    -0.8750   1.56e-14   -5.6e+13      0.000      -0.875      -0.875
C(uf_rede)[T.RR_Privada]                     -7.2843      0.174    -41.897      0.000      -7.642      -6.927
C(uf_rede)[T.RS_Estadual]                     0.5000   1.63e-14   3.06e+13      0.000       0.500       0.500
C(uf_rede)[T.RS_Privada]                     -6.2093      0.174    -35.714      0.000      -6.567      -5.852
C(uf_rede)[T.SC_Estadual]                    -1.5000    1.6e-14   -9.4e+13      0.000      -1.500      -1.500
C(uf_rede)[T.SC_Privada]                     -7.2593      0.174    -41.753      0.000      -7.617      -6.902
C(uf_rede)[T.SE_Estadual]                    -3.4500    1.4e-14  -2.47e+14      0.000      -3.450      -3.450
C(uf_rede)[T.SE_Privada]                     -7.2343      0.174    -41.610      0.000      -7.592      -6.877
C(uf_rede)[T.SP_Estadual]                    -3.1250   1.38e-14  -2.27e+14      0.000      -3.125      -3.125
C(uf_rede)[T.SP_Privada]                     -7.4843      0.174    -43.048      0.000      -7.842      -7.127
C(uf_rede)[T.TO_Estadual]                    -4.1000   1.47e-14  -2.79e+14      0.000      -4.100      -4.100
C(uf_rede)[T.TO_Privada]                     -7.3593      0.174    -42.329      0.000      -7.717      -7.002
C(ano, Treatment(reference=2022))[T.2023]    -1.5963      0.291     -5.483      0.000      -2.195      -0.998
C(ano, Treatment(reference=2022))[T.2024]    -0.8139      0.213     -3.822      0.001      -1.252      -0.376
C(ano, Treatment(reference=2022))[T.2025]    -1.5157      0.289     -5.248      0.000      -2.109      -0.922
rede_publica:pos_pedemeia                    -2.0685      0.348     -5.949      0.000      -2.783      -1.354
==============================================================================
Omnibus:                       57.462   Durbin-Watson:                   2.033
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              274.622
Skew:                           0.930   Prob(JB):                     2.33e-60
Kurtosis:                       8.201   Cond. No.                         62.6
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
Pré-Tendência FE (UFxRede + Ano) — Taxa de Abandono EM (2022 vs 2023, N=108)
====================================================================
                                OLS Regression Results                                
======================================================================================
Dep. Variable:     taxa_abandono_ensino_medio   R-squared:                       0.908
Model:                                    OLS   Adj. R-squared:                  0.810
Method:                         Least Squares   F-statistic:                     240.3
Date:                        Thu, 05 Nov 2026   Prob (F-statistic):           1.72e-17
Time:                                13:10:21   Log-Likelihood:                -156.38
No. Observations:                         108   AIC:                             424.8
Df Residuals:                              52   BIC:                             575.0
Df Model:                                  55                                         
Covariance Type:                      cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                     9.5407      0.384     24.829      0.000       8.751      10.331
C(uf_rede)[T.AC_Privada]                     -6.4852      0.455    -14.244      0.000      -7.421      -5.549
C(uf_rede)[T.AL_Estadual]                    -2.7500   9.26e-14  -2.97e+13      0.000      -2.750      -2.750
C(uf_rede)[T.AL_Privada]                     -9.0352      0.455    -19.844      0.000      -9.971      -8.099
C(uf_rede)[T.AM_Estadual]                    -1.5500   1.01e-13  -1.54e+13      0.000      -1.550      -1.550
C(uf_rede)[T.AM_Privada]                     -9.1852      0.455    -20.174      0.000     -10.121      -8.249
C(uf_rede)[T.AP_Estadual]                    -1.4500   9.96e-14  -1.46e+13      0.000      -1.450      -1.450
C(uf_rede)[T.AP_Privada]                     -8.6852      0.455    -19.075      0.000      -9.621      -7.749
C(uf_rede)[T.BA_Estadual]                     1.2000   8.97e-14   1.34e+13      0.000       1.200       1.200
C(uf_rede)[T.BA_Privada]                     -8.5852      0.455    -18.856      0.000      -9.521      -7.649
C(uf_rede)[T.CE_Estadual]                    -5.4000    1.1e-13  -4.93e+13      0.000      -5.400      -5.400
C(uf_rede)[T.CE_Privada]                     -7.9352      0.455    -17.428      0.000      -8.871      -6.999
C(uf_rede)[T.DF_Estadual]                    -3.7000   1.05e-13  -3.53e+13      0.000      -3.700      -3.700
C(uf_rede)[T.DF_Privada]                     -8.9852      0.455    -19.734      0.000      -9.921      -8.049
C(uf_rede)[T.ES_Estadual]                    -6.1000   9.66e-14  -6.31e+13      0.000      -6.100      -6.100
C(uf_rede)[T.ES_Privada]                     -9.2352      0.455    -20.283      0.000     -10.171      -8.299
C(uf_rede)[T.GO_Estadual]                    -6.7500   9.31e-14  -7.25e+13      0.000      -6.750      -6.750
C(uf_rede)[T.GO_Privada]                     -9.1352      0.455    -20.064      0.000     -10.071      -8.199
C(uf_rede)[T.MA_Estadual]                    -3.7000   8.94e-14  -4.14e+13      0.000      -3.700      -3.700
C(uf_rede)[T.MA_Privada]                     -7.7352      0.455    -16.989      0.000      -8.671      -6.799
C(uf_rede)[T.MG_Estadual]                    -1.2000   1.01e-13  -1.19e+13      0.000      -1.200      -1.200
C(uf_rede)[T.MG_Privada]                     -8.1352      0.455    -17.867      0.000      -9.071      -7.199
C(uf_rede)[T.MS_Estadual]                    -3.5000      1e-13  -3.49e+13      0.000      -3.500      -3.500
C(uf_rede)[T.MS_Privada]                     -8.9352      0.455    -19.624      0.000      -9.871      -7.999
C(uf_rede)[T.MT_Estadual]                    -1.3500    5.1e-14  -2.65e+13      0.000      -1.350      -1.350
C(uf_rede)[T.MT_Privada]                     -6.7352      0.455    -14.793      0.000      -7.671      -5.799
C(uf_rede)[T.PA_Estadual]                    -1.9000   8.73e-14  -2.18e+13      0.000      -1.900      -1.900
C(uf_rede)[T.PA_Privada]                     -8.7852      0.455    -19.295      0.000      -9.721      -7.849
C(uf_rede)[T.PB_Estadual]                     1.5500   9.85e-14   1.57e+13      0.000       1.550       1.550
C(uf_rede)[T.PB_Privada]                     -8.9852      0.455    -19.734      0.000      -9.921      -8.049
C(uf_rede)[T.PE_Estadual]                    -6.8000   9.51e-14  -7.15e+13      0.000      -6.800      -6.800
C(uf_rede)[T.PE_Privada]                     -8.9852      0.455    -19.734      0.000      -9.921      -8.049
C(uf_rede)[T.PI_Estadual]                    -2.3000   8.59e-14  -2.68e+13      0.000      -2.300      -2.300
C(uf_rede)[T.PI_Privada]                     -9.1352      0.455    -20.064      0.000     -10.071      -8.199
C(uf_rede)[T.PR_Estadual]                    -5.5500   9.49e-14  -5.85e+13      0.000      -5.550      -5.550
C(uf_rede)[T.PR_Privada]                     -9.3852      0.455    -20.613      0.000     -10.321      -8.449
C(uf_rede)[T.RJ_Estadual]                    -2.1000   9.56e-14   -2.2e+13      0.000      -2.100      -2.100
C(uf_rede)[T.RJ_Privada]                     -8.5852      0.455    -18.856      0.000      -9.521      -7.649
C(uf_rede)[T.RN_Estadual]                     3.4000   9.27e-14   3.67e+13      0.000       3.400       3.400
C(uf_rede)[T.RN_Privada]                     -7.7852      0.455    -17.099      0.000      -8.721      -6.849
C(uf_rede)[T.RO_Estadual]                    -1.8000    8.8e-14  -2.05e+13      0.000      -1.800      -1.800
C(uf_rede)[T.RO_Privada]                     -9.0852      0.455    -19.954      0.000     -10.021      -8.149
C(uf_rede)[T.RR_Estadual]                    -0.8500   8.54e-14  -9.96e+12      0.000      -0.850      -0.850
C(uf_rede)[T.RR_Privada]                     -9.2852      0.455    -20.393      0.000     -10.221      -8.349
C(uf_rede)[T.RS_Estadual]                     1.9500   8.01e-14   2.44e+13      0.000       1.950       1.950
C(uf_rede)[T.RS_Privada]                     -8.0352      0.455    -17.648      0.000      -8.971      -7.099
C(uf_rede)[T.SC_Estadual]                    -2.4500   9.28e-14  -2.64e+13      0.000      -2.450      -2.450
C(uf_rede)[T.SC_Privada]                     -9.2352      0.455    -20.283      0.000     -10.171      -8.299
C(uf_rede)[T.SE_Estadual]                    -3.7000   9.59e-14  -3.86e+13      0.000      -3.700      -3.700
C(uf_rede)[T.SE_Privada]                     -9.1352      0.455    -20.064      0.000     -10.071      -8.199
C(uf_rede)[T.SP_Estadual]                    -4.3500   9.74e-14  -4.46e+13      0.000      -4.350      -4.350
C(uf_rede)[T.SP_Privada]                     -9.4352      0.455    -20.723      0.000     -10.371      -8.499
C(uf_rede)[T.TO_Estadual]                    -4.9500   9.67e-14  -5.12e+13      0.000      -4.950      -4.950
C(uf_rede)[T.TO_Privada]                     -9.2352      0.455    -20.283      0.000     -10.171      -8.299
C(ano, Treatment(reference=2022))[T.2023]    -0.1111      0.283     -0.392      0.698      -0.694       0.471
rede_publica:ano_2023                        -2.9704      0.911     -3.262      0.003      -4.842      -1.099
==============================================================================
Omnibus:                       18.561   Durbin-Watson:                   2.165
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               97.243
Skew:                          -0.000   Prob(JB):                     7.66e-22
Kurtosis:                       7.649   Cond. No.                         65.7
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
DiD FE (UFxRede + Ano) — Taxa de Aprovação EM (2022-2025, N=216)
====================================================================
                                 OLS Regression Results                                
=======================================================================================
Dep. Variable:     taxa_aprovacao_ensino_medio   R-squared:                       0.817
Model:                                     OLS   Adj. R-squared:                  0.750
Method:                          Least Squares   F-statistic:                     518.9
Date:                         Thu, 05 Nov 2026   Prob (F-statistic):           2.20e-24
Time:                                 13:10:21   Log-Likelihood:                -516.31
No. Observations:                          216   AIC:                             1149.
Df Residuals:                              158   BIC:                             1344.
Df Model:                                   57                                         
Covariance Type:                       cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                    82.2343      0.687    119.713      0.000      80.822      83.646
C(uf_rede)[T.AC_Privada]                     11.3667      0.399     28.490      0.000      10.547      12.187
C(uf_rede)[T.AL_Estadual]                     5.1750   3.56e-13   1.45e+13      0.000       5.175       5.175
C(uf_rede)[T.AL_Privada]                     13.0917      0.399     32.813      0.000      12.272      13.912
C(uf_rede)[T.AM_Estadual]                     1.7750   3.59e-13   4.94e+12      0.000       1.775       1.775
C(uf_rede)[T.AM_Privada]                     13.3417      0.399     33.440      0.000      12.522      14.162
C(uf_rede)[T.AP_Estadual]                    -0.7500   3.36e-13  -2.23e+12      0.000      -0.750      -0.750
C(uf_rede)[T.AP_Privada]                     14.4917      0.399     36.322      0.000      13.672      15.312
C(uf_rede)[T.BA_Estadual]                    -0.5750   4.23e-13  -1.36e+12      0.000      -0.575      -0.575
C(uf_rede)[T.BA_Privada]                     12.7417      0.399     31.936      0.000      11.922      13.562
C(uf_rede)[T.CE_Estadual]                    10.9250   4.63e-13   2.36e+13      0.000      10.925      10.925
C(uf_rede)[T.CE_Privada]                     13.4917      0.399     33.816      0.000      12.672      14.312
C(uf_rede)[T.DF_Estadual]                    -1.6750   4.14e-13  -4.04e+12      0.000      -1.675      -1.675
C(uf_rede)[T.DF_Privada]                     13.0417      0.399     32.688      0.000      12.222      13.862
C(uf_rede)[T.ES_Estadual]                     9.4500    3.5e-13    2.7e+13      0.000       9.450       9.450
C(uf_rede)[T.ES_Privada]                     13.4917      0.399     33.816      0.000      12.672      14.312
C(uf_rede)[T.GO_Estadual]                    11.0750   3.62e-13   3.06e+13      0.000      11.075      11.075
C(uf_rede)[T.GO_Privada]                     13.5417      0.399     33.941      0.000      12.722      14.362
C(uf_rede)[T.MA_Estadual]                     5.8250   3.84e-13   1.52e+13      0.000       5.825       5.825
C(uf_rede)[T.MA_Privada]                     12.3917      0.399     31.059      0.000      11.572      13.212
C(uf_rede)[T.MG_Estadual]                     2.0500   3.68e-13   5.56e+12      0.000       2.050       2.050
C(uf_rede)[T.MG_Privada]                     11.8417      0.399     29.680      0.000      11.022      12.662
C(uf_rede)[T.MS_Estadual]                     2.5750   3.62e-13   7.11e+12      0.000       2.575       2.575
C(uf_rede)[T.MS_Privada]                     13.3917      0.399     33.565      0.000      12.572      14.212
C(uf_rede)[T.MT_Estadual]                     3.5000   3.95e-13   8.86e+12      0.000       3.500       3.500
C(uf_rede)[T.MT_Privada]                     12.8667      0.399     32.249      0.000      12.047      13.687
C(uf_rede)[T.PA_Estadual]                     6.7250   4.14e-13   1.63e+13      0.000       6.725       6.725
C(uf_rede)[T.PA_Privada]                     13.9667      0.399     35.006      0.000      13.147      14.787
C(uf_rede)[T.PB_Estadual]                    -0.7000   3.38e-13  -2.07e+12      0.000      -0.700      -0.700
C(uf_rede)[T.PB_Privada]                     13.6417      0.399     34.192      0.000      12.822      14.462
C(uf_rede)[T.PE_Estadual]                     9.4500   3.77e-13   2.51e+13      0.000       9.450       9.450
C(uf_rede)[T.PE_Privada]                     13.4917      0.399     33.816      0.000      12.672      14.312
C(uf_rede)[T.PI_Estadual]                     9.4000   4.04e-13   2.33e+13      0.000       9.400       9.400
C(uf_rede)[T.PI_Privada]                     12.9417      0.399     32.437      0.000      12.122      13.762
C(uf_rede)[T.PR_Estadual]                     7.8000   3.63e-13   2.15e+13      0.000       7.800       7.800
C(uf_rede)[T.PR_Privada]                     13.9167      0.399     34.881      0.000      13.097      14.737
C(uf_rede)[T.RJ_Estadual]                    -2.9500   3.46e-13  -8.52e+12      0.000      -2.950      -2.950
C(uf_rede)[T.RJ_Privada]                     11.6667      0.399     29.242      0.000      10.847      12.487
C(uf_rede)[T.RN_Estadual]                    -6.7750   4.16e-13  -1.63e+13      0.000      -6.775      -6.775
C(uf_rede)[T.RN_Privada]                     12.1917      0.399     30.557      0.000      11.372      13.012
C(uf_rede)[T.RO_Estadual]                     3.1000   3.64e-13   8.52e+12      0.000       3.100       3.100
C(uf_rede)[T.RO_Privada]                     11.9167      0.399     29.868      0.000      11.097      12.737
C(uf_rede)[T.RR_Estadual]                    -0.0250   3.53e-13  -7.07e+10      0.000      -0.025      -0.025
C(uf_rede)[T.RR_Privada]                     12.1917      0.399     30.557      0.000      11.372      13.012
C(uf_rede)[T.RS_Estadual]                    -2.3000   3.46e-13  -6.66e+12      0.000      -2.300      -2.300
C(uf_rede)[T.RS_Privada]                     11.6417      0.399     29.179      0.000      10.822      12.462
C(uf_rede)[T.SC_Estadual]                    -2.9000    3.7e-13  -7.84e+12      0.000      -2.900      -2.900
C(uf_rede)[T.SC_Privada]                     13.3667      0.399     33.502      0.000      12.547      14.187
C(uf_rede)[T.SE_Estadual]                     3.1750   3.54e-13   8.98e+12      0.000       3.175       3.175
C(uf_rede)[T.SE_Privada]                     13.5917      0.399     34.066      0.000      12.772      14.412
C(uf_rede)[T.SP_Estadual]                     6.3250   3.68e-13   1.72e+13      0.000       6.325       6.325
C(uf_rede)[T.SP_Privada]                     14.3917      0.399     36.072      0.000      13.572      15.212
C(uf_rede)[T.TO_Estadual]                     7.8500   3.48e-13   2.25e+13      0.000       7.850       7.850
C(uf_rede)[T.TO_Privada]                     13.7167      0.399     34.380      0.000      12.897      14.537
C(ano, Treatment(reference=2022))[T.2023]     2.9444      0.737      3.995      0.000       1.429       4.460
C(ano, Treatment(reference=2022))[T.2024]     1.1565      0.507      2.281      0.031       0.114       2.199
C(ano, Treatment(reference=2022))[T.2025]     3.1954      0.566      5.649      0.000       2.033       4.358
rede_publica:pos_pedemeia                     4.2833      0.798      5.368      0.000       2.643       5.924
==============================================================================
Omnibus:                       85.688   Durbin-Watson:                   2.017
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              846.691
Skew:                          -1.218   Prob(JB):                    1.39e-184
Kurtosis:                      12.389   Cond. No.                         62.6
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
Pré-Tendência FE (UFxRede + Ano) — Taxa de Aprovação EM (2022 vs 2023, N=108)
====================================================================
                                 OLS Regression Results                                
=======================================================================================
Dep. Variable:     taxa_aprovacao_ensino_medio   R-squared:                       0.883
Model:                                     OLS   Adj. R-squared:                  0.758
Method:                          Least Squares   F-statistic:                     109.1
Date:                         Thu, 05 Nov 2026   Prob (F-statistic):           2.25e-13
Time:                                 13:10:21   Log-Likelihood:                -249.80
No. Observations:                          108   AIC:                             611.6
Df Residuals:                               52   BIC:                             761.8
Df Model:                                   55                                         
Covariance Type:                       cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                    81.9704      0.946     86.638      0.000      80.026      83.915
C(uf_rede)[T.AC_Privada]                     11.3648      1.035     10.982      0.000       9.238      13.492
C(uf_rede)[T.AL_Estadual]                     4.6500    2.4e-13   1.94e+13      0.000       4.650       4.650
C(uf_rede)[T.AL_Privada]                     14.7648      1.035     14.268      0.000      12.638      16.892
C(uf_rede)[T.AM_Estadual]                     1.9500    2.1e-13   9.28e+12      0.000       1.950       1.950
C(uf_rede)[T.AM_Privada]                     14.8648      1.035     14.365      0.000      12.738      16.992
C(uf_rede)[T.AP_Estadual]                    -2.6500   2.09e-13  -1.27e+13      0.000      -2.650      -2.650
C(uf_rede)[T.AP_Privada]                     16.4648      1.035     15.911      0.000      14.338      18.592
C(uf_rede)[T.BA_Estadual]                    -4.0000   2.65e-13  -1.51e+13      0.000      -4.000      -4.000
C(uf_rede)[T.BA_Privada]                     14.3148      1.035     13.833      0.000      12.188      16.442
C(uf_rede)[T.CE_Estadual]                    12.1000   2.39e-13   5.06e+13      0.000      12.100      12.100
C(uf_rede)[T.CE_Privada]                     14.6648      1.035     14.171      0.000      12.538      16.792
C(uf_rede)[T.DF_Estadual]                     0.0500   2.12e-13   2.36e+11      0.000       0.050       0.050
C(uf_rede)[T.DF_Privada]                     14.5648      1.035     14.075      0.000      12.438      16.692
C(uf_rede)[T.ES_Estadual]                     8.6500   2.25e-13   3.84e+13      0.000       8.650       8.650
C(uf_rede)[T.ES_Privada]                     15.5148      1.035     14.993      0.000      13.388      17.642
C(uf_rede)[T.GO_Estadual]                    12.1000   2.29e-13   5.28e+13      0.000      12.100      12.100
C(uf_rede)[T.GO_Privada]                     15.5648      1.035     15.041      0.000      13.438      17.692
C(uf_rede)[T.MA_Estadual]                     6.6000   2.18e-13   3.03e+13      0.000       6.600       6.600
C(uf_rede)[T.MA_Privada]                     14.1148      1.035     13.640      0.000      11.988      16.242
C(uf_rede)[T.MG_Estadual]                     0.5500   2.23e-13   2.47e+12      0.000       0.550       0.550
C(uf_rede)[T.MG_Privada]                     13.5648      1.035     13.108      0.000      11.438      15.692
C(uf_rede)[T.MS_Estadual]                    -0.5000    2.3e-13  -2.17e+12      0.000      -0.500      -0.500
C(uf_rede)[T.MS_Privada]                     14.9148      1.035     14.413      0.000      12.788      17.042
C(uf_rede)[T.MT_Estadual]                    -1.6000   2.05e-13  -7.79e+12      0.000      -1.600      -1.600
C(uf_rede)[T.MT_Privada]                     13.5148      1.035     13.060      0.000      11.388      15.642
C(uf_rede)[T.PA_Estadual]                     2.9000   2.17e-13   1.34e+13      0.000       2.900       2.900
C(uf_rede)[T.PA_Privada]                     15.8148      1.035     15.283      0.000      13.688      17.942
C(uf_rede)[T.PB_Estadual]                    -1.9500   2.35e-13   -8.3e+12      0.000      -1.950      -1.950
C(uf_rede)[T.PB_Privada]                     15.5648      1.035     15.041      0.000      13.438      17.692
C(uf_rede)[T.PE_Estadual]                     9.6500   2.14e-13    4.5e+13      0.000       9.650       9.650
C(uf_rede)[T.PE_Privada]                     15.2648      1.035     14.751      0.000      13.138      17.392
C(uf_rede)[T.PI_Estadual]                     8.3500   2.34e-13   3.57e+13      0.000       8.350       8.350
C(uf_rede)[T.PI_Privada]                     14.6148      1.035     14.123      0.000      12.488      16.742
C(uf_rede)[T.PR_Estadual]                     7.5500    2.2e-13   3.43e+13      0.000       7.550       7.550
C(uf_rede)[T.PR_Privada]                     15.8148      1.035     15.283      0.000      13.688      17.942
C(uf_rede)[T.RJ_Estadual]                    -4.6000   2.51e-13  -1.83e+13      0.000      -4.600      -4.600
C(uf_rede)[T.RJ_Privada]                     13.0648      1.035     12.625      0.000      10.938      15.192
C(uf_rede)[T.RN_Estadual]                   -11.4500   2.14e-13  -5.34e+13      0.000     -11.450     -11.450
C(uf_rede)[T.RN_Privada]                     13.4648      1.035     13.012      0.000      11.338      15.592
C(uf_rede)[T.RO_Estadual]                     3.1500   2.09e-13   1.51e+13      0.000       3.150       3.150
C(uf_rede)[T.RO_Privada]                     13.6148      1.035     13.157      0.000      11.488      15.742
C(uf_rede)[T.RR_Estadual]                    -0.5500   2.27e-13  -2.42e+12      0.000      -0.550      -0.550
C(uf_rede)[T.RR_Privada]                     14.5648      1.035     14.075      0.000      12.438      16.692
C(uf_rede)[T.RS_Estadual]                    -4.5000    2.2e-13  -2.05e+13      0.000      -4.500      -4.500
C(uf_rede)[T.RS_Privada]                     13.3648      1.035     12.915      0.000      11.238      15.492
C(uf_rede)[T.SC_Estadual]                    -4.0500   2.23e-13  -1.82e+13      0.000      -4.050      -4.050
C(uf_rede)[T.SC_Privada]                     15.2648      1.035     14.751      0.000      13.138      17.392
C(uf_rede)[T.SE_Estadual]                     0.7500   2.18e-13   3.44e+12      0.000       0.750       0.750
C(uf_rede)[T.SE_Privada]                     15.5148      1.035     14.993      0.000      13.388      17.642
C(uf_rede)[T.SP_Estadual]                     6.4000    2.5e-13   2.56e+13      0.000       6.400       6.400
C(uf_rede)[T.SP_Privada]                     16.2648      1.035     15.717      0.000      14.138      18.392
C(uf_rede)[T.TO_Estadual]                     8.4500   2.67e-13   3.16e+13      0.000       8.450       8.450
C(uf_rede)[T.TO_Privada]                     15.1148      1.035     14.606      0.000      12.988      17.242
C(ano, Treatment(reference=2022))[T.2023]     0.2296      0.452      0.508      0.616      -0.699       1.159
rede_publica:ano_2023                         5.4296      2.070      2.623      0.014       1.175       9.684
==============================================================================
Omnibus:                       26.597   Durbin-Watson:                   2.053
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              262.454
Skew:                           0.000   Prob(JB):                     1.02e-57
Kurtosis:                      10.637   Cond. No.                         65.7
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
DiD FE (UFxRede + Ano) — Taxa de Reprovação EM (2022-2025, N=216)
====================================================================
                                 OLS Regression Results                                 
========================================================================================
Dep. Variable:     taxa_reprovacao_ensino_medio   R-squared:                       0.777
Model:                                      OLS   Adj. R-squared:                  0.696
Method:                           Least Squares   F-statistic:                     289.5
Date:                          Thu, 05 Nov 2026   Prob (F-statistic):           3.78e-21
Time:                                  13:10:21   Log-Likelihood:                -425.66
No. Observations:                           216   AIC:                             967.3
Df Residuals:                               158   BIC:                             1163.
Df Model:                                    57                                         
Covariance Type:                        cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                     9.2500      0.489     18.904      0.000       8.244      10.256
C(uf_rede)[T.AC_Privada]                     -5.6824      0.298    -19.076      0.000      -6.295      -5.070
C(uf_rede)[T.AL_Estadual]                    -2.7250   1.97e-14  -1.38e+14      0.000      -2.725      -2.725
C(uf_rede)[T.AL_Privada]                     -5.9574      0.298    -19.999      0.000      -6.570      -5.345
C(uf_rede)[T.AM_Estadual]                    -0.6500   1.93e-14  -3.37e+13      0.000      -0.650      -0.650
C(uf_rede)[T.AM_Privada]                     -6.1324      0.298    -20.586      0.000      -6.745      -5.520
C(uf_rede)[T.AP_Estadual]                     1.7250      2e-14   8.65e+13      0.000       1.725       1.725
C(uf_rede)[T.AP_Privada]                     -7.7574      0.298    -26.041      0.000      -8.370      -7.145
C(uf_rede)[T.BA_Estadual]                     0.0500   2.09e-14   2.39e+12      0.000       0.050       0.050
C(uf_rede)[T.BA_Privada]                     -5.8824      0.298    -19.747      0.000      -6.495      -5.270
C(uf_rede)[T.CE_Estadual]                    -6.6000      2e-14   -3.3e+14      0.000      -6.600      -6.600
C(uf_rede)[T.CE_Privada]                     -6.8824      0.298    -23.104      0.000      -7.495      -6.270
C(uf_rede)[T.DF_Estadual]                     4.1500   1.87e-14   2.22e+14      0.000       4.150       4.150
C(uf_rede)[T.DF_Privada]                     -5.8074      0.298    -19.495      0.000      -6.420      -5.195
C(uf_rede)[T.ES_Estadual]                    -4.3250   1.93e-14  -2.24e+14      0.000      -4.325      -4.325
C(uf_rede)[T.ES_Privada]                     -6.2574      0.298    -21.006      0.000      -6.870      -5.645
C(uf_rede)[T.GO_Estadual]                    -5.7000   1.94e-14  -2.95e+14      0.000      -5.700      -5.700
C(uf_rede)[T.GO_Privada]                     -6.6074      0.298    -22.181      0.000      -7.220      -5.995
C(uf_rede)[T.MA_Estadual]                    -3.1000   2.29e-14  -1.35e+14      0.000      -3.100      -3.100
C(uf_rede)[T.MA_Privada]                     -6.4324      0.298    -21.593      0.000      -7.045      -5.820
C(uf_rede)[T.MG_Estadual]                    -1.1000      2e-14   -5.5e+13      0.000      -1.100      -1.100
C(uf_rede)[T.MG_Privada]                     -5.5824      0.298    -18.740      0.000      -6.195      -4.970
C(uf_rede)[T.MS_Estadual]                     0.9000   1.94e-14   4.64e+13      0.000       0.900       0.900
C(uf_rede)[T.MS_Privada]                     -6.1574      0.298    -20.670      0.000      -6.770      -5.545
C(uf_rede)[T.MT_Estadual]                    -1.1500    2.2e-14  -5.22e+13      0.000      -1.150      -1.150
C(uf_rede)[T.MT_Privada]                     -6.8574      0.298    -23.020      0.000      -7.470      -6.245
C(uf_rede)[T.PA_Estadual]                    -3.9250   2.12e-14  -1.85e+14      0.000      -3.925      -3.925
C(uf_rede)[T.PA_Privada]                     -6.9824      0.298    -23.440      0.000      -7.595      -6.370
C(uf_rede)[T.PB_Estadual]                    -0.3500   1.84e-14   -1.9e+13      0.000      -0.350      -0.350
C(uf_rede)[T.PB_Privada]                     -6.5574      0.298    -22.013      0.000      -7.170      -5.945
C(uf_rede)[T.PE_Estadual]                    -3.8750   2.01e-14  -1.93e+14      0.000      -3.875      -3.875
C(uf_rede)[T.PE_Privada]                     -6.3324      0.298    -21.258      0.000      -6.945      -5.720
C(uf_rede)[T.PI_Estadual]                    -6.4250   1.88e-14  -3.42e+14      0.000      -6.425      -6.425
C(uf_rede)[T.PI_Privada]                     -5.7074      0.298    -19.160      0.000      -6.320      -5.095
C(uf_rede)[T.PR_Estadual]                    -2.9750   1.99e-14   -1.5e+14      0.000      -2.975      -2.975
C(uf_rede)[T.PR_Privada]                     -6.5074      0.298    -21.845      0.000      -7.120      -5.895
C(uf_rede)[T.RJ_Estadual]                     4.0750   2.22e-14   1.83e+14      0.000       4.075       4.075
C(uf_rede)[T.RJ_Privada]                     -4.8074      0.298    -16.138      0.000      -5.420      -4.195
C(uf_rede)[T.RN_Estadual]                     4.5250   2.77e-14   1.63e+14      0.000       4.525       4.525
C(uf_rede)[T.RN_Privada]                     -5.8074      0.298    -19.495      0.000      -6.420      -5.195
C(uf_rede)[T.RO_Estadual]                    -2.0000   2.43e-14  -8.22e+13      0.000      -2.000      -2.000
C(uf_rede)[T.RO_Privada]                     -4.7824      0.298    -16.054      0.000      -5.395      -4.170
C(uf_rede)[T.RR_Estadual]                     0.9000   1.91e-14   4.72e+13      0.000       0.900       0.900
C(uf_rede)[T.RR_Privada]                     -4.9074      0.298    -16.474      0.000      -5.520      -4.295
C(uf_rede)[T.RS_Estadual]                     1.8000    2.3e-14   7.84e+13      0.000       1.800       1.800
C(uf_rede)[T.RS_Privada]                     -5.4324      0.298    -18.236      0.000      -6.045      -4.820
C(uf_rede)[T.SC_Estadual]                     4.4000    1.9e-14   2.32e+14      0.000       4.400       4.400
C(uf_rede)[T.SC_Privada]                     -6.1074      0.298    -20.502      0.000      -6.720      -5.495
C(uf_rede)[T.SE_Estadual]                     0.2750   1.91e-14   1.44e+13      0.000       0.275       0.275
C(uf_rede)[T.SE_Privada]                     -6.3574      0.298    -21.342      0.000      -6.970      -5.745
C(uf_rede)[T.SP_Estadual]                    -3.2000   1.85e-14  -1.73e+14      0.000      -3.200      -3.200
C(uf_rede)[T.SP_Privada]                     -6.9074      0.298    -23.188      0.000      -7.520      -6.295
C(uf_rede)[T.TO_Estadual]                    -3.7500   1.95e-14  -1.93e+14      0.000      -3.750      -3.750
C(uf_rede)[T.TO_Privada]                     -6.3574      0.298    -21.342      0.000      -6.970      -5.745
C(ano, Treatment(reference=2022))[T.2023]    -1.3481      0.526     -2.563      0.017      -2.429      -0.267
C(ano, Treatment(reference=2022))[T.2024]    -0.3426      0.338     -1.013      0.321      -1.038       0.353
C(ano, Treatment(reference=2022))[T.2025]    -1.6796      0.322     -5.220      0.000      -2.341      -1.018
rede_publica:pos_pedemeia                    -2.2148      0.596     -3.718      0.001      -3.439      -0.990
==============================================================================
Omnibus:                       81.173   Durbin-Watson:                   1.993
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              870.511
Skew:                           1.100   Prob(JB):                    9.35e-190
Kurtosis:                      12.586   Cond. No.                         62.6
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
Pré-Tendência FE (UFxRede + Ano) — Taxa de Reprovação EM (2022 vs 2023, N=108)
====================================================================
                                 OLS Regression Results                                 
========================================================================================
Dep. Variable:     taxa_reprovacao_ensino_medio   R-squared:                       0.850
Model:                                      OLS   Adj. R-squared:                  0.691
Method:                           Least Squares   F-statistic:                     37.20
Date:                          Thu, 05 Nov 2026   Prob (F-statistic):           2.36e-08
Time:                                  13:10:21   Log-Likelihood:                -204.84
No. Observations:                           108   AIC:                             521.7
Df Residuals:                                52   BIC:                             671.9
Df Model:                                    55                                         
Covariance Type:                        cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                     8.4889      0.630     13.481      0.000       7.195       9.783
C(uf_rede)[T.AC_Privada]                     -4.8796      0.636     -7.670      0.000      -6.187      -3.572
C(uf_rede)[T.AL_Estadual]                    -1.9000   4.61e-14  -4.12e+13      0.000      -1.900      -1.900
C(uf_rede)[T.AL_Privada]                     -5.7296      0.636     -9.006      0.000      -7.037      -4.422
C(uf_rede)[T.AM_Estadual]                    -0.4000   6.03e-14  -6.63e+12      0.000      -0.400      -0.400
C(uf_rede)[T.AM_Privada]                     -5.6796      0.636     -8.928      0.000      -6.987      -4.372
C(uf_rede)[T.AP_Estadual]                     4.1000   5.48e-14   7.49e+13      0.000       4.100       4.100
C(uf_rede)[T.AP_Privada]                     -7.7796      0.636    -12.228      0.000      -9.087      -6.472
C(uf_rede)[T.BA_Estadual]                     2.8000   4.16e-14   6.73e+13      0.000       2.800       2.800
C(uf_rede)[T.BA_Privada]                     -5.7296      0.636     -9.006      0.000      -7.037      -4.422
C(uf_rede)[T.CE_Estadual]                    -6.7000   5.38e-14  -1.25e+14      0.000      -6.700      -6.700
C(uf_rede)[T.CE_Privada]                     -6.7296      0.636    -10.578      0.000      -8.037      -5.422
C(uf_rede)[T.DF_Estadual]                     3.6500   5.81e-14   6.28e+13      0.000       3.650       3.650
C(uf_rede)[T.DF_Privada]                     -5.5796      0.636     -8.770      0.000      -6.887      -4.272
C(uf_rede)[T.ES_Estadual]                    -2.5500   5.72e-14  -4.46e+13      0.000      -2.550      -2.550
C(uf_rede)[T.ES_Privada]                     -6.2796      0.636     -9.871      0.000      -7.587      -4.972
C(uf_rede)[T.GO_Estadual]                    -5.3500   5.01e-14  -1.07e+14      0.000      -5.350      -5.350
C(uf_rede)[T.GO_Privada]                     -6.4296      0.636    -10.106      0.000      -7.737      -5.122
C(uf_rede)[T.MA_Estadual]                    -2.9000   4.81e-14  -6.03e+13      0.000      -2.900      -2.900
C(uf_rede)[T.MA_Privada]                     -6.3796      0.636    -10.028      0.000      -7.687      -5.072
C(uf_rede)[T.MG_Estadual]                     0.6500   5.29e-14   1.23e+13      0.000       0.650       0.650
C(uf_rede)[T.MG_Privada]                     -5.4296      0.636     -8.535      0.000      -6.737      -4.122
C(uf_rede)[T.MS_Estadual]                     4.0000   5.25e-14   7.62e+13      0.000       4.000       4.000
C(uf_rede)[T.MS_Privada]                     -5.9796      0.636     -9.399      0.000      -7.287      -4.672
C(uf_rede)[T.MT_Estadual]                     2.9500    4.1e-14    7.2e+13      0.000       2.950       2.950
C(uf_rede)[T.MT_Privada]                     -6.7796      0.636    -10.657      0.000      -8.087      -5.472
C(uf_rede)[T.PA_Estadual]                    -1.0000   5.27e-14   -1.9e+13      0.000      -1.000      -1.000
C(uf_rede)[T.PA_Privada]                     -7.0296      0.636    -11.050      0.000      -8.337      -5.722
C(uf_rede)[T.PB_Estadual]                     0.4000   5.65e-14   7.08e+12      0.000       0.400       0.400
C(uf_rede)[T.PB_Privada]                     -6.5796      0.636    -10.342      0.000      -7.887      -5.272
C(uf_rede)[T.PE_Estadual]                    -2.8500   5.32e-14  -5.36e+13      0.000      -2.850      -2.850
C(uf_rede)[T.PE_Privada]                     -6.2796      0.636     -9.871      0.000      -7.587      -4.972
C(uf_rede)[T.PI_Estadual]                    -6.0500   5.37e-14  -1.13e+14      0.000      -6.050      -6.050
C(uf_rede)[T.PI_Privada]                     -5.4796      0.636     -8.613      0.000      -6.787      -4.172
C(uf_rede)[T.PR_Estadual]                    -2.0000   5.72e-14   -3.5e+13      0.000      -2.000      -2.000
C(uf_rede)[T.PR_Privada]                     -6.4296      0.636    -10.106      0.000      -7.737      -5.122
C(uf_rede)[T.RJ_Estadual]                     6.7000   5.31e-14   1.26e+14      0.000       6.700       6.700
C(uf_rede)[T.RJ_Privada]                     -4.4796      0.636     -7.041      0.000      -5.787      -3.172
C(uf_rede)[T.RN_Estadual]                     8.0500   5.35e-14   1.51e+14      0.000       8.050       8.050
C(uf_rede)[T.RN_Privada]                     -5.6796      0.636     -8.928      0.000      -6.987      -4.372
C(uf_rede)[T.RO_Estadual]                    -1.3500   3.64e-14  -3.71e+13      0.000      -1.350      -1.350
C(uf_rede)[T.RO_Privada]                     -4.5296      0.636     -7.120      0.000      -5.837      -3.222
C(uf_rede)[T.RR_Estadual]                     1.4000   3.77e-14   3.71e+13      0.000       1.400       1.400
C(uf_rede)[T.RR_Privada]                     -5.2796      0.636     -8.299      0.000      -6.587      -3.972
C(uf_rede)[T.RS_Estadual]                     2.5500   5.57e-14   4.58e+13      0.000       2.550       2.550
C(uf_rede)[T.RS_Privada]                     -5.3296      0.636     -8.377      0.000      -6.637      -4.022
C(uf_rede)[T.SC_Estadual]                     6.5000   5.77e-14   1.13e+14      0.000       6.500       6.500
C(uf_rede)[T.SC_Privada]                     -6.0296      0.636     -9.478      0.000      -7.337      -4.722
C(uf_rede)[T.SE_Estadual]                     2.9500   5.87e-14   5.03e+13      0.000       2.950       2.950
C(uf_rede)[T.SE_Privada]                     -6.3796      0.636    -10.028      0.000      -7.687      -5.072
C(uf_rede)[T.SP_Estadual]                    -2.0500   5.23e-14  -3.92e+13      0.000      -2.050      -2.050
C(uf_rede)[T.SP_Privada]                     -6.8296      0.636    -10.735      0.000      -8.137      -5.522
C(uf_rede)[T.TO_Estadual]                    -3.5000   5.64e-14   -6.2e+13      0.000      -3.500      -3.500
C(uf_rede)[T.TO_Privada]                     -5.8796      0.636     -9.242      0.000      -7.187      -4.572
C(ano, Treatment(reference=2022))[T.2023]    -0.1185      0.245     -0.483      0.633      -0.622       0.385
rede_publica:ano_2023                        -2.4593      1.272     -1.933      0.064      -5.075       0.156
==============================================================================
Omnibus:                       30.077   Durbin-Watson:                   1.956
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              388.949
Skew:                          -0.000   Prob(JB):                     3.47e-85
Kurtosis:                      12.297   Cond. No.                         65.7
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
DiD FE (UFxRede + Ano) Painel Completo — SAEB Matemática (2019-2025, N=216)
====================================================================
                             OLS Regression Results                             
================================================================================
Dep. Variable:     ideb_nota_matematica   R-squared:                       0.972
Model:                              OLS   Adj. R-squared:                  0.962
Method:                   Least Squares   F-statistic:                     2811.
Date:                  Thu, 05 Nov 2026   Prob (F-statistic):           7.33e-34
Time:                          13:10:21   Log-Likelihood:                -657.37
No. Observations:                   216   AIC:                             1431.
Df Residuals:                       158   BIC:                             1627.
Df Model:                            57                                         
Covariance Type:                cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                   271.0552      0.901    300.853      0.000     269.203     272.907
C(uf_rede)[T.AC_Privada]                     56.8101      0.515    110.349      0.000      55.752      57.868
C(uf_rede)[T.AL_Estadual]                    -8.2775   3.67e-13  -2.25e+13      0.000      -8.278      -8.277
C(uf_rede)[T.AL_Privada]                     29.7626      0.515     57.811      0.000      28.704      30.821
C(uf_rede)[T.AM_Estadual]                   -13.9875   1.14e-12  -1.23e+13      0.000     -13.988     -13.987
C(uf_rede)[T.AM_Privada]                     37.5601      0.515     72.957      0.000      36.502      38.618
C(uf_rede)[T.AP_Estadual]                   -13.1550   6.66e-13  -1.98e+13      0.000     -13.155     -13.155
C(uf_rede)[T.AP_Privada]                     37.6526      0.515     73.137      0.000      36.594      38.711
C(uf_rede)[T.BA_Estadual]                   -14.5200   3.64e-13  -3.99e+13      0.000     -14.520     -14.520
C(uf_rede)[T.BA_Privada]                     54.0151      0.515    104.920      0.000      52.957      55.073
C(uf_rede)[T.CE_Estadual]                     0.7600   3.59e-13   2.12e+12      0.000       0.760       0.760
C(uf_rede)[T.CE_Privada]                     54.5826      0.515    106.022      0.000      53.524      55.641
C(uf_rede)[T.DF_Estadual]                     2.5400   5.28e-13   4.81e+12      0.000       2.540       2.540
C(uf_rede)[T.DF_Privada]                     68.9851      0.515    133.998      0.000      67.927      70.043
C(uf_rede)[T.ES_Estadual]                    17.4275   5.13e-13    3.4e+13      0.000      17.427      17.428
C(uf_rede)[T.ES_Privada]                     68.6026      0.515    133.255      0.000      67.544      69.661
C(uf_rede)[T.GO_Estadual]                    15.0900   3.78e-13   3.99e+13      0.000      15.090      15.090
C(uf_rede)[T.GO_Privada]                     57.0001      0.515    110.718      0.000      55.942      58.058
C(uf_rede)[T.MA_Estadual]                   -16.0475    3.6e-13  -4.46e+13      0.000     -16.048     -16.047
C(uf_rede)[T.MA_Privada]                     44.2426      0.515     85.938      0.000      43.184      45.301
C(uf_rede)[T.MG_Estadual]                     7.4000   4.15e-13   1.78e+13      0.000       7.400       7.400
C(uf_rede)[T.MG_Privada]                     82.3076      0.515    159.876      0.000      81.249      83.366
C(uf_rede)[T.MS_Estadual]                     3.6925   5.75e-13   6.42e+12      0.000       3.692       3.693
C(uf_rede)[T.MS_Privada]                     66.3351      0.515    128.851      0.000      65.277      67.393
C(uf_rede)[T.MT_Estadual]                    -4.0050   3.71e-13  -1.08e+13      0.000      -4.005      -4.005
C(uf_rede)[T.MT_Privada]                     56.5426      0.515    109.830      0.000      55.484      57.601
C(uf_rede)[T.PA_Estadual]                   -11.1325   3.72e-13  -2.99e+13      0.000     -11.133     -11.132
C(uf_rede)[T.PA_Privada]                     45.0801      0.515     87.565      0.000      44.022      46.138
C(uf_rede)[T.PB_Estadual]                    -6.5525   5.92e-13  -1.11e+13      0.000      -6.553      -6.552
C(uf_rede)[T.PB_Privada]                     50.3826      0.515     97.864      0.000      49.324      51.441
C(uf_rede)[T.PE_Estadual]                     8.8050   5.13e-13   1.72e+13      0.000       8.805       8.805
C(uf_rede)[T.PE_Privada]                     55.4051      0.515    107.620      0.000      54.347      56.463
C(uf_rede)[T.PI_Estadual]                     2.2700   3.97e-13   5.71e+12      0.000       2.270       2.270
C(uf_rede)[T.PI_Privada]                     69.0426      0.515    134.110      0.000      67.984      70.101
C(uf_rede)[T.PR_Estadual]                    15.8625   3.91e-13   4.06e+13      0.000      15.862      15.863
C(uf_rede)[T.PR_Privada]                     69.2326      0.515    134.479      0.000      68.174      70.291
C(uf_rede)[T.RJ_Estadual]                    -9.2875   4.54e-13  -2.04e+13      0.000      -9.288      -9.287
C(uf_rede)[T.RJ_Privada]                     48.4101      0.515     94.033      0.000      47.352      49.468
C(uf_rede)[T.RN_Estadual]                   -12.7275   3.52e-13  -3.61e+13      0.000     -12.728     -12.727
C(uf_rede)[T.RN_Privada]                     49.0801      0.515     95.334      0.000      48.022      50.138
C(uf_rede)[T.RO_Estadual]                     2.1300   4.32e-13   4.93e+12      0.000       2.130       2.130
C(uf_rede)[T.RO_Privada]                     51.3626      0.515     99.768      0.000      50.304      52.421
C(uf_rede)[T.RR_Estadual]                    -7.4400   4.81e-13  -1.55e+13      0.000      -7.440      -7.440
C(uf_rede)[T.RR_Privada]                     48.5876      0.515     94.378      0.000      47.529      49.646
C(uf_rede)[T.RS_Estadual]                    12.7250   4.18e-13   3.05e+13      0.000      12.725      12.725
C(uf_rede)[T.RS_Privada]                     65.9776      0.515    128.156      0.000      64.919      67.036
C(uf_rede)[T.SC_Estadual]                    10.1650   4.52e-13   2.25e+13      0.000      10.165      10.165
C(uf_rede)[T.SC_Privada]                     68.9926      0.515    134.013      0.000      67.934      70.051
C(uf_rede)[T.SE_Estadual]                    -7.6975    5.7e-13  -1.35e+13      0.000      -7.698      -7.697
C(uf_rede)[T.SE_Privada]                     47.3776      0.515     92.027      0.000      46.319      48.436
C(uf_rede)[T.SP_Estadual]                     3.5850   4.87e-13   7.36e+12      0.000       3.585       3.585
C(uf_rede)[T.SP_Privada]                     65.7026      0.515    127.622      0.000      64.644      66.761
C(uf_rede)[T.TO_Estadual]                    -3.0375   4.14e-13  -7.34e+12      0.000      -3.038      -3.037
C(uf_rede)[T.TO_Privada]                     68.8801      0.515    133.794      0.000      67.822      69.938
C(ano, Treatment(reference=2019))[T.2021]    -9.8452      1.158     -8.504      0.000     -12.225      -7.466
C(ano, Treatment(reference=2019))[T.2023]    -9.8389      1.256     -7.836      0.000     -12.420      -7.258
C(ano, Treatment(reference=2019))[T.2025]   -11.6672      1.719     -6.787      0.000     -15.200      -8.134
rede_publica:pos_pedemeia                     8.1802      2.059      3.972      0.001       3.947      12.413
==============================================================================
Omnibus:                        3.628   Durbin-Watson:                   2.111
Prob(Omnibus):                  0.163   Jarque-Bera (JB):                3.232
Skew:                           0.258   Prob(JB):                        0.199
Kurtosis:                       3.306   Cond. No.                         60.7
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
DiD FE (UFxRede + Ano) Janela Imediata — SAEB Matemática (2023 vs 2025, N=108)
====================================================================
                             OLS Regression Results                             
================================================================================
Dep. Variable:     ideb_nota_matematica   R-squared:                       0.988
Model:                              OLS   Adj. R-squared:                  0.975
Method:                   Least Squares   F-statistic:                     2603.
Date:                  Thu, 05 Nov 2026   Prob (F-statistic):           1.12e-30
Time:                          13:10:21   Log-Likelihood:                -271.50
No. Observations:                   108   AIC:                             655.0
Df Residuals:                        52   BIC:                             805.2
Df Model:                            55                                         
Covariance Type:                cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                   263.3561      0.627    420.215      0.000     262.068     264.644
C(uf_rede)[T.AC_Privada]                     47.3259      1.164     40.675      0.000      44.934      49.718
C(uf_rede)[T.AL_Estadual]                    -3.6650   1.01e-12  -3.64e+12      0.000      -3.665      -3.665
C(uf_rede)[T.AL_Privada]                     28.0309      1.164     24.092      0.000      25.639      30.423
C(uf_rede)[T.AM_Estadual]                    -9.5800   9.21e-13  -1.04e+13      0.000      -9.580      -9.580
C(uf_rede)[T.AM_Privada]                     35.4109      1.164     30.435      0.000      33.019      37.803
C(uf_rede)[T.AP_Estadual]                   -11.1300   9.23e-13  -1.21e+13      0.000     -11.130     -11.130
C(uf_rede)[T.AP_Privada]                     37.3909      1.164     32.136      0.000      34.999      39.783
C(uf_rede)[T.BA_Estadual]                   -13.2750    9.4e-13  -1.41e+13      0.000     -13.275     -13.275
C(uf_rede)[T.BA_Privada]                     51.7909      1.164     44.513      0.000      49.399      54.183
C(uf_rede)[T.CE_Estadual]                     2.5150   9.46e-13   2.66e+12      0.000       2.515       2.515
C(uf_rede)[T.CE_Privada]                     49.4509      1.164     42.502      0.000      47.059      51.843
C(uf_rede)[T.DF_Estadual]                    -3.3850   9.17e-13  -3.69e+12      0.000      -3.385      -3.385
C(uf_rede)[T.DF_Privada]                     61.2009      1.164     52.601      0.000      58.809      63.593
C(uf_rede)[T.ES_Estadual]                    16.8300   9.24e-13   1.82e+13      0.000      16.830      16.830
C(uf_rede)[T.ES_Privada]                     61.6909      1.164     53.022      0.000      59.299      64.083
C(uf_rede)[T.GO_Estadual]                    18.4400   9.89e-13   1.86e+13      0.000      18.440      18.440
C(uf_rede)[T.GO_Privada]                     49.5559      1.164     42.592      0.000      47.164      51.948
C(uf_rede)[T.MA_Estadual]                   -13.4550   9.18e-13  -1.47e+13      0.000     -13.455     -13.455
C(uf_rede)[T.MA_Privada]                     43.3109      1.164     37.225      0.000      40.919      45.703
C(uf_rede)[T.MG_Estadual]                     6.6200   9.24e-13   7.17e+12      0.000       6.620       6.620
C(uf_rede)[T.MG_Privada]                     79.3109      1.164     68.166      0.000      76.919      81.703
C(uf_rede)[T.MS_Estadual]                     0.5300   9.92e-13   5.34e+11      0.000       0.530       0.530
C(uf_rede)[T.MS_Privada]                     61.4659      1.164     52.828      0.000      59.074      63.858
C(uf_rede)[T.MT_Estadual]                    -3.6450   9.25e-13  -3.94e+12      0.000      -3.645      -3.645
C(uf_rede)[T.MT_Privada]                     49.7259      1.164     42.738      0.000      47.334      52.118
C(uf_rede)[T.PA_Estadual]                    -2.9150   9.32e-13  -3.13e+12      0.000      -2.915      -2.915
C(uf_rede)[T.PA_Privada]                     39.7909      1.164     34.199      0.000      37.399      42.183
C(uf_rede)[T.PB_Estadual]                    -4.7350   9.33e-13  -5.08e+12      0.000      -4.735      -4.735
C(uf_rede)[T.PB_Privada]                     45.6309      1.164     39.219      0.000      43.239      48.023
C(uf_rede)[T.PE_Estadual]                    11.3900    9.3e-13   1.22e+13      0.000      11.390      11.390
C(uf_rede)[T.PE_Privada]                     51.3559      1.164     44.139      0.000      48.964      53.748
C(uf_rede)[T.PI_Estadual]                    11.5950   9.47e-13   1.22e+13      0.000      11.595      11.595
C(uf_rede)[T.PI_Privada]                     61.6959      1.164     53.026      0.000      59.304      64.088
C(uf_rede)[T.PR_Estadual]                    18.3400    9.2e-13   1.99e+13      0.000      18.340      18.340
C(uf_rede)[T.PR_Privada]                     60.3159      1.164     51.840      0.000      57.924      62.708
C(uf_rede)[T.RJ_Estadual]                   -13.1450   9.55e-13  -1.38e+13      0.000     -13.145     -13.145
C(uf_rede)[T.RJ_Privada]                     44.3609      1.164     38.127      0.000      41.969      46.753
C(uf_rede)[T.RN_Estadual]                   -10.8600   9.25e-13  -1.17e+13      0.000     -10.860     -10.860
C(uf_rede)[T.RN_Privada]                     47.7409      1.164     41.032      0.000      45.349      50.133
C(uf_rede)[T.RO_Estadual]                    -0.7300    9.2e-13  -7.93e+11      0.000      -0.730      -0.730
C(uf_rede)[T.RO_Privada]                     45.0059      1.164     38.681      0.000      42.614      47.398
C(uf_rede)[T.RR_Estadual]                    -8.7500   9.75e-13  -8.98e+12      0.000      -8.750      -8.750
C(uf_rede)[T.RR_Privada]                     37.3259      1.164     32.081      0.000      34.934      39.718
C(uf_rede)[T.RS_Estadual]                    13.2850   9.62e-13   1.38e+13      0.000      13.285      13.285
C(uf_rede)[T.RS_Privada]                     63.8309      1.164     54.861      0.000      61.439      66.223
C(uf_rede)[T.SC_Estadual]                     6.6400   9.37e-13   7.08e+12      0.000       6.640       6.640
C(uf_rede)[T.SC_Privada]                     62.7509      1.164     53.933      0.000      60.359      65.143
C(uf_rede)[T.SE_Estadual]                    -5.8350   9.29e-13  -6.28e+12      0.000      -5.835      -5.835
C(uf_rede)[T.SE_Privada]                     42.2809      1.164     36.339      0.000      39.889      44.673
C(uf_rede)[T.SP_Estadual]                     1.4850   1.04e-12   1.43e+12      0.000       1.485       1.485
C(uf_rede)[T.SP_Privada]                     59.7809      1.164     51.380      0.000      57.389      62.173
C(uf_rede)[T.TO_Estadual]                    -3.2900   1.02e-12  -3.21e+12      0.000      -3.290      -3.290
C(uf_rede)[T.TO_Privada]                     60.1459      1.164     51.694      0.000      57.754      62.538
C(ano, Treatment(reference=2023))[T.2025]     1.2259      2.021      0.607      0.549      -2.929       5.381
rede_publica:pos_pedemeia                     2.0719      2.327      0.890      0.381      -2.711       6.855
==============================================================================
Omnibus:                        2.753   Durbin-Watson:                   1.799
Prob(Omnibus):                  0.252   Jarque-Bera (JB):                2.684
Skew:                          -0.000   Prob(JB):                        0.261
Kurtosis:                       3.772   Cond. No.                         65.7
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
Pré-Tendência FE (UFxRede + Ano) — SAEB Matemática (2019-2023, N=162)
====================================================================
                             OLS Regression Results                             
================================================================================
Dep. Variable:     ideb_nota_matematica   R-squared:                       0.985
Model:                              OLS   Adj. R-squared:                  0.977
Method:                   Least Squares   F-statistic:                     1235.
Date:                  Thu, 05 Nov 2026   Prob (F-statistic):           3.11e-29
Time:                          13:10:21   Log-Likelihood:                -447.60
No. Observations:                   162   AIC:                             1011.
Df Residuals:                       104   BIC:                             1190.
Df Model:                            57                                         
Covariance Type:                cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                   267.7256      0.789    339.504      0.000     266.105     269.347
C(uf_rede)[T.AC_Privada]                     66.5949      1.307     50.962      0.000      63.909      69.281
C(uf_rede)[T.AL_Estadual]                   -10.3133   2.58e-13     -4e+13      0.000     -10.313     -10.313
C(uf_rede)[T.AL_Privada]                     35.9883      1.307     27.540      0.000      33.302      38.674
C(uf_rede)[T.AM_Estadual]                   -15.1367   2.64e-13  -5.73e+13      0.000     -15.137     -15.137
C(uf_rede)[T.AM_Privada]                     43.4049      1.307     33.216      0.000      40.719      46.091
C(uf_rede)[T.AP_Estadual]                   -13.3833   4.05e-13  -3.31e+13      0.000     -13.383     -13.383
C(uf_rede)[T.AP_Privada]                     42.1416      1.307     32.249      0.000      39.456      44.828
C(uf_rede)[T.BA_Estadual]                   -14.9033   3.35e-13  -4.45e+13      0.000     -14.903     -14.903
C(uf_rede)[T.BA_Privada]                     62.2516      1.307     47.639      0.000      59.566      64.938
C(uf_rede)[T.CE_Estadual]                    -0.1767   2.17e-13  -8.13e+11      0.000      -0.177      -0.177
C(uf_rede)[T.CE_Privada]                     62.3516      1.307     47.715      0.000      59.666      65.038
C(uf_rede)[T.DF_Estadual]                     5.1300   2.91e-13   1.76e+13      0.000       5.130       5.130
C(uf_rede)[T.DF_Privada]                     79.2016      1.307     60.610      0.000      76.516      81.888
C(uf_rede)[T.ES_Estadual]                    17.2700   2.17e-13   7.98e+13      0.000      17.270      17.270
C(uf_rede)[T.ES_Privada]                     76.7183      1.307     58.709      0.000      74.032      79.404
C(uf_rede)[T.GO_Estadual]                    13.1300   2.72e-13   4.83e+13      0.000      13.130      13.130
C(uf_rede)[T.GO_Privada]                     63.6116      1.307     48.679      0.000      60.926      66.298
C(uf_rede)[T.MA_Estadual]                   -16.7867    2.5e-13   -6.7e+13      0.000     -16.787     -16.787
C(uf_rede)[T.MA_Privada]                     51.8916      1.307     39.711      0.000      49.206      54.578
C(uf_rede)[T.MG_Estadual]                     7.2133   2.22e-13   3.25e+13      0.000       7.213       7.213
C(uf_rede)[T.MG_Privada]                     89.6183      1.307     68.581      0.000      86.932      92.304
C(uf_rede)[T.MS_Estadual]                     4.9433   2.71e-13   1.82e+13      0.000       4.943       4.943
C(uf_rede)[T.MS_Privada]                     74.2983      1.307     56.857      0.000      71.612      76.984
C(uf_rede)[T.MT_Estadual]                    -3.8767    3.6e-13  -1.08e+13      0.000      -3.877      -3.877
C(uf_rede)[T.MT_Privada]                     64.8316      1.307     49.613      0.000      62.146      67.518
C(uf_rede)[T.PA_Estadual]                   -14.6600   4.06e-13  -3.61e+13      0.000     -14.660     -14.660
C(uf_rede)[T.PA_Privada]                     52.6816      1.307     40.315      0.000      49.996      55.368
C(uf_rede)[T.PB_Estadual]                    -7.2533   3.22e-13  -2.25e+13      0.000      -7.253      -7.253
C(uf_rede)[T.PB_Privada]                     55.6916      1.307     42.619      0.000      53.006      58.378
C(uf_rede)[T.PE_Estadual]                     7.4633   2.29e-13   3.26e+13      0.000       7.463       7.463
C(uf_rede)[T.PE_Privada]                     61.2183      1.307     46.848      0.000      58.532      63.904
C(uf_rede)[T.PI_Estadual]                    -3.8867   2.16e-13   -1.8e+13      0.000      -3.887      -3.887
C(uf_rede)[T.PI_Privada]                     77.7683      1.307     59.513      0.000      75.082      80.454
C(uf_rede)[T.PR_Estadual]                    13.5533   2.74e-13   4.95e+13      0.000      13.553      13.553
C(uf_rede)[T.PR_Privada]                     78.5716      1.307     60.128      0.000      75.886      81.258
C(uf_rede)[T.RJ_Estadual]                    -7.6067   2.51e-13  -3.03e+13      0.000      -7.607      -7.607
C(uf_rede)[T.RJ_Privada]                     53.4516      1.307     40.904      0.000      50.766      56.138
C(uf_rede)[T.RN_Estadual]                   -13.2167    2.4e-13  -5.51e+13      0.000     -13.217     -13.217
C(uf_rede)[T.RN_Privada]                     53.8183      1.307     41.185      0.000      51.132      56.504
C(uf_rede)[T.RO_Estadual]                     3.5800   2.27e-13   1.58e+13      0.000       3.580       3.580
C(uf_rede)[T.RO_Privada]                     59.0949      1.307     45.223      0.000      56.409      61.781
C(uf_rede)[T.RR_Estadual]                    -6.9267   3.15e-13   -2.2e+13      0.000      -6.927      -6.927
C(uf_rede)[T.RR_Privada]                     57.3483      1.307     43.886      0.000      54.662      60.034
C(uf_rede)[T.RS_Estadual]                    11.2933   2.21e-13    5.1e+13      0.000      11.293      11.293
C(uf_rede)[T.RS_Privada]                     69.4883      1.307     53.177      0.000      66.802      72.174
C(uf_rede)[T.SC_Estadual]                    11.2600   2.22e-13   5.07e+13      0.000      11.260      11.260
C(uf_rede)[T.SC_Privada]                     77.7249      1.307     59.480      0.000      75.039      80.411
C(uf_rede)[T.SE_Estadual]                    -8.6500   2.19e-13  -3.94e+13      0.000      -8.650      -8.650
C(uf_rede)[T.SE_Privada]                     53.9449      1.307     41.282      0.000      51.259      56.631
C(uf_rede)[T.SP_Estadual]                     3.9600   3.58e-13   1.11e+13      0.000       3.960       3.960
C(uf_rede)[T.SP_Privada]                     72.6383      1.307     55.587      0.000      69.952      75.324
C(uf_rede)[T.TO_Estadual]                    -2.8100   2.59e-13  -1.08e+13      0.000      -2.810      -2.810
C(uf_rede)[T.TO_Privada]                     76.7449      1.307     58.730      0.000      74.059      79.431
C(ano, Treatment(reference=2019))[T.2021]   -14.5893      2.012     -7.250      0.000     -18.725     -10.453
C(ano, Treatment(reference=2019))[T.2023]   -16.7922      1.883     -8.920      0.000     -20.662     -12.922
rede_publica:ano_2021                         9.4881      2.011      4.718      0.000       5.355      13.622
rede_publica:ano_2023                        13.9067      2.268      6.133      0.000       9.246      18.568
==============================================================================
Omnibus:                        2.037   Durbin-Watson:                   1.831
Prob(Omnibus):                  0.361   Jarque-Bera (JB):                1.887
Skew:                           0.264   Prob(JB):                        0.389
Kurtosis:                       2.986   Cond. No.                         64.1
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
DiD FE (UFxRede + Ano) Painel Completo — SAEB Língua Portuguesa (2019-2025, N=216)
====================================================================
                             OLS Regression Results                            
===============================================================================
Dep. Variable:     ideb_nota_portugues   R-squared:                       0.973
Model:                             OLS   Adj. R-squared:                  0.963
Method:                  Least Squares   F-statistic:                     2128.
Date:                 Thu, 05 Nov 2026   Prob (F-statistic):           2.70e-32
Time:                         13:10:21   Log-Likelihood:                -604.40
No. Observations:                  216   AIC:                             1325.
Df Residuals:                      158   BIC:                             1521.
Df Model:                           57                                         
Covariance Type:               cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                   273.6142      0.706    387.587      0.000     272.163     275.065
C(uf_rede)[T.AC_Privada]                     48.7419      0.431    113.079      0.000      47.856      49.628
C(uf_rede)[T.AL_Estadual]                   -10.2850   4.54e-13  -2.26e+13      0.000     -10.285     -10.285
C(uf_rede)[T.AL_Privada]                     26.1619      0.431     60.694      0.000      25.276      27.048
C(uf_rede)[T.AM_Estadual]                   -12.2075   1.03e-12  -1.18e+13      0.000     -12.208     -12.207
C(uf_rede)[T.AM_Privada]                     34.1144      0.431     79.144      0.000      33.228      35.000
C(uf_rede)[T.AP_Estadual]                    -9.2300   6.67e-13  -1.38e+13      0.000      -9.230      -9.230
C(uf_rede)[T.AP_Privada]                     34.5219      0.431     80.089      0.000      33.636      35.408
C(uf_rede)[T.BA_Estadual]                   -16.0500   4.69e-13  -3.42e+13      0.000     -16.050     -16.050
C(uf_rede)[T.BA_Privada]                     43.7244      0.431    101.438      0.000      42.838      44.610
C(uf_rede)[T.CE_Estadual]                    -0.7025   4.61e-13  -1.52e+12      0.000      -0.703      -0.702
C(uf_rede)[T.CE_Privada]                     45.0369      0.431    104.483      0.000      44.151      45.923
C(uf_rede)[T.DF_Estadual]                     2.6825   6.58e-13   4.08e+12      0.000       2.682       2.683
C(uf_rede)[T.DF_Privada]                     48.4219      0.431    112.336      0.000      47.536      49.308
C(uf_rede)[T.ES_Estadual]                    12.2450   4.79e-13   2.56e+13      0.000      12.245      12.245
C(uf_rede)[T.ES_Privada]                     44.9894      0.431    104.373      0.000      44.103      45.875
C(uf_rede)[T.GO_Estadual]                    12.4900   4.54e-13   2.75e+13      0.000      12.490      12.490
C(uf_rede)[T.GO_Privada]                     41.8294      0.431     97.042      0.000      40.943      42.715
C(uf_rede)[T.MA_Estadual]                   -15.6900   4.54e-13  -3.46e+13      0.000     -15.690     -15.690
C(uf_rede)[T.MA_Privada]                     37.3244      0.431     86.591      0.000      36.438      38.210
C(uf_rede)[T.MG_Estadual]                     5.4275   4.91e-13   1.11e+13      0.000       5.427       5.428
C(uf_rede)[T.MG_Privada]                     56.8719      0.431    131.940      0.000      55.986      57.758
C(uf_rede)[T.MS_Estadual]                     2.1700   5.55e-13   3.91e+12      0.000       2.170       2.170
C(uf_rede)[T.MS_Privada]                     47.4844      0.431    110.161      0.000      46.598      48.370
C(uf_rede)[T.MT_Estadual]                    -4.8200   4.53e-13  -1.06e+13      0.000      -4.820      -4.820
C(uf_rede)[T.MT_Privada]                     39.9544      0.431     92.692      0.000      39.068      40.840
C(uf_rede)[T.PA_Estadual]                    -9.5825   4.71e-13  -2.03e+13      0.000      -9.583      -9.582
C(uf_rede)[T.PA_Privada]                     40.8344      0.431     94.734      0.000      39.948      41.720
C(uf_rede)[T.PB_Estadual]                    -6.0175   5.99e-13     -1e+13      0.000      -6.018      -6.017
C(uf_rede)[T.PB_Privada]                     38.5944      0.431     89.537      0.000      37.708      39.480
C(uf_rede)[T.PE_Estadual]                     6.5625   5.04e-13    1.3e+13      0.000       6.562       6.563
C(uf_rede)[T.PE_Privada]                     42.8019      0.431     99.298      0.000      41.916      43.688
C(uf_rede)[T.PI_Estadual]                    -3.6700   5.11e-13  -7.18e+12      0.000      -3.670      -3.670
C(uf_rede)[T.PI_Privada]                     53.7669      0.431    124.736      0.000      52.881      54.653
C(uf_rede)[T.PR_Estadual]                    14.4550   4.61e-13   3.13e+13      0.000      14.455      14.455
C(uf_rede)[T.PR_Privada]                     52.0069      0.431    120.653      0.000      51.121      52.893
C(uf_rede)[T.RJ_Estadual]                    -9.4875   4.78e-13  -1.99e+13      0.000      -9.488      -9.487
C(uf_rede)[T.RJ_Privada]                     38.6994      0.431     89.780      0.000      37.813      39.585
C(uf_rede)[T.RN_Estadual]                   -12.6125    4.9e-13  -2.58e+13      0.000     -12.613     -12.612
C(uf_rede)[T.RN_Privada]                     41.1019      0.431     95.354      0.000      40.216      41.988
C(uf_rede)[T.RO_Estadual]                    -0.0975   4.64e-13   -2.1e+11      0.000      -0.098      -0.097
C(uf_rede)[T.RO_Privada]                     43.8319      0.431    101.688      0.000      42.946      44.718
C(uf_rede)[T.RR_Estadual]                    -9.7350   5.03e-13  -1.94e+13      0.000      -9.735      -9.735
C(uf_rede)[T.RR_Privada]                     42.3244      0.431     98.190      0.000      41.438      43.210
C(uf_rede)[T.RS_Estadual]                    12.9925   4.75e-13   2.74e+13      0.000      12.992      12.993
C(uf_rede)[T.RS_Privada]                     50.0394      0.431    116.089      0.000      49.153      50.925
C(uf_rede)[T.SC_Estadual]                     7.5075   4.73e-13   1.59e+13      0.000       7.507       7.508
C(uf_rede)[T.SC_Privada]                     50.1994      0.431    116.460      0.000      49.313      51.085
C(uf_rede)[T.SE_Estadual]                    -9.2400   5.77e-13   -1.6e+13      0.000      -9.240      -9.240
C(uf_rede)[T.SE_Privada]                     38.8944      0.431     90.233      0.000      38.008      39.780
C(uf_rede)[T.SP_Estadual]                     6.2325    4.9e-13   1.27e+13      0.000       6.232       6.233
C(uf_rede)[T.SP_Privada]                     51.5969      0.431    119.702      0.000      50.711      52.483
C(uf_rede)[T.TO_Estadual]                    -7.5800   4.68e-13  -1.62e+13      0.000      -7.580      -7.580
C(uf_rede)[T.TO_Privada]                     49.6344      0.431    115.149      0.000      48.748      50.520
C(ano, Treatment(reference=2019))[T.2021]    -5.3856      0.940     -5.729      0.000      -7.318      -3.453
C(ano, Treatment(reference=2019))[T.2023]    -4.9791      0.985     -5.053      0.000      -7.005      -2.953
C(ano, Treatment(reference=2019))[T.2025]    -6.7699      1.567     -4.319      0.000      -9.992      -3.548
rede_publica:pos_pedemeia                     5.8777      1.724      3.409      0.002       2.334       9.422
==============================================================================
Omnibus:                        0.665   Durbin-Watson:                   2.088
Prob(Omnibus):                  0.717   Jarque-Bera (JB):                0.377
Skew:                           0.034   Prob(JB):                        0.828
Kurtosis:                       3.193   Cond. No.                         60.7
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
DiD FE (UFxRede + Ano) Janela Imediata — SAEB Língua Portuguesa (2023 vs 2025, N=108)
====================================================================
                             OLS Regression Results                            
===============================================================================
Dep. Variable:     ideb_nota_portugues   R-squared:                       0.987
Model:                             OLS   Adj. R-squared:                  0.973
Method:                  Least Squares   F-statistic:                     2208.
Date:                 Thu, 05 Nov 2026   Prob (F-statistic):           9.46e-30
Time:                         13:10:22   Log-Likelihood:                -256.30
No. Observations:                  108   AIC:                             624.6
Df Residuals:                       52   BIC:                             774.8
Df Model:                           55                                         
Covariance Type:               cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                   269.5800      0.553    487.766      0.000     268.444     270.716
C(uf_rede)[T.AC_Privada]                     40.9520      0.956     42.824      0.000      38.986      42.918
C(uf_rede)[T.AL_Estadual]                    -8.7600   1.01e-12   -8.7e+12      0.000      -8.760      -8.760
C(uf_rede)[T.AL_Privada]                     24.8420      0.956     25.978      0.000      22.876      26.808
C(uf_rede)[T.AM_Estadual]                    -9.6800   9.38e-13  -1.03e+13      0.000      -9.680      -9.680
C(uf_rede)[T.AM_Privada]                     33.8370      0.956     35.384      0.000      31.871      35.803
C(uf_rede)[T.AP_Estadual]                    -8.0150   9.27e-13  -8.65e+12      0.000      -8.015      -8.015
C(uf_rede)[T.AP_Privada]                     39.7720      0.956     41.590      0.000      37.806      41.738
C(uf_rede)[T.BA_Estadual]                   -17.1850   9.56e-13   -1.8e+13      0.000     -17.185     -17.185
C(uf_rede)[T.BA_Privada]                     42.0570      0.956     43.980      0.000      40.091      44.023
C(uf_rede)[T.CE_Estadual]                    -0.9250   9.52e-13  -9.72e+11      0.000      -0.925      -0.925
C(uf_rede)[T.CE_Privada]                     42.8470      0.956     44.806      0.000      40.881      44.813
C(uf_rede)[T.DF_Estadual]                    -2.4650   9.25e-13  -2.67e+12      0.000      -2.465      -2.465
C(uf_rede)[T.DF_Privada]                     43.7370      0.956     45.736      0.000      41.771      45.703
C(uf_rede)[T.ES_Estadual]                    12.0750   9.33e-13   1.29e+13      0.000      12.075      12.075
C(uf_rede)[T.ES_Privada]                     41.2420      0.956     43.127      0.000      39.276      43.208
C(uf_rede)[T.GO_Estadual]                    14.7250   9.81e-13    1.5e+13      0.000      14.725      14.725
C(uf_rede)[T.GO_Privada]                     36.8720      0.956     38.558      0.000      34.906      38.838
C(uf_rede)[T.MA_Estadual]                   -16.0750   9.27e-13  -1.73e+13      0.000     -16.075     -16.075
C(uf_rede)[T.MA_Privada]                     37.0620      0.956     38.756      0.000      35.096      39.028
C(uf_rede)[T.MG_Estadual]                     5.6000   9.44e-13   5.93e+12      0.000       5.600       5.600
C(uf_rede)[T.MG_Privada]                     53.5020      0.956     55.948      0.000      51.536      55.468
C(uf_rede)[T.MS_Estadual]                     0.0150   9.98e-13    1.5e+10      0.000       0.015       0.015
C(uf_rede)[T.MS_Privada]                     45.2870      0.956     47.357      0.000      43.321      47.253
C(uf_rede)[T.MT_Estadual]                    -4.6750    9.3e-13  -5.03e+12      0.000      -4.675      -4.675
C(uf_rede)[T.MT_Privada]                     37.4820      0.956     39.196      0.000      35.516      39.448
C(uf_rede)[T.PA_Estadual]                    -2.8800   9.37e-13  -3.07e+12      0.000      -2.880      -2.880
C(uf_rede)[T.PA_Privada]                     39.3520      0.956     41.151      0.000      37.386      41.318
C(uf_rede)[T.PB_Estadual]                    -4.8350   9.41e-13  -5.14e+12      0.000      -4.835      -4.835
C(uf_rede)[T.PB_Privada]                     36.3870      0.956     38.050      0.000      34.421      38.353
C(uf_rede)[T.PE_Estadual]                     7.0900   9.41e-13   7.54e+12      0.000       7.090       7.090
C(uf_rede)[T.PE_Privada]                     40.5270      0.956     42.380      0.000      38.561      42.493
C(uf_rede)[T.PI_Estadual]                     1.9050   9.48e-13   2.01e+12      0.000       1.905       1.905
C(uf_rede)[T.PI_Privada]                     50.7770      0.956     53.098      0.000      48.811      52.743
C(uf_rede)[T.PR_Estadual]                    18.0400   9.32e-13   1.93e+13      0.000      18.040      18.040
C(uf_rede)[T.PR_Privada]                     48.0020      0.956     50.196      0.000      46.036      49.968
C(uf_rede)[T.RJ_Estadual]                   -14.5950   9.47e-13  -1.54e+13      0.000     -14.595     -14.595
C(uf_rede)[T.RJ_Privada]                     39.4020      0.956     41.203      0.000      37.436      41.368
C(uf_rede)[T.RN_Estadual]                   -11.8000   9.31e-13  -1.27e+13      0.000     -11.800     -11.800
C(uf_rede)[T.RN_Privada]                     41.6920      0.956     43.598      0.000      39.726      43.658
C(uf_rede)[T.RO_Estadual]                    -2.5850   9.34e-13  -2.77e+12      0.000      -2.585      -2.585
C(uf_rede)[T.RO_Privada]                     40.6070      0.956     42.463      0.000      38.641      42.573
C(uf_rede)[T.RR_Estadual]                   -12.7450   9.75e-13  -1.31e+13      0.000     -12.745     -12.745
C(uf_rede)[T.RR_Privada]                     35.8620      0.956     37.501      0.000      33.896      37.828
C(uf_rede)[T.RS_Estadual]                    15.4850   9.64e-13   1.61e+13      0.000      15.485      15.485
C(uf_rede)[T.RS_Privada]                     48.9370      0.956     51.174      0.000      46.971      50.903
C(uf_rede)[T.SC_Estadual]                     6.9200   9.32e-13   7.43e+12      0.000       6.920       6.920
C(uf_rede)[T.SC_Privada]                     48.7870      0.956     51.017      0.000      46.821      50.753
C(uf_rede)[T.SE_Estadual]                    -7.7450   9.33e-13   -8.3e+12      0.000      -7.745      -7.745
C(uf_rede)[T.SE_Privada]                     37.2420      0.956     38.945      0.000      35.276      39.208
C(uf_rede)[T.SP_Estadual]                     4.3150      1e-12   4.29e+12      0.000       4.315       4.315
C(uf_rede)[T.SP_Privada]                     49.6420      0.956     51.911      0.000      47.676      51.608
C(uf_rede)[T.TO_Estadual]                    -8.3750   1.01e-12  -8.33e+12      0.000      -8.375      -8.375
C(uf_rede)[T.TO_Privada]                     48.7020      0.956     50.928      0.000      46.736      50.668
C(ano, Treatment(reference=2023))[T.2025]    -0.5841      1.746     -0.335      0.741      -4.172       3.004
rede_publica:pos_pedemeia                     3.4641      1.913      1.811      0.082      -0.467       7.395
==============================================================================
Omnibus:                        0.015   Durbin-Watson:                   1.770
Prob(Omnibus):                  0.992   Jarque-Bera (JB):                0.028
Skew:                          -0.000   Prob(JB):                        0.986
Kurtosis:                       2.921   Cond. No.                         65.7
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
Pré-Tendência FE (UFxRede + Ano) — SAEB Língua Portuguesa (2019-2023, N=162)
====================================================================
                             OLS Regression Results                            
===============================================================================
Dep. Variable:     ideb_nota_portugues   R-squared:                       0.984
Model:                             OLS   Adj. R-squared:                  0.976
Method:                  Least Squares   F-statistic:                     994.5
Date:                 Thu, 05 Nov 2026   Prob (F-statistic):           5.08e-28
Time:                         13:10:22   Log-Likelihood:                -412.98
No. Observations:                  162   AIC:                             942.0
Df Residuals:                      104   BIC:                             1121.
Df Model:                           57                                         
Covariance Type:               cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                   271.0463      0.673    402.743      0.000     269.663     272.430
C(uf_rede)[T.AC_Privada]                     57.3305      1.028     55.747      0.000      55.217      59.444
C(uf_rede)[T.AL_Estadual]                   -11.2333   2.58e-13  -4.35e+13      0.000     -11.233     -11.233
C(uf_rede)[T.AL_Privada]                     29.9638      1.028     29.136      0.000      27.850      32.078
C(uf_rede)[T.AM_Estadual]                   -12.4933   2.67e-13  -4.68e+13      0.000     -12.493     -12.493
C(uf_rede)[T.AM_Privada]                     38.7372      1.028     37.667      0.000      36.623      40.851
C(uf_rede)[T.AP_Estadual]                    -8.4300   4.19e-13  -2.01e+13      0.000      -8.430      -8.430
C(uf_rede)[T.AP_Privada]                     35.9705      1.028     34.977      0.000      33.857      38.084
C(uf_rede)[T.BA_Estadual]                   -15.1067    3.4e-13  -4.45e+13      0.000     -15.107     -15.107
C(uf_rede)[T.BA_Privada]                     49.9905      1.028     48.610      0.000      47.877      52.104
C(uf_rede)[T.CE_Estadual]                    -0.4100   2.41e-13   -1.7e+12      0.000      -0.410      -0.410
C(uf_rede)[T.CE_Privada]                     50.1838      1.028     48.798      0.000      48.070      52.298
C(uf_rede)[T.DF_Estadual]                     5.1433   3.08e-13   1.67e+13      0.000       5.143       5.143
C(uf_rede)[T.DF_Privada]                     56.1872      1.028     54.635      0.000      54.073      58.301
C(uf_rede)[T.ES_Estadual]                    12.7933   2.41e-13   5.31e+13      0.000      12.793      12.793
C(uf_rede)[T.ES_Privada]                     50.9005      1.028     49.495      0.000      48.787      53.014
C(uf_rede)[T.GO_Estadual]                    11.9600   2.78e-13   4.31e+13      0.000      11.960      11.960
C(uf_rede)[T.GO_Privada]                     46.5938      1.028     45.307      0.000      44.480      48.708
C(uf_rede)[T.MA_Estadual]                   -15.0433   2.59e-13   -5.8e+13      0.000     -15.043     -15.043
C(uf_rede)[T.MA_Privada]                     43.2205      1.028     42.027      0.000      41.107      45.334
C(uf_rede)[T.MG_Estadual]                     4.8633    2.4e-13   2.02e+13      0.000       4.863       4.863
C(uf_rede)[T.MG_Privada]                     62.3938      1.028     60.671      0.000      60.280      64.508
C(uf_rede)[T.MS_Estadual]                     3.1633   2.77e-13   1.14e+13      0.000       3.163       3.163
C(uf_rede)[T.MS_Privada]                     52.7872      1.028     51.329      0.000      50.673      54.901
C(uf_rede)[T.MT_Estadual]                    -4.3067   3.95e-13  -1.09e+13      0.000      -4.307      -4.307
C(uf_rede)[T.MT_Privada]                     46.1638      1.028     44.889      0.000      44.050      48.278
C(uf_rede)[T.PA_Estadual]                   -11.7567   3.53e-13  -3.33e+13      0.000     -11.757     -11.757
C(uf_rede)[T.PA_Privada]                     45.6972      1.028     44.435      0.000      43.583      47.811
C(uf_rede)[T.PB_Estadual]                    -6.3333   3.73e-13   -1.7e+13      0.000      -6.333      -6.333
C(uf_rede)[T.PB_Privada]                     41.8572      1.028     40.701      0.000      39.743      43.971
C(uf_rede)[T.PE_Estadual]                     6.6100   2.44e-13    2.7e+13      0.000       6.610       6.610
C(uf_rede)[T.PE_Privada]                     46.4438      1.028     45.161      0.000      44.330      48.558
C(uf_rede)[T.PI_Estadual]                    -7.0800   2.57e-13  -2.75e+13      0.000      -7.080      -7.080
C(uf_rede)[T.PI_Privada]                     59.9072      1.028     58.253      0.000      57.793      62.021
C(uf_rede)[T.PR_Estadual]                    12.4633   2.94e-13   4.24e+13      0.000      12.463      12.463
C(uf_rede)[T.PR_Privada]                     57.7672      1.028     56.172      0.000      55.653      59.881
C(uf_rede)[T.RJ_Estadual]                    -6.6133   2.57e-13  -2.57e+13      0.000      -6.613      -6.613
C(uf_rede)[T.RJ_Privada]                     42.2205      1.028     41.054      0.000      40.107      44.334
C(uf_rede)[T.RN_Estadual]                   -12.7700   2.49e-13  -5.13e+13      0.000     -12.770     -12.770
C(uf_rede)[T.RN_Privada]                     44.8372      1.028     43.599      0.000      42.723      46.951
C(uf_rede)[T.RO_Estadual]                     1.4167   2.49e-13   5.68e+12      0.000       1.417       1.417
C(uf_rede)[T.RO_Privada]                     49.6338      1.028     48.263      0.000      47.520      51.748
C(uf_rede)[T.RR_Estadual]                    -8.5167   2.81e-13  -3.04e+13      0.000      -8.517      -8.517
C(uf_rede)[T.RR_Privada]                     48.7572      1.028     47.411      0.000      46.643      50.871
C(uf_rede)[T.RS_Estadual]                    10.9667    2.5e-13   4.38e+13      0.000      10.967      10.967
C(uf_rede)[T.RS_Privada]                     52.6372      1.028     51.183      0.000      50.523      54.751
C(uf_rede)[T.SC_Estadual]                     7.0767   2.45e-13   2.89e+13      0.000       7.077       7.077
C(uf_rede)[T.SC_Privada]                     56.2072      1.028     54.655      0.000      54.093      58.321
C(uf_rede)[T.SE_Estadual]                   -10.1133   2.41e-13   -4.2e+13      0.000     -10.113     -10.113
C(uf_rede)[T.SE_Privada]                     43.0305      1.028     41.842      0.000      40.917      45.144
C(uf_rede)[T.SP_Estadual]                     7.1867   3.07e-13   2.34e+13      0.000       7.187       7.187
C(uf_rede)[T.SP_Privada]                     56.4905      1.028     54.930      0.000      54.377      58.604
C(uf_rede)[T.TO_Estadual]                    -6.3467   3.09e-13  -2.06e+13      0.000      -6.347      -6.347
C(uf_rede)[T.TO_Privada]                     54.9305      1.028     53.413      0.000      52.817      57.044
C(ano, Treatment(reference=2019))[T.2021]    -9.2159      1.553     -5.934      0.000     -12.409      -6.023
C(ano, Treatment(reference=2019))[T.2023]    -8.7044      1.494     -5.828      0.000     -11.774      -5.634
rede_publica:ano_2021                         7.6607      1.672      4.583      0.000       4.225      11.097
rede_publica:ano_2023                         7.4507      1.833      4.065      0.000       3.683      11.218
==============================================================================
Omnibus:                        0.080   Durbin-Watson:                   2.016
Prob(Omnibus):                  0.961   Jarque-Bera (JB):                0.001
Skew:                          -0.004   Prob(JB):                         1.00
Kurtosis:                       3.007   Cond. No.                         64.1
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
DiD FE (UFxRede + Ano) Painel Completo — Nota Média Padronizada SAEB (N) (2019-2025, N=216)
====================================================================
                            OLS Regression Results                            
==============================================================================
Dep. Variable:        ideb_nota_media   R-squared:                       0.974
Model:                            OLS   Adj. R-squared:                  0.965
Method:                 Least Squares   F-statistic:                     2695.
Date:                Thu, 05 Nov 2026   Prob (F-statistic):           1.26e-33
Time:                        13:10:22   Log-Likelihood:                 140.09
No. Observations:                 216   AIC:                            -164.2
Df Residuals:                     158   BIC:                             31.58
Df Model:                          57                                         
Covariance Type:              cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                     4.5925      0.023    202.055      0.000       4.546       4.639
C(uf_rede)[T.AC_Privada]                      1.5276      0.013    115.197      0.000       1.500       1.555
C(uf_rede)[T.AL_Estadual]                    -0.2702   5.18e-15  -5.21e+13      0.000      -0.270      -0.270
C(uf_rede)[T.AL_Privada]                      0.8097      0.013     61.058      0.000       0.782       0.837
C(uf_rede)[T.AM_Estadual]                    -0.3792   2.08e-14  -1.82e+13      0.000      -0.379      -0.379
C(uf_rede)[T.AM_Privada]                      1.0382      0.013     78.295      0.000       1.011       1.065
C(uf_rede)[T.AP_Estadual]                    -0.3229   1.12e-14  -2.89e+13      0.000      -0.323      -0.323
C(uf_rede)[T.AP_Privada]                      1.0456      0.013     78.853      0.000       1.018       1.073
C(uf_rede)[T.BA_Estadual]                    -0.4442   4.52e-15  -9.83e+13      0.000      -0.444      -0.444
C(uf_rede)[T.BA_Privada]                      1.4132      0.013    106.572      0.000       1.386       1.440
C(uf_rede)[T.CE_Estadual]                     0.0002   4.41e-15   3.58e+10      0.000       0.000       0.000
C(uf_rede)[T.CE_Privada]                      1.4408      0.013    108.655      0.000       1.414       1.468
C(uf_rede)[T.DF_Estadual]                     0.0758   5.67e-15   1.34e+13      0.000       0.076       0.076
C(uf_rede)[T.DF_Privada]                      1.6938      0.013    127.731      0.000       1.667       1.721
C(uf_rede)[T.ES_Estadual]                     0.4281   7.12e-15   6.02e+13      0.000       0.428       0.428
C(uf_rede)[T.ES_Privada]                      1.6370      0.013    123.451      0.000       1.610       1.664
C(uf_rede)[T.GO_Estadual]                     0.3989   5.33e-15   7.49e+13      0.000       0.399       0.399
C(uf_rede)[T.GO_Privada]                      1.4268      0.013    107.595      0.000       1.399       1.454
C(uf_rede)[T.MA_Estadual]                    -0.4603   4.53e-15  -1.02e+14      0.000      -0.460      -0.460
C(uf_rede)[T.MA_Privada]                      1.1801      0.013     88.997      0.000       1.153       1.207
C(uf_rede)[T.MG_Estadual]                     0.1852   6.89e-15   2.69e+13      0.000       0.185       0.185
C(uf_rede)[T.MG_Privada]                      2.0074      0.013    151.381      0.000       1.980       2.035
C(uf_rede)[T.MS_Estadual]                     0.0843   9.27e-15    9.1e+12      0.000       0.084       0.084
C(uf_rede)[T.MS_Privada]                      1.6425      0.013    123.866      0.000       1.615       1.670
C(uf_rede)[T.MT_Estadual]                    -0.1284   4.69e-15  -2.74e+13      0.000      -0.128      -0.128
C(uf_rede)[T.MT_Privada]                      1.3923      0.013    104.993      0.000       1.365       1.420
C(uf_rede)[T.PA_Estadual]                    -0.2998   6.84e-15  -4.38e+13      0.000      -0.300      -0.300
C(uf_rede)[T.PA_Privada]                      1.2444      0.013     93.846      0.000       1.217       1.272
C(uf_rede)[T.PB_Estadual]                    -0.1821   1.08e-14  -1.69e+13      0.000      -0.182      -0.182
C(uf_rede)[T.PB_Privada]                      1.2854      0.013     96.933      0.000       1.258       1.313
C(uf_rede)[T.PE_Estadual]                     0.2219   8.19e-15   2.71e+13      0.000       0.222       0.222
C(uf_rede)[T.PE_Privada]                      1.4189      0.013    107.003      0.000       1.392       1.446
C(uf_rede)[T.PI_Estadual]                    -0.0231   5.13e-15   -4.5e+12      0.000      -0.023      -0.023
C(uf_rede)[T.PI_Privada]                      1.7746      0.013    133.826      0.000       1.747       1.802
C(uf_rede)[T.PR_Estadual]                     0.4392   6.71e-15   6.54e+13      0.000       0.439       0.439
C(uf_rede)[T.PR_Privada]                      1.7509      0.013    132.040      0.000       1.724       1.778
C(uf_rede)[T.RJ_Estadual]                    -0.2725   6.28e-15  -4.34e+13      0.000      -0.272      -0.272
C(uf_rede)[T.RJ_Privada]                      1.2592      0.013     94.963      0.000       1.232       1.287
C(uf_rede)[T.RN_Estadual]                    -0.3676   4.44e-15  -8.27e+13      0.000      -0.368      -0.368
C(uf_rede)[T.RN_Privada]                      1.3046      0.013     98.385      0.000       1.277       1.332
C(uf_rede)[T.RO_Estadual]                     0.0285   7.02e-15   4.05e+12      0.000       0.028       0.028
C(uf_rede)[T.RO_Privada]                      1.3776      0.013    103.884      0.000       1.350       1.405
C(uf_rede)[T.RR_Estadual]                    -0.2502    7.9e-15  -3.17e+13      0.000      -0.250      -0.250
C(uf_rede)[T.RR_Privada]                      1.3160      0.013     99.243      0.000       1.289       1.343
C(uf_rede)[T.RS_Estadual]                     0.3732   7.19e-15   5.19e+13      0.000       0.373       0.373
C(uf_rede)[T.RS_Privada]                      1.6757      0.013    126.372      0.000       1.648       1.703
C(uf_rede)[T.SC_Estadual]                     0.2552   7.24e-15   3.52e+13      0.000       0.255       0.255
C(uf_rede)[T.SC_Privada]                      1.7205      0.013    129.746      0.000       1.693       1.748
C(uf_rede)[T.SE_Estadual]                    -0.2464    1.1e-14  -2.24e+13      0.000      -0.246      -0.246
C(uf_rede)[T.SE_Privada]                      1.2477      0.013     94.089      0.000       1.220       1.275
C(uf_rede)[T.SP_Estadual]                     0.1437   7.91e-15   1.82e+13      0.000       0.144       0.144
C(uf_rede)[T.SP_Privada]                      1.6952      0.013    127.839      0.000       1.668       1.722
C(uf_rede)[T.TO_Estadual]                    -0.1561   6.83e-15  -2.29e+13      0.000      -0.156      -0.156
C(uf_rede)[T.TO_Privada]                      1.7104      0.013    128.989      0.000       1.683       1.738
C(ano, Treatment(reference=2019))[T.2021]    -0.2189      0.030     -7.331      0.000      -0.280      -0.158
C(ano, Treatment(reference=2019))[T.2023]    -0.2127      0.031     -6.842      0.000      -0.277      -0.149
C(ano, Treatment(reference=2019))[T.2025]    -0.2652      0.047     -5.676      0.000      -0.361      -0.169
rede_publica:pos_pedemeia                     0.2029      0.053      3.825      0.001       0.094       0.312
==============================================================================
Omnibus:                        2.346   Durbin-Watson:                   2.093
Prob(Omnibus):                  0.309   Jarque-Bera (JB):                1.967
Skew:                           0.189   Prob(JB):                        0.374
Kurtosis:                       3.275   Cond. No.                         60.7
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
DiD FE (UFxRede + Ano) Janela Imediata — Nota Média Padronizada SAEB (N) (2023 vs 2025, N=108)
====================================================================
                            OLS Regression Results                            
==============================================================================
Dep. Variable:        ideb_nota_media   R-squared:                       0.988
Model:                            OLS   Adj. R-squared:                  0.976
Method:                 Least Squares   F-statistic:                     2641.
Date:                Thu, 05 Nov 2026   Prob (F-statistic):           9.36e-31
Time:                        13:10:22   Log-Likelihood:                 122.37
No. Observations:                 108   AIC:                            -132.7
Df Residuals:                      52   BIC:                             17.46
Df Model:                          55                                         
Covariance Type:              cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                     4.4240      0.016    271.823      0.000       4.391       4.457
C(uf_rede)[T.AC_Privada]                      1.2777      0.030     43.183      0.000       1.217       1.339
C(uf_rede)[T.AL_Estadual]                    -0.1826   1.76e-14  -1.04e+13      0.000      -0.183      -0.183
C(uf_rede)[T.AL_Privada]                      0.7656      0.030     25.874      0.000       0.705       0.826
C(uf_rede)[T.AM_Estadual]                    -0.2795   1.67e-14  -1.68e+13      0.000      -0.279      -0.279
C(uf_rede)[T.AM_Privada]                      1.0039      0.030     33.928      0.000       0.943       1.065
C(uf_rede)[T.AP_Estadual]                    -0.2763   1.65e-14  -1.67e+13      0.000      -0.276      -0.276
C(uf_rede)[T.AP_Privada]                      1.1205      0.030     37.870      0.000       1.060       1.181
C(uf_rede)[T.BA_Estadual]                    -0.4437   1.65e-14  -2.69e+13      0.000      -0.444      -0.444
C(uf_rede)[T.BA_Privada]                      1.3570      0.030     45.861      0.000       1.296       1.418
C(uf_rede)[T.CE_Estadual]                     0.0215   1.67e-14   1.28e+12      0.000       0.021       0.021
C(uf_rede)[T.CE_Privada]                      1.3360      0.030     45.150      0.000       1.275       1.397
C(uf_rede)[T.DF_Estadual]                    -0.0844   1.65e-14  -5.12e+12      0.000      -0.084      -0.084
C(uf_rede)[T.DF_Privada]                      1.5143      0.030     51.178      0.000       1.453       1.575
C(uf_rede)[T.ES_Estadual]                     0.4171   1.67e-14    2.5e+13      0.000       0.417       0.417
C(uf_rede)[T.ES_Privada]                      1.4838      0.030     50.148      0.000       1.423       1.545
C(uf_rede)[T.GO_Estadual]                     0.4794   1.75e-14   2.73e+13      0.000       0.479       0.479
C(uf_rede)[T.GO_Privada]                      1.2480      0.030     42.177      0.000       1.187       1.309
C(uf_rede)[T.MA_Estadual]                    -0.4296   1.66e-14  -2.59e+13      0.000      -0.430      -0.430
C(uf_rede)[T.MA_Privada]                      1.1631      0.030     39.309      0.000       1.102       1.224
C(uf_rede)[T.MG_Estadual]                     0.1768   1.68e-14   1.05e+13      0.000       0.177       0.177
C(uf_rede)[T.MG_Privada]                      1.9148      0.030     64.714      0.000       1.854       1.976
C(uf_rede)[T.MS_Estadual]                     0.0077   1.72e-14   4.47e+11      0.000       0.008       0.008
C(uf_rede)[T.MS_Privada]                      1.5412      0.030     52.088      0.000       1.480       1.602
C(uf_rede)[T.MT_Estadual]                    -0.1212   1.65e-14  -7.33e+12      0.000      -0.121      -0.121
C(uf_rede)[T.MT_Privada]                      1.2595      0.030     42.567      0.000       1.199       1.320
C(uf_rede)[T.PA_Estadual]                    -0.0841   1.66e-14  -5.06e+12      0.000      -0.084      -0.084
C(uf_rede)[T.PA_Privada]                      1.1480      0.030     38.797      0.000       1.087       1.209
C(uf_rede)[T.PB_Estadual]                    -0.1389   1.74e-14  -7.97e+12      0.000      -0.139      -0.139
C(uf_rede)[T.PB_Privada]                      1.1856      0.030     40.069      0.000       1.125       1.246
C(uf_rede)[T.PE_Estadual]                     0.2661   1.67e-14   1.59e+13      0.000       0.266       0.266
C(uf_rede)[T.PE_Privada]                      1.3280      0.030     44.881      0.000       1.267       1.389
C(uf_rede)[T.PI_Estadual]                     0.1914   1.66e-14   1.15e+13      0.000       0.191       0.191
C(uf_rede)[T.PI_Privada]                      1.6267      0.030     54.975      0.000       1.566       1.687
C(uf_rede)[T.PR_Estadual]                     0.5276   1.66e-14   3.18e+13      0.000       0.528       0.528
C(uf_rede)[T.PR_Privada]                      1.5657      0.030     52.916      0.000       1.505       1.627
C(uf_rede)[T.RJ_Estadual]                    -0.4031   1.71e-14  -2.35e+13      0.000      -0.403      -0.403
C(uf_rede)[T.RJ_Privada]                      1.2129      0.030     40.991      0.000       1.152       1.274
C(uf_rede)[T.RN_Estadual]                    -0.3292   1.67e-14  -1.98e+13      0.000      -0.329      -0.329
C(uf_rede)[T.RN_Privada]                      1.2947      0.030     43.754      0.000       1.234       1.355
C(uf_rede)[T.RO_Estadual]                    -0.0490   1.66e-14  -2.94e+12      0.000      -0.049      -0.049
C(uf_rede)[T.RO_Privada]                      1.2400      0.030     41.907      0.000       1.179       1.301
C(uf_rede)[T.RR_Estadual]                    -0.3137    1.7e-14  -1.84e+13      0.000      -0.314      -0.314
C(uf_rede)[T.RR_Privada]                      1.0611      0.030     35.861      0.000       1.000       1.122
C(uf_rede)[T.RS_Estadual]                     0.4184   1.72e-14   2.44e+13      0.000       0.418       0.418
C(uf_rede)[T.RS_Privada]                      1.6291      0.030     55.057      0.000       1.568       1.690
C(uf_rede)[T.SC_Estadual]                     0.1969   1.65e-14   1.19e+13      0.000       0.197       0.197
C(uf_rede)[T.SC_Privada]                      1.6117      0.030     54.469      0.000       1.551       1.673
C(uf_rede)[T.SE_Estadual]                    -0.1979   1.68e-14  -1.18e+13      0.000      -0.198      -0.198
C(uf_rede)[T.SE_Privada]                      1.1513      0.030     38.911      0.000       1.091       1.212
C(uf_rede)[T.SP_Estadual]                     0.0855   1.86e-14    4.6e+12      0.000       0.085       0.085
C(uf_rede)[T.SP_Privada]                      1.5828      0.030     53.491      0.000       1.522       1.644
C(uf_rede)[T.TO_Estadual]                    -0.1716   1.78e-14  -9.63e+12      0.000      -0.172      -0.172
C(uf_rede)[T.TO_Privada]                      1.5738      0.030     53.189      0.000       1.513       1.635
C(ano, Treatment(reference=2023))[T.2025]     0.0085      0.053      0.161      0.874      -0.100       0.117
rede_publica:pos_pedemeia                     0.0810      0.059      1.368      0.183      -0.041       0.203
==============================================================================
Omnibus:                        1.446   Durbin-Watson:                   1.764
Prob(Omnibus):                  0.485   Jarque-Bera (JB):                0.967
Skew:                          -0.000   Prob(JB):                        0.617
Kurtosis:                       3.464   Cond. No.                         65.7
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
Pré-Tendência FE (UFxRede + Ano) — Nota Média Padronizada SAEB (N) (2019-2023, N=162)
====================================================================
                            OLS Regression Results                            
==============================================================================
Dep. Variable:        ideb_nota_media   R-squared:                       0.986
Model:                            OLS   Adj. R-squared:                  0.978
Method:                 Least Squares   F-statistic:                     1105.
Date:                Thu, 05 Nov 2026   Prob (F-statistic):           1.30e-28
Time:                        13:10:22   Log-Likelihood:                 149.97
No. Observations:                 162   AIC:                            -183.9
Df Residuals:                     104   BIC:                            -4.868
Df Model:                          57                                         
Covariance Type:              cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                     4.5073      0.021    217.461      0.000       4.465       4.550
C(uf_rede)[T.AC_Privada]                      1.7936      0.033     54.121      0.000       1.725       1.862
C(uf_rede)[T.AL_Estadual]                    -0.3130   6.04e-15  -5.18e+13      0.000      -0.313      -0.313
C(uf_rede)[T.AL_Privada]                      0.9540      0.033     28.788      0.000       0.886       1.022
C(uf_rede)[T.AM_Estadual]                    -0.3996   5.64e-15  -7.08e+13      0.000      -0.400      -0.400
C(uf_rede)[T.AM_Privada]                      1.1895      0.033     35.894      0.000       1.121       1.258
C(uf_rede)[T.AP_Estadual]                    -0.3142   8.93e-15  -3.52e+13      0.000      -0.314      -0.314
C(uf_rede)[T.AP_Privada]                      1.1304      0.033     34.109      0.000       1.062       1.198
C(uf_rede)[T.BA_Estadual]                    -0.4355   7.24e-15  -6.02e+13      0.000      -0.435      -0.435
C(uf_rede)[T.BA_Privada]                      1.6227      0.033     48.965      0.000       1.555       1.691
C(uf_rede)[T.CE_Estadual]                    -0.0086   5.93e-15  -1.45e+12      0.000      -0.009      -0.009
C(uf_rede)[T.CE_Privada]                      1.6270      0.033     49.094      0.000       1.559       1.695
C(uf_rede)[T.DF_Estadual]                     0.1490   5.83e-15   2.56e+13      0.000       0.149       0.149
C(uf_rede)[T.DF_Privada]                      1.9535      0.033     58.947      0.000       1.885       2.022
C(uf_rede)[T.ES_Estadual]                     0.4341   6.03e-15    7.2e+13      0.000       0.434       0.434
C(uf_rede)[T.ES_Privada]                      1.8395      0.033     55.507      0.000       1.771       1.908
C(uf_rede)[T.GO_Estadual]                     0.3635   7.38e-15   4.92e+13      0.000       0.363       0.363
C(uf_rede)[T.GO_Privada]                      1.5909      0.033     48.007      0.000       1.523       1.659
C(uf_rede)[T.MA_Estadual]                    -0.4610   6.26e-15  -7.36e+13      0.000      -0.461      -0.461
C(uf_rede)[T.MA_Privada]                      1.3758      0.033     41.516      0.000       1.308       1.444
C(uf_rede)[T.MG_Estadual]                     0.1741   6.06e-15   2.88e+13      0.000       0.174       0.174
C(uf_rede)[T.MG_Privada]                      2.1927      0.033     66.166      0.000       2.125       2.261
C(uf_rede)[T.MS_Estadual]                     0.1168    7.6e-15   1.54e+13      0.000       0.117       0.117
C(uf_rede)[T.MS_Privada]                      1.8337      0.033     55.334      0.000       1.766       1.902
C(uf_rede)[T.MT_Estadual]                    -0.1189   8.81e-15  -1.35e+13      0.000      -0.119      -0.119
C(uf_rede)[T.MT_Privada]                      1.6016      0.033     48.330      0.000       1.534       1.670
C(uf_rede)[T.PA_Estadual]                    -0.3819   8.81e-15  -4.34e+13      0.000      -0.382      -0.382
C(uf_rede)[T.PA_Privada]                      1.4240      0.033     42.969      0.000       1.356       1.492
C(uf_rede)[T.PB_Estadual]                    -0.1967   8.19e-15   -2.4e+13      0.000      -0.197      -0.197
C(uf_rede)[T.PB_Privada]                      1.4088      0.033     42.511      0.000       1.341       1.477
C(uf_rede)[T.PE_Estadual]                     0.2038   6.22e-15   3.28e+13      0.000       0.204       0.204
C(uf_rede)[T.PE_Privada]                      1.5551      0.033     46.925      0.000       1.487       1.623
C(uf_rede)[T.PI_Estadual]                    -0.1606   6.09e-15  -2.64e+13      0.000      -0.161      -0.161
C(uf_rede)[T.PI_Privada]                      1.9891      0.033     60.020      0.000       1.921       2.057
C(uf_rede)[T.PR_Estadual]                     0.3769   6.77e-15   5.56e+13      0.000       0.377       0.377
C(uf_rede)[T.PR_Privada]                      1.9683      0.033     59.394      0.000       1.900       2.036
C(uf_rede)[T.RJ_Estadual]                    -0.2058   6.33e-15  -3.25e+13      0.000      -0.206      -0.206
C(uf_rede)[T.RJ_Privada]                      1.3828      0.033     41.725      0.000       1.315       1.451
C(uf_rede)[T.RN_Estadual]                    -0.3768   5.65e-15  -6.67e+13      0.000      -0.377      -0.377
C(uf_rede)[T.RN_Privada]                      1.4271      0.033     43.063      0.000       1.359       1.495
C(uf_rede)[T.RO_Estadual]                     0.0715   6.32e-15   1.13e+13      0.000       0.071       0.071
C(uf_rede)[T.RO_Privada]                      1.5730      0.033     47.466      0.000       1.505       1.641
C(uf_rede)[T.RR_Estadual]                    -0.2248   5.83e-15  -3.85e+13      0.000      -0.225      -0.225
C(uf_rede)[T.RR_Privada]                      1.5354      0.033     46.330      0.000       1.467       1.603
C(uf_rede)[T.RS_Estadual]                     0.3228   6.19e-15   5.21e+13      0.000       0.323       0.323
C(uf_rede)[T.RS_Privada]                      1.7639      0.033     53.227      0.000       1.696       1.832
C(uf_rede)[T.SC_Estadual]                     0.2641   6.77e-15    3.9e+13      0.000       0.264       0.264
C(uf_rede)[T.SC_Privada]                      1.9331      0.033     58.331      0.000       1.865       2.001
C(uf_rede)[T.SE_Estadual]                    -0.2729   6.37e-15  -4.28e+13      0.000      -0.273      -0.273
C(uf_rede)[T.SE_Privada]                      1.4018      0.033     42.300      0.000       1.334       1.470
C(uf_rede)[T.SP_Estadual]                     0.1632   7.66e-15   2.13e+13      0.000       0.163       0.163
C(uf_rede)[T.SP_Privada]                      1.8659      0.033     56.303      0.000       1.798       1.934
C(uf_rede)[T.TO_Estadual]                    -0.1345   7.72e-15  -1.74e+13      0.000      -0.134      -0.134
C(uf_rede)[T.TO_Privada]                      1.9002      0.033     57.339      0.000       1.832       1.968
C(ano, Treatment(reference=2019))[T.2021]    -0.3429      0.050     -6.841      0.000      -0.446      -0.240
C(ano, Treatment(reference=2019))[T.2023]    -0.3662      0.047     -7.823      0.000      -0.462      -0.270
rede_publica:ano_2021                         0.2479      0.051      4.833      0.000       0.142       0.353
rede_publica:ano_2023                         0.3069      0.058      5.322      0.000       0.188       0.425
==============================================================================
Omnibus:                        0.581   Durbin-Watson:                   1.911
Prob(Omnibus):                  0.748   Jarque-Bera (JB):                0.422
Skew:                           0.123   Prob(JB):                        0.810
Kurtosis:                       3.040   Cond. No.                         64.1
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
DiD FE (UFxRede + Ano) Painel Completo — Indicador de Rendimento IDEB (P) (2019-2025, N=216)
====================================================================
                                OLS Regression Results                               
=====================================================================================
Dep. Variable:     ideb_indicador_rendimento   R-squared:                       0.776
Model:                                   OLS   Adj. R-squared:                  0.695
Method:                        Least Squares   F-statistic:                     282.3
Date:                       Thu, 05 Nov 2026   Prob (F-statistic):           5.21e-21
Time:                               13:10:22   Log-Likelihood:                 450.57
No. Observations:                        216   AIC:                            -785.1
Df Residuals:                            158   BIC:                            -589.4
Df Model:                                 57                                         
Covariance Type:                     cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                     0.8377      0.004    192.182      0.000       0.829       0.847
C(uf_rede)[T.AC_Privada]                      0.1183      0.003     42.304      0.000       0.113       0.124
C(uf_rede)[T.AL_Estadual]                     0.0444   1.64e-15    2.7e+13      0.000       0.044       0.044
C(uf_rede)[T.AL_Privada]                      0.1127      0.003     40.291      0.000       0.107       0.118
C(uf_rede)[T.AM_Estadual]                     0.0220   3.06e-15   7.18e+12      0.000       0.022       0.022
C(uf_rede)[T.AM_Privada]                      0.1143      0.003     40.883      0.000       0.109       0.120
C(uf_rede)[T.AP_Estadual]                    -0.0446   2.36e-15  -1.89e+13      0.000      -0.045      -0.045
C(uf_rede)[T.AP_Privada]                      0.1260      0.003     45.061      0.000       0.120       0.132
C(uf_rede)[T.BA_Estadual]                     0.0069   2.03e-15   3.38e+12      0.000       0.007       0.007
C(uf_rede)[T.BA_Privada]                      0.1036      0.003     37.061      0.000       0.098       0.109
C(uf_rede)[T.CE_Estadual]                     0.1024   1.75e-15   5.85e+13      0.000       0.102       0.102
C(uf_rede)[T.CE_Privada]                      0.1238      0.003     44.283      0.000       0.118       0.130
C(uf_rede)[T.DF_Estadual]                    -0.0315   1.86e-15  -1.69e+13      0.000      -0.032      -0.032
C(uf_rede)[T.DF_Privada]                      0.1179      0.003     42.162      0.000       0.112       0.124
C(uf_rede)[T.ES_Estadual]                     0.0782   1.77e-15   4.42e+13      0.000       0.078       0.078
C(uf_rede)[T.ES_Privada]                      0.1116      0.003     39.909      0.000       0.106       0.117
C(uf_rede)[T.GO_Estadual]                     0.1047   1.74e-15   6.01e+13      0.000       0.105       0.105
C(uf_rede)[T.GO_Privada]                      0.1203      0.003     43.036      0.000       0.115       0.126
C(uf_rede)[T.MA_Estadual]                     0.0435   1.72e-15   2.54e+13      0.000       0.044       0.044
C(uf_rede)[T.MA_Privada]                      0.0950      0.003     33.970      0.000       0.089       0.101
C(uf_rede)[T.MG_Estadual]                     0.0156   1.69e-15    9.2e+12      0.000       0.016       0.016
C(uf_rede)[T.MG_Privada]                      0.0850      0.003     30.397      0.000       0.079       0.091
C(uf_rede)[T.MS_Estadual]                    -0.0024   1.81e-15  -1.31e+12      0.000      -0.002      -0.002
C(uf_rede)[T.MS_Privada]                      0.1208      0.003     43.199      0.000       0.115       0.127
C(uf_rede)[T.MT_Estadual]                     0.0228   1.65e-15   1.38e+13      0.000       0.023       0.023
C(uf_rede)[T.MT_Privada]                      0.1256      0.003     44.915      0.000       0.120       0.131
C(uf_rede)[T.PA_Estadual]                     0.0141   1.64e-15   8.59e+12      0.000       0.014       0.014
C(uf_rede)[T.PA_Privada]                      0.1256      0.003     44.916      0.000       0.120       0.131
C(uf_rede)[T.PB_Estadual]                     0.0199    2.1e-15   9.46e+12      0.000       0.020       0.020
C(uf_rede)[T.PB_Privada]                      0.1114      0.003     39.839      0.000       0.106       0.117
C(uf_rede)[T.PE_Estadual]                     0.0902   1.69e-15   5.34e+13      0.000       0.090       0.090
C(uf_rede)[T.PE_Privada]                      0.1218      0.003     43.565      0.000       0.116       0.128
C(uf_rede)[T.PI_Estadual]                     0.0791   1.87e-15   4.22e+13      0.000       0.079       0.079
C(uf_rede)[T.PI_Privada]                      0.1116      0.003     39.912      0.000       0.106       0.117
C(uf_rede)[T.PR_Estadual]                     0.0838   1.66e-15   5.04e+13      0.000       0.084       0.084
C(uf_rede)[T.PR_Privada]                      0.1280      0.003     45.761      0.000       0.122       0.134
C(uf_rede)[T.RJ_Estadual]                    -0.0089   1.88e-15  -4.74e+12      0.000      -0.009      -0.009
C(uf_rede)[T.RJ_Privada]                      0.0538      0.003     19.227      0.000       0.048       0.060
C(uf_rede)[T.RN_Estadual]                    -0.0719   1.64e-15  -4.38e+13      0.000      -0.072      -0.072
C(uf_rede)[T.RN_Privada]                      0.1122      0.003     40.137      0.000       0.106       0.118
C(uf_rede)[T.RO_Estadual]                     0.0218   1.66e-15   1.31e+13      0.000       0.022       0.022
C(uf_rede)[T.RO_Privada]                      0.0987      0.003     35.282      0.000       0.093       0.104
C(uf_rede)[T.RR_Estadual]                    -0.0088   1.69e-15   -5.2e+12      0.000      -0.009      -0.009
C(uf_rede)[T.RR_Privada]                      0.1156      0.003     41.360      0.000       0.110       0.121
C(uf_rede)[T.RS_Estadual]                    -0.0139   1.72e-15  -8.09e+12      0.000      -0.014      -0.014
C(uf_rede)[T.RS_Privada]                      0.1116      0.003     39.902      0.000       0.106       0.117
C(uf_rede)[T.SC_Estadual]                    -0.0539   1.66e-15  -3.25e+13      0.000      -0.054      -0.054
C(uf_rede)[T.SC_Privada]                      0.1177      0.003     42.101      0.000       0.112       0.123
C(uf_rede)[T.SE_Estadual]                     0.0204   1.69e-15    1.2e+13      0.000       0.020       0.020
C(uf_rede)[T.SE_Privada]                      0.1178      0.003     42.132      0.000       0.112       0.124
C(uf_rede)[T.SP_Estadual]                     0.0600    1.9e-15   3.17e+13      0.000       0.060       0.060
C(uf_rede)[T.SP_Privada]                      0.1285      0.003     45.963      0.000       0.123       0.134
C(uf_rede)[T.TO_Estadual]                     0.0742   1.67e-15   4.43e+13      0.000       0.074       0.074
C(uf_rede)[T.TO_Privada]                      0.1181      0.003     42.233      0.000       0.112       0.124
C(ano, Treatment(reference=2019))[T.2021]     0.0209      0.006      3.270      0.003       0.008       0.034
C(ano, Treatment(reference=2019))[T.2023]     0.0284      0.007      4.001      0.000       0.014       0.043
C(ano, Treatment(reference=2019))[T.2025]     0.0272      0.004      6.532      0.000       0.019       0.036
rede_publica:pos_pedemeia                     0.0517      0.011      4.623      0.000       0.029       0.075
==============================================================================
Omnibus:                       33.867   Durbin-Watson:                   2.059
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              129.554
Skew:                          -0.528   Prob(JB):                     7.37e-29
Kurtosis:                       6.644   Cond. No.                         60.7
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
DiD FE (UFxRede + Ano) Janela Imediata — Indicador de Rendimento IDEB (P) (2023 vs 2025, N=108)
====================================================================
                                OLS Regression Results                               
=====================================================================================
Dep. Variable:     ideb_indicador_rendimento   R-squared:                       0.865
Model:                                   OLS   Adj. R-squared:                  0.722
Method:                        Least Squares   F-statistic:                     111.7
Date:                       Thu, 05 Nov 2026   Prob (F-statistic):           1.72e-13
Time:                               13:10:22   Log-Likelihood:                 280.63
No. Observations:                        108   AIC:                            -449.3
Df Residuals:                             52   BIC:                            -299.1
Df Model:                                 55                                         
Covariance Type:                     cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                     0.8677      0.006    137.720      0.000       0.855       0.881
C(uf_rede)[T.AC_Privada]                      0.0984      0.006     15.439      0.000       0.085       0.111
C(uf_rede)[T.AL_Estadual]                     0.0756   2.48e-15   3.05e+13      0.000       0.076       0.076
C(uf_rede)[T.AL_Privada]                      0.0985      0.006     15.467      0.000       0.085       0.112
C(uf_rede)[T.AM_Estadual]                     0.0077   2.45e-15   3.16e+12      0.000       0.008       0.008
C(uf_rede)[T.AM_Privada]                      0.1033      0.006     16.215      0.000       0.090       0.116
C(uf_rede)[T.AP_Estadual]                    -0.0097   2.46e-15  -3.94e+12      0.000      -0.010      -0.010
C(uf_rede)[T.AP_Privada]                      0.1113      0.006     17.472      0.000       0.098       0.124
C(uf_rede)[T.BA_Estadual]                     0.0359   2.59e-15   1.39e+13      0.000       0.036       0.036
C(uf_rede)[T.BA_Privada]                      0.0980      0.006     15.378      0.000       0.085       0.111
C(uf_rede)[T.CE_Estadual]                     0.0938   2.43e-15   3.86e+13      0.000       0.094       0.094
C(uf_rede)[T.CE_Privada]                      0.1107      0.006     17.381      0.000       0.098       0.124
C(uf_rede)[T.DF_Estadual]                    -0.0532   2.37e-15  -2.24e+13      0.000      -0.053      -0.053
C(uf_rede)[T.DF_Privada]                      0.0994      0.006     15.597      0.000       0.086       0.112
C(uf_rede)[T.ES_Estadual]                     0.0921   2.37e-15   3.88e+13      0.000       0.092       0.092
C(uf_rede)[T.ES_Privada]                      0.1001      0.006     15.717      0.000       0.087       0.113
C(uf_rede)[T.GO_Estadual]                     0.1004   2.38e-15   4.21e+13      0.000       0.100       0.100
C(uf_rede)[T.GO_Privada]                      0.1081      0.006     16.962      0.000       0.095       0.121
C(uf_rede)[T.MA_Estadual]                     0.0423   2.35e-15    1.8e+13      0.000       0.042       0.042
C(uf_rede)[T.MA_Privada]                      0.0758      0.006     11.896      0.000       0.063       0.089
C(uf_rede)[T.MG_Estadual]                     0.0266   2.28e-15   1.16e+13      0.000       0.027       0.027
C(uf_rede)[T.MG_Privada]                      0.0392      0.006      6.145      0.000       0.026       0.052
C(uf_rede)[T.MS_Estadual]                     0.0059   2.47e-15    2.4e+12      0.000       0.006       0.006
C(uf_rede)[T.MS_Privada]                      0.1048      0.006     16.455      0.000       0.092       0.118
C(uf_rede)[T.MT_Estadual]                     0.0974   2.39e-15   4.07e+13      0.000       0.097       0.097
C(uf_rede)[T.MT_Privada]                      0.1111      0.006     17.437      0.000       0.098       0.124
C(uf_rede)[T.PA_Estadual]                     0.1048   2.37e-15   4.42e+13      0.000       0.105       0.105
C(uf_rede)[T.PA_Privada]                      0.1071      0.006     16.813      0.000       0.094       0.120
C(uf_rede)[T.PB_Estadual]                     0.0015    2.4e-15   6.32e+11      0.000       0.002       0.002
C(uf_rede)[T.PB_Privada]                      0.0929      0.006     14.578      0.000       0.080       0.106
C(uf_rede)[T.PE_Estadual]                     0.0856   2.38e-15    3.6e+13      0.000       0.086       0.086
C(uf_rede)[T.PE_Privada]                      0.1075      0.006     16.866      0.000       0.094       0.121
C(uf_rede)[T.PI_Estadual]                     0.0954   2.39e-15   3.98e+13      0.000       0.095       0.095
C(uf_rede)[T.PI_Privada]                      0.0977      0.006     15.332      0.000       0.085       0.111
C(uf_rede)[T.PR_Estadual]                     0.0911   2.37e-15   3.84e+13      0.000       0.091       0.091
C(uf_rede)[T.PR_Privada]                      0.1120      0.006     17.572      0.000       0.099       0.125
C(uf_rede)[T.RJ_Estadual]                    -0.0221   2.51e-15   -8.8e+12      0.000      -0.022      -0.022
C(uf_rede)[T.RJ_Privada]                      0.0693      0.006     10.877      0.000       0.056       0.082
C(uf_rede)[T.RN_Estadual]                    -0.0335   2.39e-15   -1.4e+13      0.000      -0.033      -0.033
C(uf_rede)[T.RN_Privada]                      0.1000      0.006     15.703      0.000       0.087       0.113
C(uf_rede)[T.RO_Estadual]                     0.0234   2.39e-15   9.76e+12      0.000       0.023       0.023
C(uf_rede)[T.RO_Privada]                      0.0926      0.006     14.535      0.000       0.080       0.106
C(uf_rede)[T.RR_Estadual]                    -0.0111   2.39e-15  -4.66e+12      0.000      -0.011      -0.011
C(uf_rede)[T.RR_Privada]                      0.0923      0.006     14.487      0.000       0.079       0.105
C(uf_rede)[T.RS_Estadual]                    -0.0110   2.41e-15  -4.57e+12      0.000      -0.011      -0.011
C(uf_rede)[T.RS_Privada]                      0.1005      0.006     15.770      0.000       0.087       0.114
C(uf_rede)[T.SC_Estadual]                    -0.0224   2.37e-15  -9.47e+12      0.000      -0.022      -0.022
C(uf_rede)[T.SC_Privada]                      0.1025      0.006     16.086      0.000       0.089       0.116
C(uf_rede)[T.SE_Estadual]                     0.0312   2.37e-15   1.32e+13      0.000       0.031       0.031
C(uf_rede)[T.SE_Privada]                      0.1048      0.006     16.453      0.000       0.092       0.118
C(uf_rede)[T.SP_Estadual]                     0.0481   2.41e-15   1.99e+13      0.000       0.048       0.048
C(uf_rede)[T.SP_Privada]                      0.1135      0.006     17.819      0.000       0.100       0.127
C(uf_rede)[T.TO_Estadual]                     0.0754   2.64e-15   2.86e+13      0.000       0.075       0.075
C(uf_rede)[T.TO_Privada]                      0.1086      0.006     17.048      0.000       0.096       0.122
C(ano, Treatment(reference=2023))[T.2025]     0.0116      0.007      1.700      0.101      -0.002       0.026
rede_publica:pos_pedemeia                     0.0261      0.013      2.051      0.050   -6.04e-05       0.052
==============================================================================
Omnibus:                       13.704   Durbin-Watson:                   1.831
Prob(Omnibus):                  0.001   Jarque-Bera (JB):               47.881
Skew:                           0.000   Prob(JB):                     4.01e-11
Kurtosis:                       6.262   Cond. No.                         65.7
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
Pré-Tendência FE (UFxRede + Ano) — Indicador de Rendimento IDEB (P) (2019-2023, N=162)
====================================================================
                                OLS Regression Results                               
=====================================================================================
Dep. Variable:     ideb_indicador_rendimento   R-squared:                       0.829
Model:                                   OLS   Adj. R-squared:                  0.736
Method:                        Least Squares   F-statistic:                     76.60
Date:                       Thu, 05 Nov 2026   Prob (F-statistic):           5.32e-14
Time:                               13:10:22   Log-Likelihood:                 348.91
No. Observations:                        162   AIC:                            -581.8
Df Residuals:                            104   BIC:                            -402.7
Df Model:                                 57                                         
Covariance Type:                     cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                     0.8328      0.007    117.257      0.000       0.818       0.847
C(uf_rede)[T.AC_Privada]                      0.1383      0.008     16.423      0.000       0.121       0.156
C(uf_rede)[T.AL_Estadual]                     0.0331   1.16e-15   2.87e+13      0.000       0.033       0.033
C(uf_rede)[T.AL_Privada]                      0.1305      0.008     15.492      0.000       0.113       0.148
C(uf_rede)[T.AM_Estadual]                     0.0294   1.15e-15   2.57e+13      0.000       0.029       0.029
C(uf_rede)[T.AM_Privada]                      0.1305      0.008     15.493      0.000       0.113       0.148
C(uf_rede)[T.AP_Estadual]                    -0.0612    1.8e-15  -3.39e+13      0.000      -0.061      -0.061
C(uf_rede)[T.AP_Privada]                      0.1447      0.008     17.173      0.000       0.127       0.162
C(uf_rede)[T.BA_Estadual]                    -0.0038   1.46e-15  -2.58e+12      0.000      -0.004      -0.004
C(uf_rede)[T.BA_Privada]                      0.1182      0.008     14.028      0.000       0.101       0.135
C(uf_rede)[T.CE_Estadual]                     0.1075   1.24e-15   8.69e+13      0.000       0.107       0.107
C(uf_rede)[T.CE_Privada]                      0.1416      0.008     16.808      0.000       0.124       0.159
C(uf_rede)[T.DF_Estadual]                    -0.0182   1.16e-15  -1.57e+13      0.000      -0.018      -0.018
C(uf_rede)[T.DF_Privada]                      0.1365      0.008     16.201      0.000       0.119       0.154
C(uf_rede)[T.ES_Estadual]                     0.0729   1.21e-15   6.03e+13      0.000       0.073       0.073
C(uf_rede)[T.ES_Privada]                      0.1312      0.008     15.575      0.000       0.114       0.149
C(uf_rede)[T.GO_Estadual]                     0.1091   1.37e-15   7.96e+13      0.000       0.109       0.109
C(uf_rede)[T.GO_Privada]                      0.1378      0.008     16.363      0.000       0.121       0.155
C(uf_rede)[T.MA_Estadual]                     0.0453   1.23e-15   3.68e+13      0.000       0.045       0.045
C(uf_rede)[T.MA_Privada]                      0.1077      0.008     12.780      0.000       0.090       0.125
C(uf_rede)[T.MG_Estadual]                     0.0007   1.15e-15   6.29e+11      0.000       0.001       0.001
C(uf_rede)[T.MG_Privada]                      0.0947      0.008     11.239      0.000       0.077       0.112
C(uf_rede)[T.MS_Estadual]                    -0.0169   1.55e-15  -1.09e+13      0.000      -0.017      -0.017
C(uf_rede)[T.MS_Privada]                      0.1395      0.008     16.556      0.000       0.122       0.157
C(uf_rede)[T.MT_Estadual]                    -0.0027   1.47e-15  -1.83e+12      0.000      -0.003      -0.003
C(uf_rede)[T.MT_Privada]                      0.1442      0.008     17.114      0.000       0.127       0.161
C(uf_rede)[T.PA_Estadual]                    -0.0139    1.8e-15  -7.71e+12      0.000      -0.014      -0.014
C(uf_rede)[T.PA_Privada]                      0.1457      0.008     17.298      0.000       0.128       0.163
C(uf_rede)[T.PB_Estadual]                     0.0129   1.58e-15   8.19e+12      0.000       0.013       0.013
C(uf_rede)[T.PB_Privada]                      0.1302      0.008     15.459      0.000       0.113       0.148
C(uf_rede)[T.PE_Estadual]                     0.0914   1.31e-15   6.97e+13      0.000       0.091       0.091
C(uf_rede)[T.PE_Privada]                      0.1415      0.008     16.798      0.000       0.124       0.159
C(uf_rede)[T.PI_Estadual]                     0.0720    1.2e-15   5.99e+13      0.000       0.072       0.072
C(uf_rede)[T.PI_Privada]                      0.1299      0.008     15.422      0.000       0.113       0.147
C(uf_rede)[T.PR_Estadual]                     0.0817   1.38e-15   5.91e+13      0.000       0.082       0.082
C(uf_rede)[T.PR_Privada]                      0.1475      0.008     17.504      0.000       0.130       0.165
C(uf_rede)[T.RJ_Estadual]                    -0.0208   1.33e-15  -1.56e+13      0.000      -0.021      -0.021
C(uf_rede)[T.RJ_Privada]                      0.0563      0.008      6.687      0.000       0.039       0.074
C(uf_rede)[T.RN_Estadual]                    -0.1106   1.25e-15  -8.85e+13      0.000      -0.111      -0.111
C(uf_rede)[T.RN_Privada]                      0.1292      0.008     15.333      0.000       0.112       0.146
C(uf_rede)[T.RO_Estadual]                     0.0233   1.24e-15   1.88e+13      0.000       0.023       0.023
C(uf_rede)[T.RO_Privada]                      0.1127      0.008     13.381      0.000       0.095       0.130
C(uf_rede)[T.RR_Estadual]                    -0.0054   1.19e-15  -4.53e+12      0.000      -0.005      -0.005
C(uf_rede)[T.RR_Privada]                      0.1393      0.008     16.537      0.000       0.122       0.157
C(uf_rede)[T.RS_Estadual]                    -0.0300   1.15e-15  -2.61e+13      0.000      -0.030      -0.030
C(uf_rede)[T.RS_Privada]                      0.1282      0.008     15.215      0.000       0.111       0.145
C(uf_rede)[T.SC_Estadual]                    -0.0738   1.16e-15  -6.36e+13      0.000      -0.074      -0.074
C(uf_rede)[T.SC_Privada]                      0.1372      0.008     16.281      0.000       0.120       0.154
C(uf_rede)[T.SE_Estadual]                     0.0104   1.18e-15   8.78e+12      0.000       0.010       0.010
C(uf_rede)[T.SE_Privada]                      0.1368      0.008     16.244      0.000       0.120       0.154
C(uf_rede)[T.SP_Estadual]                     0.0634   1.44e-15   4.39e+13      0.000       0.063       0.063
C(uf_rede)[T.SP_Privada]                      0.1469      0.008     17.434      0.000       0.130       0.164
C(uf_rede)[T.TO_Estadual]                     0.0760   1.46e-15    5.2e+13      0.000       0.076       0.076
C(uf_rede)[T.TO_Privada]                      0.1338      0.008     15.887      0.000       0.117       0.151
C(ano, Treatment(reference=2019))[T.2021]     0.0093      0.008      1.131      0.268      -0.008       0.026
C(ano, Treatment(reference=2019))[T.2023]     0.0034      0.006      0.572      0.572      -0.009       0.016
rede_publica:ano_2021                         0.0233      0.019      1.233      0.228      -0.015       0.062
rede_publica:ano_2023                         0.0500      0.013      3.719      0.001       0.022       0.078
==============================================================================
Omnibus:                       22.619   Durbin-Watson:                   1.965
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              116.525
Skew:                           0.143   Prob(JB):                     4.98e-26
Kurtosis:                       7.145   Cond. No.                         64.1
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
DiD FE (UFxRede + Ano) Painel Completo — IDEB Observado (N x P) (2019-2025, N=216)
====================================================================
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         ideb_observado   R-squared:                       0.954
Model:                            OLS   Adj. R-squared:                  0.938
Method:                 Least Squares   F-statistic:                     1890.
Date:                Thu, 05 Nov 2026   Prob (F-statistic):           1.26e-31
Time:                        13:10:22   Log-Likelihood:                 37.543
No. Observations:                 216   AIC:                             40.91
Df Residuals:                     158   BIC:                             236.7
Df Model:                          57                                         
Covariance Type:              cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                     3.8522      0.031    123.045      0.000       3.788       3.917
C(uf_rede)[T.AC_Privada]                      2.0031      0.018    109.580      0.000       1.966       2.041
C(uf_rede)[T.AL_Estadual]                    -0.0500   8.49e-15  -5.89e+12      0.000      -0.050      -0.050
C(uf_rede)[T.AL_Privada]                      1.2781      0.018     69.919      0.000       1.241       1.316
C(uf_rede)[T.AM_Estadual]                    -0.2500   1.62e-14  -1.54e+13      0.000      -0.250      -0.250
C(uf_rede)[T.AM_Privada]                      1.5281      0.018     83.595      0.000       1.491       1.566
C(uf_rede)[T.AP_Estadual]                    -0.4750    9.8e-15  -4.85e+13      0.000      -0.475      -0.475
C(uf_rede)[T.AP_Privada]                      1.6281      0.018     89.066      0.000       1.591       1.666
C(uf_rede)[T.BA_Estadual]                    -0.3250   1.09e-14  -2.99e+13      0.000      -0.325      -0.325
C(uf_rede)[T.BA_Privada]                      1.8281      0.018    100.007      0.000       1.791       1.866
C(uf_rede)[T.CE_Estadual]                     0.5000   8.32e-15   6.01e+13      0.000       0.500       0.500
C(uf_rede)[T.CE_Privada]                      1.9781      0.018    108.213      0.000       1.941       2.016
C(uf_rede)[T.DF_Estadual]                    -0.0500   1.04e-14   -4.8e+12      0.000      -0.050      -0.050
C(uf_rede)[T.DF_Privada]                      2.2031      0.018    120.521      0.000       2.166       2.241
C(uf_rede)[T.ES_Estadual]                     0.7750   7.78e-15   9.96e+13      0.000       0.775       0.775
C(uf_rede)[T.ES_Privada]                      2.0781      0.018    113.683      0.000       2.041       2.116
C(uf_rede)[T.GO_Estadual]                     0.8500   9.15e-15   9.29e+13      0.000       0.850       0.850
C(uf_rede)[T.GO_Privada]                      1.9281      0.018    105.477      0.000       1.891       1.966
C(uf_rede)[T.MA_Estadual]                    -0.2000    8.9e-15  -2.25e+13      0.000      -0.200      -0.200
C(uf_rede)[T.MA_Privada]                      1.5531      0.018     84.963      0.000       1.516       1.591
C(uf_rede)[T.MG_Estadual]                     0.2500   7.87e-15   3.18e+13      0.000       0.250       0.250
C(uf_rede)[T.MG_Privada]                      2.2781      0.018    124.624      0.000       2.241       2.316
C(uf_rede)[T.MS_Estadual]                     0.0750   7.81e-15   9.61e+12      0.000       0.075       0.075
C(uf_rede)[T.MS_Privada]                      2.1531      0.018    117.786      0.000       2.116       2.191
C(uf_rede)[T.MT_Estadual]                 -6.292e-15   7.67e-15     -0.821      0.419   -2.21e-14    9.47e-15
C(uf_rede)[T.MT_Privada]                      1.9281      0.018    105.477      0.000       1.891       1.966
C(uf_rede)[T.PA_Estadual]                    -0.1500   7.89e-15   -1.9e+13      0.000      -0.150      -0.150
C(uf_rede)[T.PA_Privada]                      1.8031      0.018     98.639      0.000       1.766       1.841
C(uf_rede)[T.PB_Estadual]                    -0.0750   9.19e-15  -8.16e+12      0.000      -0.075      -0.075
C(uf_rede)[T.PB_Privada]                      1.7281      0.018     94.536      0.000       1.691       1.766
C(uf_rede)[T.PE_Estadual]                     0.6250   7.87e-15   7.94e+13      0.000       0.625       0.625
C(uf_rede)[T.PE_Privada]                      1.9031      0.018    104.110      0.000       1.866       1.941
C(uf_rede)[T.PI_Estadual]                     0.3500   9.16e-15   3.82e+13      0.000       0.350       0.350
C(uf_rede)[T.PI_Privada]                      2.2031      0.018    120.521      0.000       2.166       2.241
C(uf_rede)[T.PR_Estadual]                     0.8250   7.81e-15   1.06e+14      0.000       0.825       0.825
C(uf_rede)[T.PR_Privada]                      2.2781      0.018    124.624      0.000       2.241       2.316
C(uf_rede)[T.RJ_Estadual]                    -0.2750   7.72e-15  -3.56e+13      0.000      -0.275      -0.275
C(uf_rede)[T.RJ_Privada]                      1.4031      0.018     76.757      0.000       1.366       1.441
C(uf_rede)[T.RN_Estadual]                    -0.6000      8e-15   -7.5e+13      0.000      -0.600      -0.600
C(uf_rede)[T.RN_Privada]                      1.8031      0.018     98.639      0.000       1.766       1.841
C(uf_rede)[T.RO_Estadual]                     0.1000    7.7e-15    1.3e+13      0.000       0.100       0.100
C(uf_rede)[T.RO_Privada]                      1.7781      0.018     97.271      0.000       1.741       1.816
C(uf_rede)[T.RR_Estadual]                    -0.2500   7.95e-15  -3.15e+13      0.000      -0.250      -0.250
C(uf_rede)[T.RR_Privada]                      1.8031      0.018     98.639      0.000       1.766       1.841
C(uf_rede)[T.RS_Estadual]                     0.3000   7.67e-15   3.91e+13      0.000       0.300       0.300
C(uf_rede)[T.RS_Privada]                      2.1531      0.018    117.786      0.000       2.116       2.191
C(uf_rede)[T.SC_Estadual]                 -5.881e-15   7.74e-15     -0.760      0.454   -2.18e-14       1e-14
C(uf_rede)[T.SC_Privada]                      2.2281      0.018    121.889      0.000       2.191       2.266
C(uf_rede)[T.SE_Estadual]                    -0.1250    7.9e-15  -1.58e+13      0.000      -0.125      -0.125
C(uf_rede)[T.SE_Privada]                      1.7531      0.018     95.904      0.000       1.716       1.791
C(uf_rede)[T.SP_Estadual]                     0.4250   7.92e-15   5.37e+13      0.000       0.425       0.425
C(uf_rede)[T.SP_Privada]                      2.2531      0.018    123.257      0.000       2.216       2.291
C(uf_rede)[T.TO_Estadual]                     0.1750   7.67e-15   2.28e+13      0.000       0.175       0.175
C(uf_rede)[T.TO_Privada]                      2.2031      0.018    120.521      0.000       2.166       2.241
C(ano, Treatment(reference=2019))[T.2021]    -0.1130      0.041     -2.746      0.011      -0.198      -0.028
C(ano, Treatment(reference=2019))[T.2023]    -0.0796      0.048     -1.647      0.112      -0.179       0.020
C(ano, Treatment(reference=2019))[T.2025]    -0.1284      0.047     -2.713      0.012      -0.226      -0.031
rede_publica:pos_pedemeia                     0.4123      0.073      5.639      0.000       0.262       0.563
==============================================================================
Omnibus:                        9.933   Durbin-Watson:                   2.063
Prob(Omnibus):                  0.007   Jarque-Bera (JB):               15.511
Skew:                          -0.257   Prob(JB):                     0.000428
Kurtosis:                       4.208   Cond. No.                         60.7
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
DiD FE (UFxRede + Ano) Janela Imediata — IDEB Observado (N x P) (2023 vs 2025, N=108)
====================================================================
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         ideb_observado   R-squared:                       0.981
Model:                            OLS   Adj. R-squared:                  0.962
Method:                 Least Squares   F-statistic:                     1420.
Date:                Thu, 05 Nov 2026   Prob (F-statistic):           2.82e-27
Time:                        13:10:23   Log-Likelihood:                 82.052
No. Observations:                 108   AIC:                            -52.10
Df Residuals:                      52   BIC:                             98.09
Df Model:                          55                                         
Covariance Type:              cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                     3.8259      0.033    117.476      0.000       3.759       3.893
C(uf_rede)[T.AC_Privada]                      1.6407      0.033     49.150      0.000       1.572       1.709
C(uf_rede)[T.AL_Estadual]                     0.1500   2.48e-14   6.05e+12      0.000       0.150       0.150
C(uf_rede)[T.AL_Privada]                      1.1907      0.033     35.670      0.000       1.122       1.259
C(uf_rede)[T.AM_Estadual]                    -0.2500    2.2e-14  -1.14e+13      0.000      -0.250      -0.250
C(uf_rede)[T.AM_Privada]                      1.4407      0.033     43.159      0.000       1.372       1.509
C(uf_rede)[T.AP_Estadual]                    -0.3000   2.24e-14  -1.34e+13      0.000      -0.300      -0.300
C(uf_rede)[T.AP_Privada]                      1.6407      0.033     49.150      0.000       1.572       1.709
C(uf_rede)[T.BA_Estadual]                    -0.2000   2.37e-14  -8.42e+12      0.000      -0.200      -0.200
C(uf_rede)[T.BA_Privada]                      1.7407      0.033     52.145      0.000       1.672       1.809
C(uf_rede)[T.CE_Estadual]                     0.5000   2.34e-14   2.14e+13      0.000       0.500       0.500
C(uf_rede)[T.CE_Privada]                      1.8407      0.033     55.141      0.000       1.772       1.909
C(uf_rede)[T.DF_Estadual]                    -0.3000    2.2e-14  -1.36e+13      0.000      -0.300      -0.300
C(uf_rede)[T.DF_Privada]                      1.9407      0.033     58.136      0.000       1.872       2.009
C(uf_rede)[T.ES_Estadual]                     0.8500   2.19e-14   3.87e+13      0.000       0.850       0.850
C(uf_rede)[T.ES_Privada]                      1.8907      0.033     56.639      0.000       1.822       1.959
C(uf_rede)[T.GO_Estadual]                     0.9000   2.37e-14   3.79e+13      0.000       0.900       0.900
C(uf_rede)[T.GO_Privada]                      1.6907      0.033     50.647      0.000       1.622       1.759
C(uf_rede)[T.MA_Estadual]                    -0.2000    2.2e-14   -9.1e+12      0.000      -0.200      -0.200
C(uf_rede)[T.MA_Privada]                      1.4407      0.033     43.159      0.000       1.372       1.509
C(uf_rede)[T.MG_Estadual]                     0.3000   2.53e-14   1.19e+13      0.000       0.300       0.300
C(uf_rede)[T.MG_Privada]                      1.8907      0.033     56.639      0.000       1.822       1.959
C(uf_rede)[T.MS_Estadual]                     0.0500    2.4e-14   2.09e+12      0.000       0.050       0.050
C(uf_rede)[T.MS_Privada]                      1.9907      0.033     59.634      0.000       1.922       2.059
C(uf_rede)[T.MT_Estadual]                     0.3000   2.21e-14   1.36e+13      0.000       0.300       0.300
C(uf_rede)[T.MT_Privada]                      1.7407      0.033     52.145      0.000       1.672       1.809
C(uf_rede)[T.PA_Estadual]                     0.4000   2.31e-14   1.73e+13      0.000       0.400       0.400
C(uf_rede)[T.PA_Privada]                      1.6407      0.033     49.150      0.000       1.572       1.709
C(uf_rede)[T.PB_Estadual]                    -0.1000   2.52e-14  -3.98e+12      0.000      -0.100      -0.100
C(uf_rede)[T.PB_Privada]                      1.5407      0.033     46.154      0.000       1.472       1.609
C(uf_rede)[T.PE_Estadual]                     0.6500   2.33e-14   2.79e+13      0.000       0.650       0.650
C(uf_rede)[T.PE_Privada]                      1.7407      0.033     52.145      0.000       1.672       1.809
C(uf_rede)[T.PI_Estadual]                     0.6500   2.25e-14   2.89e+13      0.000       0.650       0.650
C(uf_rede)[T.PI_Privada]                      1.9907      0.033     59.634      0.000       1.922       2.059
C(uf_rede)[T.PR_Estadual]                     0.9500   2.26e-14   4.21e+13      0.000       0.950       0.950
C(uf_rede)[T.PR_Privada]                      2.0407      0.033     61.132      0.000       1.972       2.109
C(uf_rede)[T.RJ_Estadual]                    -0.4500   2.47e-14  -1.82e+13      0.000      -0.450      -0.450
C(uf_rede)[T.RJ_Privada]                      1.4407      0.033     43.159      0.000       1.372       1.509
C(uf_rede)[T.RN_Estadual]                    -0.4000   2.29e-14  -1.75e+13      0.000      -0.400      -0.400
C(uf_rede)[T.RN_Privada]                      1.7407      0.033     52.145      0.000       1.672       1.809
C(uf_rede)[T.RO_Estadual]                     0.0500   2.16e-14   2.31e+12      0.000       0.050       0.050
C(uf_rede)[T.RO_Privada]                      1.6407      0.033     49.150      0.000       1.572       1.709
C(uf_rede)[T.RR_Estadual]                    -0.3000   2.31e-14   -1.3e+13      0.000      -0.300      -0.300
C(uf_rede)[T.RR_Privada]                      1.4407      0.033     43.159      0.000       1.372       1.509
C(uf_rede)[T.RS_Estadual]                     0.3500   2.43e-14   1.44e+13      0.000       0.350       0.350
C(uf_rede)[T.RS_Privada]                      2.0407      0.033     61.132      0.000       1.972       2.109
C(uf_rede)[T.SC_Estadual]                     0.1000    2.2e-14   4.55e+12      0.000       0.100       0.100
C(uf_rede)[T.SC_Privada]                      2.0407      0.033     61.132      0.000       1.972       2.109
C(uf_rede)[T.SE_Estadual]                    -0.0500   2.33e-14  -2.15e+12      0.000      -0.050      -0.050
C(uf_rede)[T.SE_Privada]                      1.5907      0.033     47.652      0.000       1.522       1.659
C(uf_rede)[T.SP_Estadual]                     0.3000   2.38e-14   1.26e+13      0.000       0.300       0.300
C(uf_rede)[T.SP_Privada]                      2.0907      0.033     62.630      0.000       2.022       2.159
C(uf_rede)[T.TO_Estadual]                     0.1500   2.54e-14   5.92e+12      0.000       0.150       0.150
C(uf_rede)[T.TO_Privada]                      2.0407      0.033     61.132      0.000       1.972       2.109
C(ano, Treatment(reference=2023))[T.2025]     0.0667      0.062      1.072      0.294      -0.061       0.195
rede_publica:pos_pedemeia                     0.1815      0.067      2.718      0.012       0.044       0.319
==============================================================================
Omnibus:                        0.087   Durbin-Watson:                   1.667
Prob(Omnibus):                  0.957   Jarque-Bera (JB):                0.000
Skew:                           0.000   Prob(JB):                         1.00
Kurtosis:                       2.993   Cond. No.                         65.7
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)

====================================================================
Pré-Tendência FE (UFxRede + Ano) — IDEB Observado (N x P) (2019-2023, N=162)
====================================================================
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         ideb_observado   R-squared:                       0.971
Model:                            OLS   Adj. R-squared:                  0.955
Method:                 Least Squares   F-statistic:                     614.1
Date:                Thu, 05 Nov 2026   Prob (F-statistic):           2.53e-25
Time:                        13:10:23   Log-Likelihood:                 57.289
No. Observations:                 162   AIC:                             1.423
Df Residuals:                     104   BIC:                             180.5
Df Model:                          57                                         
Covariance Type:              cluster                                         
=============================================================================================================
                                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------------------------
Intercept                                     3.7593      0.035    107.330      0.000       3.687       3.831
C(uf_rede)[T.AC_Privada]                      2.3432      0.054     43.364      0.000       2.232       2.454
C(uf_rede)[T.AL_Estadual]                    -0.1333   1.03e-14  -1.29e+13      0.000      -0.133      -0.133
C(uf_rede)[T.AL_Privada]                      1.4765      0.054     27.326      0.000       1.365       1.588
C(uf_rede)[T.AM_Estadual]                    -0.2333    3.3e-15  -7.07e+13      0.000      -0.233      -0.233
C(uf_rede)[T.AM_Privada]                      1.7432      0.054     32.261      0.000       1.632       1.854
C(uf_rede)[T.AP_Estadual]                    -0.5333   2.25e-15  -2.37e+14      0.000      -0.533      -0.533
C(uf_rede)[T.AP_Privada]                      1.7765      0.054     32.877      0.000       1.665       1.888
C(uf_rede)[T.BA_Estadual]                    -0.3667    1.5e-15  -2.45e+14      0.000      -0.367      -0.367
C(uf_rede)[T.BA_Privada]                      2.0765      0.054     38.429      0.000       1.965       1.188
C(uf_rede)[T.CE_Estadual]                     0.5000    3.5e-15   1.43e+14      0.000       0.500       0.500
C(uf_rede)[T.CE_Privada]                      2.2099      0.054     40.897      0.000       2.099       2.321
C(uf_rede)[T.DF_Estadual]                     0.0667    5.9e-15   1.13e+13      0.000       0.067       0.067
C(uf_rede)[T.DF_Privada]                      2.5099      0.054     46.449      0.000       2.399       2.621
C(uf_rede)[T.ES_Estadual]                     0.7333   2.89e-15   2.53e+14      0.000       0.733       0.733
C(uf_rede)[T.ES_Privada]                      2.3432      0.054     43.364      0.000       2.232       2.454
C(uf_rede)[T.GO_Estadual]                     0.8333   1.76e-15   4.74e+14      0.000       0.833       0.833
C(uf_rede)[T.GO_Privada]                      2.1432      0.054     39.663      0.000       2.032       2.254
C(uf_rede)[T.MA_Estadual]                    -0.2000    2.6e-15  -7.68e+13      0.000      -0.200      -0.200
C(uf_rede)[T.MA_Privada]                      1.7765      0.054     32.877      0.000       1.665       1.888
C(uf_rede)[T.MG_Estadual]                     0.1667   1.97e-15   8.48e+13      0.000       0.167       0.167
C(uf_rede)[T.MG_Privada]                      2.4765      0.054     45.832      0.000       2.365       2.588
C(uf_rede)[T.MS_Estadual]                     0.0333   1.21e-15   2.74e+13      0.000       0.033       0.033
C(uf_rede)[T.MS_Privada]                      2.4099      0.054     44.598      0.000       2.299       2.521
C(uf_rede)[T.MT_Estadual]                    -0.1000   2.81e-15  -3.55e+13      0.000      -0.100      -0.100
C(uf_rede)[T.MT_Privada]                      2.2099      0.054     40.897      0.000       2.099       2.321
C(uf_rede)[T.PA_Estadual]                    -0.3333   3.47e-15  -9.62e+13      0.000      -0.333      -0.333
C(uf_rede)[T.PA_Privada]                      2.0432      0.054     37.813      0.000       1.932       2.154
C(uf_rede)[T.PB_Estadual]                    -0.1333   3.33e-15  -4.01e+13      0.000      -0.133      -0.133
C(uf_rede)[T.PB_Privada]                      1.9099      0.054     35.345      0.000       1.799       2.021
C(uf_rede)[T.PE_Estadual]                     0.6000   1.07e-15   5.59e+14      0.000       0.600       0.600
C(uf_rede)[T.PE_Privada]                      2.1099      0.054     39.046      0.000       1.999       2.221
C(uf_rede)[T.PI_Estadual]                     0.1667   1.51e-15    1.1e+14      0.000       0.167       0.167
C(uf_rede)[T.PI_Privada]                      2.4765      0.054     45.832      0.000       2.365       2.588
C(uf_rede)[T.PR_Estadual]                     0.7333   1.24e-15   5.93e+14      0.000       0.733       0.733
C(uf_rede)[T.PR_Privada]                      2.5432      0.054     47.066      0.000       2.432       2.654
C(uf_rede)[T.RJ_Estadual]                    -0.2667   2.01e-15  -1.33e+14      0.000      -0.267      -0.267
C(uf_rede)[T.RJ_Privada]                      1.5099      0.054     27.942      0.000       1.399       1.621
C(uf_rede)[T.RN_Estadual]                    -0.7667   2.98e-15  -2.58e+14      0.000      -0.767      -0.767
C(uf_rede)[T.RN_Privada]                      1.9765      0.054     36.579      0.000       1.865       2.088
C(uf_rede)[T.RO_Estadual]                     0.1333   2.28e-15   5.86e+13      0.000       0.133       0.133
C(uf_rede)[T.RO_Privada]                      2.0099      0.054     37.196      0.000       1.899       2.121
C(uf_rede)[T.RR_Estadual]                    -0.2333   5.23e-15  -4.46e+13      0.000      -0.233      -0.233
C(uf_rede)[T.RR_Privada]                      2.1099      0.054     39.046      0.000       1.999       2.221
C(uf_rede)[T.RS_Estadual]                     0.1667   1.19e-15    1.4e+14      0.000       0.167       0.167
C(uf_rede)[T.RS_Privada]                      2.3099      0.054     42.748      0.000       2.199       2.421
C(uf_rede)[T.SC_Estadual]                    -0.1000   1.82e-15  -5.49e+13      0.000      -0.100      -0.100
C(uf_rede)[T.SC_Privada]                      2.5099      0.054     46.449      0.000       2.399       2.621
C(uf_rede)[T.SE_Estadual]                    -0.2000   1.82e-15   -1.1e+14      0.000      -0.200      -0.200
C(uf_rede)[T.SE_Privada]                      1.9765      0.054     36.579      0.000       1.865       2.088
C(uf_rede)[T.SP_Estadual]                     0.4667   2.76e-15   1.69e+14      0.000       0.467       0.467
C(uf_rede)[T.SP_Privada]                      2.4765      0.054     45.832      0.000       2.365       2.588
C(uf_rede)[T.TO_Estadual]                     0.2000   1.61e-15   1.24e+14      0.000       0.200       0.200
C(uf_rede)[T.TO_Privada]                      2.4432      0.054     45.215      0.000       2.332       2.554
C(ano, Treatment(reference=2019))[T.2021]    -0.2741      0.076     -3.625      0.001      -0.429      -0.119
C(ano, Treatment(reference=2019))[T.2023]    -0.3333      0.059     -5.612      0.000      -0.455      -0.211
rede_publica:ano_2021                         0.3222      0.103      3.136      0.004       0.111       0.533
rede_publica:ano_2023                         0.5074      0.090      5.634      0.000       0.322       0.693
==============================================================================
Omnibus:                       11.746   Durbin-Watson:                   1.946
Prob(Omnibus):                  0.003   Jarque-Bera (JB):               30.746
Skew:                          -0.008   Prob(JB):                     2.11e-07
Kurtosis:                       5.134   Cond. No.                         64.1
==============================================================================

Notes:
[1] Standard Errors are robust to cluster correlation (CRV1)
```
