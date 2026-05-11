def sort_desc_bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Exemplo de uso
numbers = [5, 3, 8, 4, 2]
sorted_numbers = sort_desc_bubble(numbers)
print(sorted_numbers)  # Saída: [8, 5, 4, 3, 2]