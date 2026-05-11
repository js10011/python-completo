def check_positive(number):
    if number <= 0:
        raise ValueError("Number must be positive")
    return True