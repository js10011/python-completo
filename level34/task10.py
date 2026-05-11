# Importamos a biblioteca para realizar requisições HTTP
import requests

# Solicitamos ao usuário a chave API OpenWeather e o nome da cidade
api_key = input("Digite sua chave API OpenWeather: ")
city = input("Digite o nome da cidade: ")

# Formamos a URL para a solicitação de dados meteorológicos
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Tentamos realizar a requisição à API
try:
    response = requests.get(url)
    response.raise_for_status()  # Verificamos se há erros HTTP
    data = response.json()  # Obtemos os dados em formato JSON

    # Verificamos se há erros na resposta da API
    if data['cod'] != 200:
        print(f"Erro: {data['message']}")
    else:
        # Extraímos os dados meteorológicos necessários
        main = data['main']
        weather = data['weather'][0]

        # Convertamos a temperatura de Kelvin para Celsius
        temperature_celsius = main['temp'] - 273.15
        humidity = main['humidity']
        description = weather['description']

        # Exibimos os dados meteorológicos
        print(f"Temperatura: {temperature_celsius:.2f}°C")
        print(f"Umidade: {humidity}%")
        print(f"Descrição do tempo: {description}")

# Tratamento de possíveis erros de requisição
except requests.exceptions.HTTPError as http_err:
    print(f"Erro HTTP: {http_err}")
except requests.exceptions.ConnectionError:
    print("Erro de conexão")
except requests.exceptions.Timeout:
    print("Tempo de espera esgotado")
except requests.exceptions.RequestException as err:
    print(f"Erro: {err}")