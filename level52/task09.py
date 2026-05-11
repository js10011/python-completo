import math

n = 1_000_000_000

time_algorithm_1 = 100 * n * math.log(n)
time_algorithm_2 = 10 * n ** 2
time_algorithm_3 = n ** 3

print(time_algorithm_1)
print(time_algorithm_2)
print(time_algorithm_3)