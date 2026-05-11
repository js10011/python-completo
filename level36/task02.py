import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Criamos uma instância do driver do navegador
driver = webdriver.Chrome()

# Carregamos a página com o formulário de registro
driver.get('file:///path/to/solution/registration_form.html')  # Substitua pelo caminho para o seu arquivo HTML local

# Encontramos os elementos do formulário de registro e o botão para envio
first_name_field = driver.find_element(By.ID, 'first_name')  # Campo para inserir o primeiro nome
last_name_field = driver.find_element(By.ID, 'last_name')    # Campo para inserir o sobrenome
email_field = driver.find_element(By.ID, 'email')            # Campo para inserir o email
password_field = driver.find_element(By.ID, 'password')      # Campo para inserir a senha
register_button = driver.find_element(By.ID, 'register')     # Botão "Registrar"

# Preenchemos os campos do formulário com valores
first_name_field.send_keys('John')                           # Inserimos "John" no campo de primeiro nome
last_name_field.send_keys('Doe')                             # Inserimos "Doe" no campo de sobrenome
email_field.send_keys('johndoe@example.com')                 # Inserimos "johndoe@example.com" no campo email
password_field.send_keys('SecurePassword123')                # Inserimos "SecurePassword123" no campo de senha

# Clicamos no botão para enviar o formulário
register_button.click()

# Opcional: Pausa de 5 segundos para ver o resultado do envio do formulário
time.sleep(5)

# Fechamos o navegador
driver.quit()