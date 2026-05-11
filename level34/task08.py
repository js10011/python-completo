import requests

# Função para enviar uma requisição para obter comentários via URL
def fetch_comments_page(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

# Função para verificar se há uma próxima página nos dados
def has_next_page(data):
    return 'next_page' in data and data['next_page']

# Função para atualizar os parâmetros da requisição para a próxima página
def update_params_for_next_page(params, next_page):
    params.update({'page': next_page})
    return params

# Função para extrair todos os comentários usando requisição paginada
def get_all_comments(url, initial_params=None):
    if initial_params is None:
        initial_params = {}

    comments = []
    params = initial_params.copy()

    while True:
        data = fetch_comments_page(url, params)
        comments.extend(data.get('comments', []))

        # Verifique se existe a próxima página
        if not has_next_page(data):
            break

        # Atualiza os parâmetros para a próxima página
        params = update_params_for_next_page(params, data['next_page'])

    return comments

# Função para exibir o autor e o texto do comentário
def print_comment_details(comment):
    author = comment.get('author', 'Anonymous')
    text = comment.get('text', '')
    print(f"Autor: {author}")
    print(f"Comentário: {text}\n")

# Função principal para carregar e exibir todos os comentários
def main():
    comments_url = "https://example.com/api/comments"
    initial_params = {'page': 1}  # Página inicial para paginação

    all_comments = get_all_comments(comments_url, initial_params)

    # Exibe o autor e o texto de cada comentário
    for comment in all_comments:
        print_comment_details(comment)

main()