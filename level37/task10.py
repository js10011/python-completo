import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# URL, nome do campo de entrada, texto para inserir e ID do botão
url = "http://example.com"  # Substitua pela URL necessária
input_name = "exampleInputName"  # Substitua pelo nome necessário do campo de entrada
input_text = "Hello, Selenium!"  # Texto para inserir
button_id = "exampleButtonId"  # Substitua pelo ID necessário do botão

# Criar uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrir a página web especificada
driver.get(url)

# Esperar para que a página carregue completamente
time.sleep(2)

# Encontrar o campo de entrada pelo nome e inserir texto
input_field = driver.find_element(By.NAME, input_name)
input_field.send_keys(input_text)

# Encontrar o botão pelo ID e clicar nele
button = driver.find_element(By.ID, button_id)
button.click()

# Esperar para ver o resultado
time.sleep(2)

# Fechar o navegador
driver.quit()