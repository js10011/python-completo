from selenium import webdriver
from selenium.webdriver.common.by import By

# Criamos uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrimos a página web
driver.get("https://www.wikipedia.org")

# Extraímos todos os elementos com a tag a
links = driver.find_elements(By.TAG_NAME, 'a')

# Coletamos todos os URLs dos atributos href
urls = [link.get_attribute('href') for link in links if link.get_attribute('href')]

# Exibimos a lista de todas as URLs encontradas
print("URLs encontradas:")
for u in urls:
    print(u)

# Fechamos o driver
driver.quit()