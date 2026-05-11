import tkinter as tk

# Criação da janela principal
root = tk.Tk()
root.title("Aplicativo Simples com Label")  # Definição do título da janela
root.geometry("500x300")  # Definição do tamanho da janela

# Criação e adição do Label na janela
label = tk.Label(root, text="Clique em mim")
label.pack(expand=True)  # Posicionamento do Label no centro da janela

# Iniciando o loop principal do aplicativo
root.mainloop()