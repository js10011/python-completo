import tkinter as tk

def show_text():
    # Obtém o texto do campo de entrada
    entered_text = entry.get()
    # Exibe o texto no console
    print(entered_text)

# Cria a janela principal do aplicativo
root = tk.Tk()
root.title("Aplicativo Simples")

# Cria o campo de entrada
entry = tk.Entry(root, width=30)
entry.pack(padx=10, pady=10)

# Cria o botão e o vincula à função show_text
button = tk.Button(root, text="Mostrar", command=show_text)
button.pack(padx=10, pady=10)

# Inicia o loop principal do aplicativo
root.mainloop()