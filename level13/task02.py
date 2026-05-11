# Duas listas para unir
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

# União das listas em uma lista de tuplas
zipped_list = list(zip(list1, list2))
print("Lista unida:", zipped_list)

# Lista de números para encontrar min, max e sum
numbers = [10, 20, 30, 40, 50]

# Encontrar o menor e o maior elemento
min_element = min(numbers)
max_element = max(numbers)
print("Menor elemento:", min_element)
print("Maior elemento:", max_element)

# Calcular a soma de todos os elementos
sum_elements = sum(numbers)
print("Soma de todos os elementos:", sum_elements)