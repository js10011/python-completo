from requests_html import HTMLSession

# Especificando a URL da página dinâmica e o seletor CSS para extração
url = 'https://example.com/dynamic-page'  # Exemplo de URL
selector = '.list-item'  # Exemplo de seletor CSS do elemento a ser extraído

# Criando uma nova sessão para fazer requisições HTTP
session = HTMLSession()

# Enviando um pedido GET para a URL especificada
response = session.get(url)

# Executando JavaScript na página para carregar dados dinâmicos
response.html.render()

# Extraindo elementos de acordo com o seletor CSS especificado
elements = response.html.find(selector)

# Percorrendo cada elemento encontrado e exibindo seu conteúdo de texto
for element in elements:
    print(element.text)