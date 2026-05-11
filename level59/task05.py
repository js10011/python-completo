def max_subarray_sum(arr, k):
    if len(arr) < k:
        return None  # Se o tamanho do array for menor que k, retorne None

    # Calcule a soma do primeiro subarray de tamanho k
    max_sum = current_sum = sum(arr[:k])
    
    for i in range(k, len(arr)):
        # Atualize a soma atual subtraindo o primeiro elemento do subarray anterior e adicionando o próximo elemento
        current_sum += arr[i] - arr[i - k]
        # Atualize o máximo se a soma atual for maior
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum

# Exemplo de uso
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(max_subarray_sum(arr, k))  # Saída: 24 (7 + 8 + 9)