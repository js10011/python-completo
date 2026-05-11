from datetime import datetime

# Determinação da data atual
current_date = datetime.now()

# Formatação da data no formato "YYYY-MM-DD"
date_format_1 = current_date.strftime("%Y-%m-%d")

# Formatação da data no formato "DD.MM.YYYY"
date_format_2 = current_date.strftime("%d.%m.%Y")

# Exibição da data na tela
print("Data no formato YYYY-MM-DD:", date_format_1)
print("Data no formato DD.MM.YYYY:", date_format_2)