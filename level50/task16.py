import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CSVGrapherApp:
    def __init__(self, root):
        # Inicialização da janela principal
        self.root = root
        self.root.title("CSV Grapher")

        # Criar uma moldura para os botões
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Botão para carregar o arquivo CSV
        self.load_button = tk.Button(self.frame, text="Carregar CSV", command=self.load_csv)
        self.load_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Botão para gerar gráfico, inativo antes de carregar os dados 
        self.plot_button = tk.Button(self.frame, text="Gerar Relatório", command=self.plot_data, state=tk.DISABLED)
        self.plot_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Criamos um objeto Figure para o gráfico e o vinculamos à interface
        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Variável para armazenar dados do CSV
        self.data = None

    # Função para carregar o arquivo CSV
    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                # Carregar dados do arquivo CSV em um DataFrame
                self.data = pd.read_csv(file_path)
                if not self.data.empty:
                    self.plot_button.config(state=tk.NORMAL)  # Ativar botão para gerar gráfico
                else:
                    tk.messagebox.showwarning("Atenção", "Arquivo CSV está vazio.")  # Aviso se o arquivo estiver vazio
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Não foi possível carregar o arquivo: {e}")

    # Função para gerar gráfico com base nos dados carregados
    def plot_data(self):
        if self.data is not None:
            # Limpar gráfico anterior
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            # Criar gráfico
            self.data.plot(ax=ax)
            # Atualizar gráfico no Canvas
            self.canvas.draw()

# Iniciar aplicativo
root = tk.Tk()
app = CSVGrapherApp(root)
root.mainloop()