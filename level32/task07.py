# Importamos a biblioteca BeautifulSoup para parsear HTML
from bs4 import BeautifulSoup

# Caminho para o arquivo HTML que será analisado
file_path = "example.html"  # Indique o caminho para o seu arquivo HTML

# Abrimos o arquivo HTML e lemos seu conteúdo
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criamos um objeto BeautifulSoup para parsear o conteúdo HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Procuramos a tabela com a classe 'data-table'
table = soup.find('table', class_='data-table')

# Se a tabela não for encontrada, exibimos uma lista vazia de dados
table_data = []
if table:
    # Encontramos todas as linhas da tabela (tags <tr>)
    rows = table.find_all('tr')

    # Percorremos cada linha
    for row in rows:
        # Extraímos todas as células da linha (tags <td>)
        cells = row.find_all('td')
        # Extraímos o texto de cada célula e formamos uma lista de dados para a linha
        row_data = [cell.get_text(strip=True) for cell in cells]
        # Adicionamos a lista da linha na lista geral de dados, se a linha não estiver vazia
        if row_data:
            table_data.append(row_data)

# Exibimos os dados obtidos da tabela
print(table_data)