from bs4 import BeautifulSoup

# Abrir e ler o conteúdo do arquivo HTML
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criar um objeto BeautifulSoup para analisar o HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrar todos os elementos com a tag <a>
a_tags = soup.find_all('a')

# Extrair os atributos href de cada elemento encontrado
hrefs = [a.get('href') for a in a_tags]

# Exibir a lista de atributos href
for href in hrefs:
    print(href)