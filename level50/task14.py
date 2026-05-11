import tkinter as tk
from tkinter import messagebox
import subprocess

# Função para executar o script
def run_script():
    try:
        # Aqui 'run_script.py' é o script que você deseja executar
        result = subprocess.run(['python', 'run_script.py'], capture_output=True, text=True, check=True)
        output_text.delete("1.0", tk.END)  # Limpa o campo de texto
        output_text.insert(tk.END, result.stdout)  # Insere a saída do script
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao executar o script:\n{e.stderr}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado:\n{str(e)}")

# Cria a janela principal
root = tk.Tk()
root.title("Execução de Script")

# Cria o campo de texto para exibir a saída
output_text = tk.Text(root, wrap='word', width=80, height=20)
output_text.pack(padx=10, pady=10)

# Cria o botão para executar o script
run_button = tk.Button(root, text="Executar Script", command=run_script)
run_button.pack(pady=10)

# Executa o loop principal de eventos
root.mainloop()