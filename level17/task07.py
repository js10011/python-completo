def read_integer(input_string):
    exception_instance = None
    try:
        return int(input_string)
    except ValueError as e:
        exception_instance = e
        print(f"Error arguments: {e.args}")
        print(f"Error type: {type(e)}")
    print(f"Exception instance: {exception_instance}")

# Exemplo de chamada da função
read_integer("abc")