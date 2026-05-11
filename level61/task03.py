import cProfile

def example_function():
    total = 0
    for i in range(10000):
        total += i
    return total

def optimized_example_function():
    # Utilizamos a fórmula da soma da progressão aritmética
    n = 9999
    total = n * (n + 1) // 2
    return total


# Perfilamento da função original
print("Profiling example_function:")
cProfile.run('example_function()')

# Perfilamento da função otimizada
print("Profiling optimized_example_function:")
cProfile.run('optimized_example_function()')