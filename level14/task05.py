def sum_numbers(*args):
    return sum(args)

# Exemplo de uso:
numbers = [1, 2, 3, 4, 5]
print(sum_numbers(*numbers))  # Saída: 15

# Você também pode passar os números diretamente:
print(sum_numbers(1, 2, 3, 4, 5))  # Saída: 15