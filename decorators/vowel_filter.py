def vowel_filter(function):
    def wrapper():
        filtered = function()
        result = [x for x in filtered if x.lower() in "aeiou"]
        return result
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
