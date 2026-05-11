from selenium import webdriver

# Criando uma instância do driver do navegador
driver = webdriver.Chrome()

# Abertura da página inicial
driver.get('https://www.example.com')

# Navegação para outra página
driver.get('https://www.example.org')

# Retorno para a página anterior
driver.back()

# Nova navegação para frente
driver.forward()

# Fechamento do navegador
driver.quit()