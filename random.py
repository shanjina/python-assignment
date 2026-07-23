import random
print("Random examples:")
print(random.randint(1, 10))
print(random.choice(["apple", "banana", "cherry"]))
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
print()