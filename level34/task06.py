# Importamos as bibliotecas necessárias para realizar solicitações HTTP e fazer o parsing do HTML
import requests
from bs4 import BeautifulSoup

# URL da página de produtos e número de página para começar
base_url = "http://example.com/products"
page_number = 1

# Iniciamos a iteração pelas páginas
while True:
    # Formamos a URL para a página atual
    url = f"{base_url}?page={page_number}"
    # Realizamos uma solicitação GET para a página
    response = requests.get(url)
    # Criamos um objeto BeautifulSoup para fazer o parsing do conteúdo HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraímos dados dos produtos com a classe 'product'
    products = soup.find_all(class_='product')
    for product in products:
        # Extraímos o nome e o preço do produto
        name = product.find(class_='name').text.strip()  # Supõe-se que a classe 'name' contém o nome
        price = product.find(class_='price').text.strip()  # Supõe-se que a classe 'price' contém o preço
        print(f"Nome: {name}, Preço: {price}")

    # Verificamos se há um link "Próximo" para ir para a próxima página
    next_link = soup.find('a', text='Próximo')
    if not next_link:
        break  # Se não houver link "Próximo", terminamos a iteração pelas páginas

    # Passamos para a próxima página
    page_number += 1