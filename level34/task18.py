# Importamos as bibliotecas para realizar solicitações HTTP, cache e logging
import requests
import requests_cache
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuração de cache com requests-cache (tempo de vida do cache de 90 segundos)
requests_cache.install_cache('comments_cache', expire_after=90)

# URL para solicitação de comentários
url = "https://jsonplaceholder.typicode.com/comments"

# Realizamos a solicitação à API com verificação de cache
try:
    response = requests.get(url)

    # Verificamos se os dados foram obtidos do cache
    if response.from_cache:
        logging.info("Dados extraídos do cache")
    else:
        logging.info("Dados obtidos do servidor")

    # Verificamos a presença de erros HTTP
    response.raise_for_status()
    comments = response.json()  # Salvamos os dados na variável

except requests.exceptions.RequestException as e:
    logging.error(f"Erro ao extrair dados: {e}")
    comments = None

# Exibimos a quantidade de comentários obtidos, se foram extraídos com sucesso
if comments:
    print(f"Quantidade de comentários obtidos: {len(comments)}")
else:
    print("Não foi possível obter os comentários.")