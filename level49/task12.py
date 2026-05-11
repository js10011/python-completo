import tkinter as tk

# Inicialização da janela principal
root = tk.Tk()
root.title("Calculator")

# Variáveis para expressão e valor exibido
expression = ""
input_value = tk.StringVar()

# Campo de entrada
input_field = tk.Entry(root, textvariable=input_value, font=('arial', 18, 'bold'), bd=10, insertwidth=4, width=14, justify='right')
input_field.grid(row=0, column=0, columnspan=4)

# Manipulador de cliques de botão
def on_button_click(char):
    global expression
    if char == 'C':
        expression = ""
    elif char == '=':
        try:
            expression = str(eval(expression))
        except ZeroDivisionError:
            expression = "Error"
    else:
        expression += str(char)

    input_value.set(expression)

# Criação dos botões
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
    # Botões de operações
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('=', 4, 2), ('C', 4, 0)
]

# Adicionando botões à janela
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), bd=8, command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col)

# Executando o loop principal do aplicativo
root.mainloop()