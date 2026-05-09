# Negativo

# Escreva um programa que peça ao usuário um número e verifique se ele é negativo.
# Utilize o operador if para a verificação.

# Escreva seu código aqui
numero = int(input())

if numero < 0:
    print("Numero negativo")
else:
    print("Numero positivo")


score = int(input("Digite a quantidade de pontos obtidos: "))

if score >= 90:
    print("Excelente")
elif 75 <= score < 90:
    print("Bom")
elif 50 <= score < 75:
    print("Satisfatório")
else:
    print("Insatisfatório")