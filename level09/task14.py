import random

# Criando dois conjuntos de números aleatórios
set1 = set(random.randint(1, 20) for _ in range(10))
set2 = set(random.randint(10, 30) for _ in range(10))

# Encontrando a diferença do primeiro conjunto com o segundo
difference = set1.difference(set2)

# Encontrando a diferença simétrica
symmetric_difference = set1.symmetric_difference(set2)

# Exibindo os resultados
print("Primeiro conjunto:", set1)
print("Segundo conjunto:", set2)
print("Diferença do primeiro conjunto com o segundo:", difference)
print("Diferença simétrica:", symmetric_difference)