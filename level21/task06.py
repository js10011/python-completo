# Abrindo o arquivo no modo de adição com codificação UTF-8
file = open('example.txt', 'a', encoding='utf-8')

# Escrevendo linhas no arquivo
file.write('Nós adicionamos esta linha.\n')
file.write('E esta também.\n')

# Fechando o arquivo
file.close()