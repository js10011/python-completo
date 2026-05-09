# Lista de quadrados

# Escreva um programa que cria uma lista de quadrados de números de -100 a 100. Para criar a lista, use a função list().
# No final, exiba a lista resultante na tela.

# Escreva seu código aqui
squares = list(x**2 for x in range(-100, 101))
print(squares)