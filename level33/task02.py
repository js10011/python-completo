import requests
import time
import random

# Definindo a URL para a qual enviaremos as solicitações
url = "https://httpbin.org/get"

# Cabeçalhos para imitar um agente de usuário
headers = {
    "User-Agent": "MyCustomUserAgent/1.0"
}

# Criando uma sessão para manter o estado (por exemplo, cookies)
session = requests.Session()

# Loop para enviar cinco solicitações
for _ in range(5):
    # Enviando uma solicitação GET para a URL com os cabeçalhos especificados
    response = session.get(url, headers=headers)

    # Exibindo o código de status da resposta
    print(f"Código de Status: {response.status_code}")

    # Pausa por um tempo aleatório de 2 a 5 segundos entre as solicitações
    time.sleep(random.uniform(2, 5))