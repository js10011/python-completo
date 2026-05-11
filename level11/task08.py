# Criação do dicionário com informações sobre o estudante
student_info = {
    "nome": "John Doe",
    "idade": 22,
    "universidade": "MIT"
}

# Verificação da presença do valor "MIT" usando o método values()
contains_mit = "MIT" in student_info.values()
print(f"Contains MIT: {contains_mit}")

# Verificação da presença do valor "Harvard" usando a função set()
contains_harvard = "Harvard" in set(student_info.values())
print(f"Contains Harvard: {contains_harvard}")

# Verificação da presença do valor 22 usando um gerador
contains_22 = any(value == 22 for value in student_info.values())
print(f"Contains 22: {contains_22}")