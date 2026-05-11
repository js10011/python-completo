def count_ways(coins, S):
    # Criamos o array dp, onde dp[i] conterá o número de maneiras de alcançar a soma i
    dp = [0] * (S + 1)
    dp[0] = 1  # Inicializamos o caso base, 1 maneira de alcançar a soma 0 - não usar nada

    # Processamos cada valor de moeda
    for coin in coins:
        for i in range(coin, S + 1):
            dp[i] += dp[i - coin]

    return dp[S]

# Exemplo de uso
coins = [1, 2, 5]
S = 11
print(count_ways(coins, S))  # Saída: número de maneiras de alcançar a soma 11