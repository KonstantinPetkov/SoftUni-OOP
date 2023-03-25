def even_parameters(func):

    def wrapper(*args):
        for a in args:
            if isinstance(a, int):
                if a % 2 == 0:
                    continue

            return "Please use only even numbers!"

        return func(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))
