def print_pattern(data):
    space, stars = data
    result = ' ' * space + '* ' * stars
    return result

def get_pattern(data):
    data = size
    for x in range(size):
        space = size - x - 1
        star = x + 1
        print(' ' * space + '* ' * star)


size = int(input())
print(get_pattern(print_pattern()))