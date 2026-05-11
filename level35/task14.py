from selenium import webdriver
from selenium.webdriver.common.by import By

# Criamos uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrimos a página da web
driver.get("https://example.com")

# Procuramos o elemento com a classe 'footer-link'
footer_link_element = driver.find_element(By.CLASS_NAME, 'footer-link')

# Extraímos o URL do elemento-link
footer_link_url = footer_link_element.get_attribute('href')

# Exibimos o URL na tela
print(footer_link_url)

# Fechamos a sessão do navegador
driver.quit()