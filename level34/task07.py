import requests
from bs4 import BeautifulSoup

# URL inicial da página com as postagens
current_url = 'http://example.com/start'  # Substitua pelo URL inicial real
all_titles = []  # Lista para armazenar todos os títulos

# Loop para iterar pelas páginas com postagens
while current_url:
    # Fazendo uma requisição GET para a página atual
    response = requests.get(current_url)
    # Criando um objeto BeautifulSoup para parsear o conteúdo HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraindo os títulos das postagens, assumindo que estão em tags <h2> com classe 'post-title'
    post_titles = soup.find_all('h2', class_='post-title')
    for title in post_titles:
        # Adicionando o texto do título na lista, removendo espaços extras
        all_titles.append(title.get_text(strip=True))

    # Procurando pelo link para a próxima página com o texto "Próximo"
    next_link = soup.find('a', text='Próximo')
    # Atualizando o URL para a próxima iteração ou terminando o loop se o link "Próximo" não existir
    current_url = next_link.get('href') if next_link else None

# Exibindo todos os títulos coletados
for title in all_titles:
    print(title)