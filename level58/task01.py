def bubble_sort_by_length(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(arr[j]) > len(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Exemplo de uso
strings = ["apple", "banana", "kiwi", "cherry", "mango"]
sorted_strings = bubble_sort_by_length(strings)
print(sorted_strings)