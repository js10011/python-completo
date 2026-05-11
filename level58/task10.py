def quick_sort(arr, pivot_selection):
    if len(arr) <= 1:
        return arr
    pivot = pivot_selection(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left, pivot_selection) + middle + quick_sort(right, pivot_selection)

# 5 variantes de escolha do pivô

# 1. Primeiro elemento
pivot_first = lambda arr: arr[0]

# 2. Último elemento
pivot_last = lambda arr: arr[-1]

# 3. Elemento do meio
pivot_middle = lambda arr: arr[len(arr) // 2]

# 4. Elemento aleatório
import random
pivot_random = lambda arr: arr[random.randint(0, len(arr) - 1)]

# 5. Mediana de três (primeiro, meio, último)
pivot_median_three = lambda arr: sorted([arr[0], arr[len(arr) // 2], arr[-1]])[1]

# Exemplo de uso:
arr = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(arr, pivot_first))
print(quick_sort(arr, pivot_last))
print(quick_sort(arr, pivot_middle))
print(quick_sort(arr, pivot_random))
print(quick_sort(arr, pivot_median_three))