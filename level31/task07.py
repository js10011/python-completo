import requests
from bs4 import BeautifulSoup

# Carregar página HTML
url = "http://example.com"  # Substitua pelo URL da sua página
response = requests.get(url)

# Fazer o parsing do HTML com BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar o primeiro link com a classe "external-link"
link = soup.select_one('a.external-link')

# Verificar se o link foi encontrado e exibir seu URL
if link and 'href' in link.attrs:
    print(link['href'])
else:
    print("Link com a classe 'external-link' não encontrado.")