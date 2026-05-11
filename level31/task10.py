import requests
from bs4 import BeautifulSoup

# Carregando HTML com requests
url = "http://example.com"
response = requests.get(url)
html_content = response.text

# Analisando HTML com BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extraindo todas as tags <a>
links = soup.find_all('a')

# Exibindo links e seus atributos href
for link in links:
    # Obtendo o atributo href, se existir
    href = link.get('href', None)
    if href:
        print(f"Link: {link.text}, Href: {href}")
    else:
        print(f"Link: {link.text}, Href: None")