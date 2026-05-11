import os

# Obtém a lista de arquivos e diretórios no diretório de trabalho atual
items = os.listdir('.')

# Percorre cada elemento e verifica seu tipo
for item in items:
    if os.path.isdir(item):
        print(f'{item} - Diretório')
    elif os.path.isfile(item):
        print(f'{item} - Arquivo')
    else:
        print(f'{item} - Tipo desconhecido')