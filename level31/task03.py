# Importamos a biblioteca para realizar requisições HTTP
import urllib.request

# URL do qual vamos obter o código HTML
url = "https://example.com"

# Abrimos o URL e lemos o código HTML
with urllib.request.urlopen(url) as response:
    # Lemos o conteúdo da página
    html_code = response.read()

# Decodificamos o código HTML para o formato de string e exibimos na tela
print(html_code.decode('utf-8'))