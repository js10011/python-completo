from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicialização do web driver (por exemplo, Chrome)
driver = webdriver.Chrome()

# Abertura da página web
driver.get("https://example.com")

# Busca pelo elemento com o texto "Example Domain" usando XPath
element = driver.find_element(By.XPATH, "//*[text()='Example Domain']")

# Exibição do texto do elemento encontrado
print(element.text)

# Fechamento do navegador
driver.quit()