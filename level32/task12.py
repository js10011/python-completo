from bs4 import BeautifulSoup

# Caminho para o arquivo HTML que será analisado
file_path = "example.html"  # Indique o caminho para o seu arquivo HTML

# Abrimos o arquivo HTML e lemos seu conteúdo
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criamos um objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extraímos dados da tabela
table_fruits = {row.find('td').text for row in soup.find_all('tr')[1:]}

# Extraímos dados da lista
list_fruits = {li.text for li in soup.find_all('ul')[0].find_all('li')}

# Comparamos e obtemos o conjunto comum
common_fruits = list(table_fruits & list_fruits)

# Exibimos o resultado
print(common_fruits)