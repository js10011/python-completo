import time

def time_decorator(func):
    def wrapper(n):
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        print(f"Tempo de execução: {end_time - start_time} segundos")
        return result
    return wrapper

@time_decorator
def compute_square(n):
    time.sleep(2)  # simulação de atraso
    return n * n

compute_square(5)