from selenium import webdriver

# Criar uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrir a página web
driver.get("https://www.example.com")

# Extrair e imprimir o título da página
title = driver.title
print("Título da página:", title)

# Fechar o navegador
driver.quit()