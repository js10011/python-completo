import time

def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

array = [5, 3, 8, 6, 2, 7, 1, 0, 9, 4]

def bubble_sort(arr):
    new_arr = arr.copy()
    n = len(new_arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if new_arr[j] > new_arr[j+1]:
                new_arr[j], new_arr[j+1] = new_arr[j+1], new_arr[j]
    return new_arr

def insertion_sort(arr):
    new_arr = arr.copy()
    for i in range(1, len(new_arr)):
        key = new_arr[i]
        j = i - 1
        while j >= 0 and key < new_arr[j]:
            new_arr[j + 1] = new_arr[j]
            j -= 1
        new_arr[j + 1] = key
    return new_arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort
}

times = {name: measure_time(func, array) for name, func in algorithms.items()}
best_algorithm = min(times, key=times.get)

print(f"Melhor algoritmo: {best_algorithm}")