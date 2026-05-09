# Filtragem

# Escreva um programa que cria uma lista de 20 números aleatórios no intervalo de 1 a 100 usando List Comprehension.
# Em seguida, usando List Comprehension, crie uma nova lista contendo apenas números pares da lista original.
# O programa deve imprimir ambas as listas.

# Escreva seu código aqui
import random 

numeros = [random.randint(1, 100) for i in range(20)]
pares = [x for x in numeros if x % 2 == 0]
print(f"Lista original :{numeros}\nLista so com pares : {pares}")