import numpy as np

# Criando o array 10x10
array = np.fromfunction(lambda i, j: (i + 1) * (j + 1), (10, 10), dtype=int)

# Exibindo o array na tela
print(array)