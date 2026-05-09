# Criar uma tupla com tuplas aninhadas
nested_tuples = ((1, 3, 5), (6, 3, 8), (2, 4, 0), (7, 9, -1))

# Inicializa uma variável para armazenar o valor máximo
max_value = float('-inf')

# Percorre cada tupla aninhada
for sub_tuple in nested_tuples:
    # Encontra o valor máximo na sub-tupla atual e compara com o máximo global
    if max(sub_tuple) > max_value:
        max_value = max(sub_tuple)

print("O valor máximo nas tuplas aninhadas:", max_value)


