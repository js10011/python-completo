from bs4 import BeautifulSoup

# Carregar o arquivo HTML
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criar o objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extrair todos os div com a classe section
sections = soup.find_all('div', class_='section')

# Iterar por todas as seções encontradas
for section in sections:
    # Extrair o cabeçalho h2
    header = section.find('h2').text
    print(header)

    # Extrair todos os parágrafos p dentro da seção atual
    paragraphs = section.find_all('p')

    # Exibir todos os parágrafos
    for paragraph in paragraphs:
        print(paragraph.text)
    print()  # Linha vazia após cada seção