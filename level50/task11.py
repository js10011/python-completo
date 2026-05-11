import tkinter as tk
from tkinter import ttk

# Variáveis globais para estado
notifications_var = tk.BooleanVar()
night_mode_var = tk.BooleanVar()
theme_var = tk.StringVar(value="Clássica")
font_size_var = tk.IntVar(value=12)

# Função para aplicar configurações
def apply_settings():
    # Aplicar modo noturno
    if night_mode_var.get():
        root.configure(bg="black")
        theme_label.configure(foreground="white")
        font_size_label.configure(foreground="white")
    else:
        root.configure(bg="white")
        theme_label.configure(foreground="black")
        font_size_label.configure(foreground="black")

    # Aplicar tamanho da fonte
    font_size = font_size_var.get()
    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", font_size))
    style.configure("TButton", font=("Helvetica", font_size))
    style.configure("TCheckbutton", font=("Helvetica", font_size))
    style.configure("TRadiobutton", font=("Helvetica", font_size))

    # Tema selecionado (para demonstração)
    selected_theme = theme_var.get()
    print(f"Tema selecionado: {selected_theme}")
    # Aqui você pode adicionar lógica mais complexa para o tema

# Criação da janela principal
root = tk.Tk()
root.title("Interface gráfica configurável")
root.geometry("400x300")

# Criação dos checkboxes
notifications_check = ttk.Checkbutton(
    root, text="Mostrar notificações", variable=notifications_var
)
notifications_check.pack(anchor=tk.W)

night_mode_check = ttk.Checkbutton(
    root, text="Ativar modo noturno", variable=night_mode_var
)
night_mode_check.pack(anchor=tk.W)

# Rótulo e interruptores para seleção de tema
theme_label = ttk.Label(root, text="Escolha o tema:")
theme_label.pack(anchor=tk.W)

themes = ["Clássica", "Moderna", "Minimalista"]
for theme in themes:
    rb = ttk.Radiobutton(root, text=theme, variable=theme_var, value=theme)
    rb.pack(anchor=tk.W)

# Rótulo e escala para mudança do tamanho da fonte
font_size_label = ttk.Label(root, text="Tamanho da fonte:")
font_size_label.pack(anchor=tk.W)

font_size_scale = ttk.Scale(root, from_=10, to=20, variable=font_size_var, orient=tk.HORIZONTAL)
font_size_scale.pack(anchor=tk.W, fill=tk.X)

# Botão para aplicar configurações
apply_button = ttk.Button(root, text="Aplicar configurações", command=apply_settings)
apply_button.pack(anchor=tk.CENTER, pady=20)

# Iniciar o loop principal do aplicativo
root.mainloop()