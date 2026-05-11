import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# URL e dados para autorização
url = 'https://example.com/login'
username = 'test_user'
password = 'test_password'

def setup_driver():
    """Configura e inicializa o ChromeDriver."""
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        logging.info("Web driver do Chrome inicializado com sucesso.")
        return driver
    except WebDriverException as e:
        logging.error("Erro ao inicializar o ChromeDriver: %s", e)
        return None

def login(driver, url, username, password):
    """Executa a autorização no site."""
    try:
        # Abertura da página de autorização
        driver.get(url)
        logging.info("Página aberta: %s", url)

        # Inserção do login
        username_field = driver.find_element(By.NAME, "username")  # Usando NAME como exemplo, adapte para a página
        username_field.send_keys(username)
        logging.info("Login inserido: %s", username)

        # Inserção da senha
        password_field = driver.find_element(By.NAME, "password")  # Usando NAME como exemplo, adapte para a página
        password_field.send_keys(password)
        logging.info("Senha inserida.")

        # Clique no botão de entrada
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Pressupõe-se que este é o botão de entrada
        login_button.click()
        logging.info("Botão de entrar no site clicado.")

    except WebDriverException as e:
        logging.error("Erro ao executar a autorização: %s", e)

driver = setup_driver()
if driver:
    login(driver, url, username, password)
    driver.quit()
    logging.info("Web driver fechado.")
else:
    logging.error("Não foi possível inicializar o web driver.")