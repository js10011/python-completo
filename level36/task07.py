from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Criar uma instância do driver do navegador
driver = webdriver.Chrome()

# Abertura da página web
driver.get('https://example.com/scroll_and_click')

# Rolagem da página até o final
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Espera explícita para o aparecimento do link 'Load More'
wait = WebDriverWait(driver, 10)
load_more_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Load More')))

# Clique no primeiro link 'Load More' encontrado
load_more_link.click()

# Fechamento do navegador
driver.quit()