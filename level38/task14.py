from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL da página que precisa ser aberta
url = 'https://example.com'  # Substitua pela URL necessária
element_id = 'target-element-id'  # Substitua pelo ID necessário do elemento

# Inicialização do web driver (por exemplo, para Chrome)
driver = webdriver.Chrome()

try:
    # Abertura da página da web
    driver.get(url)

    # Espera explícita pelo aparecimento do elemento com o ID especificado
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, element_id))
    )

    # Se o elemento foi encontrado, exibe a mensagem
    print("Elemento encontrado")

except Exception as e:
    # Tratamento de exceções, se o elemento não for encontrado ou outro erro ocorrer
    print("Elemento não encontrado dentro do tempo especificado:", e)

finally:
    # Fechamento do driver
    driver.quit()