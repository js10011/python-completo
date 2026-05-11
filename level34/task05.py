import requests
from bs4 import BeautifulSoup

# URL para a primeira página do blog e lista geral para armazenar todos os títulos
base_url = "http://example.com/blog?page="
all_titles = []

# Percorremos as três primeiras páginas do blog
for page in range(1, 4):
    # Formamos o URL para a página atual
    url = base_url + str(page)
    # Fazemos uma requisição GET para a página
    response = requests.get(url)
    # Criamos um objeto BeautifulSoup para parsear o conteúdo HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraímos os títulos dos artigos localizados nas tags h2 com classe 'post-title'
    titles = soup.find_all('h2', class_='post-title')

    # Adicionamos o texto de cada título na lista geral, removendo espaços em excesso
    all_titles.extend([title.get_text(strip=True) for title in titles])

# Exibimos todos os títulos dos artigos
for title in all_titles:
    print(title)