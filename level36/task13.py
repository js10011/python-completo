from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Criando uma instância do driver do navegador
driver = webdriver.Chrome()

# Abertura da página web
driver.get('http://example.com')  # Substitua 'http://example.com' pelo URL da página desejada

# Aguardando o aparecimento do elemento com id "dynamic_element"
dynamic_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "dynamic_element"))
)

# Extração do texto do elemento e exibição na tela
print(dynamic_element.text)

# Fechando o driver
driver.quit()