# Importamos a biblioteca BeautifulSoup para análise do HTML
from bs4 import BeautifulSoup

# Abrimos o arquivo HTML e lemos seu conteúdo
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criamos um objeto BeautifulSoup para análise do conteúdo HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Encontramos todas as tags <a> no código HTML
a_tags = soup.find_all('a')

# Extraímos os links de cada tag <a>, obtendo os valores do atributo href
links = [a.get('href') for a in a_tags if a.get('href')]

# Exibimos cada link em uma nova linha
for link in links:
    print(link)