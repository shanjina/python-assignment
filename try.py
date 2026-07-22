try:
    num = int(input("Enter a number:"))
    result = 10/num
except ValueError:
    print("Error: Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Cannot be divided by zero.")
else:
    print("Success! Result = ",result)
finally:
    print("Execution finished(cleaned here,)")
    