import random

# Criação do conjunto de 10 números aleatórios no intervalo de 1 a 100
random_numbers = {random.randint(1, 100) for _ in range(10)}

# Obtenção do subconjunto de todos os números pares
even_numbers = {num for num in random_numbers if num % 2 == 0}

# Exibição do subconjunto de números pares
print(even_numbers)