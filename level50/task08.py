import tkinter as tk

def update_status():
    option1_status = "Ativada" if var1.get() else "Desativada"
    option2_status = "Ativada" if var2.get() else "Desativada"
    print(f"Opção 1: {option1_status}, Opção 2: {option2_status}")

# Criação da janela principal
root = tk.Tk()
root.title("Aplicativo com Checkboxes")

# Variáveis para armazenar o estado das checkboxes
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()

# Criação das checkboxes
checkbox1 = tk.Checkbutton(root, text="Opção 1", variable=var1, command=update_status)
checkbox2 = tk.Checkbutton(root, text="Opção 2", variable=var2, command=update_status)

# Posicionamento das checkboxes na janela
checkbox1.pack(anchor=tk.W)
checkbox2.pack(anchor=tk.W)

# Início do loop principal do aplicativo
root.mainloop()