from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicialização do web driver, por exemplo, para o Chrome
driver = webdriver.Chrome()

try:
    # Abertura da página de um site dinâmico
    driver.get('https://example.com/dynamic-content-page')

    # Espera explícita pelo carregamento do elemento com texto
    # Aqui 'ELEMENT_ID' é o identificador do elemento que é carregado dinamicamente
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ELEMENT_ID"))
    )

    # Extração do conteúdo textual do elemento
    text_content = element.text

    # Exibição do texto extraído na tela
    print("Conteúdo textual do elemento:", text_content)

finally:
    # Fechamento do web driver
    driver.quit()