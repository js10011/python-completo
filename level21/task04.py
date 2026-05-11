# Abertura do arquivo em modo de leitura
file = open('example.txt', 'r')

# Leitura do arquivo linha por linha e exibição do conteúdo
for line in file:
    print(line, end='')

# Fechamento do arquivo
file.close()