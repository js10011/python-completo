from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Criamos uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrimos a página web
driver.get('http://example.com')

# Esperamos até que os elementos com a classe dynamic-content estejam completamente carregados
elements = WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'dynamic-content'))
)

# Extraímos dados dos elementos
data = []
for element in elements:
    text = element.text
    data_type = element.get_attribute('data-type')
    data.append((text, data_type))

# Salvamos os dados em um arquivo CSV
with open('extracted_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Text', 'Data-Type'])  # Cabeçalhos das colunas
    csvwriter.writerows(data)

# Fechamos o driver do navegador
driver.quit()