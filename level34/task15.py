# Importamos bibliotecas para cache e execução de solicitações HTTP
import requests_cache
import requests

# Configuramos o cache com tempo de vida de 60 segundos
requests_cache.install_cache('user_cache', expire_after=60)

# Executamos a solicitação GET para a API
response = requests.get('https://jsonplaceholder.typicode.com/users')

# Determinamos de onde os dados foram carregados — do cache ou do servidor
if response.from_cache:
    print("Dados foram obtidos do cache.")
else:
    print("Dados foram obtidos do servidor.")

# Extraímos e exibimos os nomes dos usuários
users = response.json()
for user in users:
    print(user['name'])