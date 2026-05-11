from bs4 import BeautifulSoup

# Carregamento do arquivo HTML
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criação do objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Busca por todos os produtos
products = soup.find_all('div', class_='product')

# Processamento de cada produto
for product in products:
    # Extração do nome do produto
    title = product.find('h3').text

    # Extração do preço do produto
    price = product.find('span', class_='price').text

    # Extração da descrição do produto
    description = product.find('p').text

    # Verificação da presença e extração da informação de desconto
    discount_tag = product.find('div', class_='discount')
    discount = discount_tag.text if discount_tag else 'No discount'

    # Exibição das informações do produto
    print(f"Title: {title}, Price: {price}, Discount: {discount}")