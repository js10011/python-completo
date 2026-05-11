from bs4 import BeautifulSoup

# Carregamento do arquivo HTML
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criação do objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Uso do seletor CSS para buscar todos os elementos <a> dentro do elemento com a classe "navigation"
navigation_links = soup.select('.navigation a')

# Extração e exibição de links
for link in navigation_links:
    print(link.get('href'))