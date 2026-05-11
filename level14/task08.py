import platform
import socket

print("Nome do sistema operacional:", platform.system())
print("Nome do computador na rede (hostname):", socket.gethostname())
print("Versão do sistema operacional:", platform.version())
print("Arquitetura do processador:", platform.architecture()[0])
print("Versão do Python:", platform.python_version())