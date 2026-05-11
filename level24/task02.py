import http.client

# Proxy server
proxy_host = "proxy.example.com"
proxy_port = 8080

# Servidor de destino e solicitação
target_host = "www.example.com"
target_path = "/"

# Estabelecendo conexão com o proxy server
conn = http.client.HTTPConnection(proxy_host, proxy_port)

# Enviando solicitação GET através do proxy server
conn.request("GET", target_path, headers={"Host": target_host})

# Obtendo resposta
response = conn.getresponse()

# Imprimindo status e dados da resposta
print(response.status, response.reason)
data = response.read()
print(data.decode('utf-8'))

# Fechando conexão
conn.close()