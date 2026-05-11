def find_pairs(nums, target):
    pairs = []
    seen = set()
    
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

# Exemplo de uso
nums = [2, 4, 3, 5, 7, 8, 9]
target = 10
print(find_pairs(nums, target))