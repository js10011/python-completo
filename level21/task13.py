import os
import shutil

# Criação do diretório new_directory
os.makedirs('new_directory')

# Criação do diretório aninhado parent_directory/child_directory
os.makedirs('parent_directory/child_directory')

# Exclusão do diretório new_directory
shutil.rmtree('new_directory')

# Exclusão do diretório aninhado parent_directory/child_directory
shutil.rmtree('parent_directory')