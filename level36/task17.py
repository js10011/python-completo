# Importamos a biblioteca para gerenciar o navegador web
from selenium import webdriver

# Inicialização do web driver
driver = webdriver.Chrome()

# Abertura do URL especificado
driver.get("http://example.com")

# Fechamento do navegador e encerramento da sessão
driver.quit()