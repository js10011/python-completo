import requests

# Execução da solicitação GET a uma API
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Exibição do resultado da solicitação
print(response.json())