import time
from selenium import webdriver

# Criando uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrindo a página web
driver.get('https://example.com/sample_page')

# Pequena pausa para carregamento da página
time.sleep(2)

# Executando JavaScript para rolar a página até o fim
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Pausa para visualização da rolagem (pode ser removida)
time.sleep(2)

# Fechando o navegador
driver.quit()