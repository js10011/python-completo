from requests_html import HTMLSession
import time
import hashlib

# Função para criar sessão e renderizar página
def create_session():
    return HTMLSession()

# Função para obter o conteúdo da página pelo URL
def fetch_page_content(session, url):
    response = session.get(url)
    response.html.render()
    return response.html.html

# Função para calcular hash do conteúdo da página
def compute_content_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

# Função para salvar novo conteúdo da página em um arquivo
def save_content_to_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Novo conteúdo salvo em {filename}.")

# Função para verificar mudanças no conteúdo da página
def is_content_changed(current_hash, previous_hash):
    return current_hash != previous_hash

# Função para monitorar a página web em busca de mudanças
def monitor_website(session, url, check_interval, output_file):
    previous_content_hash = ''

    while True:
        # Obtemos o conteúdo atual da página
        current_content = fetch_page_content(session, url)

        # Calculamos o hash do conteúdo atual
        current_content_hash = compute_content_hash(current_content)

        # Verificamos se o conteúdo da página mudou
        if is_content_changed(current_content_hash, previous_content_hash):
            save_content_to_file(current_content, output_file)
            previous_content_hash = current_content_hash
        else:
            print("Nenhuma mudança no conteúdo detectada.")

        # Esperamos o intervalo definido antes da próxima verificação
        time.sleep(check_interval)

# Função principal, que prepara os dados para monitoramento
def main():
    url_to_monitor = 'https://example.com'  # URL da página web para monitoramento
    interval = 60  # Intervalo de verificação em segundos
    output_filename = 'new_content.html'

    session = create_session()
    monitor_website(session, url_to_monitor, interval, output_filename)

# Executa a função principal
main()