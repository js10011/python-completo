nested_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

total_sum = 0
for inner_tuple in nested_tuples:
    for num in inner_tuple:
        total_sum += num

print(total_sum)