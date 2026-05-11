import pandas as pd

# Dados dos produtos
products_data = {
    "nome": ["Produto A", "Produto B", "Produto C"],
    "preço": [23.5, 45.2, 12.0],
    "quantidade em estoque": [10, 5, 20]
}

# Criação do DataFrame
df = pd.DataFrame(products_data)

# Gravação do DataFrame no Excel com ajuste automático da largura das colunas
with pd.ExcelWriter('products.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    worksheet = writer.sheets['Sheet1']
    
    # Ajuste da largura das colunas de acordo com o conteúdo dos dados
    for column in df:
        max_len = max(
            df[column].astype(str).map(len).max(),  # comprimento do valor mais longo na coluna
            len(column)  # comprimento do cabeçalho da coluna
        )
        col_idx = df.columns.get_loc(column)  # índice da coluna atual
        worksheet.set_column(col_idx, col_idx, max_len + 2)  # ajusta a largura da coluna