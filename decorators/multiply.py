def multiply(times):

    def decorator(function):

        def wrapper(parameter):
            return times * function(parameter)

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 4

print(add_ten(3))

