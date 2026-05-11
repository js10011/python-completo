# Importamos a biblioteca BeautifulSoup para parsing de HTML
from bs4 import BeautifulSoup

# Abrimos o arquivo HTML para leitura do conteúdo
with open('example.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Criamos um objeto BeautifulSoup para parsing do conteúdo HTML
soup = BeautifulSoup(content, 'html.parser')

# Encontramos todas as tags <img> no código HTML
images = soup.find_all('img')

# Iteramos por cada tag <img> encontrada
for img in images:
    # Obtemos o valor do atributo src (link da imagem)
    src = img.get('src')
    # Obtemos o valor do atributo alt, se estiver ausente - retornamos None
    alt = img.get('alt', None)

    # Verificamos se o atributo src existe
    if src:
        # Se o atributo alt existir, exibimos o URL e o texto
        if alt:
            print(f"URL da imagem: {src}, Texto alternativo: {alt}")
        else:
            # Alertamos se o atributo alt estiver ausente
            print(f"URL da imagem: {src}, Texto alternativo: [AVISO: atributo alt ausente]")
    else:
        # Se o atributo src estiver ausente, exibimos uma mensagem de erro
        print("Atributo src não encontrado para a tag <img>.")