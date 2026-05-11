import time
import random
import bisect

# Criar um array de 1000 elementos aleatórios
arr = [random.randint(1, 10000) for _ in range(1000)]

# Método 1: Usar a busca linear 10 vezes
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

start_time = time.time()
for _ in range(10):
    target = random.choice(arr)
    linear_search(arr, target)
linear_search_time = time.time() - start_time

# Método 2: Ordenar o array + usar a busca binária 10 vezes
sorted_arr = sorted(arr)

def binary_search(arr, target):
    index = bisect.bisect_left(arr, target)
    if index != len(arr) and arr[index] == target:
        return index
    return -1

start_time = time.time()
for _ in range(10):
    target = random.choice(sorted_arr)
    binary_search(sorted_arr, target)
binary_search_time = time.time() - start_time

# Exibir os resultados
print(f"Tempo de busca linear: {linear_search_time:.6f} segundos")
print(f"Tempo de busca binária após ordenação: {binary_search_time:.6f} segundos")