import hashlib

def hash_password(password: str) -> str:
    # Criar um objeto de hash com o algoritmo SHA-256
    hasher = hashlib.sha256()
    # Codificar a senha em bytes e atualizar o hasher
    hasher.update(password.encode('utf-8'))
    # Retornar o hash como uma string hexadecimal
    return hasher.hexdigest()

# Exemplo de uso:
password = "my_secure_password"
hashed_password = hash_password(password)
print(hashed_password)