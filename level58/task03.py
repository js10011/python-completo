def insertion_sort(strings):
    for i in range(1, len(strings)):
        key = strings[i]
        j = i - 1
        while j >= 0 and strings[j] > key:
            strings[j + 1] = strings[j]
            j -= 1
        strings[j + 1] = key
    return strings

# Exemplo de uso:
strings = ["banana", "apple", "cherry", "date"]
sorted_strings = insertion_sort(strings)
print(sorted_strings)  # Output: ['apple', 'banana', 'cherry', 'date']