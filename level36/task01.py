import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configuramos o web driver para trabalhar com o navegador Chrome
driver = webdriver.Chrome()

# Carregamos a página da web a partir do caminho local
driver.get("file:///path/to/your/form.html")  # Substitua pelo caminho do seu arquivo local form.html

# Encontramos os campos de texto pelos seus IDs
first_name_field = driver.find_element(By.ID, "first_name")  # Campo para entrada do nome
last_name_field = driver.find_element(By.ID, "last_name")    # Campo para entrada do sobrenome

# Inserimos o primeiro conjunto de dados (nome e sobrenome)
first_name_field.send_keys("John")  # Inserimos "John" no campo do nome
last_name_field.send_keys("Doe")    # Inserimos "Doe" no campo do sobrenome

# Fazemos uma pausa de 2 segundos para ver os dados inseridos
time.sleep(2)

# Limpamos os campos de texto
first_name_field.clear()  # Limpamos o campo do nome
last_name_field.clear()    # Limpamos o campo do sobrenome

# Fazemos uma pausa de 2 segundos para ver os campos limpos
time.sleep(2)

# Inserimos o segundo conjunto de dados (outro nome e sobrenome)
first_name_field.send_keys("Jane")  # Inserimos "Jane" no campo do nome
last_name_field.send_keys("Smith")  # Inserimos "Smith" no campo do sobrenome

# Fazemos uma pausa de 2 segundos para ver o segundo conjunto de dados inserido
time.sleep(2)

# Fechamos o navegador
driver.quit()