def knapsack_with_restrictions(items, k, max_weight):
    dp = [0] * (max_weight + 1)

    for weight, value, quantity in items:
        for _ in range(min(quantity, k)):
            for w in range(max_weight, weight - 1, -1):
                dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[max_weight]

# Exemplo de uso
items = [(2, 3, 5), (3, 4, 2), (4, 5, 8)]
k = 3
max_weight = 10
print(knapsack_with_restrictions(items, k, max_weight))