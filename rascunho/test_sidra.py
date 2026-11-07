import requests

# Test IBGE SIDRA API for PNAD Contínua Educação
# Tabela 7268: Pessoas de 15 a 29 anos de idade por motivo de não frequentar escola
url = "https://servicodados.ibge.gov.br/api/v3/agregados/7268/periodos/-1/variaveis/10323?localidades=N1[all]|N3[27]"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    r = requests.get(url, headers=headers, timeout=10)
    print("SIDRA Status:", r.status_code)
    if r.status_code == 200:
        data = r.json()
        print("Retornou dados da Tabela 7268! Qtd de variáveis:", len(data))
        if data:
            print("Nome agregado:", data[0].get("nome"))
except Exception as e:
    print("Erro ao acessar SIDRA API:", e)

