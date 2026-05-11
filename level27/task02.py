# Dicionário com dados de receitas e despesas para cada dia da semana
week_financials = {
    "Segunda-feira": 100,
    "Terça-feira": 150,
    "Quarta-feira": 200,
    "Quinta-feira": 250,
    "Sexta-feira": 300,
    "Sábado": 200,
    "Domingo": 200
}

# Cálculo do lucro total da semana
total_profit = sum(week_financials.values())

# Cálculo do lucro médio diário
average_daily_profit = total_profit / 7

# Exibição dos resultados
print("Lucro total da semana:", total_profit)
print("Lucro médio diário:", average_daily_profit)