class PasswordError(Exception):
    pass


class PasswordTooShortError(PasswordError):
    pass


class PasswordTooWeakError(PasswordError):
    pass


def validate_password(password):
    if len(password) < 8:
        raise PasswordTooShortError("Password is too short.")

    if not any(char.isdigit() for char in password):
        raise PasswordTooWeakError("Password must contain at least one number.")

    return "Password is valid"


# Examples
print(validate_password("hello"))
print(validate_password("helloworld"))
print(validate_password("hello123"))