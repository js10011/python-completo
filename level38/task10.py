from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# URL e número de páginas
URL = "https://example.com/page"
TOTAL_PAGES = 5  # Defina o número total de páginas para coleta de dados

def setup_driver():
    """Inicializa e retorna o ChromeDriver."""
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        logging.info("Web driver do Chrome inicializado com sucesso.")
        return driver
    except WebDriverException as e:
        logging.error("Erro ao inicializar o ChromeDriver: %s", e)
        return None

def collect_data_from_page(driver):
    """Coleta dados dos elementos com o identificador 'data_item' na página atual."""
    data_items = []
    try:
        elements = driver.find_elements(By.ID, "data_item")
        data_items = [element.text for element in elements]
        logging.info("Coletados %d itens de dados na página atual.", len(data_items))
    except NoSuchElementException:
        logging.warning("Elementos com o identificador 'data_item' não encontrados na página atual.")
    return data_items

def go_to_next_page(driver, page_number):
    """Navega para a página especificada usando links numerados."""
    try:
        next_page_link = driver.find_element(By.LINK_TEXT, str(page_number))
        next_page_link.click()
        logging.info("Navegou para a página %d.", page_number)
    except NoSuchElementException:
        logging.warning("Link para a página %d não encontrado.", page_number)

def main():
    driver = setup_driver()
    all_data = []

    if driver:
        driver.get(URL)  # Abre a página inicial
        logging.info("Página inicial aberta: %s", URL)

        for page in range(1, TOTAL_PAGES + 1):
            data = collect_data_from_page(driver)
            all_data.extend(data)
            if page < TOTAL_PAGES:  # Navega para a próxima página, se não for a última
                go_to_next_page(driver, page + 1)

        driver.quit()
        logging.info("Web driver fechado.")
    else:
        logging.error("Falha ao inicializar o web driver.")

    # Exibe os dados coletados no console
    print("Dados coletados:", all_data)

main()