import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

def load_file():
    # Abrimos a janela de diálogo para selecionar o arquivo
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Lemos o conteúdo do arquivo
            content = file.read()
            # Exibimos o conteúdo no campo de texto
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)

# Criamos a janela principal
root = tk.Tk()
root.title("Editor de Texto")

# Criamos o rótulo
label = tk.Label(root, text="Editor de Texto", font=("Arial", 12))
label.pack(pady=10)

# Criamos o campo de texto com barra de rolagem
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 10))
text_area.pack(expand=True, fill='both', padx=10, pady=10)

# Criamos o botão "Carregar arquivo"
load_button = tk.Button(root, text="Carregar arquivo", command=load_file)
load_button.pack(pady=10)

root.geometry("600x400")  # Definimos o tamanho inicial da janela
root.mainloop()