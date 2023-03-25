def uppercase(function):
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper

@uppercase
def new_func():
    return 'hello softuni'

print(new_func())