# Incerteza

# Escreva um programa que solicita dois números do usuário.
# Se o usuário não inserir um valor (string vazia),
# utilize o valor padrão None para esse número.
# Calcule e exiba a soma desses números.

# Escreva seu código aqui

a = input("Digite o primeiro número: ")
b = input("Digite o segundo número: ")

a = None if a == "" else float(a)
b = None if b == "" else float(b)

if a is None or b is None:
    print("A soma dos números é desconhecida")
else:
    sum_result = a + b
    print("A soma dos números:", sum_result)