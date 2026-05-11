def insertion_sort_tuples(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key[0] < arr[j][0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Exemplo de uso:
tuples_list = [(3, 'c'), (1, 'a'), (2, 'b'), (4, 'd')]
sorted_list = insertion_sort_tuples(tuples_list)
print(sorted_list)