from bs4 import BeautifulSoup

# Carregando o arquivo HTML
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criar o objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrar todas as linhas da tabela
rows = soup.find_all('tr')

# Iterar sobre as linhas e células, extraindo o texto
for row in rows:
    cells = row.find_all('td')
    for cell in cells:
        # Usar .get_text() com o parâmetro strip=True para extrair apenas o texto, ignorando tags aninhadas
        cell_text = cell.get_text(strip=True)
        print(cell_text)