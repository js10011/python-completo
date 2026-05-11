import numpy as np

# Criamos um array de 10 números aleatórios de 0 a 1000
random_array = np.random.randint(0, 1001, 10)

# Ordenamos o array
sorted_array = np.sort(random_array)

# Exibimos o array ordenado
print(sorted_array)