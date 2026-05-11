import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class GraphApp:
    def __init__(self, root):
        # Inicialização da janela principal
        self.root = root
        self.root.title("Exportador de Gráficos CSV")

        # Botão para abrir o arquivo CSV
        self.open_button = tk.Button(root, text="Abrir arquivo CSV", command=self.open_csv)
        self.open_button.pack(pady=10)

        # Botão para exportar o gráfico para PDF, inativo até que os dados sejam carregados
        self.export_button = tk.Button(root, text="Exportar gráfico para PDF", command=self.export_pdf)
        self.export_button.pack(pady=10)
        self.export_button.config(state=tk.DISABLED)  # Desativa o botão até que os dados sejam carregados

        # Criação da figura e eixo para o gráfico com o Matplotlib
        self.fig, self.ax = plt.subplots()

    # Método para abrir o arquivo CSV e construir o gráfico
    def open_csv(self):
        # Abre a janela de diálogo para seleção de arquivo
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
        if not file_path:
            return

        # Carrega os dados do arquivo CSV
        data = pd.read_csv(file_path)

        # Verifica se o arquivo está vazio
        if data.empty:
            tk.messagebox.showerror("Erro", "O arquivo CSV selecionado está vazio ou não pode ser lido.")
            return

        # Limpa o eixo e cria um novo gráfico
        self.ax.clear()
        data.plot(ax=self.ax)
        plt.show(block=False)  # Exibe o gráfico sem bloquear a interface

        # Ativa o botão de exportação após a construção bem-sucedida do gráfico
        self.export_button.config(state=tk.NORMAL)

    # Método para exportar o gráfico para PDF
    def export_pdf(self):
        # Abre a janela de diálogo para salvar o arquivo
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Arquivos PDF", "*.pdf")])
        if not file_path:
            return

        # Salva o gráfico no arquivo PDF
        with PdfPages(file_path) as pdf:
            pdf.savefig(self.fig)
            tk.messagebox.showinfo("Sucesso", f"Gráfico exportado com sucesso para {file_path}")

# Inicia o aplicativo
root = tk.Tk()
app = GraphApp(root)
root.mainloop()