from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Criando uma instância do driver do navegador
driver = webdriver.Chrome()

# Acessando o site google.com
driver.get("https://www.google.com")

# Encontrando o campo de entrada para a consulta de busca
search_box = driver.find_element(By.NAME, "q")

# Inserindo o texto "Selenium automation" na barra de busca
search_box.send_keys("Selenium automation")

# Imitando o pressionamento da tecla Enter para realizar a busca
search_box.send_keys(Keys.RETURN)

# Dando um tempo para carregar os resultados da pesquisa
time.sleep(2)

# Encontrando o primeiro link dos resultados da pesquisa
first_link = driver.find_element(By.CSS_SELECTOR, "a:has(h3)")
url = first_link.get_attribute("href")
print(url)

# Fechando o navegador
driver.quit()