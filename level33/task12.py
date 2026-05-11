import random
import requests

# Lista de servidores proxy. Para exemplo, são indicados endereços fictícios, substitua-os por reais.
proxy_list = [
    'http://123.456.789.1:8080',
    'http://987.654.321.0:8080',
    'http://192.168.1.1:8080'
]

# Escolha aleatória de servidor proxy da lista
selected_proxy = random.choice(proxy_list)

# Configuração do proxy para a biblioteca requests
proxies = {
    'http': selected_proxy,
    'https': selected_proxy
}

# Envio da solicitação GET através do servidor proxy escolhido
response = requests.get('http://example.com', proxies=proxies)

# Exibição do conteúdo da página no console
print(response.text)