# Comparar é muito fácil

# Escreva um programa que solicita ao usuário dois números de ponto flutuante
# e os compare usando uma margem de erro aceitável epsilon.
# Imprima o resultado da comparação na tela.

# Escreva seu código aqui
import math

n1=float(input("Digite um valor: "))
n2=float(input("Digite outro valor: "))

if abs(n1 - n2) < 0.00001:
    print("iguais")
else:
    print("diferentes")