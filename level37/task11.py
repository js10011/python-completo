from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# URL da página e ID do botão
url = "http://example.com"  # Substitua pela URL desejada
button_id = "dynamic-button-id"  # Substitua pelo ID do botão desejado
wait_time = 10  # Tempo de espera do botão em segundos

# Criando uma instância do driver do navegador
driver = webdriver.Chrome()

try:
    # Abrindo a URL
    driver.get(url)

    # Configurando a espera pelo aparecimento do botão
    wait = WebDriverWait(driver, wait_time)

    # Esperando o aparecimento do botão com o ID especificado e clicando nele
    button = wait.until(EC.presence_of_element_located((By.ID, button_id)))
    button.click()

except TimeoutException:
    # Exibindo mensagem se o botão não apareceu dentro do tempo especificado
    print(f"O botão com ID '{button_id}' não apareceu dentro de {wait_time} segundos.")

finally:
    # Fechando o web driver
    driver.quit()