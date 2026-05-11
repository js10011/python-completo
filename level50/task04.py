import tkinter as tk

def submit():
    name = name_entry.get()
    email = email_entry.get()
    print(f"Name: {name}, Email: {email}")

# Criando a janela principal
root = tk.Tk()
root.title("Cadastro")

# Criando e posicionando o título
header = tk.Label(root, text="Cadastro", font=("Arial", 16))
header.pack(side=tk.TOP, pady=10)

# Criando frame para posicionar os elementos de entrada e botão
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Criando campo de texto para entrada de nome
name_label = tk.Label(frame, text="Nome:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Criando campo de texto para entrada de e-mail
email_label = tk.Label(frame, text="Email:")
email_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Criando botão "Enviar"
submit_button = tk.Button(frame, text="Enviar", command=submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Definindo pesos para as colunas para adaptação ao redimensionar a janela
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

# Executando o loop principal do programa
root.mainloop()