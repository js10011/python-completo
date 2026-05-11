# Passo 1: Crie um novo ambiente virtual com o nome "myenv"
python3 -m venv myenv

# Passo 2: Ative o ambiente virtual
source myenv/bin/activate

# Passo 3: Instale as bibliotecas pandas e openpyxl usando pip
pip install pandas openpyxl

# Passo 4: Verifique a instalação exibindo as versões do pandas e openpyxl
pip show pandas | grep Version
pip show openpyxl | grep Version


# Criação do ambiente virtual no diretório 'venv'
python3 -m venv venv

# Ativação do ambiente virtual
source venv/bin/activate

# Instalação das bibliotecas necessárias
pip install pandas openpyxl

# Exibição das versões das bibliotecas instaladas
pip show pandas | grep Version
pip show openpyxl | grep Version

# Desativação do ambiente virtual
deactivate