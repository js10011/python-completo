import requests

# Exemplo: presume-se que você já obteve cookies da aba Application no DevTools
cookies = {
    'session_id': 'your_session_id',
    'auth_token': 'your_auth_token'
}

# URL da página protegida
url = 'https://example.com/protected-page'

# Envio de uma solicitação GET com cookies
response = requests.get(url, cookies=cookies)

# Verificação do sucesso da solicitação
if response.status_code == 200:
    # Exibição dos dados na tela
    print("Dados da página protegida:")
    print(response.text)
else:
    print("Não foi possível acessar a página protegida. Código de erro:", response.status_code)