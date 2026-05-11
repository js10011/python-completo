from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializamos o driver do Chrome
driver = webdriver.Chrome()

# Abrimos a URL
driver.get("https://example.com/products")

# Criamos um conjunto para armazenar produtos únicos
products = set()
last_height = driver.execute_script("return document.body.scrollHeight")

# Loop infinito para rolar e buscar produtos
while True:
    # Extraímos elementos com nomes e preços dos produtos
    names = driver.find_elements(By.CLASS_NAME, "product-name")
    prices = driver.find_elements(By.CLASS_NAME, "product-price")

    # Adicionamos os produtos encontrados ao conjunto, evitando duplicatas
    for name, price in zip(names, prices):
        product = (name.text, price.text)
        products.add(product)

    # Rolamos a página para baixo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Esperamos para que novos produtos possam carregar
    time.sleep(2)

    # Verificamos se a altura da página mudou após a rolagem
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  # Paramos se a altura da página não mudou
    last_height = new_height

# Exibimos os resultados
for name, price in products:
    print(f"Nome do produto: {name}, Preço: {price}")

# Fechamos o navegador
driver.quit()