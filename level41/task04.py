import matplotlib.pyplot as plt
import pandas as pd

# Leitura de dados do arquivo stock_prices.csv com o tratamento adequado de valores ausentes
df = pd.read_csv("stock_prices.csv", na_values="-")

# Construção do gráfico
plt.figure(figsize=(12, 8))

for company in df.columns[1:]:
    plt.plot(df['Ano'], df[company], label=company)

# Configuração dos eixos e título
plt.xlabel("Ano")
plt.ylabel("Preço das Ações")
plt.title("Evolução dos preços das ações das 10 principais empresas de tecnologia dos EUA")
plt.legend()
plt.grid(True)

plt.show()