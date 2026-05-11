import random

# Geração de listas de elementos aleatórios
list1 = [random.randint(0, 99) for _ in range(100)]
list2 = [random.randint(50, 125) for _ in range(100)]

# Conversão das listas em conjuntos
set1 = set(list1)
set2 = set(list2)

# União dos conjuntos
combined_set = set1.union(set2)

# Exibição da quantidade de elementos do conjunto resultante
print(len(combined_set))