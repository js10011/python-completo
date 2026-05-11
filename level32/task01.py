from bs4 import BeautifulSoup

# Carrega o HTML de um arquivo local 'example.html'
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Cria um objeto BeautifulSoup para análise do HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extrai o texto do primeiro <h1>
h1_tag = soup.find('h1')
if h1_tag:
    print(h1_tag.text)
else:
    print("Tag <h1> não encontrada.")