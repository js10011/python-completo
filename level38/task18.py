import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

# Configuração do log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Criar uma instância do driver do navegador
    driver = webdriver.Chrome()

    # Abrir a página
    url = 'https://example.com'  # substitua pelo URL necessário
    logging.info('Abrindo a página: %s', url)
    driver.get(url)

    # Aguardar o carregamento da página
    time.sleep(3)

    # Procurar o elemento por id e interagir com ele
    element_id = 'element-id'  # substitua pelo id real do seu elemento
    logging.info('Procurando elemento com id: %s', element_id)
    element = driver.find_element(By.ID, element_id)
    
    # Exemplo de interação (por exemplo, clique)
    logging.info('Interagindo com o elemento: %s', element_id)
    element.click()

except NoSuchElementException as e:
    logging.error('Elemento não encontrado: %s', e)
    driver.save_screenshot('error_screenshot.png')
    logging.info('Captura de tela da página salva como error_screenshot.png')

except Exception as e:
    logging.error('Ocorreu um erro: %s', e)
    driver.save_screenshot('error_screenshot.png')
    logging.info('Captura de tela da página salva como error_screenshot.png')

finally:
    # Fechar o navegador
    logging.info('Fechando o navegador')
    driver.quit()