def remove_duplicates(sorted_arr):
    if not sorted_arr:
        return []
    
    unique_arr = [sorted_arr[0]]
    
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] != sorted_arr[i - 1]:
            unique_arr.append(sorted_arr[i])
    
    return unique_arr

# Exemplo de uso
sorted_arr = [1, 1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(sorted_arr))  # Output: [1, 2, 3, 4, 5]