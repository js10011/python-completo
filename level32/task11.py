from bs4 import BeautifulSoup
import csv

# Caminho para o arquivo HTML que será analisado
file_path = "example.html"  # Especifique o caminho para o seu arquivo HTML

# Abrindo o arquivo HTML e lendo seu conteúdo
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Fazendo o parsing do conteúdo HTML
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table')

# Extraindo os cabeçalhos
headers = [th.text for th in table.find_all('th')]

# Extraindo os dados das linhas
rows = []
for row in table.find_all('tr')[1:]:
    cols = [td.text for td in row.find_all('td')]
    rows.append(cols)

# Escrevendo os dados no arquivo CSV
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # escrevendo os cabeçalhos
    writer.writerows(rows)    # escrevendo as linhas de dados