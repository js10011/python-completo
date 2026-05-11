# Lista de tuplas com informações sobre funcionários
employees = [("Ivan", "Engenheiro"), ("Maria", "Gerente"), ("Pedro", "Analista")]

# Criação de dicionário usando dictionary comprehension
employee_dict = {name: position for name, position in employees}

# Exibição do dicionário criado
print(employee_dict)