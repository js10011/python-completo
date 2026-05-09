# Média Aleatória

# Escreva um programa que gera 10 números aleatórios no intervalo de 1 a 100, utilizando a biblioteca random.
# Depois, calcule a média deles e exiba na tela.

# Escreva seu código aqui

import random

numbers = [random.randint(1, 100) for _ in range(10)]
average = sum(numbers) / len(numbers)

print("Números aleatórios:", numbers)
print("Valor médio:", average)