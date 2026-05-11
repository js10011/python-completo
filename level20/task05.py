x = 10

def foo_correct():
    global x
    x += 1
    print(x)

foo_correct()  # Saída: 11