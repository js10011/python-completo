# Variante incorreta: várias exceções são capturadas de forma errada
try:
    number = int(input("Digite um número: "))
    result = 10 / number
except (ValueError, ZeroDivisionError):
    print("Ocorreu um erro: insira apenas números diferentes de zero.")

# Variante corrigida: tratamento correto de exceções
try:
    number = int(input("Digite um número: "))
    result = 10 / number
except ValueError:
    print("Erro: insira um número válido.")
except ZeroDivisionError:
    print("Erro: divisão por zero não é possível.")