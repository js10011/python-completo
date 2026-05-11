def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero"
    except TypeError:
        return "Erro: tipo de dado incorreto"
    return result