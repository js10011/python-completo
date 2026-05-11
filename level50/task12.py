import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def run_script():
    # Abre a janela de diálogo para seleção do arquivo
    file_path = filedialog.askopenfilename(title="Selecione o script Python", filetypes=[("Python Files", "*.py")])
    if file_path:
        try:
            # Executa o script selecionado usando subprocess
            subprocess.Popen(["python", file_path], shell=True)
            # Notificação de execução do script
            messagebox.showinfo("Sucesso", "Script executado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível executar o script: {str(e)}")

# Criação da janela principal do aplicativo
root = tk.Tk()
root.title("Executar script")

# Criação e posicionamento do botão "Executar script"
run_button = tk.Button(root, text="Executar script", command=run_script)
run_button.pack(pady=20)

# Inicia o loop principal de eventos
root.mainloop()