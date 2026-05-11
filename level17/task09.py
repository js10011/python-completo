import traceback

def complex_operation():
    def inner_function_1():
        def inner_function_2():
            def inner_function_3():
                # Aqui geramos uma exceção
                raise ValueError("An error occurred")
            inner_function_3()
        inner_function_2()
    try:
        inner_function_1()
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        for frame in tb:
            print(f"File: {frame.filename}, Line: {frame.lineno}, Function: {frame.name}, Code: {frame.line}")

# Exemplo de chamada da função
complex_operation()