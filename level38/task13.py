import time

# Início da medição do tempo
start_time = time.time()

# Inicialização da soma
total_sum = 0

# Loop de 1 a 1000000
for number in range(1, 1000001):
    # Verifica se o número é par
    if number % 2 == 0:
        total_sum += number

# Fim da medição do tempo
end_time = time.time()

# Calcula o tempo total de execução
execution_time = end_time - start_time

# Exibe o tempo total de execução em segundos
print(f"Tempo total de execução: {execution_time:.6f} segundos")