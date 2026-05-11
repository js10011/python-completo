def closest_element(arr, low, high, target, best=None):
    if low > high:
        return best

    mid = (low + high) // 2

    if best is None or abs(arr[mid] - target) < abs(best - target):
        best = arr[mid]

    if arr[mid] < target:
        return closest_element(arr, mid + 1, high, target, best)
    else:
        return closest_element(arr, low, mid - 1, target, best)


# Exemplo de uso:
arr = [1, 3, 5, 8, 10, 14, 17]
target = 9
result = closest_element(arr, 0, len(arr) - 1, target)
print(f"Element closest to {target} is {result}") # 8