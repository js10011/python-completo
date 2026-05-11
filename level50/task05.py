import tkinter as tk
from tkinter import messagebox

# Criar a janela principal do aplicativo (invisível, pois não estamos mostrando-a)
root = tk.Tk()
root.withdraw()  # Esconder a janela principal

# Mostrar a caixa de diálogo informativa
messagebox.showinfo("Informação", "Bem-vindo ao aplicativo!")

# Encerrar o aplicativo após fechar a caixa de diálogo
root.quit()