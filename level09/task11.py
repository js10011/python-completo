import random

# Criamos um conjunto de números aleatórios no intervalo de 1 a 50
random_set = {random.randint(1, 50) for _ in range(10)}

# Imprimimos os elementos do conjunto junto com seus "índices"
for index, value in enumerate(random_set):
    print(f"{index}: {value}")