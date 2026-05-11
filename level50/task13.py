import tkinter as tk
from tkinter import filedialog, scrolledtext
import subprocess

# Função para selecionar o arquivo através de um diálogo
def select_file():
    filepath = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
    if filepath:
        file_path_var.set(filepath)  # Define o caminho do arquivo na variável

# Função para executar o script selecionado
def execute_script():
    script_path = file_path_var.get()
    if not script_path:
        result_area.configure(state='normal')
        result_area.delete(1.0, tk.END)
        result_area.insert(tk.END, "Arquivo não selecionado.")
        result_area.configure(state='disabled')
        return

    try:
        # Executa o script e captura a saída
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        output = result.stdout if result.stdout else result.stderr  # Obtém a saída ou erros
    except Exception as e:
        output = str(e)  # Em caso de erro, exibe o texto do erro

    # Exibe o resultado da execução no campo de texto
    result_area.configure(state='normal')  # Permite modificar o conteúdo
    result_area.delete(1.0, tk.END)  # Limpa o campo
    result_area.insert(tk.END, output)  # Insere a nova saída
    result_area.configure(state='disabled')  # Bloqueia o campo para edição

# Cria a janela principal
root = tk.Tk()
root.title("Script Runner")  # Título da janela

# Variável para armazenar o caminho do arquivo
file_path_var = tk.StringVar()

# Botão "Selecionar arquivo"
select_button = tk.Button(root, text="Selecionar arquivo", command=select_file)
select_button.grid(row=0, column=0, padx=5, pady=5)

# Campo para exibir o caminho do arquivo selecionado
file_path_entry = tk.Entry(root, textvariable=file_path_var, width=50)
file_path_entry.grid(row=0, column=1, padx=5, pady=5)

# Botão "Executar script"
run_button = tk.Button(root, text="Executar script", command=execute_script)
run_button.grid(row=0, column=2, padx=5, pady=5)

# Campo de texto com rolagem para exibir a saída do script
result_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=60, height=15)
result_area.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Inicia o loop principal de processamento de eventos
root.mainloop()