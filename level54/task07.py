def find_duplicates(nums):
    duplicates = []
    seen = set()
    for num in nums:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

# Exemplo de uso:
nums = [1, 2, 3, 2, 4, 5, 6, 3, 7, 8, 1]
print(find_duplicates(nums))  # Output: [2, 3, 1]