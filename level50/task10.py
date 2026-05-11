import tkinter as tk

def show_selections():
    checkbox_status = "Ativado" if checkbox_var.get() else "Não ativado"
    season = season_var.get()
    number = scale_var.get()

    result = f"Checkbox: {checkbox_status}, Estação: {season}, Número: {number}"
    result_label.config(text=result)

# Criação da janela principal
root = tk.Tk()
root.title("Aplicativo com elementos de controle")

# Checkbox
checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Ativar", variable=checkbox_var)
checkbox.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

# Botões de rádio
season_var = tk.StringVar(value="Verão")
radiobutton_frame = tk.LabelFrame(root, text="Selecione a estação")
radiobutton_frame.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

for season in ["Verão", "Outono", "Inverno"]:
    rb = tk.Radiobutton(radiobutton_frame, text=season, variable=season_var, value=season)
    rb.pack(anchor=tk.W)

# Slider
scale_label = tk.Label(root, text="Selecione o número:")
scale_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

scale_var = tk.IntVar(value=1)
scale = tk.Scale(root, from_=1, to=5, variable=scale_var, orient='horizontal')
scale.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

# Botão para exibição da seleção
button = tk.Button(root, text="Mostrar seleção", command=show_selections)
button.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

# Label para exibição das seleções atuais
result_label = tk.Label(root, text="Suas seleções atuais serão exibidas aqui.")
result_label.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)

# Início do loop principal
root.mainloop()