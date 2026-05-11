# Importamos bibliotecas para trabalhar com Redis e realizar requisições HTTP
import redis
import requests

# Configuramos a conexão com o Redis
cache = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
# Chave para armazenar dados no cache e tempo de vida do cache em segundos
cache_key = 'todos_cache'
cache_expiration = 120  # 120 segundos

# Verificamos se há dados no cache do Redis
cached_data = cache.get(cache_key)
if cached_data:
    print("Dados obtidos do cache.")
    todos_data = cached_data
else:
    # Fazemos a requisição à API se não houver dados no cache
    print("Dados obtidos do servidor.")
    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    if response.status_code == 200:
        # Armazenamos os dados no cache com o tempo de vida especificado
        cache.setex(cache_key, cache_expiration, response.text)
        todos_data = response.text
    else:
        raise Exception("Não foi possível obter dados do servidor.")

# Exibimos os dados
print(todos_data)