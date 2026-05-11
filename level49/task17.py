import tkinter as tk

# Função para exibir saudação
def greet():
    print("Olá!")

# Função para exibir despedida
def farewell():
    print("Até logo!")

# Função para fechar a janela
def close_window():
    window.destroy()  # Fecha a janela

# Criação da janela principal
window = tk.Tk()
window.title("Janela de Saudação")  # Define o título da janela

# Adiciona os botões
greet_button = tk.Button(window, text="Olá", command=greet)  # Botão para saudação
farewell_button = tk.Button(window, text="Adeus", command=farewell)  # Botão para despedida
close_button = tk.Button(window, text="Fechar", command=close_window)  # Botão para fechar a janela

# Posiciona os botões na janela com espaçamento
greet_button.pack(pady=5)    # Espaçamento acima e abaixo de 5 pixels
farewell_button.pack(pady=5) # Espaçamento acima e abaixo de 5 pixels
close_button.pack(pady=5)    # Espaçamento acima e abaixo de 5 pixels

# Inicia o loop principal de manipulação de eventos
window.mainloop()