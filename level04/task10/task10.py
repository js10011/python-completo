# Ano Bissexto

# Escreva um programa que peça ao usuário um ano e verifique se ele é bissexto.
# Use operadores lógicos para verificar as condições de um ano bissexto.
# Um ano bissexto é divisível por 4, mas não é divisível por 100, exceto nos anos que são divisíveis por 400.

# Escreva seu código aqui

n= int(input("Em que ano você está? "))
if (n % 4 ==0 and n % 100 !=0) or (n % 400 ==0) :
    print("O ano é bissexto")
else:
    print("Não bissexto")
