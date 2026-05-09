# Maximalista

# Escreva uma função find_m ax(a, b) que receba dois números como argumentos e retorne o maior deles.
# Se os números forem iguais, a função deve retornar qualquer um deles.
# Em seguida, escreva um programa que solicite ao usuário dois números, chame essa função e imprima o resultado.

# Escreva seu código aqui

#import random

def find_max(a, b):
    
    if a > b :
        return a
        
    else:
        return b
n1=int(input())
n2= int(input())
resultado= find_max(n1, n2)
print(resultado)
       