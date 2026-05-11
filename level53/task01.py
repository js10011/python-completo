def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

# Exemplo de uso:
# arr = [10, 20, 30, 40, 50]
# target = 30
# print(linear_search(arr, target))  # Saída: 2