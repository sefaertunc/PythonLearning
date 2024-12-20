operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Cannot divide by zero"
}


def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Not a valid number. Try again.")


def get_operation():
    while True:
        operation = input("Enter an operation (+, -, *, /): ")
        if operation in operations:
            return operation
        print("Invalid operation. Try again.")



while True:
    num1 = get_number("Enter the first number: ")
    op = get_operation()
    num2 = get_number("Enter the second number: ")

    result = operations[op](num1, num2)
    print(f"Result: {result}")

    if input("Do you want to continue? (y/n): ").lower() != "y":
        break
