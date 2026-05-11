class ApplicationError(Exception):
    pass

class NegativeValueError(ApplicationError):
    pass

class ValueTooLargeError(ApplicationError):
    pass

def check_number(number):
    if number < 0:
        raise NegativeValueError("The value is negative.")
    elif number > 100:
        raise ValueTooLargeError("The value is too large.")
    else:
        return "The value is acceptable."

try:
    num = int(input("Enter a number: "))
    result = check_number(num)
    print(result)
except NegativeValueError as e:
    print(f"Error: {e}")
except ValueTooLargeError as e:
    print(f"Error: {e}")
except ApplicationError as e:
    print(f"An application error occurred: {e}")