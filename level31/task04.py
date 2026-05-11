import requests
from bs4 import BeautifulSoup

# URL para download
url = 'https://example.com'

# Realizando uma solicitação HTTP para obter o código HTML da página
response = requests.get(url)

# Parsing do código HTML com BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extraindo o título da página
title = soup.title.string if soup.title else 'Título não encontrado'

# Exibindo o título da página
print('Título da página:', title)