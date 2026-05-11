from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Criamos uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrimos a página web no URL especificado
driver.get("https://example.com")

# Encontramos o botão com a classe `submit-btn` e clicamos nele
submit_button = driver.find_element(By.CLASS_NAME, "submit-btn")
submit_button.click()

# Esperamos um pouco para a página carregar
time.sleep(2)

# Extraímos o texto do título com a tag `h1`
header_text = driver.find_element(By.TAG_NAME, "h1").text
print(header_text)

# Concluímos a sessão de trabalho do navegador
driver.quit()