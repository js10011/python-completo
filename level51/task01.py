import array
import random

# Criamos um array com tipo de elementos 'i' (números inteiros)
arr = array.array('i')

# Adicionamos 10 números aleatórios de 0 a 1000
for _ in range(10):
    arr.append(random.randint(0, 1000))

# Ordenamos o array
arr = array.array('i', sorted(arr))

# Imprimimos o array
print(arr)