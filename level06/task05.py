# IVA

# Escreva uma função calculate_total_cost(price, tax=0.2) que recebe o preço de um produto e um parâmetro opcional de taxa (por padrão 20%).
# A função deve calcular e imprimir o custo total do produto considerando o imposto.
# Em seguida, escreva um programa que chama essa função com diferentes parâmetros.

# Escreva seu código aqui
def calculate_total_cost(price=19, tax =0.2):
    print(price *(1 + tax))
calculate_total_cost(15, 0.18)
calculate_total_cost(16, 0.11)
calculate_total_cost(8, 2.8)
    