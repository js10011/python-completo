from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Criando uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrindo a página web do formulário de pesquisa
driver.get('URL_DA_SUA_FORMULARIO')

# Espera explícita para o carregamento do campo de texto
text_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'text_field_name'))
)

# Inserindo texto no campo de texto
text_field.send_keys('Sua resposta')

# Localizando e selecionando o botão de opção
radio_button = driver.find_element(By.ID, 'radio_button_id')
radio_button.click()

# Localizando e selecionando a caixa de seleção
checkbox = driver.find_element(By.ID, 'checkbox_id')
checkbox.click()

# Localizando o botão de envio e enviando o formulário
submit_button = driver.find_element(By.NAME, 'submit_button_name')
submit_button.send_keys(Keys.RETURN)

# Fechando o web driver
driver.quit()