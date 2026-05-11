import requests
import schedule
from datetime import datetime
import time

# URL para obtenção de dados sobre a taxa de câmbio
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

# Função para obter as taxas de câmbio
def get_exchange_rates():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Lança um erro em caso de resposta ruim
        data = response.json()
        # Retorna apenas as taxas para EUR e GBP
        return {
            "EUR": data['rates'].get("EUR"),
            "GBP": data['rates'].get("GBP")
        }
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter dados: {e}")
        return None

# Função para exibir as taxas de câmbio
def display_rates():
    rates = get_exchange_rates()
    if rates:
        # Obtém o horário atual
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Horário: {now}")
        print(f"Taxa USD para EUR: {rates['EUR']}")
        print(f"Taxa USD para GBP: {rates['GBP']}")
    else:
        print("Não foi possível obter as taxas de câmbio.")

# Configuração do cronograma para execução da tarefa a cada hora
schedule.every().hour.do(display_rates)

# Ciclo principal para a execução das tarefas no cronograma
print("Iniciando o programa para atualizar as taxas de câmbio a cada hora.")
while True:
    schedule.run_pending()  # Verifica se há tarefas a serem executadas
    time.sleep(1)  # Atraso de 1 segundo antes da próxima verificação