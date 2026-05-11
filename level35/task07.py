from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager  # Para gerenciar as versões do GeckoDriver
from selenium.common.exceptions import WebDriverException

# URL para navegação
url = "https://www.example.com"

try:
    # Inicializar o GeckoDriver e abrir o navegador Firefox
    service = Service(GeckoDriverManager().install())  # Instala automaticamente a versão necessária do GeckoDriver
    driver = webdriver.Firefox(service=service)

    # Navegar para a página especificada
    driver.get(url)

    # Espera para verificar se a página carregou (útil para observar a abertura do navegador)
    driver.implicitly_wait(5)

except WebDriverException as e:
    print("Erro ao iniciar o GeckoDriver:", e)
    print("Verifique se a versão do Firefox e do GeckoDriver são compatíveis.")

finally:
    # Fechar o navegador
    driver.quit()