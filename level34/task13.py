# Importamos a biblioteca para realizar requisições HTTP e tratar exceções
import requests
from requests.exceptions import Timeout, RequestException

# URL do site e duração do timeout
url = "https://example.com"
timeout_duration = 5  # Timeout em segundos

# Tentamos realizar um GET request para o URL especificado com o timeout
try:
    response = requests.get(url, timeout=timeout_duration)
    # Se a requisição for bem-sucedida, exibimos o status da resposta
    print("Site carregado com sucesso, status code:", response.status_code)

# Tratamento do erro de timeout
except Timeout:
    print("Tempo limite da requisição excedido. Tente novamente mais tarde.")

# Tratamento de outros possíveis erros de requisição
except RequestException as e:
    print(f"Ocorreu um erro: {e}")