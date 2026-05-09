# Ordenações

# Escreva um programa que cria uma lista de 10 números aleatórios no intervalo de 1 a 100.
# Em seguida, ordene-a em ordem crescente e decrescente.
# O programa deve exibir a lista original, as listas ordenadas em ordem crescente e decrescente.

# Escreva seu código aqui
import random  # biblioteca que gera números aleatórios.

numeros = [random.randint(1, 100) for i in range(10)]
cres=sorted(numeros)
print(f"Lista ordenada crescente:{cres}\n")
decre= sorted(numeros, reverse= True)
print(f"Lista na ordena decrescente: {decre}\n")
print(f"Lista original: {numeros}")
   