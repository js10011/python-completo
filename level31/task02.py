import requests

# Solicitação do usuário para entrada de userId
user_id = input("Digite o userId: ")

# URL para acessar a API
url = "https://jsonplaceholder.typicode.com/posts"

# Parâmetros da solicitação
params = {'userId': user_id}

# Envio de solicitação GET
response = requests.get(url, params=params)

# Processamento da resposta em formato JSON
posts = response.json()

# Extração e exibição dos títulos (title) de todas as postagens
for post in posts:
    print(post['title'])