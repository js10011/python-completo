from bs4 import BeautifulSoup

# Caminho para o arquivo HTML que vamos analisar
file_path = "example.html"  # Indique o caminho para o seu arquivo HTML

# Abrimos o arquivo HTML e lemos seu conteúdo
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criação de um objeto BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extração dos cabeçalhos da tabela
headers = [th.text for th in soup.find_all('th')]

# Exibição dos cabeçalhos na tela
print(headers)