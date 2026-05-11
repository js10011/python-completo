from collections import Counter

def word_frequency(text):
    words = text.split()
    frequency = Counter(words)
    return frequency

# Exemplo de uso da função
text = "Escreva uma função para contar a frequência de cada palavra em um texto."
print(word_frequency(text))