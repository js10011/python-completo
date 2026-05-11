import tkinter as tk

# Variáveis globais para rastrear o tempo e o estado do timer
time_elapsed = 0
running = False

# Função para atualizar o timer
def update_timer():
    global time_elapsed, running
    if running:
        time_elapsed += 1
        label.config(text=str(time_elapsed))
        root.after(1000, update_timer)  # Chamada repetida após 1 segundo

# Função para iniciar o timer
def start_timer():
    global running
    if not running:
        running = True
        update_timer()

# Função para parar o timer
def stop_timer():
    global running
    running = False

# Função para reiniciar o timer
def reset_timer():
    global time_elapsed, running
    running = False
    time_elapsed = 0
    label.config(text="0")

# Criando a janela principal
root = tk.Tk()
root.title("Timer")

# Rótulo para exibir o tempo
label = tk.Label(root, text="0", font=("Helvetica", 48))
label.pack()

# Botão Iniciar
start_button = tk.Button(root, text="Iniciar", command=start_timer)
start_button.pack(side=tk.LEFT)

# Botão Parar
stop_button = tk.Button(root, text="Parar", command=stop_timer)
stop_button.pack(side=tk.LEFT)

# Botão Reiniciar
reset_button = tk.Button(root, text="Reiniciar", command=reset_timer)
reset_button.pack(side=tk.LEFT)

# Iniciando o loop principal do aplicativo
root.mainloop()