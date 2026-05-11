import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Criar uma instância do driver do navegador
driver = webdriver.Chrome()

# Abra a página web com a tabela
url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"
driver.get(url)

# Espere um tempo para que a página carregue completamente
time.sleep(3)

# Encontre a tabela pelo identificador
table = driver.find_element(By.ID, 'Highest-grossing_films')

# Extraia todas as linhas da tabela
rows = table.find_elements(By.TAG_NAME, 'tr')

for row in rows:
    # Extraia todas as células da linha
    cells = row.find_elements(By.TAG_NAME, 'td')

    for cell in cells:
        # Obtenha o texto da célula
        cell_text = cell.text
        # Verifique a presença do atributo 'data-sort-value'
        data_sort_value = cell.get_attribute('data-sort-value')

        # Formate a saída de acordo com a presença do atributo 'data-sort-value'
        if data_sort_value:
            print(f"{cell_text} - data-sort-value: {data_sort_value}")
        else:
            print(cell_text)

# Feche o driver
driver.quit()