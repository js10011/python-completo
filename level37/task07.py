from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Inicializa o WebDriver para o navegador Chrome
driver = webdriver.Chrome()

# Abre a página web alvo
driver.get('https://www.wikipedia.org')  # Substitua pela URL real

# Espera que todos os elementos com a classe 'dynamic-content' estejam disponíveis na página
elements = WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'dynamic-content'))
)

# Coleta dados dos elementos
data = []
for element in elements:
    text = element.text  # Texto do elemento
    data_type = element.get_attribute('data-type')  # Atributo 'data-type'
    data.append((text, data_type))

# Salva os dados em um arquivo CSV
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Text', 'Data Type'])  # Escreve o cabeçalho
    writer.writerows(data)  # Escreve os dados coletados

# Fecha o WebDriver
driver.quit()