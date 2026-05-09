# Ímpar

# Escreva um programa que exiba números de 1 a 100, pulando os números pares.
# Use um loop while e a instrução continue para pular os números pares.

# Escreva seu código

num = 1
while num <= 100:
    if num % 2 == 0:
        num += 1
        continue
    print(num)
    num += 1
