import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Configuração do driver Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Abrindo a página HTML local
    driver.get("file:///path/to/your/local/form_page.html")  # Indique o caminho para sua página HTML local

    # Buscando os campos do formulário
    name_input = driver.find_element(By.NAME, "name")
    email_input = driver.find_element(By.NAME, "email")
    submit_button = driver.find_element(By.NAME, "submit")

    # Preenchimento do formulário
    name_input.send_keys("Seu Nome")
    email_input.send_keys("example@example.com")

    # Simulando o clique no botão "Submit"
    submit_button.click()

    # Pequena pausa para ver o resultado
    time.sleep(2)

finally:
    # Fechando o navegador
    driver.quit()