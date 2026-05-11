from requests_html import HTMLSession
import requests


# Função para carregar e renderizar conteúdo dinâmico de uma URL especificada
def fetch_dynamic_content(url):
    session = HTMLSession()
    response = session.get(url)
    response.html.render()  # Necessário para processar conteúdo dinâmico
    return response.html.html


# Função para extrair dados do conteúdo HTML
def extract_data_from_html(html_content):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    data = soup.find_all('p', class_='data')
    return [d.text for d in data]


# Função para enviar dados para a API especificada
def send_data_to_api(data, api_url):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, json=data, headers=headers)
    return response.status_code, response.text


# Função principal para executar todos os passos
def main():
    url = "https://example.com/dynamic-content"  # Substitua pela URL real
    api_url = "https://api.example.com/receive-data"  # Substitua pela URL real da API

    # Carregamos o conteúdo dinâmico
    html_content = fetch_dynamic_content(url)

    # Extraímos os dados
    data = extract_data_from_html(html_content)

    # Enviamos os dados para a API
    status_code, response_text = send_data_to_api(data, api_url)

    print(f"Status Code: {status_code}")
    print(f"Response: {response_text}")


main()