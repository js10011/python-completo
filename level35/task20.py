from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Criando o web driver para trabalhar com o navegador
driver = webdriver.Chrome()

# Abrindo a página web
driver.get("https://example.com/products")

# Extração de dados usando XPath
start_xpath = time.time()
products_xpath = driver.find_elements(By.XPATH, "//table[@class='product-table']//tr")
xpath_results = []
for product in products_xpath[1:]:  # Pulando o cabeçalho da tabela
    name = product.find_element(By.XPATH, "./td[1]").text
    price = product.find_element(By.XPATH, "./td[2]").text
    xpath_results.append(f"Product: {name}, Price: {price}")
end_xpath = time.time()

# Extração de dados usando seletores CSS
start_css = time.time()
products_css = driver.find_elements(By.CSS_SELECTOR, "table.product-table tr")
css_results = []
for product in products_css[1:]:  # Pulando o cabeçalho da tabela
    name = product.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text
    price = product.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
    css_results.append(f"Product: {name}, Price: {price}")
end_css = time.time()

# Medição e impressão do tempo de execução
xpath_time = end_xpath - start_xpath
css_time = end_css - start_css
print(f"XPath Time: {xpath_time:.4f} seconds")
print(f"CSS Selector Time: {css_time:.4f} seconds")

# Impressão da lista de todos os produtos na tela
print("\nProducts extracted using XPath:")
for item in xpath_results:
    print(item)

print("\nProducts extracted using CSS Selectors:")
for item in css_results:
    print(item)

# Fechando o navegador
driver.quit()