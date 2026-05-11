def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# Exemplo de uso:
print(fibonacci(10))  # Saída: 55

# A complexidade espacial do algoritmo recursivo de cálculo dos números de Fibonacci é O(n)
print("A complexidade espacial do algoritmo recursivo de cálculo dos números de Fibonacci é O(n)")