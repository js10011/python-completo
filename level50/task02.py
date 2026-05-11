import tkinter as tk

# Cria a janela principal do aplicativo
root = tk.Tk()
root.title("Botões usando o método pack")

# Cria os botões
button_up = tk.Button(root, text="Cima")
button_down = tk.Button(root, text="Baixo")
button_left = tk.Button(root, text="Esquerda")
button_right = tk.Button(root, text="Direita")

# Posiciona os botões usando o método pack
button_up.pack(side=tk.TOP, fill=tk.X)
button_down.pack(side=tk.BOTTOM, fill=tk.X)
button_left.pack(side=tk.LEFT, fill=tk.Y)
button_right.pack(side=tk.RIGHT, fill=tk.Y)

# Inicia o loop principal de eventos
root.mainloop()