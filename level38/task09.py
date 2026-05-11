from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Criando uma instância do driver do navegador
with webdriver.Chrome() as driver:
    # Abrindo a página inicial (substitua o URL pelo necessário)
    driver.get("URL_OF_THE_PAGE")

    while True:
        # Esperando pelo aparecimento de elementos com a classe "title_class" e obtendo os títulos
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "title_class"))
            )
            titles = driver.find_elements(By.CLASS_NAME, "title_class")

            # Exibindo o texto de cada título encontrado
            for title in titles:
                print(title.text)

        except NoSuchElementException:
            # Se os elementos não forem encontrados, exibir mensagem
            print("Títulos não encontrados nesta página.")

        # Procurando o botão "Próximo" para ir para a próxima página
        try:
            next_button = driver.find_element(By.XPATH, "//a[text()='Próximo']")

            # Clicando no botão "Próximo"
            next_button.click()

            # Opcionalmente, esperando o carregamento da próxima página
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "title_class"))
            )

        except NoSuchElementException:
            # Se o botão "Próximo" não for encontrado, encerrar a execução
            print("Botão 'Próximo' não encontrado. Finalizando.")
            break