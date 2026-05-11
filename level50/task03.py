import tkinter as tk

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora")

# Criação dos botões
button7 = tk.Button(root, text="7")
button8 = tk.Button(root, text="8")
button9 = tk.Button(root, text="9")
button0 = tk.Button(root, text="0")

# Posicionamento dos botões usando o método grid
button7.grid(row=0, column=0)
button8.grid(row=0, column=1)
button9.grid(row=1, column=0)
button0.grid(row=1, column=1)

# Execução do loop principal do aplicativo
root.mainloop()