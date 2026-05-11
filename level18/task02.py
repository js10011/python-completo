class InputValidationError(Exception):
    def __init__(self, message, original_exception):
        super().__init__(message)
        self.original_exception = original_exception

def validate_input(input_str):
    try:
        if not input_str:
            raise ValueError("Input cannot be empty")
        if len(input_str) > 10:
            raise ValueError("Input is too long")
    except ValueError as e:
        raise InputValidationError("Validation error occurred", e)

# Exemplo de uso:
try:
    validate_input("")
except InputValidationError as e:
    print(f"Caught custom exception: {e}")
    print(f"Original exception: {e.original_exception}")