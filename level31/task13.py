from bs4 import BeautifulSoup

# Carregando o arquivo HTML
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criando um objeto BeautifulSoup para analisar o HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrando todas as tags <a> com a classe link
links = soup.find_all('a', class_='link')

# Extraindo os valores dos atributos href
hrefs = [link['href'] for link in links]

# Exibindo os links extraídos
for href in hrefs:
    print(href)