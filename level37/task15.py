from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Caminho do arquivo que será carregado
file_path = "/path/to/your/file.txt"

# URL da página com o formulário de upload de arquivo
url = "http://example.com/upload"

# Criamos uma instância do driver do navegador
driver = webdriver.Chrome()

# Acessamos a página especificada
driver.get(url)

# Aguardamos até que o elemento de upload de arquivo esteja disponível e o encontramos
file_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "fileUpload"))
)

# Especificamos o caminho do arquivo para upload
file_input.send_keys(file_path)

# Encontramos e clicamos no botão de envio do formulário
submit_button = driver.find_element(By.NAME, "submit")
submit_button.click()

# Aguardamos a confirmação de upload bem-sucedido do arquivo
confirmation_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "confirmation"))
)

# Verificamos o texto de confirmação
assert "File uploaded successfully" in confirmation_text.text
print("File upload confirmed.")

# Fechamos o navegador
driver.quit()