import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Criando uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrindo a página HTML com o formulário
driver.get('file:///path/to/report_form.html')  # Insira o caminho para o seu arquivo HTML

# Preenchimento dos campos do formulário
try:
    name_input = driver.find_element(By.NAME, 'name')
    department_input = driver.find_element(By.NAME, 'department')
    report_input = driver.find_element(By.NAME, 'report')

    name_input.send_keys('Ivan Ivanov')
    department_input.send_keys('Departamento de Desenvolvimento')
    report_input.send_keys('Hoje, finalizei o trabalho no projeto.')
except Exception as e:
    print("Erro ao preencher os campos do formulário:", e)

# Clicando no botão de enviar o formulário
try:
    submit_button = driver.find_element(By.NAME, 'submit')
    submit_button.click()
    time.sleep(2)  # Esperando o envio do formulário ser concluído
except Exception as e:
    print("Erro ao clicar no botão de envio:", e)

driver.quit()