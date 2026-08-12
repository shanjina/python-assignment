
def safe_divide(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return "Error: Cannot divide by zero or use incompatible types."


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "2"))