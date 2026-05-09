# Apagador

# Escreva um programa que cria uma lista de 10 elementos, depois substitua os elementos do terceiro ao quinto por um único valor solicitado ao usuário.
# O programa deve imprimir a lista atualizada.

# Escreva seu código aqui
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
atua = int(input())
numbers[2:5] = [atua]
print(numbers)