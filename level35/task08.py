from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import WebDriverException

# URL para navegação
URL = "https://www.example.com"

# Instruções para instalação do Chrome
CHROME_INSTALL_INSTRUCTIONS = """
Não foi possível iniciar o Chrome. Uma possível razão é a incompatibilidade de versões do Chrome e do ChromeDriver.
Certifique-se de que o Chrome está instalado e sua versão é compatível com o ChromeDriver.
1. Para encontrar a versão do Chrome, abra o Chrome e vá para 'Configurações' -> 'Sobre o Chrome'.
2. Baixe a versão compatível do ChromeDriver aqui: https://sites.google.com/chromium.org/driver/
3. Certifique-se de que o driver está no PATH ou especifique o seu caminho ao inicializar o driver.
"""

CHROME_DOWNLOAD_INSTRUCTIONS = """
Problema ao instalar o ChromeDriver.
1. Certifique-se de que você tem acesso à Internet para instalação automática.
2. Se o problema persistir, baixe o ChromeDriver manualmente em https://sites.google.com/chromium.org/driver/
3. Coloque o driver no PATH ou especifique o caminho ao iniciar o programa.
"""

# Instruções para instalação do Firefox
FIREFOX_INSTALL_INSTRUCTIONS = """
Não foi possível iniciar o Firefox. Uma possível razão é a incompatibilidade de versões do Firefox e do GeckoDriver.
Certifique-se de que o Firefox está instalado e sua versão é compatível com o GeckoDriver.
1. Para encontrar a versão do Firefox, abra o Firefox e vá para 'Ajuda' -> 'Sobre o Firefox'.
2. Baixe a versão compatível do GeckoDriver aqui: https://github.com/mozilla/geckodriver/releases
3. Certifique-se de que o driver está no PATH ou especifique o seu caminho ao inicializar o driver.
"""

FIREFOX_DOWNLOAD_INSTRUCTIONS = """
Problema ao instalar o GeckoDriver.
1. Certifique-se de que você tem acesso à Internet para instalação automática.
2. Se o problema persistir, baixe o GeckoDriver manualmente em https://github.com/mozilla/geckodriver/releases
3. Coloque o driver no PATH ou especifique o caminho ao iniciar o programa.
"""

def setup_chrome():
    """Inicializa o ChromeDriver com tratamento de erros e instruções de instalação do driver."""
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        print("Chrome iniciado com sucesso.")
        return driver
    except WebDriverException as e:
        print("Erro ao iniciar o Chrome:", e)
        print(CHROME_INSTALL_INSTRUCTIONS)
    except Exception as e:
        print("Erro ao instalar o ChromeDriver:", e)
        print(CHROME_DOWNLOAD_INSTRUCTIONS)
    return None

def setup_firefox():
    """Inicializa o GeckoDriver com tratamento de erros e instruções de instalação do driver."""
    try:
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        print("Firefox iniciado com sucesso.")
        return driver
    except WebDriverException as e:
        print("Erro ao iniciar o Firefox:", e)
        print(FIREFOX_INSTALL_INSTRUCTIONS)
    except Exception as e:
        print("Erro ao instalar o GeckoDriver:", e)
        print(FIREFOX_DOWNLOAD_INSTRUCTIONS)
    return None

def main():
    # Tentativa de iniciar o Chrome
    driver = setup_chrome()

    # Se o Chrome não estiver disponível, tente iniciar o Firefox
    if not driver:
        driver = setup_firefox()

    # Navegação para o site e encerramento do navegador
    if driver:
        try:
            driver.get(URL)
            print("Página aberta com sucesso:", URL)
        finally:
            driver.quit()
            print("Navegador fechado.")
    else:
        print("Não foi possível iniciar o Chrome nem o Firefox. Verifique a instalação dos drivers e dos navegadores.")

main()