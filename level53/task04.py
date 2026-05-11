import time
import numpy as np

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def measure_time(search_func, arr, target):
    start_time = time.time()
    search_func(arr, target)
    end_time = time.time()
    return end_time - start_time

n = 20
target = -1  # Alvo que não está no array para garantir busca completa
threshold_found = False

for i in range(n + 1):
    arr_length = 2 ** i
    arr = list(range(arr_length))  # Array ordenado para busca binária
    linear_time = measure_time(linear_search, arr, target)
    binary_time = measure_time(binary_search, arr, target)
    
    print(f"Tamanho do array: {arr_length}, Tempo de busca linear: {linear_time:.6f}, Tempo de busca binária: {binary_time:.6f}")
    
    if binary_time < linear_time and not threshold_found:
        print(f"A busca binária se torna mais eficiente no tamanho do array: {arr_length}")
        threshold_found = True
        break

if not threshold_found:
    print("A busca binária não se tornou mais eficiente dentro do intervalo dado.")