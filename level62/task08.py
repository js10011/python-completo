def nth_minimum(arr, n):
    if n <= 0 or len(arr) < n:
        return None 

    sorted_arr = sorted(arr)
    return sorted_arr[n-1]

# Exemplo de uso:
arr = [7, 2, 5, 3, 9, 1]
n = 3
print(nth_minimum(arr, n))  # Output: 3