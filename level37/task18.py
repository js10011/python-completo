import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# URL e dados de autorização
URL = 'https://example.com/login'
USERNAME = 'test_user'
PASSWORD = 'test_password'

def setup_driver():
    """Configura e inicializa o ChromeDriver."""
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        logging.info("WebDriver Chrome inicializado com sucesso.")
        return driver
    except WebDriverException as e:
        logging.error("Erro ao inicializar o ChromeDriver: %s", e)
        return None

def open_login_page(driver, url):
    """Abre a página de login."""
    try:
        driver.get(url)
        logging.info("Página aberta: %s", url)
    except WebDriverException as e:
        logging.error("Erro ao abrir a página %s: %s", url, e)

def enter_credentials(driver, username, password):
    """Entra com usuário e senha nos campos de entrada."""
    try:
        username_field = driver.find_element(By.NAME, "username")
        username_field.send_keys(username)
        logging.info("Usuário inserido: %s", username)

        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(password)
        logging.info("Senha inserida.")
    except WebDriverException as e:
        logging.error("Erro ao inserir as credenciais: %s", e)

def click_login_button(driver):
    """Clica no botão para acessar o site."""
    try:
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        logging.info("Botão de login clicado.")
    except WebDriverException as e:
        logging.error("Erro ao clicar no botão de login: %s", e)

def close_driver(driver):
    """Fecha o WebDriver."""
    try:
        driver.quit()
        logging.info("WebDriver fechado.")
    except WebDriverException as e:
        logging.error("Erro ao fechar o WebDriver: %s", e)

def main():
    driver = setup_driver()
    if driver:
        open_login_page(driver, URL)
        enter_credentials(driver, USERNAME, PASSWORD)
        click_login_button(driver)
        close_driver(driver)
    else:
        logging.error("Falha ao inicializar o WebDriver.")

main()