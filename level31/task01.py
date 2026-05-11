import requests
import json

# Envia uma solicitação HTTP para o site
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

# Extrai dados da resposta JSON
todo_data = response.json()

# Exibe os dados em formato formatado
print(json.dumps(todo_data, indent=4))