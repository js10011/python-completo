from requests_html import HTMLSession

# URL da página com elementos de notícias (substitua 'your_url_here' pelo URL real)
url = 'your_url_here'

# Criamos uma sessão para realizar requisições HTTP e renderizar
session = HTMLSession()
response = session.get(url)

# Realizamos a rolagem da página para carregar conteúdo
scroll_count = 5
for _ in range(scroll_count):
    response.html.render(scrolldown=1, sleep=1)  # Rolamos a página e esperamos 1 segundo

# Extraímos o texto dos elementos com a classe 'news-item'
news_items = response.html.find('.news-item')
for item in news_items:
    print(item.text)  # Imprimimos o texto de cada elemento de notícia