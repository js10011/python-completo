import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Criando uma instância do driver do navegador
driver = webdriver.Chrome()

# Abertura da página web
driver.get("https://example.com")

# Pequena pausa para carregamento da página
time.sleep(2)

# Encontrar o elemento pelo identificador único 'header'
header_element = driver.find_element(By.ID, 'header')

# Extração e exibição do texto do elemento
print(header_element.text)

# Encerramento da sessão do navegador
driver.quit()