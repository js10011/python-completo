import tkinter as tk

# Função manipuladora de clique do botão
def button_click_handler():
    # Altera o texto do rótulo ao clicar no botão
    label.config(text="Botão pressionado")

# Cria a janela principal do aplicativo
root = tk.Tk()
root.title("Problema com manipulador de eventos")  # Título da janela

# Cria um rótulo com texto inicial
label = tk.Label(root, text="Pressione o botão")
label.pack(pady=10)  # Espaçamento acima e abaixo

# Cria um botão, vinculando-o ao manipulador de eventos
button = tk.Button(root, text="Clique em mim", command=button_click_handler)
button.pack(pady=5)  # Espaçamento acima e abaixo

# Executa o loop principal da janela
root.mainloop()