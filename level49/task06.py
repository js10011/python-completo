import tkinter as tk

def on_button_click():
    print("O botão foi clicado")

# Criação da janela principal
window = tk.Tk()
window.title("Aplicativo")

# Adição do rótulo
label = tk.Label(window, text="Bem-vindo ao aplicativo")
label.pack()

# Adição do botão
button = tk.Button(window, text="Clique em mim", command=on_button_click)
button.pack()

# Iniciar o loop principal do aplicativo
window.mainloop()