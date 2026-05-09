total_grains = 2**64 - 1
print(total_grains)

# Somador

# Escreva um programa que solicita ao usuário dois números, guarda-os em variáveis e exibe a soma deles.
# Exemplo:
# Digite o primeiro número: 5
# Digite o segundo número: 7
# Soma: 12

# Escreva seu código aqui
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("Soma: ", n1+n2)


# Usuário de idade

# Escreva um programa que solicita ao usuário sua idade atual (um número inteiro) e exibe sua idade daqui a 50 anos.
# Para converter a entrada, use a função int().
# Exemplo:
# Digite sua idade atual: 20
# Daqui a 50 anos você terá 70 anos.

# Escreva seu código aquid
idade = int(input("Digite sua idade atual : "))
print(f"Daqui a 50 anos você terá {idade + 50} anos")

radius = float(input("Digite o raio do círculo: "))
pi = 3.14
area = pi * radius * radius
print("Área do círculo:", area)