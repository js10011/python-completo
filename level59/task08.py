def fractional_knapsack(values, weights, capacity):
    index = list(range(len(values)))
    ratio = [v / w for v, w in zip(values, weights)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    
    max_value = 0
    for i in index:
        if capacity == 0:
            break
        amount = min(weights[i], capacity)
        max_value += amount * ratio[i]
        capacity -= amount
    
    return max_value

# Exemplo de uso
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print(fractional_knapsack(values, weights, capacity))