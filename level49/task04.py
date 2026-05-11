import tkinter as tk

def on_button_click():
    print("O botão foi clicado")

# Criando a janela principal
root = tk.Tk()
root.title("Aplicação Simples com Botão")
root.geometry("500x300")

# Criando o botão e adicionando-o à janela
button = tk.Button(root, text="Clique em mim", command=on_button_click)
button.pack(pady=20)

# Iniciando o loop principal da janela
root.mainloop()