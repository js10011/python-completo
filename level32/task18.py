# Importamos as bibliotecas necessárias para realizar requisições HTTP, fazer parsing de HTML e trabalhar com CSV
import requests
from bs4 import BeautifulSoup
import csv
import time

# URL da página de onde vamos extrair o título
url = 'https://example.com'

# Definimos o número máximo de tentativas
retries = 3
attempts = 0  # Contador de tentativas

# Tentamos realizar a requisição ao URL várias vezes em caso de erros
while attempts < retries:
    try:
        # Realizamos a requisição GET com timeout de 5 segundos
        response = requests.get(url, timeout=5)
        # Verificamos se a requisição foi bem-sucedida; se não for, uma exceção é levantada
        response.raise_for_status()

        # Criamos um objeto BeautifulSoup para fazer o parsing do conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extraímos o título da página, se existir, ou exibimos 'No Title Found'
        title = soup.title.string.strip() if soup.title else 'No Title Found'

        # Interrompemos o loop se o título for extraído com sucesso
        break
    except (requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
        # Se a requisição falhar, exibimos uma mensagem de erro e incrementamos o contador de tentativas
        print(f"Tentativa {attempts + 1} falhou: {e}")
        attempts += 1
        # Pausa antes de tentar novamente
        time.sleep(1)

# Se o título for extraído com sucesso, salvamos no arquivo CSV
if title:
    with open('titles.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Escrevemos o título em uma nova linha no arquivo CSV
        writer.writerow([title])
    print(f"Título '{title}' salvo em 'titles.csv'.")
else:
    print("Não foi possível extrair o título após várias tentativas.")