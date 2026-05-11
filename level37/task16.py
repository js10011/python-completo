import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Criamos uma instância do driver do navegador
driver = webdriver.Chrome()
driver.get('https://example.com/login')

# Incrivelmente importante esperar que os elementos carreguem
time.sleep(3)

# Encontrar o campo de login e inserir o login
login_field = driver.find_element(By.NAME, 'username')
login_field.send_keys('test_user')

# Encontrar o campo de senha e inserir a senha
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('test_password')

# Encontrar o botão de login e clicar nele
login_button = driver.find_element(By.NAME, 'login')  
login_button.click()

# Espere um pouco para ver o que aconteceu
time.sleep(5)

# Fechar o navegador
driver.quit()