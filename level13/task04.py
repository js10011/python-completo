# Criamos uma lista de strings
strings = ["apple", "banana", "cherry", "date", "fig", "grape"]

# Usamos sorted() e uma lambda função para ordenar as strings pelo comprimento
sorted_strings = sorted(strings, key=lambda x: len(x))

# Exibimos o resultado
print(sorted_strings)