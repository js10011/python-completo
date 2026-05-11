import tkinter as tk

def on_button_click():
    global click_count
    click_count += 1
    button.config(text=f"Clique {click_count}")
    print(f"Quantidade de cliques: {click_count}")

# Criação da janela principal do aplicativo
root = tk.Tk()
root.title("Botão-contador")

# Inicialização do contador de cliques
click_count = 0

# Criação do botão com texto inicial
button = tk.Button(root, text="Clique em mim", command=on_button_click)
button.pack(padx=20, pady=20)

# Início do loop principal do aplicativo
root.mainloop()