from bs4 import BeautifulSoup
import csv

# Carregamento do arquivo HTML
with open('products.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criação do objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Configuração de seletores CSS para extração de dados
product_selector = '.product'
name_selector = '.product-name'
price_selector = '.product-price'

# Extração de dados
products = soup.select(product_selector)
product_data = []

for product in products:
    name = product.select_one(name_selector).get_text(strip=True)
    price = product.select_one(price_selector).get_text(strip=True)
    product_data.append((name, price))
    print(f'Product: {name}, Price: {price}')

# Exportação de dados para CSV
with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Product Name', 'Price'])
    for name, price in product_data:
        csv_writer.writerow([name, price])