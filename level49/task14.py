import tkinter as tk

def clear_text():
    text_field.delete(1.0, tk.END)

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo de Campo de Texto")

# Criação do campo de texto
text_field = tk.Text(root, height=10, width=40)
text_field.pack(pady=10)

# Criação do botão "Limpar"
clear_button = tk.Button(root, text="Limpar", command=clear_text)
clear_button.pack()

# Execução do loop principal do aplicativo
root.mainloop()