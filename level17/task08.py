import traceback

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        traceback.print_exc()

# Exemplo de chamada da função
divide_numbers(10, 0)