import tkinter as tk

# Criando a janela principal do aplicativo
root = tk.Tk()
root.title("Labels no Tkinter")

# Primeiro label
label1 = tk.Label(root, text="Bem-vindo!", font=("Arial", 14), fg="green")
label1.pack()

# Segundo label
label2 = tk.Label(root, text="Aplicativo de Estudo", font=("Courier", 12), fg="blue")
label2.pack()

# Terceiro label
label3 = tk.Label(root, text="Encerrando o programa", font=("Times", 16), fg="red")
label3.pack()

# Iniciando o loop principal do aplicativo
root.mainloop()