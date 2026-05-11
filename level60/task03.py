def count_partitions(n, max_summand):
    if n == 0:
        return 1
    if n < 0 or max_summand == 0:
        return 0
    return count_partitions(n, max_summand - 1) + count_partitions(n - max_summand, max_summand)

def number_of_ways(n):
    return count_partitions(n, n)

n = int(input("Digite o número n: "))
print("Número de maneiras de decompor o número", n, "em parcelas:", number_of_ways(n))