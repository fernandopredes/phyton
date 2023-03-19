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
