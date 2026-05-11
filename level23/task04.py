import requests
import json

# URL para envio da solicitação POST
url = 'http://example.com/api'

# Dados que serão enviados como JSON
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Envio da solicitação POST com dados JSON
response = requests.post(url, json=data)

# Verificação do sucesso da solicitação
if response.status_code == 200:
    # Processamento da resposta JSON recebida
    response_data = response.json()
    print(json.dumps(response_data, indent=4))  # Impressão dos dados da resposta em formato legível
else:
    print(f"Solicitação POST falhou, código de status: {response.status_code}")