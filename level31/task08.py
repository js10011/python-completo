import requests
from bs4 import BeautifulSoup

# Carrega a página HTML
url = "http://example.com"
response = requests.get(url)

# Cria um objeto BeautifulSoup para fazer o parsing do HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Extrai o texto do título da página
title_text = soup.title.string

# Exibe o texto do título
print(title_text)