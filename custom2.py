class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}")


def check_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    return "Age is valid"


# Examples
print(check_age(25))
print(check_age(-5))