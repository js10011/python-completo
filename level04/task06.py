# Contando dinheiro

# Escreva um programa que solicite números ao usuário e os some até que o usuário insira um número negativo.
# Use um loop while e o operador break para encerrar a entrada ao encontrar um número negativo.

# Escreva seu código aqui
total = 0

while True:
    num = float(input("Digite um número: "))
    if num < 0:
        break
    total += num

print(f"Soma dos números inseridos: {total}")

