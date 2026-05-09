# Tupla inversa

# Escreva um programa que crie uma tupla a partir de uma quantidade arbitrária de elementos solicitados ao usuário.
# Em seguida, o programa deve exibir a tupla na ordem inversa usando slicing.

# Escreva seu código aqui

my_tuple = tuple(input("Insira elementos: ").split())
reversed_tuple = my_tuple[::-1]
print(reversed_tuple)