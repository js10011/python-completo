# Abre o arquivo de origem para leitura em modo binário
with open('source.txt', 'rb') as source_file:
    # Lê o conteúdo do arquivo de origem
    content = source_file.read()

# Abre o arquivo de destino para escrita em modo binário
with open('destination.txt', 'wb') as destination_file:
    # Escreve o conteúdo no arquivo de destino
    destination_file.write(content)