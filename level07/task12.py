# Lista clara

# Escreva um programa que cria uma lista de 10 números inteiros.
# Usando um loop for, substitua todos os elementos pares da lista pela string "par".
# O programa deve exibir a lista atualizada.

# Escreva seu código aqui

my_list = [1, 3, 5, 6, 3, 9, 34, 12, 9, 21]
for index, element in enumerate(my_list):
    if element % 2 == 0:
        my_list[index]= "par"
print(my_list)
        