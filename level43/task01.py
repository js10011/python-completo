""" # Instalação da biblioteca PyPDF2
pip install PyPDF2

# Verificação da instalação bem-sucedida
pip show PyPDF2 | grep Version"""


try:
    import PyPDF2
    print("PyPDF2 is successfully installed and ready to use!")
except ImportError:
    print("PyPDF2 is not installed. Please install it to proceed.")