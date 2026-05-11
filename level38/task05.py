from selenium import webdriver

# Criamos uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrimos a página web
driver.get("http://example.com/start-page")
# Aqui você pode adicionar quaisquer ações adicionais, se necessário

# Fechamos o navegador
driver.quit()