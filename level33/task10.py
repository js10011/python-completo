import requests
import random
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Indique sua chave de API 2Captcha
CAPTCHA_API_KEY = 'YOUR_2CAPTCHA_API_KEY'
# URL do site de destino
TARGET_URL = 'https://example.com'

# Função para obter um User-Agent aleatório
def get_random_user_agent():
    return UserAgent().random

# Função para adicionar atraso aleatório
def random_delay():
    delay = random.uniform(2, 5)
    time.sleep(delay)
    print(f"Atraso de {delay:.2f} segundos.")

# Função para solicitar a solução do CAPTCHA
def request_captcha_solution(captcha_site_key, url):
    response = requests.post('http://2captcha.com/in.php', data={
        'key': CAPTCHA_API_KEY,
        'method': 'userrecaptcha',
        'googlekey': captcha_site_key,
        'pageurl': url,
        'json': 1
    }).json()
    return response['request']

# Função para verificar o status da solução do CAPTCHA
def get_captcha_result(captcha_id):
    while True:
        time.sleep(5)
        response = requests.get('http://2captcha.com/res.php', params={
            'key': CAPTCHA_API_KEY,
            'action': 'get',
            'id': captcha_id,
            'json': 1
        }).json()
        if response['status'] == 1:
            return response['request']
        elif response['request'] != 'CAPCHA_NOT_READY':
            raise Exception(f'Erro ao resolver CAPTCHA: {response["request"]}')

# Função para extrair o site-key do HTML
def get_captcha_site_key(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    site_key_element = soup.find('div', {'data-sitekey': True})
    if site_key_element:
        return site_key_element['data-sitekey']
    else:
        raise Exception('Site-key não encontrado na página.')

# Função principal para solicitar a página e resolver o CAPTCHA
def fetch_page_content():
    session = requests.Session()

    # Primeira solicitação para obter a página e o site-key
    random_delay()
    headers = {'User-Agent': get_random_user_agent()}
    response = session.get(TARGET_URL, headers=headers)

    # Verificação e resolução de CAPTCHA se necessário
    if 'site-key' in response.text:
        captcha_site_key = get_captcha_site_key(response.text)
        print("Resolvendo CAPTCHA...")

        # Solicitação de solução do CAPTCHA
        captcha_id = request_captcha_solution(captcha_site_key, TARGET_URL)
        captcha_token = get_captcha_result(captcha_id)

        # Nova solicitação com CAPTCHA resolvido
        random_delay()
        headers = {'User-Agent': get_random_user_agent()}
        response = session.post(TARGET_URL, data={'g-recaptcha-response': captcha_token}, headers=headers)

    return response.text

# Execução do programa
def main():
    try:
        page_content = fetch_page_content()
        print(page_content)
    except Exception as e:
        print("Ocorreu um erro:", e)

main()