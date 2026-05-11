def common_subarray(arr1, arr2):
    return [element for element in arr1 if element in arr2]

# Exemplo de uso
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

result = common_subarray(arr1, arr2)
print(result)