def divide(a, b):
    try:
        return a/b
    execpt(ZeroDivisionError, TypeError) as e:
        print(f"Error occureed: {e}")
        raise
    try:
        divide(10, 0)
    execpt ZeroDivisionError:
          print("Handled: cannot divided by zero")
    try:
        divide(10,"a")
    execpt TypeError:
          print("Handled: invalid types for division")
    