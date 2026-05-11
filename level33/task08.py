from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# Criação de uma instância do web driver para o navegador, por exemplo, Chrome
driver = webdriver.Chrome()

# Abertura da página da web
url = 'http://example.com'  # Indique aqui a URL da página da web
driver.get(url)

# Encontrar o elemento do botão na página
button = driver.find_element(By.ID, 'your-button-id')  # Indique aqui o ID correto do botão

# Emulação do movimento do mouse para o botão
actions = ActionChains(driver)
actions.move_to_element(button).perform()
time.sleep(random.uniform(1, 3))  # Atraso de 1 a 3 segundos

# Emulação de clique no botão
button.click()
time.sleep(random.uniform(1, 3))  # Atraso de 1 a 3 segundos

# Fechamento do navegador
driver.quit()