from selenium import webdriver
from selenium.webdriver.common.by import By

# Cria uma instância do driver do navegador
driver = webdriver.Chrome()

# Abre a página web www.example.com
driver.get("http://www.example.com")

# Encontra o primeiro elemento <p> na página
first_paragraph = driver.find_element(By.TAG_NAME, "p")

# Extrai o texto do elemento encontrado
paragraph_text = first_paragraph.text

# Exibe o texto do parágrafo na tela
print(paragraph_text)

# Fecha o navegador
driver.quit()