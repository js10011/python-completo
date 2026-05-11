import pandas as pd
from pandas import ExcelWriter

# Dados sobre os resultados dos alunos
data = {
    'nome do aluno': ['Alexey', 'Maria', 'Ivan', 'Olga', 'Svetlana'],
    'disciplina': ['Matemática', 'Física', 'Química', 'Literatura', 'Biologia'],
    'nota': [5, 4, 3, 5, 4]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Cálculo das estatísticas necessárias
total_students = df['nome do aluno'].nunique()
average_grade = df['nota'].mean()
unique_subjects = df['disciplina'].nunique()

# Criação da folha adicional 'Summary'
summary_data = {
    'Total de alunos': [total_students],
    'Nota média': [average_grade],
    'Quantidade de disciplinas': [unique_subjects]
}

summary_df = pd.DataFrame(summary_data)

# Exportação para Excel
with ExcelWriter('student_report.xlsx') as writer:
    df.to_excel(writer, sheet_name='Students', index=False)
    summary_df.to_excel(writer, sheet_name='Summary', index=False)

    # Ajuste automático da largura das colunas
    for sheet_name in writer.sheets:
        worksheet = writer.sheets[sheet_name]
        for column in worksheet.columns:
            max_length = 0
            column = [cell for cell in column]
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            adjusted_width = (max_length + 2)
            worksheet.column_dimensions[column[0].column_letter].width = adjusted_width