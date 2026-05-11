import tkinter as tk

def update_title():
    selected_color = color_var.get()
    window.title(selected_color)

# Criando a janela principal
window = tk.Tk()
window.title("Escolha uma cor")

# Criando StringVar para rastrear a seleção do usuário
color_var = tk.StringVar(value="Vermelho")

# Criando os botões de rádio para escolha de cor
radio_red = tk.Radiobutton(window, text="Vermelho", variable=color_var, value="Vermelho", command=update_title)
radio_green = tk.Radiobutton(window, text="Verde", variable=color_var, value="Verde", command=update_title)
radio_blue = tk.Radiobutton(window, text="Azul", variable=color_var, value="Azul", command=update_title)

# Posicionando os botões de rádio na janela
radio_red.pack()
radio_green.pack()
radio_blue.pack()

# Iniciando o loop principal do aplicativo
window.mainloop()