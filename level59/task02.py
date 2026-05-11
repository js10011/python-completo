
def count_occurrences(arr):
    count_dict = {}
    for elem in arr:
        if elem in count_dict:
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1
    return count_dict

# Exemplo de uso:
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(count_occurrences(arr))