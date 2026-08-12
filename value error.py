try:
 number = int(input("Enter an integer:"))
 print("You entered:", number)
except ValueError: 
 print("Error: Please enter a valid integer")