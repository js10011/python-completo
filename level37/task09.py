from selenium import webdriver
from selenium.webdriver.common.by import By

# Criando uma instância do driver do navegador
driver = webdriver.Chrome()

# Carregamento da página web
driver.get('https://example.com')  # Substitua pela URL desejada

# Busca de elementos pelo seletor CSS
css_selector = 'your-css-selector'  # Substitua pelo seletor CSS desejado
elements = driver.find_elements(By.CSS_SELECTOR, css_selector)

# Extração e impressão dos textos dos elementos
for element in elements:
    print(element.text)

# Fechamento do navegador
driver.quit()