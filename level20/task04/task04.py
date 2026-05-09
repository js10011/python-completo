import random
import time

# Geração de um array de 1 milhão de valores aleatórios
array = [random.randint(0, 1000000) for _ in range(1000000)]

# Implementação da função merge_sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Implementação da função quick_sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Ordenação e exibição do tempo de execução para merge_sort
start_time = time.time()
sorted_array_merge = merge_sort(array.copy())
merge_sort_time = time.time() - start_time
print(f"Tempo de Merge Sort: {merge_sort_time} segundos")

# Ordenação e exibição do tempo de execução para quick_sort
start_time = time.time()
sorted_array_quick = quick_sort(array.copy())
quick_sort_time = time.time() - start_time
print(f"Tempo de Quick Sort: {quick_sort_time} segundos")