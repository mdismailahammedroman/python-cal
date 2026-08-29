def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        if b == 0:
            raise ValueError("Cannot divide by zero")

        return a / b

    except ValueError as error:
        return f"Error: {error}"