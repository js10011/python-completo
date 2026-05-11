from requests_html import HTMLSession

# Solicita ao usuário o URL da página web
url = input("Digite o URL da página web: ")

# Cria uma sessão para realizar requisições HTTP
session = HTMLSession()

# Tenta realizar a requisição para a página web especificada e extrair o título
try:
    # Executa a requisição GET para a página web
    response = session.get(url)

    # Procura pelo elemento do título (tag <title>) na página
    title_element = response.html.find('title', first=True)

    # Verifica se o elemento do título foi encontrado
    if title_element:
        # Se o título for encontrado, imprime seu texto
        print("Título da página:", title_element.text)
    else:
        # Se o título não for encontrado, imprime uma mensagem
        print("Título não encontrado na página.")

# Tratamento de erros na requisição ou parsing
except Exception as e:
    print("Ocorreu um erro:", e)