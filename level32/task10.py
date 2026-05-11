from bs4 import BeautifulSoup

# Caminho para o arquivo HTML que será analisado
file_path = "example.html"  # Especifique o caminho para o seu arquivo HTML

# Abrindo o arquivo HTML e lendo seu conteúdo
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criação do objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extração dos elementos da lista <li>
list_items = soup.find_all('li')

# Formação de uma lista Python a partir do texto dos elementos
fruits = [item.get_text() for item in list_items]

# Exibição do resultado
print(fruits)