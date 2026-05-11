import http.client
import json

def make_post_request(host, endpoint, data):
    try:
        # Estabelecer conexão com o host
        connection = http.client.HTTPConnection(host)
        
        # Converter dados para formato JSON
        json_data = json.dumps(data)
        
        # Cabeçalhos para a requisição POST
        headers = {'Content-type': 'application/json'}
        
        # Executar a requisição POST
        connection.request('POST', endpoint, body=json_data, headers=headers)
        
        # Obter resposta
        response = connection.getresponse()
        
        # Ler e retornar dados da resposta
        return response.status, response.reason, response.read().decode()
    
    except Exception as e:
        # Tratamento de erros
        return None, None, f'Error: {e}'
    
    finally:
        # Fechar conexão
        connection.close()

# Exemplo de uso da função
host = 'example.com'
endpoint = '/api/data'
data = {'key': 'value'}

status, reason, response = make_post_request(host, endpoint, data)
print(f'Status: {status}')
print(f'Reason: {reason}')
print(f'Response: {response}')