from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Instale a biblioteca webdriver_manager para gerenciar o driver facilmente

# Definimos o URL que precisamos abrir
url = "https://www.example.com"

# Instalação automática da versão correspondente do ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navegação para a página especificada
driver.get(url)

# Espera para verificar que a página foi carregada (pode ser usado para observar o lançamento do navegador)
driver.implicitly_wait(5)

# Fechamento do navegador
driver.quit()