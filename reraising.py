def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print("Logging: Division by zero attempted")
        raise 
try:
    result = divide(10, 0)
except ZeroDivisionError:
    print("Handled again in outer block")
    
