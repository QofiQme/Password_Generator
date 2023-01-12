import random
import string

def generate_password(length):
    if length < 8:
        raise ValueError("Your password is weak. It should be at least 8 characters")
    characters = string.ascii_letters + string.digits + string.punctuation
    # check if at least one uppercase letter, one digit, one special character and one lowercase
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if (any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            break
    return password

length = int(input("Enter number of characters for desired password: "))
print(generate_password(length))
