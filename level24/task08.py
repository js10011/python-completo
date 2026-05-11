import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Para temperatura em Celsius
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        print(f"Temperatura atual em {city_name}: {weather_data['main']['temp']}°C")
        print(f"Descrição do clima: {weather_data['weather'][0]['description']}")
    else:
        print(f"Erro: {response.status_code} - {response.json()['message']}")

# Substitua 'your_api_key' pela sua chave de API do OpenWeatherMap
api_key = 'your_api_key'
city_name = input("Digite o nome da cidade: ")
get_weather(city_name, api_key)