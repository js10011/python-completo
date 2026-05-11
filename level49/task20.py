import tkinter as tk

# Variáveis globais para rastreamento do contador e mensagem de erro
counter = 0
message = ""

# Função para atualizar a interface
def update_interface():
    label.config(text=f'Contador: {counter}')
    error_label.config(text=message)

# Função para incrementar o contador
def increment():
    global counter, message
    counter += 1
    message = ""
    update_interface()

# Função para decrementar o contador
def decrement():
    global counter, message
    counter -= 1
    if counter < 0:
        message = "Erro: número negativo"
        counter = 0
    else:
        message = ""
    update_interface()

# Função para resetar o contador
def reset():
    global counter, message
    counter = 0
    message = ""
    update_interface()

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora de cliques")

# Criação do rótulo para exibir o contador
label = tk.Label(root, text=f'Contador: {counter}', font=("Helvetica", 16))
label.pack(pady=10)

# Criação do rótulo para exibir erros
error_label = tk.Label(root, text=message, font=("Helvetica", 12), fg="red")
error_label.pack(pady=5)

# Criação dos botões para incrementar, decrementar e resetar o contador
increment_button = tk.Button(root, text="+", command=increment, width=10, height=2)
increment_button.pack(side='left', padx=5, pady=5)

decrement_button = tk.Button(root, text="-", command=decrement, width=10, height=2)
decrement_button.pack(side='left', padx=5, pady=5)

reset_button = tk.Button(root, text="Redefinir", command=reset, width=10, height=2)
reset_button.pack(side='left', padx=5, pady=5)

# Início do loop principal do aplicativo
root.mainloop()