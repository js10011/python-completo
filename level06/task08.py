
def outer_function():
    x = 10
    
    def inner_function():
        nonlocal x
        x += 5
    
    inner_function()
    print(x)

outer_function()