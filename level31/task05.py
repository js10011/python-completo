import requests
from bs4 import BeautifulSoup

# Defina o URL da página que precisa ser carregada
url = 'http://example.com'  # Você pode substituir este URL pelo necessário

# Baixe a página HTML
response = requests.get(url)

# Converta o conteúdo da página em um objeto BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Encontre todas as tags <p> e extraia o texto
paragraphs = soup.find_all('p')

# Exiba o texto de cada parágrafo
for p in paragraphs:
    print(p.get_text())