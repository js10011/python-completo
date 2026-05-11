import bisect

def search(sorted_db, target):
    index = bisect.bisect_left(sorted_db, target)
    if index < len(sorted_db) and sorted_db[index] == target:
        return index
    return -1

# Exemplo de uso
sorted_db = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
result = search(sorted_db, target)
print("Registro encontrado no índice:", result)