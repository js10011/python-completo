import requests

# Servidor proxy e porta
proxy = {
    'http': 'http://your_proxy_server:port',
    'https': 'https://your_proxy_server:port'
}

# URL para enviar a requisição GET
url = 'http://example.com'

try:
    response = requests.get(url, proxies=proxy)
    print(response.status_code)
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro: {e}")