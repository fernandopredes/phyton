def multiply(*args):
    total = 1
    for arg in args:
        total *= arg

    return total

print(multiply(2,2,3))

def apply(*args, operator):
    if operator == "*":
        return multiply(*args) #must have the * or it'll be considered a tuple
    elif operator == "+":
        return sum(args)
    else:
        return "no valid operator"

print(apply(2,3,operator="*"))

def name(**kwargs):
    print(kwargs)

name(name='bob', age='25')

def print_nicely(**kwargs):
    name(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name='hannah',age='32')

