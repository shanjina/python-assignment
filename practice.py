with open("practice.txt", "w") as f:
    f.write("""Hi everyone
We are learning File I/O
using Java.
I like programming in Java.""")
with open("practice.txt", "r") as f:
    data = f.read()
data = data.replace("Java", "Python")
with open("practice.txt", "w") as f:
    f.write(data)
if "learning" in data:
    print("The word 'learning' exists in the file.")
else:
    print("The word 'learning' does not exist in the file.")
    f = open("practice.txt", "r")
    lines = f.readlines()
    print(lines)
