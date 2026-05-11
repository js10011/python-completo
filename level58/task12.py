def in_place_quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        in_place_quick_sort(arr, low, pivot_index - 1)
        in_place_quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Exemplo de uso
arr = [3, 6, 8, 10, 1, 2, 1]
in_place_quick_sort(arr, 0, len(arr) - 1)
print(arr)