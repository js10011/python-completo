def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1: Antes da chamada da função")
        result = func(*args, **kwargs)
        print("Decorator 1: Depois da chamada da função")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2: Antes da chamada da função")
        result = func(*args, **kwargs)
        print("Decorator 2: Depois da chamada da função")
        return result
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello, world!")

say_hello()