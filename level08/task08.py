# Solicita ao usuário 6 elementos e cria uma tupla
elements = tuple(input("Digite o elemento {}: ".format(i + 1)) for i in range(6))

# Agrupa os elementos em 3 tuplas de 2 elementos
tuple1 = elements[:2]
tuple2 = elements[2:4]
tuple3 = elements[4:]

# Combina a 1ª e a 3ª tuplas
combined_tuple = tuple1 + tuple3

# Exibe a tupla atualizada na tela
print("Tupla atualizada:", combined_tuple)