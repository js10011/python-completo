import http.client

def get_request(host, path):
    try:
        connection = http.client.HTTPConnection(host)
        connection.request("GET", path)
        response = connection.getresponse()
        
        if response.status == 200:
            data = response.read()
            print(data.decode('utf-8'))
        else:
            print(f"Erro: {response.status}, {response.reason}")

    except http.client.HTTPException as e:
        print(f"Erro de HTTP ocorreu: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        connection.close()

# Exemplo de uso
host = "example.com"
path = "/"
get_request(host, path)