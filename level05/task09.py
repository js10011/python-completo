# Acesso negado

# Escreva um programa que solicite ao usuário um nome de usuário e uma senha.
# Se o nome de usuário for "admin" e a senha for "1234", o programa deve exibir a mensagem "Acesso permitido".
# Caso contrário, o programa deve exibir a mensagem "Acesso negado".

# Escreva seu código aqui
nome = input("Digite seu nome : ")
senha = input("Agora digite sua senha: ")
if nome == "admin" and senha =="123":
    print("Acesso permitido")
else:
    print("Acesso negado")