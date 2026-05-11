def hanoi_moves(n):
    # Caso base: se houver apenas um disco, é necessário um movimento
    if n == 1:
        return 1
    # Caso recursivo: 2 * movimentos de n-1 discos + 1 movimento do maior disco
    else:
        return 2 * hanoi_moves(n - 1) + 1

# Exemplo de uso
n = 4
print(hanoi_moves(n))  # Saída: 15