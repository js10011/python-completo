import requests
from bs4 import BeautifulSoup
import csv
import time
import schedule

# URL da página do produto (substitua pelo URL atual)
URL = "https://www.example.com/product"

# Cabeçalhos para imitar a visita de um navegador
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    )
}

# Nome do arquivo CSV para gravar o histórico de preços
CSV_FILE = 'price_history.csv'

# Função para obter o preço atual do produto
def fetch_price():
    # Envio do pedido para o URL com cabeçalhos
    response = requests.get(URL, headers=HEADERS)
    # Parseamento do conteúdo HTML com BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Procurando o elemento que contém o preço (substitua 'span' e 'id' pelos valores necessários)
    price_tag = soup.find('span', {'id': 'priceblock_ourprice'})

    # Se o elemento for encontrado, obtenha o texto do preço
    if price_tag:
        price = price_tag.text.strip()
        print(f"Preço atual: {price}")
        return price
    else:
        print("Elemento com o preço não encontrado")
        return None

# Função para gravar o preço no arquivo CSV
def write_price_to_csv(price):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Gravação da data, hora e preço atuais
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), price])

# Função para verificar o preço e gravá-lo no CSV
def check_price():
    price = fetch_price()  # Obtém o preço atual
    if price:
        write_price_to_csv(price)  # Grava o preço no arquivo

# Função principal
def main():
    # Configuração do agendamento para verificar a cada 2 horas
    schedule.every(2).hours.do(check_price)

    # Loop infinito para executar tarefas agendadas
    while True:
        schedule.run_pending()  # Executa as tarefas se for a hora marcada
        time.sleep(1)  # Atraso de 1 segundo antes da próxima verificação

# Inicialização do programa
main()