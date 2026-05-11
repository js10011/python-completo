import threading
import time

class Timer:
    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.thread = None

    def start(self):
        self.thread = threading.Timer(self.interval, self.function, self.args, self.kwargs)
        self.thread.start()

    def cancel(self):
        if self.thread:
            self.thread.cancel()

def my_function():
    print("O timer disparou!")

# Cria uma instância do Timer com intervalo de 5 segundos
t = Timer(5, my_function)

# Inicia o timer
print("Iniciando o timer")
t.start()

# Espera 2 segundos e então cancela o timer
time.sleep(2)
print("Cancelando o timer")
t.cancel()