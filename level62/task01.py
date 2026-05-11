import multiprocessing

def partial_sum(array_slice):
    return sum(array_slice)


array = [i for i in range(1, 1000001)]  # Grande array para somar
num_processes = multiprocessing.cpu_count()  # Número de processadores disponíveis

# Dividimos o array em partes iguais
chunk_size = len(array) // num_processes
chunks = [array[i * chunk_size: (i + 1) * chunk_size] for i in range(num_processes)]

# Criamos um pool de processos
with multiprocessing.Pool(processes=num_processes) as pool:
    # Calculamos a soma de cada parte em paralelo
    partial_sums = pool.map(partial_sum, chunks)

# Combinamos os resultados
total_sum = sum(partial_sums)

print(f"Total sum: {total_sum}")