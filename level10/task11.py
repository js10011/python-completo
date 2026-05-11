# Criamos frozenset a partir de uma lista
list_frozen = frozenset([1, 2, 3, 4, 5])

# Criamos frozenset a partir de uma string
string_frozen = frozenset("abcde")

# União
union_result = list_frozen | string_frozen

# Interseção
intersection_result = list_frozen & string_frozen

# Diferença
difference_result = list_frozen - string_frozen

# Diferença simétrica
symmetric_difference_result = list_frozen ^ string_frozen

# Exibir resultados
print(f"União: {union_result}")
print(f"Interseção: {intersection_result}")
print(f"Diferença: {difference_result}")
print(f"Diferença simétrica: {symmetric_difference_result}")