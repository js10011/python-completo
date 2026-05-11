import requests

# Definindo o URL
url = "https://httpbin.org/user-agent"

# Definindo um User-Agent falso para Safari no macOS
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"
}

# Enviando uma requisição HTTP com o User-Agent falso
response = requests.get(url, headers=headers)

# Exibindo o conteúdo da resposta do servidor
print(response.text)