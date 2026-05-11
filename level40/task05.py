import requests
import schedule
import time


# Função para obter dados meteorológicos
def get_weather_data(api_key, city):
    # Formamos a URL para a solicitação API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    # Realizamos a solicitação GET à API
    response = requests.get(url)
    # Convertendo a resposta no formato JSON
    data = response.json()
    return data


# Função para exibir dados meteorológicos
def print_weather(data):
    # Verificamos se os dados de temperatura e descrição do tempo existem
    if data.get("main") and data.get("weather"):
        temperature = data["main"]["temp"]  # Temperatura
        weather_description = data["weather"][0]["description"]  # Descrição do tempo
        print(f"Temperatura atual em Nova York: {temperature}°C")
        print(f"Descrição do tempo: {weather_description}")
    else:
        print("Não foi possível obter dados meteorológicos")


# Função que será executada conforme o agendamento
def scheduled_weather_check():
    api_key = "your_api_key"  # Substitua 'your_api_key' pela sua chave de API real do OpenWeather
    city = "New York"  # Cidade para monitoramento do tempo
    weather_data = get_weather_data(api_key, city)  # Obtemos dados meteorológicos
    print_weather(weather_data)  # Exibimos os dados meteorológicos


# Configuramos o agendamento para executar a tarefa a cada 15 minutos
schedule.every(15).minutes.do(scheduled_weather_check)

# Loop principal para executar tarefas conforme o agendamento
while True:
    schedule.run_pending()  # Verificamos se há tarefas para executar
    time.sleep(1)  # Atraso de 1 segundo antes da próxima verificação