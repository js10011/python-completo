def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

# Exemplos de uso
str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))  # True

str1 = "hello"
str2 = "bello"
print(are_anagrams(str1, str2))  # False