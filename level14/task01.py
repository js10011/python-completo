def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Antes de chamar a função")
        result = func(*args, **kwargs)
        print("Depois de chamar a função")
        return result
    return wrapper

@log_decorator
def greet():
    print("Olá!")

greet()