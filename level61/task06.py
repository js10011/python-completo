def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Exemplo de uso:
print(factorial(5))  # Saída: 120

# A complexidade espacial do algoritmo recursivo para calcular o fatorial de um número n é O(n),
# pois a profundidade máxima das chamadas recursivas é n.

print("A complexidade espacial do algoritmo recursivo para calcular o fatorial de um número n é O(n)")