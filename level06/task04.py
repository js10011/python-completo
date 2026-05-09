# Cálculo de fatorial

# Escreva uma função factorial(n), que recebe um número inteiro n e retorna seu fatorial. Se n for igual a 0, a função deve retornar 1
# O fatorial de um número n é denotado por n! e é o produto de todos os números de 1 até n.

# Escreva seu código aqui
import math 
def factorial(n):
    if n  == 0 :
        return 1
    else:
        return  math.factorial(n)
factorial(4)        