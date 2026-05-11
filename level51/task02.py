import array

# Dimensão da matriz
size = 10

# Criação de um array unidimensional para imitar uma matriz 10x10
matrix = array.array('i', (0,) * (size * size))

# Preenchimento do array como uma tabela de multiplicação x * y
for x in range(1, size + 1):
    for y in range(1, size + 1):
        # Indexação através do array unidimensional
        matrix[(x - 1) * size + (y - 1)] = x * y

# Exibição do array na tela em forma de tabela
for x in range(size):
    for y in range(size):
        # Acesso aos elementos do array utilizando indexação
        print(matrix[x * size + y], end='\t')
    print()