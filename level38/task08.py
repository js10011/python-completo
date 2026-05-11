from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
import time

# Função para abrir a página pelo URL
def open_page(driver, url):
    try:
        # Abrindo a página
        driver.get(url)
        return True
    except WebDriverException as e:
        # Tratamento de exceção, caso não seja possível abrir a página
        print(f"Erro ao abrir a página {url}: {e}")
        return False

# Função para extrair dados da página atual
def extract_data(driver):
    try:
        # Tentando encontrar um elemento com a classe "content" e extrair seu texto
        data_element = driver.find_element(By.CLASS_NAME, "content")
        return data_element.text
    except NoSuchElementException:
        # Se o elemento não for encontrado, retorna None
        return None

def main():
    # Inicialização do driver, por exemplo, para Chrome ou Firefox
    with webdriver.Chrome() as driver:
        page_number = 1
        base_url = "http://example.com/page/"

        while True:
            # Formação do URL com o número da página
            url = base_url + str(page_number)
            print(f"Abrindo a página {url}")

            # Abrindo a página e verificando o sucesso
            if not open_page(driver, url):
                print(f"Não foi possível abrir a página {page_number}. Encerrando.")
                break

            # Extraindo dados da página atual
            data = extract_data(driver)

            # Verificando se há dados na página
            if not data:
                print(f"Dados na página {page_number} não encontrados. Encerrando.")
                break

            # Exibindo dados no console
            print(f"Dados da página {page_number}: {data}")

            # Passando para a próxima página
            page_number += 1
            # Atraso de 2 segundos entre requisições
            time.sleep(2)

# Executando a função principal
main()