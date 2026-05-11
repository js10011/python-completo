import requests
import time
from itertools import cycle

# Função para carregar a lista de proxies de um arquivo
def load_proxies(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Função para enviar uma requisição de teste para verificar a disponibilidade do proxy
def send_test_request(proxy_url):
    try:
        response = requests.get('http://example.com', proxies={"http": proxy_url, "https": proxy_url}, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Função para filtrar proxies disponíveis
def filter_available_proxies(proxies):
    return [proxy for proxy in proxies if send_test_request(proxy)]

# Função para registrar uma requisição bem-sucedida no log
def log_request(proxy, log_filename):
    with open(log_filename, 'a') as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {proxy}\n")

# Função para realizar requisição através de um proxy dado e registrar seu resultado
def make_request_with_proxy(url, proxy, log_filename):
    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            print(f"Página obtida com sucesso usando o proxy {proxy}")
            log_request(proxy, log_filename)
            return True
    except requests.RequestException:
        print(f"Não foi possível obter a página usando o proxy {proxy}. Passando para o próximo proxy.")
    return False

# Função principal para gerenciar o pool de proxies e enviar requisições
def send_requests_with_proxy_pool(proxies, url, log_filename, request_limit=5):
    proxy_pool = cycle(proxies)
    for _ in range(request_limit):
        proxy = next(proxy_pool)
        if make_request_with_proxy(url, proxy, log_filename):
            continue

# Função principal do programa
def main():
    filename = 'proxies.txt'
    log_filename = 'requests_log.txt'
    url = "http://example.com"

    # Passo 1: Carregar proxies do arquivo
    proxies = load_proxies(filename)

    # Passo 2: Filtrar proxies disponíveis
    available_proxies = filter_available_proxies(proxies)

    # Passo 3: Enviar requisições através do pool de proxies
    send_requests_with_proxy_pool(available_proxies, url, log_filename)

# Executa a função principal
main()