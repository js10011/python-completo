from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# URL base e quantidade de páginas para processar
BASE_URL = "https://example.com/page/"
TOTAL_PAGES = 5  # Definimos o número total de páginas para percorrer

def setup_driver():
    """Inicializa e retorna o ChromeDriver."""
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        logging.info("Web driver Chrome inicializado com sucesso.")
        return driver
    except WebDriverException as e:
        logging.error("Erro ao inicializar o ChromeDriver: %s", e)
        return None

def collect_data_from_page(driver, page_number):
    """Coleta dados dos elementos da classe 'content_item' na página atual."""
    data_items = []
    try:
        elements = driver.find_elements(By.CLASS_NAME, "content_item")
        data_items = [element.text for element in elements]
        logging.info("Foram coletados %d itens de dados na página %d.", len(data_items), page_number)
    except NoSuchElementException:
        logging.warning("Elementos com a classe 'content_item' não encontrados na página %d.", page_number)
    return data_items

def main():
    driver = setup_driver()
    all_data = {}

    if driver:
        for page in range(1, TOTAL_PAGES + 1):
            url = f"{BASE_URL}{page}"  # Formamos a URL para cada página
            driver.get(url)
            logging.info("Página aberta: %s", url)

            # Coleta de dados e adição ao dicionário
            data = collect_data_from_page(driver, page)
            all_data[page] = data

        driver.quit()
        logging.info("Web driver fechado.")
    else:
        logging.error("Não foi possível inicializar o web driver.")

    # Imprime os dados coletados no console
    print("Dados coletados:", all_data)

main()