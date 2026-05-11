import PyPDF2

def extract_text_from_pdf(pdf_file):
    # Abrimos o arquivo PDF
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        # Extraímos o texto de todas as páginas
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def save_text_to_file(text, txt_file):
    # Salvamos o texto no arquivo
    with open(txt_file, 'w', encoding='utf-8') as file:
        file.write(text)

def count_keywords_in_file(txt_file, keywords):
    # Contamos as ocorrências das palavras-chave
    counts = {keyword: 0 for keyword in keywords}
    
    with open(txt_file, 'r', encoding='utf-8') as file:
        text = file.read()
        for keyword in keywords:
            counts[keyword] = text.lower().count(keyword.lower())
    
    return counts

def main():
    pdf_file = 'example.pdf'
    txt_file = 'extracted_text.txt'
    keywords = ['dados', 'análise', 'relatório']

    # Extração de texto do PDF e salvamento no arquivo
    extracted_text = extract_text_from_pdf(pdf_file)
    save_text_to_file(extracted_text, txt_file)

    # Contagem das palavras-chave no arquivo
    keyword_counts = count_keywords_in_file(txt_file, keywords)
    
    # Exibição do resultado
    print(keyword_counts)

main()