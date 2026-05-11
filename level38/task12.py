import logging
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, WebDriverException

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constantes
BASE_URL = "https://example.com/page/"
CSV_FILE = "collected_data.csv"
DELAY = 2  # Delay entre requisições em segundos

def setup_driver():
    """Inicializa e retorna o ChromeDriver."""
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        logging.info("Chrome WebDriver inicializado com sucesso.")
        return driver
    except WebDriverException as e:
        logging.error("Erro ao inicializar o ChromeDriver: %s", e)
        return None

def collect_data_from_page(driver, page_number):
    """Coleta dados de elementos com a classe 'content_item' na página atual."""
    data_items = []
    try:
        elements = driver.find_elements(By.CLASS_NAME, "content_item")
        data_items = [element.text for element in elements]
        logging.info("Coletados %d elementos de dados na página %d.", len(data_items), page_number)
    except NoSuchElementException:
        logging.warning("Elementos com a classe 'content_item' não encontrados na página %d.", page_number)
    return data_items

def save_data_to_csv(data, filename):
    """Salva os dados em um arquivo CSV."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Número da Página", "Dados"])
        for page, items in data.items():
            writer.writerow([page, "; ".join(items)])  # Une dados de uma página em uma linha

def navigate_pages(driver):
    """Navega pelas páginas usando o botão 'Próximo' e coleta dados."""
    all_data = {}
    page_number = 1

    while True:
        # Navegação para a URL da primeira página e registro de informações no log
        url = f"{BASE_URL}{page_number}"
        driver.get(url)
        logging.info("Página aberta: %s", url)

        # Coleta de dados na página atual
        data = collect_data_from_page(driver, page_number)
        all_data[page_number] = data

        # Execução de delay para simular comportamento natural
        logging.info("Execução de delay de %d segundos.", DELAY)
        time.sleep(DELAY)

        # Verificação da presença do botão "Próximo" para ir para a próxima página
        try:
            next_button = driver.find_element(By.LINK_TEXT, "Próximo")
            next_button.click()
            logging.info("Botão 'Próximo' encontrado e clicado. Indo para a próxima página.")
            page_number += 1
        except NoSuchElementException:
            logging.warning("Botão 'Próximo' ausente na página %d. Encerrando a navegação.", page_number)
            break

    return all_data

def main():
    driver = setup_driver()
    if driver:
        try:
            collected_data = navigate_pages(driver)
        finally:
            driver.quit()
            logging.info("WebDriver encerrado.")

        # Salvar os dados coletados em um arquivo CSV
        save_data_to_csv(collected_data, CSV_FILE)
        logging.info("Dados salvos no arquivo %s", CSV_FILE)
    else:
        logging.error("Falha ao inicializar o WebDriver.")

main()