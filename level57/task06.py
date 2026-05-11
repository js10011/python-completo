def count_paths(m, n, i, j, memo):
    # Tratamento de casos de borda
    if i == m - 1 and j == n - 1:
        return 1  # Chegamos ao canto inferior direito
    if i >= m or j >= n:
        return 0  # Saímos dos limites da grade

    # Verificação de memoization
    if (i, j) in memo:
        return memo[(i, j)]

    # Cálculo recursivo do número de caminhos
    memo[(i, j)] = count_paths(m, n, i + 1, j, memo) + count_paths(m, n, i, j + 1, memo)
    return memo[(i, j)]

def unique_paths(m, n):
    if m == 0 or n == 0:
        return 0

    # Início da função recursiva a partir do ponto inicial (0, 0)
    return count_paths(m, n, 0, 0, {})

# Exemplos de uso
print(unique_paths(3, 7))  # Resultado esperado: 28
print(unique_paths(3, 3))  # Resultado esperado: 6
print(unique_paths(1, 1))  # Resultado esperado: 1
print(unique_paths(0, 0))  # Resultado esperado: 0