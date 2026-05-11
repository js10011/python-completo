import requests

# Indique o endereço e a porta do seu servidor proxy nesta variável
proxy = "http://your-proxy-address:port"

# Configurações do proxy
proxies = {
    "http": proxy,
    "https": proxy
}

# Fazendo uma solicitação GET para o site "http://example.com" usando o proxy
response = requests.get("http://example.com", proxies=proxies)

# Verificando o sucesso da solicitação
response.raise_for_status()

# Impressão do conteúdo da página
print(response.text)