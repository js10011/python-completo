def generate_permutations(elements):
    if len(elements) == 1:
        return [elements]
    
    permutations = []
    for i in range(len(elements)):
        current = elements[i]
        remaining = elements[:i] + elements[i+1:]
        for p in generate_permutations(remaining):
            permutations.append([current] + p)
    return permutations

def all_unique_permutations(input_set):
    elements = list(input_set)
    raw_permutations = generate_permutations(elements)
    unique_permutations = []
    for perm in raw_permutations:
        if perm not in unique_permutations:
            unique_permutations.append(perm)
    return unique_permutations

# Exemplo de uso
input_set = {1, 2, 3}
permutations = all_unique_permutations(input_set)
for perm in permutations:
    print(perm)