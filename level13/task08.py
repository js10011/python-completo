# Expressão geradora para quadrados de números de 1 a 10
squares = (x**2 for x in range(1, 11))

# Exibe todos os valores da sequência
for square in squares:
    print(square)