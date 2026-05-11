import requests

# Define o URL para verificar o endereço IP
url = 'http://httpbin.org/ip'

# Lista de servidores proxy
proxies = [
    {'http': 'http://ip1:port', 'https': 'http://ip1:port'},
    {'http': 'http://ip2:port', 'https': 'http://ip2:port'},
    {'http': 'http://ip3:port', 'https': 'http://ip3:port'}
]

# Itera sobre cada proxy na lista
for proxy in proxies:
    try:
        # Imprime o proxy sendo usado
        print(f"Uso do proxy: {proxy['http']}")

        # Executa a solicitação GET ao URL com o proxy especificado
        response = requests.get(url, proxies=proxy, timeout=5)

        # Verifica o status da resposta
        print(f"HTTP-status: {response.status_code}")

        # Se o status for bem-sucedido, imprime o endereço IP do qual a solicitação foi feita
        if response.status_code == 200:
            print(f"Endereço IP: {response.json()['origin']}")
        else:
            print("Erro ao obter dados de httpbin.org")

    # Trata possíveis erros de solicitação
    except requests.exceptions.RequestException as e:
        print(f"Erro de solicitação: {e}")