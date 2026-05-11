import tkinter as tk

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        print(f"Soma: {result}")
    except ValueError:
        print("Erro: por favor, insira valores numéricos.")

def multiply_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        print(f"Produto: {result}")
    except ValueError:
        print("Erro: por favor, insira valores numéricos.")

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora")

# Campos de entrada
entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Botão "Somar"
add_button = tk.Button(root, text="Somar", command=add_numbers)
add_button.pack(pady=5)

# Botão "Multiplicar"
multiply_button = tk.Button(root, text="Multiplicar", command=multiply_numbers)
multiply_button.pack(pady=5)

# Iniciar o loop principal do aplicativo
root.mainloop()