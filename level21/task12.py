import os

file_path = 'example.txt'

if os.path.exists(file_path):
    os.remove(file_path)
    print(f'Arquivo {file_path} foi excluído.')
else:
    print(f'Arquivo {file_path} não existe.')