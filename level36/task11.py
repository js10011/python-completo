from selenium import webdriver
from selenium.webdriver.common.by import By

# Criando uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrindo a página da web
driver.get('https://example.com')

# Encontrando a tabela pelo identificador especificado
table = driver.find_element(By.ID, 'your_table_id')

# Extraindo todas as linhas da tabela
rows = table.find_elements(By.TAG_NAME, 'tr')

for row in rows:
    # Extraindo todas as células da linha atual
    cells = row.find_elements(By.TAG_NAME, 'td')

    for cell in cells:
        # Extraindo o texto da célula
        cell_text = cell.text

        # Extraindo o valor do atributo 'data-id', se estiver presente
        data_id = cell.get_attribute('data-id')

        # Formando a linha de saída
        if data_id:
            print(f'{cell_text} - data-id: {data_id}')
        else:
            print(cell_text)

# Fechando o driver
driver.quit()