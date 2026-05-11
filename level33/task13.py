import requests

# URL da página alvo e lista de proxies
url = "http://example.com"
proxy_list = [
    "http://proxy1.example.com:8080",
    "http://proxy2.example.com:8080",
    "http://proxy3.example.com:8080",
]

# Percorre cada proxy na lista
for proxy in proxy_list:
    try:
        # Configura o proxy atual para requisições HTTP e HTTPS
        proxies = {
            'http': proxy,
            'https': proxy,
        }
        # Envia uma requisição GET através do proxy atual
        response = requests.get(url, proxies=proxies, timeout=5)

        # Se a requisição for bem-sucedida (código 200), exibe o conteúdo da página
        if response.status_code == 200:
            print(response.text)
            break  # Encerra o loop se a requisição for bem-sucedida

    except requests.RequestException:
        # Informa sobre erro de acesso através do proxy atual e passa para o próximo
        print(f"Proxy {proxy} indisponível, tentando o próximo...")

# Se nenhum proxy funcionou, exibe a mensagem de falha
else:
    print("A requisição falhou")