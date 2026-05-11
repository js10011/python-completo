# Caracteres na string

# Escreva um programa que receba uma string do usuário, exiba seu comprimento
# e, em seguida, solicite um índice ao usuário.
# O programa deve exibir o caractere da string nesse índice.
# Se o índice estiver fora dos limites da string, o programa deve exibir uma mensagem correspondente.

# Escreva seu código aqui
string = input("Digite uma string: ")
length = len(string)
print(f"Comprimento da string: {length}")

index = int(input("Digite um índice: "))
if index < 0 or index >= length:
    print("Índice fora dos limites da string")
else:
    print(f"Caractere no índice {index}: {string[index]}")