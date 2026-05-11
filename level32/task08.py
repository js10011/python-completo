# Importa a biblioteca BeautifulSoup para análise de HTML
from bs4 import BeautifulSoup

# Caminho para o arquivo HTML que vamos analisar
file_path = "example.html"  # Indique o caminho para seu arquivo HTML

# Abre o arquivo HTML e lê seu conteúdo
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Cria um objeto BeautifulSoup para analisar o conteúdo HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Encontra todos os títulos <h2> com a classe 'article-title'
titles = soup.find_all('h2', class_='article-title')

# Passa por cada título encontrado
for title in titles:
    # Extrai o texto do título, removendo espaços extras
    title_text = title.get_text(strip=True)
    # Tenta encontrar a tag <a> dentro do título para obter o link
    link_tag = title.find('a')
    # Se a tag <a> existir e contiver o atributo href, extrai a URL
    link_url = link_tag['href'] if link_tag and 'href' in link_tag.attrs else None

    # Exibe a informação no formato especificado
    if title_text and link_url:
        print(f"Title: {title_text}, Link: {link_url}")
    elif title_text:
        print(f"Title: {title_text}, Link: [nenhum link]")
    else:
        print("Title: [nenhum título], Link: [nenhum link]")