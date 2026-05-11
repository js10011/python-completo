def length_of_lis(arr):
    if not arr:
        return 0

    dp = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Exemplo de uso
arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(arr))  # Output: 4 (2,5,7,101 ou 2,5,7,18)