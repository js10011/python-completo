import requests
from bs4 import BeautifulSoup

# URL para carregar a página HTML
url = "http://example.com"  # substitua pela URL da página que precisa ser carregada

# Carregamento da página HTML
response = requests.get(url)

# Parse da página HTML usando BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Seleção de todos os elementos h2 usando seletores CSS
headers = soup.select('h2')

# Extração e exibição de textos
for header in headers:
    print(header.get_text())