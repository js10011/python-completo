from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

def extract_titles(driver):
    # Aqui se assume que os títulos dos artigos têm a tag h2
    titles = driver.find_elements(By.TAG_NAME, "h2")
    for title in titles:
        print(title.text)

def main():
    # Criamos uma instância do driver do navegador
    driver = webdriver.Chrome()

    try:
        # Abertura da página web
        driver.get("http://example.com/articles")
        time.sleep(2)  # Atraso para o carregamento da página, recomenda-se adicionar uma espera mais robusta

        while True:
            # Extração dos títulos
            extract_titles(driver)
            
            try:
                # Navegação para a próxima página
                next_button = driver.find_element(By.LINK_TEXT, "Next")
                next_button.click()
                
                # Atraso para dar tempo à próxima página carregar
                time.sleep(2)
            except NoSuchElementException:
                # Se o botão "Next" não for encontrado, significa que a última página foi alcançada
                print("Última página alcançada.")
                break
    finally:
        # Fechamento do driver
        driver.quit()

main()