import csv
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configuração do logging
def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Inicialização do driver do navegador
def setup_driver():
    driver = webdriver.Chrome()
    return driver

# Carregamento da página
def load_page(driver, url):
    logging.info(f"Carregando a página: {url}")
    driver.get(url)
    time.sleep(2)  # Aguardando o carregamento completo da página
    logging.info("Página carregada com sucesso.")

# Extração de dados da página
def extract_data(driver):
    logging.info("Extraindo dados da página.")
    data = []
    elements = driver.find_elements(By.CSS_SELECTOR, "div.someClass")  # Altere o seletor conforme necessário
    for element in elements:
        data.append(element.text)
    logging.info("Extração de dados concluída.")
    return data

# Salvamento de dados em arquivo CSV
def save_data(data, filename):
    logging.info(f"Salvando dados no arquivo {filename}")
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Dados'])  # Cabeçalho da coluna
        for row in data:
            writer.writerow([row])
    logging.info("Dados salvos com sucesso.")

# Função principal
def main():
    # Lista de URLs para processamento
    urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        # Adicione outros URLs conforme necessário
    ]

    output_file = "extracted_data.csv"  # Nome do arquivo para salvar os dados
    setup_logging()  # Configuração do logging
    driver = setup_driver()  # Inicialização do driver do navegador
    all_data = []  # Lista para armazenar todos os dados extraídos

    for url in urls:
        load_page(driver, url)  # Carregamento da página
        data = extract_data(driver)  # Extração de dados
        all_data.extend(data)  # Adição dos dados extraídos à lista geral

    save_data(all_data, output_file)  # Salvamento de dados em arquivo
    driver.quit()  # Fechamento do driver do navegador
    logging.info("Execução do script concluída.")

# Execução da função principal
main()