import tkinter as tk

def greet_user():
    name = entry.get()  # Obtém o texto do campo de texto
    greeting = f"Olá, {name}!"
    label.config(text=greeting)  # Atualiza o texto do rótulo

# Cria a janela principal do aplicativo
root = tk.Tk()
root.title("Saudação Personalizada")  # Define o título da janela

# Cria o rótulo com o texto inicial
label = tk.Label(root, text="Saudação Personalizada")
label.pack(pady=10)

# Cria o campo de texto para entrada do nome
entry = tk.Entry(root)
entry.pack(pady=10)

# Cria o botão que, ao ser pressionado, chama a função greet_user
button = tk.Button(root, text="Cumprimentar", command=greet_user)
button.pack(pady=10)

# Inicia o loop principal de processamento de eventos
root.mainloop()