import tkinter as tk

def on_button_click():
    print("Olá, mundo!")

# Criando a janela principal
root = tk.Tk()
root.title("Janela Simples")

# Criando o botão com o texto "Olá"
button = tk.Button(root, text="Olá", command=on_button_click)

# Colocando o botão na janela
button.pack(pady=20)

# Iniciando o loop principal de eventos
root.mainloop()