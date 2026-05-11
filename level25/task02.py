import threading

# Criando um objeto ThreadLocal
thread_local_data = threading.local()

# Função que trabalha com dados ThreadLocal
def process_data():
    thread_local_data.value = threading.current_thread().name
    print(f"Hello from {thread_local_data.value}")

# Função para a thread
def thread_function():
    process_data()

# Criando várias threads
threads = []
for i in range(5):
    thread = threading.Thread(target=thread_function, name=f"Thread-{i}")
    threads.append(thread)
    thread.start()

# Esperando a conclusão de todas as threads
for thread in threads:
    thread.join()