import requests

# URL para enviar a solicitação GET
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Envio da solicitação GET
response = requests.get(url)

# Processamento da resposta
status_code = response.status_code
headers = response.headers
body = response.text

# Exibição dos resultados
print(f'Status Code: {status_code}')
print('Headers:')
for key, value in headers.items():
    print(f'  {key}: {value}')
print('Body:')
print(body)