from selenium import webdriver

# Cria uma instância do driver do navegador
driver = webdriver.Chrome()

# Abre a página www.example.com
driver.get("http://www.example.com")

# Extrai o título da página
title = driver.title
print("Título da página:", title)

# Fecha o navegador
driver.quit()