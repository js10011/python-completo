import requests

# URL para envio da solicitação GET
url = 'https://api.example.com/data'

# Parâmetros da solicitação
params = {
    'param1': 'value1',
    'param2': 'value2'
}

# Envio da solicitação GET
response = requests.get(url, params=params)

# Verificação de sucesso da solicitação
if response.status_code == 200:
    # Processamento da resposta JSON
    data = response.json()
    # Impressão dos dados
    print(data)
else:
    print(f"Solicitação falhou com o código de status: {response.status_code}")