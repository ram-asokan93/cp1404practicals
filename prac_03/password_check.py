"""
Program that asks for password with error checking and loop if invalid
also print "*" for the number of char in password
"""

MAX_LENGTH = 16
MIN_LENGTH = 4

def main():
    print("Password must be between {} and {} characters long".format(MIN_LENGTH, MAX_LENGTH))
    print("Password must include at least 1 Upper case and 1 numeric character")

    password = str(input("Please choose a password \n\t> "))
    while not password_checker(password):
        print("invalid password!")
        password = str(input("\t> "))

    print("password accepted!")
    print("\t", end="")
    for char in password:
        print("*", end="")


def password_checker(password):
    if MIN_LENGTH < len(password) > MAX_LENGTH:
        return False

    upper_count = 0
    num_count = 0

    for char in password:
        if char.isupper():
            upper_count += 1
            pass
        elif char.isdigit():
            num_count += 1
            pass

    if upper_count == 0 or num_count == 0:
        return False
    else:
        pass

    return True


main()




