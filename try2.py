try:
    num = int(input("Enter a number:"))
    result = 10/num
except(ValueError,ZeroDivisionError) as e:
    print("Caught an exeception:", type(e.__name__))