from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # Importamos time para adicionar pausas

# Criamos uma instância do driver do navegador
driver = webdriver.Chrome()

# Carregamos o arquivo HTML local
driver.get("file://" + "<path_to_your_directory>/index.html")  # Substitua pelo caminho do seu arquivo index.html

# Espera explícita pelo aparecimento do botão com ID 'submit'
wait = WebDriverWait(driver, 10)  # Definimos o tempo de espera (até 10 segundos)
button = wait.until(EC.presence_of_element_located((By.ID, 'submit')))  # Esperamos até que o botão apareça na página

# Clicamos no botão assim que ele estiver disponível
button.click()

# Pausa adicional de 2 segundos para ver o efeito do clique (se necessário)
time.sleep(2)

# Fechamos o navegador e encerramos a sessão do WebDriver
driver.quit()