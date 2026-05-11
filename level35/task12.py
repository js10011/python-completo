from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Criar uma instância do driver do navegador
driver = webdriver.Chrome()

# Acessar a página principal do Google
driver.get("https://www.google.com")

# Encontrar o campo de texto de busca pelo nome da tag
search_box = driver.find_element_by_name("q")

# Inserir a consulta "Selenium Python" no campo de texto
search_box.send_keys("Selenium Python")

# Enviar o formulário (pressionar Enter)
search_box.send_keys(Keys.RETURN)

# Aguardar algum tempo para que a página carregue
time.sleep(2)

# Extrair o título da página atual
title = driver.title

# Exibir o título no console
print(title)

# Fechar o navegador
driver.quit()