def test_function():
    try:
        x = 10 / 0
    except Exception:
        print("Logging error...")
        raise

test_function()