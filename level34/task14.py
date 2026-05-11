# Importamos a biblioteca para realizar requisições HTTP e configurar retries
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# URL para carregamento de dados
url = "http://example.com"

# Criamos uma sessão para realizar requisições HTTP
session = requests.Session()

# Configuramos a estratégia de tentativas repetidas
retries = Retry(
    total=5,  # Número total de tentativas repetidas
    backoff_factor=1,  # Atraso entre tentativas repetidas
    status_forcelist=[500, 502, 503, 504]  # Repetir para estes códigos de status
)

# Configuramos o adaptador com as configurações de tentativas repetidas
adapter = HTTPAdapter(max_retries=retries)
session.mount('http://', adapter)
session.mount('https://', adapter)

# Tentamos realizar a requisição com timeout de 10 segundos
try:
    response = session.get(url, timeout=10)
    # Verificamos o sucesso da resposta
    response.raise_for_status()  # Gera um erro se o status não for bem-sucedido
    print("Dados carregados com sucesso!")
    data = response.content  # Salvamos o conteúdo da resposta

# Tratamento de todos os possíveis erros de requisição
except requests.exceptions.RequestException as e:
    print(f"Erro ao carregar dados: {e}")