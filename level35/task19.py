import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Criamos uma instância do driver do navegador
driver = webdriver.Chrome()

# Abertura da página web
driver.get("https://example.com/products")

# É necessário esperar um pouco para que a página carregue completamente
time.sleep(3)

# Busca da tabela com a classe "product-table"
products_table = driver.find_element(By.CLASS_NAME, "product-table")

# Busca de todas as linhas da tabela
rows = products_table.find_elements(By.CSS_SELECTOR, "tr")

for row in rows:
    # Busca de células na linha
    cells = row.find_elements(By.CSS_SELECTOR, "td")
    if len(cells) >= 2:
        # Extração do nome e preço do produto
        name = cells[0].text
        price = cells[1].text
        # Saída formatada
        print(f"Product: {name}, Price: {price}")

# Fechamento do navegador
driver.quit()