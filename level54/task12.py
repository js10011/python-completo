import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(email, password):
    hashed_password = hash_password(password)
    users[email] = hashed_password
    print(f"Usuário {email} registrado com sucesso.")

def login(email, password):
    hashed_password = hash_password(password)
    if email in users and users[email] == hashed_password:
        print(f"Usuário {email} conectado com sucesso.")
    else:
        print("Falha no login: Email ou senha inválidos.")

# Exemplo de uso
register("user@example.com", "securepassword123")
login("user@example.com", "securepassword123")
login("user@example.com", "wrongpassword")