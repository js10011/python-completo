from bs4 import BeautifulSoup

# Abrimos e lemos o arquivo HTML
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Analisamos o conteúdo HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Encontramos todos os elementos input cujo atributo 'name' contém 'user'
user_inputs = soup.find_all('input', attrs={'name': lambda x: x and 'user' in x})

# Extraímos e exibimos os valores dos elementos input encontrados
for input_element in user_inputs:
    print(f"Name: {input_element.get('name')}, Value: {input_element.get('value')}")