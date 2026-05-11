import tkinter as tk
from tkinter import messagebox

def on_exit():
    # Criar uma janela de diálogo com a pergunta e opções "Yes" ou "No"
    if messagebox.askyesno("Confirmação de saída", "Você realmente deseja sair?"):
        root.destroy()  # Fecha o aplicativo se o usuário escolher "Yes"

# Criar a janela principal do aplicativo
root = tk.Tk()
root.title("Aplicativo com confirmação de saída")

# Criar o botão "Sair"
exit_button = tk.Button(root, text="Sair", command=on_exit)
exit_button.pack(pady=20)

# Inicia o loop principal de eventos
root.mainloop()