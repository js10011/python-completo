import tkinter as tk
from tkinter import scrolledtext

# Função para destacar palavras-chave
def highlight_keywords():
    # Removemos os destaques anteriores
    text_area.tag_remove("highlight", "1.0", tk.END)

    # Definimos palavras-chave para destacar
    keywords = ["def", "import", "as", "from", "class", "return"]

    # Iteramos por cada palavra-chave e procuramos no texto
    for keyword in keywords:
        start_index = "1.0"  # Começamos do início do texto
        while True:
            # Procuramos a palavra-chave considerando os limites da palavra (\b) e case sensitive
            start_index = text_area.search(keyword, start_index, stopindex=tk.END, nocase=False)
            if not start_index:  # Interrompemos se a palavra não for encontrada
                break
            end_index = f"{start_index}+{len(keyword)}c"  # Definimos o final da palavra encontrada
            text_area.tag_add("highlight", start_index, end_index)  # Adicionamos tag para destaque
            start_index = end_index  # Continuamos a busca do final da palavra atual

    # Definimos parâmetros da tag para destaque
    text_area.tag_config("highlight", foreground="red")

# Criamos a janela principal
root = tk.Tk()
root.title("Editor de Texto com Destaque de Palavras-Chave")  # Título da janela

# Criamos o campo de texto com rolagem e quebra de palavras
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
text_area.pack(expand=True, fill=tk.BOTH)  # Preenchemos todo o espaço disponível

# Criamos o botão para destacar
highlight_button = tk.Button(root, text="Destacar", command=highlight_keywords)
highlight_button.pack()

# Iniciamos o loop principal de eventos
root.mainloop()