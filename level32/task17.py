import logging
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout

# Configuramos o logging, especificando o arquivo para registrar erros e o formato das mensagens
logging.basicConfig(filename='scraper.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Especificamos a URL que vamos escanear
url = "http://example.com"

# Tentamos realizar uma requisição GET para a URL especificada com timeout de 5 segundos
try:
    response = requests.get(url, timeout=5)
    # Verificamos o status da resposta; se não for bem-sucedido, ocorrerá um erro HTTP
    response.raise_for_status()
    # Se a requisição for bem-sucedida, salvamos o conteúdo da página
    page_content = response.text

# Tratamento de exceções quando ocorre um erro HTTP
except HTTPError as http_err:
    logging.error(f'Ocorreu um erro HTTP: {http_err}')

# Tratamento de exceções quando ocorre um erro de conexão
except ConnectionError as conn_err:
    logging.error(f'Ocorreu um erro de conexão: {conn_err}')

# Tratamento de exceções quando ocorre um timeout
except Timeout as timeout_err:
    logging.error(f'Ocorreu um timeout: {timeout_err}')

# Tratamento geral de todos os outros erros
except Exception as err:
    logging.error(f'Ocorreu um erro: {err}')