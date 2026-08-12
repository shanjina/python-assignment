items = ["Apple&quot", "Banana", "Mango", "Orange", "Grapes"]
try:
 index = int(input("Enter index (0-4): "))
 print("Item:", items[index])
except IndexError:
 print("Error: Index is out of range.")