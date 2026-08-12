def test_function():
    try:
        x = 10 / 0
    except Exception:
        print("Logging error...")
        raise


try:
    test_function()
except ZeroDivisionError:
    print("Caller caught the exception.")