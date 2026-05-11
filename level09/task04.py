# Detetive

# Escreva a função set_detector, que percorre a lista (tupla) de seus argumentos e determina - se há um conjunto entre eles ou não.
# Chame a função set_detector com diferentes opções de parâmetros (com e sem conjunto).

# Escreva seu código aqui
def set_detector(*args):
    for elemento in args:
        if isinstance(elemento, set):
            return True
    return False
print(set_detector(5, 1, 9, "sun"))
print(set_detector(1, 2, {3}))
print(set_detector(0, 8, 6, {"Planet"}))