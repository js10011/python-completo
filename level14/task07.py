import os

# Criamos o diretório
os.makedirs('test_directory', exist_ok=True)

# Entramos no diretório
os.chdir('test_directory')

# Criamos o arquivo e escrevemos a string nele
with open('test_file.txt', 'w') as file:
    file.write('Hello, World!')

# Lemos o conteúdo do arquivo
with open('test_file.txt', 'r') as file:
    content = file.read()
    print(content)

# Removemos o arquivo
os.remove('test_file.txt')

# Voltamos para o diretório pai
os.chdir('..')

# Removemos o diretório
os.rmdir('test_directory')