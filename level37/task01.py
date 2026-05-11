from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Instalação e configuração do driver web Chrome
driver_service = Service(ChromeDriverManager().install())

# Inicialização do navegador usando Selenium
driver = webdriver.Chrome(service=driver_service)

# Abertura da página web indicada
driver.get("http://example.com")