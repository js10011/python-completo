# Solicitando ao usuário os elementos para o primeiro conjunto
set1 = set(map(int, input("Digite os elementos do primeiro conjunto separados por espaço: ").split()))

# Solicitando ao usuário os elementos para o segundo conjunto
set2 = set(map(int, input("Digite os elementos do segundo conjunto separados por espaço: ").split()))

# União dos conjuntos
union_set = set1.union(set2)
print("União dos conjuntos:", union_set)

# Interseção dos conjuntos
intersection_set = set1.intersection(set2)
print("Interseção dos conjuntos:", intersection_set)