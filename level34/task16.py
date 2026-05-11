import requests_cache
import requests

# Inicializamos a sessão com caching (tempo de vida do cache — 300 segundos)
session = requests_cache.CachedSession('posts_cache', expire_after=300)

# Loop para obter postagens para usuários com ID de 1 a 5
for user_id in range(1, 6):
    # Definimos a URL e os parâmetros da requisição
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {'userId': user_id}

    # Realizamos a requisição GET com caching
    response = session.get(url, params=params)

    # Verificamos se os dados foram carregados do cache
    if response.from_cache:
        print(f"Dados para userId={user_id} obtidos do cache.")
    else:
        print(f"Dados para userId={user_id} obtidos do servidor.")

    # Exibimos os títulos das postagens do usuário
    posts = response.json()
    for post in posts:
        print(f"Título: {post['title']}")