# Primeiro a sair

# Escreva um programa que cria uma lista com 5 elementos, solicita ao usuário um elemento para remover
# e remove o primeiro elemento encontrado da lista usando o método remove().
# O programa deve imprimir a lista atualizada.

# Escreva seu código aqui
my_list = ['apple', 'banana', 'cherry', 'apple', 'banana']
print(f"Lista atual:\n{my_list}")
remov= input("Digite um item para eliminar: ")
my_list.remove(remov)
print(f"Lista atualizada:\n{my_list}") 