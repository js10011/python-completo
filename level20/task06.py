def create_multipliers_correct():
    return [lambda x, i=i: i * x for i in range(5)]

for multiplier in create_multipliers_correct():
    print(multiplier(2))  # Saída: 0 2 4 6 8