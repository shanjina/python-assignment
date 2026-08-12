class NegativeNumberError(Exception):
    pass


def check_number(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    return number


# Example
print(check_number(10))
print(check_number(-5))