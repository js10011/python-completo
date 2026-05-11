import requests

def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança HTTPError para respostas ruins (4xx e 5xx)
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"Ocorreu um erro HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Ocorreu um erro de conexão: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Ocorreu um erro de timeout: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Ocorreu um erro: {req_err}")

url = "http://example.com"
content = fetch_url(url)
if content:
    print(content)