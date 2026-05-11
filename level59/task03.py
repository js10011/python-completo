def find_two_numbers(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return arr[left], arr[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

# Exemplo de uso
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
result = find_two_numbers(sorted_array, target)
if result:
    print(f"A soma dos números {result[0]} e {result[1]} é igual a {target}")
else:
    print(f"Não foram encontrados pares de números cuja soma seja {target}")