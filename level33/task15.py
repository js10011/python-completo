from requests_html import HTMLSession

# URL da página com conteúdo dinâmico, carregado através de JavaScript
url = 'https://your-example-website.com/path-to-page-with-dynamic-content'

# Criamos uma sessão para executar solicitações HTTP e renderização
session = HTMLSession()
response = session.get(url)

# Executamos JavaScript na página para carregar conteúdo dinâmico
response.html.render()

# Extraímos o texto do elemento com id 'dynamic-content'
dynamic_content = response.html.find('#dynamic-content', first=True).text

# Imprimimos o conteúdo dinâmico extraído
print(dynamic_content)