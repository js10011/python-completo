from bs4 import BeautifulSoup

# Carregamento do arquivo HTML
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criação do objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Uso do seletor CSS para buscar todos os títulos (tags h2) com a classe "headline"
headlines = soup.select('h2.headline')

# Extração e impressão dos títulos
for headline in headlines:
    print(headline.get_text())