import requests
from bs4 import BeautifulSoup
import csv
import logging
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Logging
logging.basicConfig(filename='scraper.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Configuração da sessão HTTP com tentativas de repetição
session = requests.Session()
retry = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# Função para extrair dados da tabela
def extract_table_data(soup):
    table = soup.find('table')
    data = []
    if not table:
        logging.warning('Nenhuma tabela encontrada na página.')
        return data

    headers = [header.text.strip() for header in table.find_all('th')]
    rows = table.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        if cols:
            data.append([col.text.strip() for col in cols])

    return headers, data

# Escrita dos dados em CSV
def write_to_csv(filename, headers, data_rows):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if headers:
            writer.writerow(headers)
        writer.writerows(data_rows)

# Função principal de scraping
def scrape_website(base_url, num_pages):
    csv_file = 'scraped_data.csv'
    for page in range(1, num_pages + 1):
        try:
            url = f"{base_url}/page/{page}"
            response = session.get(url, timeout=10)
            response.raise_for_status()  # Erro HTTP se status não for 200
            soup = BeautifulSoup(response.content, 'html.parser')

            headers, data_rows = extract_table_data(soup)

            if data_rows:
                write_to_csv(csv_file, headers if page == 1 else None, data_rows)

            logging.info(f"Página {page} raspada com sucesso")

        except requests.exceptions.HTTPError as errh:
            logging.error(f"Erro HTTP: {errh} na página {page}")
        except requests.exceptions.ConnectionError as errc:
            logging.error(f"Erro de Conexão: {errc} na página {page}")
        except requests.exceptions.Timeout as errt:
            logging.error(f"Erro de Timeout: {errt} na página {page}")
        except requests.exceptions.RequestException as err:
            logging.error(f"Ocorreu um erro inesperado: {err} na página {page}")

        # Pausa entre as requisições
        time.sleep(1)

BASE_URL = 'http://example.com'  # substitua pela URL do seu site
NUM_PAGES = 5  # número de páginas para scraping
scrape_website(BASE_URL, NUM_PAGES)