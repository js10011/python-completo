from bs4 import BeautifulSoup

# Carregando o arquivo HTML
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criando um objeto BeautifulSoup para analisar o HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extraindo texto de todas as tags <h1> e <h2>
headings = soup.find_all(['h1', 'h2'])

# Exibindo todos os títulos e subtítulos
for heading in headings:
    print(heading.get_text())