from selenium import webdriver
from selenium.webdriver.common.by import By

# Criamos uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrimos a página web pelo URL fornecido
driver.get("https://www.wikipedia.org")

# Procuramos o primeiro elemento com a tag <h1> e extraímos seu texto
h1_text = driver.find_element(By.TAG_NAME, 'h1').text

# Imprimimos o texto do elemento h1
print(h1_text)

# Fechamos o navegador
driver.quit()