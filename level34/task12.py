import urllib3
from urllib3.util import Retry
from urllib3.exceptions import HTTPError

# URL para solicitação de dados
url = "https://example.com"

# Criar um objeto PoolManager para gerenciar as solicitações
http = urllib3.PoolManager()

# Configurar parâmetros de tentativas repetidas
retries = Retry(
    total=3,  # Número total de tentativas repetidas
    backoff_factor=1,  # Atraso entre as tentativas
    status_forcelist=[500, 502, 503, 504]  # Repetir para esses códigos de status
)

# Envolver PoolManager em uma configuração de tentativas repetidas
http = urllib3.PoolManager(retries=retries)

# Tentar executar a solicitação GET para a URL especificada
try:
    response = http.request('GET', url)
    # Exibir o status da resposta e os dados
    print("Dados obtidos com sucesso!")
    print("Código de status:", response.status)
    print("Dados da resposta:", response.data.decode('utf-8'))

# Tratar possíveis erros HTTP
except HTTPError as e:
    print("Ocorreu um erro HTTP:", e)

# Tratar erros gerais
except Exception as e:
    print("Ocorreu um erro:", e)