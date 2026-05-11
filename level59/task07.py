def min_coins(coins, amount):
    coins.sort(reverse=True)  # Ordenamos as moedas em ordem decrescente de valor nominal
    count = 0
    for coin in coins:
        if amount == 0:
            break
        count += amount // coin  # Quantidade de moedas desse valor nominal
        amount %= coin  # Quantia restante
    if amount != 0:
        return -1  # Se a quantia não puder ser trocada por essas moedas
    return count

# Exemplo de uso
coins = [1, 2, 5, 10, 25]
amount = 63
print(min_coins(coins, amount))  # Saída: 5 (25 + 25 + 10 + 2 + 1)