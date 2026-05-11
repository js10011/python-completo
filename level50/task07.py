import tkinter as tk
from tkinter import Toplevel

def show_popup():
    def greet():
        name = name_var.get()
        greeting_label.config(text=f"Olá, {name}!")
        popup.destroy()
    
    popup = Toplevel(root)
    popup.title("Janela Pop-Up")

    tk.Label(popup, text="Digite seu nome:").pack(pady=5)
    name_var = tk.StringVar()
    tk.Entry(popup, textvariable=name_var).pack(pady=5)

    tk.Button(popup, text="Saudação", command=greet).pack(pady=5)

# Cria a janela principal
root = tk.Tk()
root.title("Janela Principal")

tk.Button(root, text="Abrir Janela Pop-Up", command=show_popup).pack(pady=20)
greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=20)

root.mainloop()