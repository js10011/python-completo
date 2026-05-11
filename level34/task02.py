from bs4 import BeautifulSoup

# Carregamento do arquivo HTML
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Cria um objeto BeautifulSoup para parsing do documento HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extrai todos os elementos <li> do documento
li_elements = soup.find_all('li')

# Imprime o texto de todos os elementos <li> encontrados
for li in li_elements:
    print(li.get_text(strip=True))