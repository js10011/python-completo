# Limpando a lista

# Escreva um programa que crie uma lista de 10 números aleatórios no intervalo de 1 a 20.
# Em seguida, o programa deve remover todos os números pares da lista usando um loop.
# O programa deve exibir as listas original e atualizada.

# Escreva seu código aqui

import random  

numeros = [random.randint(1, 20) for i in range(10)]
print(numeros)
for i in range(len(numeros) - 1, -1, -1):
    if numeros[i] % 2 == 0: 
        del numeros[i]
print(numeros)