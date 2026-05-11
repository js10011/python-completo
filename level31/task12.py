from bs4 import BeautifulSoup

# Carregando o arquivo HTML
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criando um objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrando todos os elementos <p>
paragraphs = soup.find_all('p')

# Exibindo o texto de cada elemento <p>
for p in paragraphs:
    print(p.get_text())