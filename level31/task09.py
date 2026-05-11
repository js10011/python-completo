import requests
from bs4 import BeautifulSoup

# Download do conteúdo HTML da URL especificada
response = requests.get("http://example.com")
html_content = response.text

# Análise do conteúdo HTML com o BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extração e exibição do texto da tag h1
h1_text = soup.find('h1').get_text()
print("Texto do título h1:", h1_text)

# Extração e exibição do texto do primeiro parágrafo
p_text = soup.find('p').get_text()
print("Texto do primeiro parágrafo:", p_text)