import requests
from requests.exceptions import RequestException

# Lista de proxies fictícios
proxies = [
    {"http": "http://123.45.67.89:8080", "https": "https://123.45.67.89:8080"},
    {"http": "http://98.76.54.32:8000", "https": "https://98.76.54.32:8000"},
    {"http": "http://11.22.33.44:3128", "https": "https://11.22.33.44:3128"}
]

# URL para requisição
url = "https://httpbin.org/ip"

# Função para enviar requisição
def get_ip_via_proxy(proxy):
    try:
        response = requests.get(url, proxies=proxy, timeout=5)
        response.raise_for_status()
        ip = response.json().get("origin")
        return ip
    except RequestException as e:
        return f"Erro ao fazer requisição através do proxy {proxy}: {e}"

# Envio de requisições e exibição do resultado
for i, proxy in enumerate(proxies, start=1):
    ip = get_ip_via_proxy(proxy)
    print(f"Requisição {i}, endereço IP visível pelo servidor: {ip}")