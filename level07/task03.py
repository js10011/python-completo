# Programa Aleatório

# Escreva um programa que cria uma lista de elementos aleatórios, exibe o comprimento da lista e, em seguida, o primeiro e o último elemento da lista.

# Escreva seu código aqui

import random
lista_ale = [random.randint(1, 100) for i in range(10)]
print(len(lista_ale))
print(lista_ale[0])
print(lista_ale[-1])
