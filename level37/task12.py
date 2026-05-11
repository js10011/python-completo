import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Criando uma instância do driver do navegador
driver = webdriver.Chrome()

# Abertura da página com o formulário de login
driver.get('https://example.com/login')  # Substitua o URL pelo necessário

# Busca do campo para inserir o nome de usuário e inserção do valor
username_field = driver.find_element(By.ID, 'username')  # Presumimos o uso de ID
username_field.send_keys('your_username')  # Substitua pelo nome de usuário necessário

# Busca do campo para inserir a senha e inserção do valor
password_field = driver.find_element(By.ID, 'password')  # Presumimos o uso de ID
password_field.send_keys('your_password')  # Substitua pela senha necessária

# Busca do botão de login e clique nele
login_button = driver.find_element(By.ID, 'login-button')  # Presumimos o uso de ID
login_button.click()

# Tempo para ver o resultado (pode ser removido em uso real)
time.sleep(5)

# Fechamento do web driver
driver.quit()