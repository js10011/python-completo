from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Criar uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrir a página web com o formulário
driver.get('URL_DA_PAGINA_COM_FORMULARIO')

# Espera explícita pelo carregamento do campo dinâmico com id "dynamic_form_field"
dynamic_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'dynamic_form_field'))
)

# Inserção do texto no campo
dynamic_field.send_keys('Entrada automatizada')

# Espera explícita pela aparição do botão com id "submit_button"
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'submit_button'))
)

# Clique no botão de envio do formulário
submit_button.click()

# Espera explícita pela aparição da mensagem de envio bem-sucedido
success_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'success_message'))
)

# Obter e exibir o texto da mensagem de envio bem-sucedido do formulário
print(success_message.text)

# Fechar o navegador
driver.quit()