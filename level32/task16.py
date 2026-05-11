import requests

# Define a URL para checar
url = "http://example.com/some-nonexistent-page"

# Tenta realizar um GET request para a URL indicada
try:
    # Realiza um GET request e verifica o status da resposta
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    # Se a solicitação for bem sucedida, exibe informação sobre a disponibilidade da página
    print("Página disponível:", url)

# Tratamento de exceções de erros HTTP com exibição detalhada pelo código de erro
except requests.exceptions.HTTPError as http_err:
    status_code = http_err.response.status_code
    if status_code == 404:
        print(f"Erro 404: Página não encontrada no endereço {url}")
    elif status_code == 403:
        print(f"Erro 403: Acesso à página proibido no endereço {url}")
    elif status_code == 500:
        print(f"Erro 500: Erro interno do servidor no endereço {url}")
    else:
        print(f"Ocorreu um erro HTTP {status_code}: {http_err}")

# Tratamento de erros de conexão de rede
except requests.exceptions.ConnectionError:
    print(f"Erro de conexão: Não foi possível conectar ao {url}")

# Tratamento de tempo limite de solicitação
except requests.exceptions.Timeout:
    print(f"Erro: O tempo de espera da solicitação para {url} expirou")

# Tratamento geral de todos os outros erros
except Exception as err:
    print(f"Ocorreu um erro: {err}")