import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graph():
    # Dados de origem
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    
    # Criamos um novo gráfico
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    
    # Definimos os títulos
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Exemplo de Gráfico')

    # Integramos o gráfico na janela Tkinter
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Criamos a janela principal do aplicativo
window = tk.Tk()
window.title("Construção de Gráfico")

# Criamos e posicionamos o botão para plotar o gráfico
plot_button = ttk.Button(window, text="Plotar Gráfico", command=plot_graph)
plot_button.pack()

# Iniciamos o loop principal de eventos
window.mainloop()