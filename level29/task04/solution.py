import os
import PyPDF2

# Solicita ao usuário o caminho do diretório com arquivos PDF
directory_path = input("Digite o caminho do diretório com arquivos PDF: ")

# Lista todos os arquivos PDF no diretório especificado
pdf_files = [f for f in os.listdir(directory_path) if f.endswith('.pdf')]

# Variáveis para o número total de palavras e armazenamento de todo o texto
total_word_count = 0
all_text = ""

# Processa cada arquivo PDF no diretório
for pdf_file in pdf_files:
    pdf_path = os.path.join(directory_path, pdf_file)
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # Extração de texto de cada página
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    all_text += text + "\n"  # Adiciona o texto ao texto total
                    total_word_count += len(text.split())  # Contagem de palavras na página
    except Exception as e:
        print(f"Erro ao processar o arquivo {pdf_file}: {e}")

# Exibe o número total de palavras em todos os arquivos PDF
print(f"Número total de palavras em todos os arquivos PDF: {total_word_count}")

# Salva todo o texto em um arquivo de texto
with open("all_texts.txt", "w", encoding='utf-8') as output_file:
    output_file.write(all_text)