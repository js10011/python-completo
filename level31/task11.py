import requests
from bs4 import BeautifulSoup

# URL para extrair os dados
url = "http://example.com"

# Realiza uma solicitação GET para o URL especificado
response = requests.get(url)

# Analisa o documento HTML com o BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extrai e exibe todos os cabeçalhos (h1, h2, h3)
for heading in soup.find_all(['h1', 'h2', 'h3']):
    # Obtém o texto do cabeçalho e o exibe
    print(heading.get_text())

# Extrai e exibe o conteúdo de todos os parágrafos
for paragraph in soup.find_all('p'):
    # Obtém o texto do parágrafo
    paragraph_text = paragraph.get_text()
    # Exibe o texto somente se tiver mais de 100 caracteres
    if len(paragraph_text) > 100:
        print(paragraph_text)