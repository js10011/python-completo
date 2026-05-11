import time

from selenium import webdriver

# Inicialização do driver do navegador
driver = webdriver.Chrome()

try:
    # Abertura da primeira página da web
    driver.get('https://www.example.com')
    time.sleep(2)  # Espera para que a página seja totalmente carregada
    title1 = driver.title
    print(f"Título da primeira página: {title1}")

    # Abertura de uma nova aba e navegação para outra página da web
    driver.execute_script("window.open('https://www.python.org', '_blank');")
    time.sleep(2)  # Espera para que a nova aba seja carregada

    # Alternância para a segunda aba (índice 1)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)  # Espera para carregar a página na nova aba
    title2 = driver.title
    print(f"Título da segunda página: {title2}")

    # Alternância de volta para a primeira aba (índice 0)
    driver.switch_to.window(driver.window_handles[0])
    print(f"Agora na primeira aba: {driver.title}")

finally:
    # Fechamento do navegador
    time.sleep(2)
    driver.quit()