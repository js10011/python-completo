from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Criando uma instância do driver do navegador
driver = webdriver.Chrome()

# Abertura da página
driver.get('https://example.com/dynamic_content')

# Rolagem da página e espera pelo aparecimento do elemento 'Continue'
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[text()='Continue']"))
)

# Rolando a página para baixo
continue_element = None
while True:
    try:
        continue_element = driver.find_element(By.XPATH, "//*[text()='Continue']")
        break
    except:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

# Clique no elemento 'Continue'
continue_element.click()

# Alternativamente, se o texto do botão pode estar escondido, pode-se usar a espera
WebDriverWait(driver, 10).until(
    EC.url_changes('https://example.com/dynamic_content')
)

# Fechamento do navegador
driver.quit()