def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(4, 20, operator=divide)
print(result)


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

friends = [
    {"name": "rolf", "age": 24},
    {"name": "lara", "age": 35},
    {"name": "bid ed", "age": 36},
]

def get_friend_name(friend):
    return friend['name']

print(search(friends, 'rolf', get_friend_name))
