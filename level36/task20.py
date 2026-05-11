# Importamos bibliotecas para log e trabalho com navegador web
import logging
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

# Configuramos o módulo de log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Criamos uma instância do web driver para o navegador Chrome
driver = webdriver.Chrome()

# Lista de URLs para abrir
urls_to_open = [
    "https://www.example.com",
    "https://www.nonexistentwebsite.com",
    "https://www.python.org"
]

# Abrimos cada página da lista
for url in urls_to_open:
    try:
        # Abrimos o URL
        driver.get(url)
        logger.info(f"Página aberta com sucesso: {url}")
    except WebDriverException as e:
        # Logamos o erro se a página não abrir
        logger.error(f"Erro ao abrir a página {url}: {e}")

# Fechamos o web driver e encerramos a sessão do navegador
driver.quit()