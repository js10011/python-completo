from selenium import webdriver
from selenium.webdriver.common.by import By

# Criando uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrindo a página
driver.get('https://example.com/dynamic_content')

# Procurando o primeiro elemento h1 e imprimindo seu texto
h1_element = driver.find_element(By.TAG_NAME, 'h1')
print(h1_element.text)

# Fechando o navegador
driver.quit()