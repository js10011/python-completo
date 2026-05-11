import tkinter as tk

# Criando a janela principal do aplicativo
root = tk.Tk()
root.title("Exemplo com Tkinter")

# Criando três botões
button1 = tk.Button(root, text="Botão 1")
button2 = tk.Button(root, text="Botão 2")
button3 = tk.Button(root, text="Botão 3")

# Posicionando os botões verticalmente uns abaixo dos outros usando o método pack
button1.pack()
button2.pack()
button3.pack()

# Executando o loop principal de eventos
root.mainloop()