from selenium import webdriver
import time

# Criamos uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrindo a primeira página em uma nova aba
driver.get('https://www.example.com')
# Atraso para carregar a página
time.sleep(2)

# Abrindo a segunda página em uma nova aba
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://www.example.org')
# Atraso para carregar a página
time.sleep(2)

# Alternando de volta para a primeira aba
driver.switch_to.window(driver.window_handles[0])
# Atraso para demonstrar a alternância
time.sleep(2)

# Alternando novamente para a segunda aba
driver.switch_to.window(driver.window_handles[1])
# Atraso para demonstrar a alternância
time.sleep(2)

# Fechando todas as abas e encerrando o navegador
driver.quit()