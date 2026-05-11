import os

def traverse_directory(path):
    try:
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            print(full_path)
            if os.path.isdir(full_path):
                traverse_directory(full_path)
    except PermissionError:
        pass  # Ignorar diretórios aos quais não há acesso

# Exemplo de uso
start_path = '/path/to/start/directory'  # Substitua pelo caminho desejado
traverse_directory(start_path)