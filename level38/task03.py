# Importamos bibliotecas para log e trabalho com o web driver
import logging
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

# Configuração do log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Log do início da inicialização do web driver
logger.info("Inicialização do web driver")

try:
    # Criamos uma instância do driver do navegador
    driver = webdriver.Chrome()

    # Abertura da página python.org
    logger.info("Abertura da página python.org")
    driver.get("https://www.python.org")

    # Extração e log do título da página
    title = driver.title
    logger.info(f"Título da página: {title}")

# Tratamento de erros do web driver
except WebDriverException as e:
    logger.error(f"Erro do web driver: {e}")

# Tratamento de outros erros
except Exception as e:
    logger.error(f"Ocorreu um erro: {e}")

# Fechamento do web driver e log da conclusão do script
finally:
    logger.info("Fechamento do web driver")
    driver.quit()
    logger.info("O script concluiu a execução")