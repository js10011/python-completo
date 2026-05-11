def count_elements(arr):
    element_count = {}
    for element in arr:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    return element_count

# Exemplo de uso:
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(count_elements(arr))  # Output: {1: 1, 2: 2, 3: 3, 4: 4}