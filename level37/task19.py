from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Função para inicializar o WebDriver
def initialize_driver():
    logging.info("Initializing the WebDriver.")
    return webdriver.Chrome()

# Função para navegar até a página de login
def navigate_to_login_page(driver):
    logging.info("Opening the login page.")
    driver.get("https://example.com/login")
    time.sleep(2)

# Função para realizar login na conta
def perform_login(driver, username, password):
    logging.info("Performing login.")
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "loginButton")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    time.sleep(2)

# Função para navegar até o catálogo de produtos
def navigate_to_catalog(driver):
    logging.info("Navigating to the product catalog.")
    driver.get("https://example.com/catalog")
    time.sleep(2)

# Função para adicionar o primeiro produto ao carrinho
def add_first_item_to_cart(driver):
    logging.info("Adding the first item to the cart.")
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]")
    add_to_cart_button.click()
    time.sleep(2)

# Função para navegar até a página do carrinho
def navigate_to_cart(driver):
    logging.info("Navigating to the cart page.")
    driver.get("https://example.com/cart")
    time.sleep(2)

# Função para iniciar o processo de checkout
def initiate_checkout(driver):
    logging.info("Initiating checkout.")
    checkout_button = driver.find_element(By.ID, "checkoutButton")
    checkout_button.click()
    time.sleep(2)

# Função principal para executar o cenário de compra
def main():
    driver = initialize_driver()

    try:
        navigate_to_login_page(driver)
        perform_login(driver, "your_username", "your_password")

        navigate_to_catalog(driver)
        add_first_item_to_cart(driver)

        navigate_to_cart(driver)
        initiate_checkout(driver)
    finally:
        driver.quit()
        logging.info("Browser closed.")

main()