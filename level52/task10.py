import math

n = 100

# Complexidade do primeiro algoritmo: 100 * n^10
first_algorithm_time = 100 * n ** 10

# Complexidade do segundo algoritmo: 10 * 2^n
second_algorithm_time = 10 * (2 ** n)

# Complexidade do terceiro algoritmo: n!
third_algorithm_time = math.factorial(n)

print(f"Tempo de execução do primeiro algoritmo: {first_algorithm_time}")
print(f"Tempo de execução do segundo algoritmo: {second_algorithm_time}")
print(f"Tempo de execução do terceiro algoritmo: {third_algorithm_time}")