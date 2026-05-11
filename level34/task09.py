# Importamos a biblioteca para realizar solicitações HTTP
import requests

# URL para a solicitação da piada sobre programadores
url = "https://v2.jokeapi.dev/joke/Programming?type=single"

# Realizamos a solicitação GET à API
response = requests.get(url)

# Verificamos se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Extraímos os dados no formato JSON
    json_data = response.json()
    # Extraímos o texto da piada e exibimos na tela
    joke = json_data.get("joke")
    print(joke)
else:
    # Mensagem de erro, se a solicitação falhou
    print("Não foi possível obter a piada. Tente novamente.")