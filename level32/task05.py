from bs4 import BeautifulSoup

# Abrindo o arquivo HTML e lendo seu conteúdo
with open('document.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criando um objeto BeautifulSoup para fazer o parsing do HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrando o primeiro elemento <p>
first_paragraph = soup.find('p')

# Extraindo e exibindo o conteúdo de texto do elemento <p> encontrado
if first_paragraph:
    print(first_paragraph.get_text())