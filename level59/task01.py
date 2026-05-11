def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# Exemplo de uso:
example = "radar"
print(is_palindrome(example))  # True