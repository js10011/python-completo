import requests
import base64
import time

# Especifica-se a chave de API para o serviço 2Captcha e a URL da imagem CAPTCHA
API_KEY = 'SEU_API_KEY_2CAPTCHA'  # Substitua pela sua real chave de API
CAPTCHA_URL = 'URL_IMAGEM_CAPTCHA'  # Substitua pelo real URL da imagem CAPTCHA

# Carrega a imagem CAPTCHA
captcha_image = requests.get(CAPTCHA_URL).content

# Codifica a imagem CAPTCHA em base64
captcha_base64 = base64.b64encode(captcha_image).decode('utf-8')

# Envia a imagem para resolução no serviço 2Captcha
response = requests.post(
    'http://2captcha.com/in.php',
    data={
        'key': API_KEY,
        'method': 'base64',
        'body': captcha_base64,  # Passa a imagem CAPTCHA codificada em base64
        'json': 1  # Solicita resposta no formato JSON
    }
)

# Obtém o identificador da solicitação para resolução do CAPTCHA
request_id = response.json().get('request')

# Inicia o loop de verificação do status da resolução do CAPTCHA
while True:
    # Envia solicitação para verificar o status da resolução
    result = requests.get(f'http://2captcha.com/res.php?key={API_KEY}&action=get&id={request_id}&json=1').json()

    # Se o CAPTCHA estiver resolvido, exibe a solução
    if result.get('status') == 1:
        captcha_solution = result.get('request')
        print("Solução do CAPTCHA:", captcha_solution)
        break
    # Se a solução ainda não estiver pronta, aguarda 5 segundos e repete a solicitação
    elif result.get('request') == 'CAPCHA_NOT_READY':
        time.sleep(5)
    # Se ocorreu um erro, exibe a mensagem e para a execução
    else:
        raise Exception('Erro ao resolver CAPTCHA: ' + result.get('request'))