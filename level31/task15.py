# Importa a biblioteca BeautifulSoup para parsear conteúdo HTML
from bs4 import BeautifulSoup

# Carrega o arquivo HTML
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parseia o conteúdo HTML usando BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Encontra todos os elementos com a classe 'article'
articles = soup.find_all('div', class_='article')

# Cria uma lista vazia para salvar os resultados
results = []

# Itera sobre cada elemento de artigo encontrado
for article in articles:
    # Extrai o título do artigo
    headline = article.find('h3', class_='headline').text
    # Extrai o link do artigo
    link = article.find('a', class_='read-more')['href']
    # Adiciona a string formatada com o título e o link à lista de resultados
    results.append(f"Artigo: {headline}, Link: {link}")

# Imprime cada artigo com seu título e link
for article_info in results:
    print(article_info)