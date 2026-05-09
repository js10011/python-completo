# Ordenação sem Ordenação

# Escreva um programa que crie uma lista de 10 números aleatórios no intervalo de 1 a 100.
# Em seguida, o programa deve criar uma cópia dessa lista e ordenar a cópia em ordem crescente, sem alterar a lista original.
# O programa deve exibir as listas original e ordenada.

# Escreva seu código aqui
import random  

numeros = [random.randint(1, 100) for i in range(10)]
copy = numeros[:]
cres=sorted(numeros)
print(numeros)
print(cres)
