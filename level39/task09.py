import datetime
import os

def generate_report(directory):
    # Obtemos a data e hora atuais
    now = datetime.datetime.now()
    
    # Formatamos o nome do arquivo
    filename = now.strftime("Relatorio_%Y%m%d_%H%M%S.txt")
    
    # Caminho completo para o arquivo
    full_path = os.path.join(directory, filename)
    
    # Criamos e salvamos o arquivo de texto
    with open(full_path, 'w') as file:
        file.write("Este é um relatório gerado automaticamente.\n")
    
    # Exibimos mensagem com o nome do arquivo
    print(f"Arquivo salvo: {filename}")

# Indique aqui o caminho para o diretório onde o arquivo deve ser salvo
directory = "reports"

# Criamos o diretório, caso ele não exista
os.makedirs(directory, exist_ok=True)

# Geramos o relatório
generate_report(directory)