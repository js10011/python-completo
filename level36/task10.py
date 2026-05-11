from selenium import webdriver
from selenium.webdriver.common.by import By

# Cria uma instância do driver do navegador
driver = webdriver.Chrome()

# Abre a página web
driver.get("https://example.com")

# Busca todos os elementos com a tag 'a'
links = driver.find_elements(By.TAG_NAME, "a")

# Extrai os atributos href e os exibe na tela
hrefs = [link.get_attribute("href") for link in links if link.get_attribute("href") is not None]
print("URLs extraídas:")
for href in hrefs:
    print(href)

# Fecha o navegador
driver.quit()