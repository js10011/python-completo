import multiprocessing
from functools import reduce
from operator import mul

def partial_factorial(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result

def factorial(n, num_processes):
    if n == 0 or n == 1:
        return 1

    # Divida o intervalo em partes aproximadamente iguais
    chunk_size = n // num_processes
    ranges = [(i * chunk_size + 1, (i + 1) * chunk_size) for i in range(num_processes - 1)]
    ranges.append(((num_processes - 1) * chunk_size + 1, n))

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(partial_factorial, ranges)

    final_result = reduce(mul, results)
    return final_result


if __name__ == '__main__':
    number = 1000  # Calculamos o fatorial do número
    num_processes = 4  # Número de processadores
    result = factorial(number, num_processes)
    print(f"O fatorial de {number} é {result}")