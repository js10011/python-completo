# Criação do dicionário com informações sobre o estudante  
student = {  
    "nome": "Ivan",  
    "idade": 20  
}  

# Adição de um novo elemento "universidade"  
student["universidade"] = "MGU"  
print("Após adicionar 'universidade':", student)  

# Adição do elemento "cidade" apenas se ele ainda não estiver no dicionário  
if "cidade" not in student:  
    student["cidade"] = "Moscou"  
print("Após possível adição de 'cidade':", student)  

# Adição de vários novos elementos usando o método update()  
student.update({"faculdade": "Física", "ano": 3})  
print("Após adicionar novos elementos usando update():", student)