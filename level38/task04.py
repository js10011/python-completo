from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import logging
import time

# Configuração do log
logging.basicConfig(filename='selenium_search.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')

def find_element_with_retries(driver, selector, retries=3, wait_time=2):
    for attempt in range(retries):
        try:
            logging.info(f'Tentativa {attempt + 1} de {retries}: Buscando elemento com o seletor "{selector}"')
            element = driver.find_element_by_css_selector(selector)
            logging.info('Elemento encontrado.')
            return element
        except NoSuchElementException as e:
            logging.warning(f'Tentativa {attempt + 1} falhou. Erro: {e}')
            time.sleep(wait_time)
    
    logging.error(f'Elemento com o seletor "{selector}" não encontrado após {retries} tentativas.')
    return None

def main():
    # Aqui é necessário indicar o caminho para o driver e a URL da página para teste
    url = 'https://example.com'

    # Criar uma instância do driver do navegador
    driver = webdriver.Chrome()
    
    try:
        driver.get(url)
        # Exemplo de seletor
        css_selector = '#some-element'
        find_element_with_retries(driver, css_selector)
    finally:
        driver.quit()

main()