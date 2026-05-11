# Importando a biblioteca BeautifulSoup para fazer parsing de HTML
from bs4 import BeautifulSoup

# Nome do arquivo HTML que vamos ler
html_filename = 'example.html'  # Substitua pelo nome do seu arquivo HTML
# Nome do arquivo de saída para gravar os resultados
output_filename = 'output.txt'

# Abrimos o arquivo HTML e lemos seu conteúdo
with open(html_filename, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Fazemos o parsing do conteúdo HTML com BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Encontramos todos os elementos <p> dentro das classes content e highlighted-content
content_paragraphs = soup.select('.content p')
highlighted_paragraphs = soup.select('.highlighted-content p')

# Criamos uma lista vazia para armazenar as informações dos parágrafos
paragraphs_info = []

# Percorremos todos os parágrafos encontrados na classe content
for p in content_paragraphs:
    # Adicionamos o texto do parágrafo com informações sobre sua classe
    paragraphs_info.append(f"Class: content\n{p.get_text(strip=True)}\n")

# Percorremos todos os parágrafos encontrados na classe highlighted-content
for p in highlighted_paragraphs:
    # Adicionamos o texto do parágrafo com informações sobre sua classe
    paragraphs_info.append(f"Class: highlighted-content\n{p.get_text(strip=True)}\n")

# Gravamos todos os parágrafos extraídos no arquivo de saída
with open(output_filename, 'w', encoding='utf-8') as file:
    for paragraph in paragraphs_info:
        # Escrevemos cada parágrafo em uma nova linha
        file.write(paragraph + "\n")