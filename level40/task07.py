import requests
from bs4 import BeautifulSoup
import schedule
import time

def fetch_headlines():
    # URL do site da BBC
    url = "https://www.bbc.com/news"

    # Solicitar o código HTML da página
    response = requests.get(url)
    
    # Se a página foi recebida com sucesso
    if response.status_code == 200:
        # Analisar o conteúdo da página
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar as manchetes (pressupondo que as manchetes estão na tag <h3>)
        headlines = soup.find_all('h3', limit=10)

        # Imprimir as primeiras 10 manchetes
        for index, headline in enumerate(headlines, start=1):
            print(f"{index}. {headline.get_text(strip=True)}")
    else:
        print("Não foi possível acessar o site da BBC.")

# Agendar a tarefa para todos os dias às 8:00
schedule.every().day.at("08:00").do(fetch_headlines)

# Execução contínua do programa
while True:
    schedule.run_pending()
    time.sleep(60)  # Verificar a cada minuto