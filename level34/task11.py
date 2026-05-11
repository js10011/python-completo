import requests

# Especifica o URL da página que precisa ser carregada
url = "https://example.com"

# Tenta realizar a requisição GET para o URL especificado
try:
    response = requests.get(url)
    # Verifica se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        html_content = response.text
        print("Página carregada com sucesso.")
    else:
        # Se o código de resposta não for 200, exibe uma mensagem com o código de erro
        print(f"Não foi possível carregar a página. Código de resposta: {response.status_code}")
        html_content = None

# Trata possíveis erros de conexão
except requests.exceptions.RequestException as e:
    print(f"Erro de conexão: {e}")
    html_content = None