from selenium import webdriver
from selenium.webdriver.common.by import By

def get_element_text_by_id(url, element_id):
    # Criamos uma instância do driver do navegador
    driver = webdriver.Chrome()

    # Carregamos a página da web
    driver.get(url)

    # Encontramos o elemento pelo seu ID e obtemos o texto dele
    element_text = driver.find_element(By.ID, element_id).text

    # Fechamos o WebDriver
    driver.quit()

    # Retornamos o texto do elemento
    return element_text


# Exemplo de uso da função
url = "http://example.com"
element_id = "exampleId"  # Substitua pelo ID necessário do elemento
element_text = get_element_text_by_id(url, element_id)
print(element_text)