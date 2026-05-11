from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Abertura da página web indicada
driver.get("https://example.com")

# Busca de todas as linhas na tabela com a classe `data-row`
rows = driver.find_elements(By.CSS_SELECTOR, "tr.data-row")

# Extração e impressão dos valores das células com a classe `data-value` para cada linha
for row in rows:
    value_element = row.find_element(By.CSS_SELECTOR, ".data-value")
    print(value_element.text)

# Término correto da sessão
driver.quit()