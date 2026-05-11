# Criamos dois frozenset a partir de listas
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([4, 5, 6])

# Criamos um dicionário, onde as chaves são frozenset e os valores são strings
dictionary = {
    frozenset1: "Primeiro conjunto de números",
    frozenset2: "Segundo conjunto de números"
}

# Exibimos o dicionário
print(dictionary)