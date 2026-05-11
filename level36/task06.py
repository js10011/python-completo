from selenium import webdriver
from selenium.webdriver.common.by import By

# Criar uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrir a página web
driver.get('https://example.com/links_page')

# Encontrar o primeiro link com o texto 'Next Page'
next_page_link = driver.find_element(By.LINK_TEXT, 'Next Page')

# Clicar no link
next_page_link.click()

# Fechar o navegador após navegar para a nova página
driver.quit()