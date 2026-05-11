import psutil
from selenium import webdriver

# Criamos uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrimos a página da web usando o Selenium
driver.get("https://www.example.com")

# Fechamos o web driver, encerrando a sessão no navegador
driver.quit()

# Fechamos todos os processos do Chrome que possam ter ficado
for process in psutil.process_iter(attrs=['pid', 'name']):
    # Verificamos se o nome do processo é 'chrome'
    if process.info['name'] == 'chrome':
        try:
            # Finalizamos o processo
            process.terminate()
            process.wait(timeout=3)  # Aguardamos o término do processo
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
            pass  # Ignoramos se o processo já foi finalizado ou está inacessível