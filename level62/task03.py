def find_subsets(arr, target, index=0, current_subset=[]):
    # Caso base: se o alvo for atingido, imprima o subconjunto atual
    if sum(current_subset) == target:
        print(current_subset)
        return True
    if index >= len(arr):
        return False

    # Inclua o elemento atual no subconjunto
    if find_subsets(arr, target, index + 1, current_subset + [arr[index]]):
        return True
    
    # Exclua o elemento atual do subconjunto
    if find_subsets(arr, target, index + 1, current_subset):
        return True
    
    return False

# Exemplo de uso
arr = [3, 34, 4, 12, 5, 2]
target = 9
find_subsets(arr, target)