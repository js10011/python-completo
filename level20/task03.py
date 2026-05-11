# Parâmetros padrão.

# Escreva 2 funções: def foo(bar=[]) e foo_correct(bar=None).
# Cada função recebe uma lista e adiciona a ela o elemento "baz".
# Se a lista não for fornecida, a função deve usar uma nova lista vazia.
# Mostre como o uso de um objeto mutável como valor padrão pode levar a um comportamento inesperado, e corrija isso (na segunda função).


# Escreva aqui o seu código

# Verificação da função corrigida
print(foo_correct())  # Imprime: ['baz']
print(foo_correct())  # Imprime: ['baz']
print(foo_correct())  # Imprime: ['baz']

# Verificação passando uma lista
lst = [1, 2, 3]
print(foo_correct(lst))  # Imprime: [1, 2, 3, "baz"]
print(foo_correct(lst))  # Imprime: [1, 2, 3, "baz", "baz"]