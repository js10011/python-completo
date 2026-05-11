# Importa a biblioteca BeautifulSoup para análise de HTML
from bs4 import BeautifulSoup

# Caminho para o arquivo HTML que vamos analisar
file_path = 'example.html'  # Substitua pelo caminho atual do seu arquivo

# Abre o arquivo HTML e lê seu conteúdo
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Cria um objeto BeautifulSoup para análise do conteúdo HTML
soup = BeautifulSoup(content, 'html.parser')

# Extração de todos os links (tags <a>)
print("Links:")
links = soup.find_all('a')
# Itera sobre cada link
for link in links:
    # Extrai o texto do link, se estiver ausente, exibe "Sem dados"
    text = link.get_text(strip=True) or "Sem dados"
    # Extrai o URL do link, se estiver ausente, exibe "Sem dados"
    url = link.get('href') or "Sem dados"
    # Exibe o texto do link e seu URL
    print(f"Texto: {text}, URL: {url}")

# Extração de todas as imagens (tags <img>)
print("\nImagens:")
images = soup.find_all('img')
# Itera sobre cada imagem
for image in images:
    # Extrai o URL da imagem, se estiver ausente, exibe "Sem dados"
    url = image.get('src') or "Sem dados"
    # Extrai o texto alternativo, se estiver ausente, exibe "Sem dados"
    alt_text = image.get('alt') or "Sem dados"
    # Exibe o URL da imagem e seu texto alternativo
    print(f"URL: {url}, Texto alternativo: {alt_text}")