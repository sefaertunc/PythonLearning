from numpy.ma.core import swapaxes

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while True:
    while True:
        try:
            number_1 = int(input("enter a number: "))
            break
        except:
            print("not a number")

    while True:
        try:
            operation = input("enter an operation: ")
            if operation not in operations:
                raise ValueError("Invalid operation")
            break
        except ValueError:
            print("Invalid operation")

    while True:
        try:
            number_2 = int(input("enter another number: "))
            break
        except:
            print("not a number")

    try:
        result = operations[operation](number_1, number_2)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero")

    to_continue = input("Do you want to continue? (y/n): ")
    try:
        if to_continue.lower() != "y":
            break
    except:
        continue