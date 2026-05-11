def selection_sort_by_length(strings):
    n = len(strings)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if len(strings[j]) < len(strings[min_idx]):
                min_idx = j
        strings[i], strings[min_idx] = strings[min_idx], strings[i]
    return strings

# Exemplo de uso
strings = ["apple", "dog", "banana", "cat", "elephant"]
sorted_strings = selection_sort_by_length(strings)
print(sorted_strings)  # ['dog', 'cat', 'apple', 'banana', 'elephant']