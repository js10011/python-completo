import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Criar uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrindo a página da web
driver.get("https://example.com")

# Pequeno atraso para carregar completamente a página
time.sleep(2)

# Encontrar o elemento com o texto "More information..." usando seletor CSS
element = driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.iana.org/domains/example"]')

# Exibir o texto do elemento encontrado na tela
print(element.text)

# Fechar o navegador
driver.quit()