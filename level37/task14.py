import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Criando uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrindo a página web com o formulário
driver.get('URL_TO_YOUR_FORM_PAGE')

# Encontrando a lista suspensa pelo seu identificador e selecionando um item
dropdown = Select(driver.find_element(By.ID, 'dropdown_id'))  # substitua 'dropdown_id' pelo ID real
dropdown.select_by_visible_text('Option Text')  # substitua 'Option Text' pelo texto do item desejado

# Encontrando a área de texto pelo seu identificador e inserindo o texto
textarea = driver.find_element(By.ID, 'textarea_id')  # substitua 'textarea_id' pelo ID real
textarea.send_keys('Your text here')  # insira o texto necessário

# Encontrando o botão de envio do formulário pelo seu identificador e clicando nele
submit_button = driver.find_element(By.ID, 'submit_button_id')  # substitua 'submit_button_id' pelo ID real
submit_button.click()

# Dando algum tempo para garantir o envio do formulário
time.sleep(3)

# Fechando o navegador
driver.quit()