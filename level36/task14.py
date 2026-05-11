import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Cria uma instância do driver do navegador
driver = webdriver.Chrome()

# Abre a página especificada
driver.get("https://example.com/dynamic-content")

# Role a página até o final
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Rola para baixo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Espera o carregamento do conteúdo dinâmico
    time.sleep(2)  # O tempo de espera pode ser alterado dependendo das condições de carregamento da página

    # Calcula a nova altura da página e compara com a anterior
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Conta os elementos com a classe "content-item"
content_items = driver.find_elements(By.CLASS_NAME, "content-item")
print("Número total de elementos carregados com a classe 'content-item':", len(content_items))

# Fecha o web driver
driver.quit()